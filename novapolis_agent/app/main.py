from __future__ import annotations

import asyncio
import hashlib as _hashlib
import json as _json
import logging
import os as _os
import platform as _platform
import threading
import time
from collections.abc import Mapping as _Mapping
from typing import Any
from typing import cast as _cast

import fastapi as _fastapi
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse

from .api.chat import process_chat_request, stream_chat_request
from .api.models import ApiErrorResponse, ChatMessage, ChatRequest, ChatResponse
from .api.tts_models import (
    TtsCacheCleanupResponse,
    TtsCacheStatsResponse,
    TtsHealthResponse,
    TtsSynthesizeRequest,
    TtsSynthesizeResponse,
    TtsVoicesResponse,
)
from .core.settings import settings
from .tts.providers import TtsProviderUnavailableError, build_tts_provider

# Logger-Konfiguration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI-App erstellen
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

_tts_cache_lock = threading.Lock()
_tts_cache_store: dict[str, dict[str, Any]] = {}
_tts_cache_stats: dict[str, int] = {
    "hits": 0,
    "misses": 0,
    "evictions_ttl": 0,
    "evictions_size": 0,
}

_tts_provider_instance = build_tts_provider(settings.TTS_PROVIDER)


def _tts_cache_total_size_unlocked() -> int:
    total = 0
    for item in _tts_cache_store.values():
        total += int(item.get("size_bytes", 0))
    return total


def _tts_cache_cleanup_unlocked(now: float | None = None) -> dict[str, int]:
    if now is None:
        now = time.time()

    removed_expired = 0
    removed_size = 0

    ttl = int(settings.TTS_CACHE_TTL_SEC)
    max_entries = int(settings.TTS_CACHE_MAX_ENTRIES)
    max_bytes = int(settings.TTS_CACHE_MAX_BYTES)

    expired_keys: list[str] = []
    for key, item in _tts_cache_store.items():
        created_at = float(item.get("created_at", now))
        if (now - created_at) > ttl:
            expired_keys.append(key)

    for key in expired_keys:
        _tts_cache_store.pop(key, None)
        removed_expired += 1

    _tts_cache_stats["evictions_ttl"] += removed_expired

    def _oldest_key() -> str | None:
        if not _tts_cache_store:
            return None
        return min(
            _tts_cache_store.items(),
            key=lambda kv: float(kv[1].get("last_access", 0.0)),
        )[0]

    while len(_tts_cache_store) > max_entries:
        oldest_key = _oldest_key()
        if oldest_key is None:
            break
        _tts_cache_store.pop(oldest_key, None)
        removed_size += 1

    while _tts_cache_total_size_unlocked() > max_bytes and _tts_cache_store:
        oldest_key = _oldest_key()
        if oldest_key is None:
            break
        _tts_cache_store.pop(oldest_key, None)
        removed_size += 1

    _tts_cache_stats["evictions_size"] += removed_size

    return {
        "removed_expired": removed_expired,
        "removed_size": removed_size,
    }


def _tts_cache_key_from_payload(payload: str) -> str:
    return _hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _tts_cache_get(cache_key: str, now: float) -> tuple[dict[str, Any] | None, dict[str, int]]:
    if not settings.TTS_CACHE_ENABLED:
        return None, {"removed_expired": 0, "removed_size": 0}

    with _tts_cache_lock:
        cleanup = _tts_cache_cleanup_unlocked(now)
        item = _tts_cache_store.get(cache_key)
        if item is None:
            _tts_cache_stats["misses"] += 1
            return None, cleanup

        item["last_access"] = now
        _tts_cache_stats["hits"] += 1
        response = dict(_cast(dict[str, Any], item.get("response", {})))
        return response, cleanup


def _tts_cache_put(cache_key: str, response: dict[str, Any], now: float) -> dict[str, int]:
    if not settings.TTS_CACHE_ENABLED:
        return {"removed_expired": 0, "removed_size": 0}

    response_bytes = len(_json.dumps(response, ensure_ascii=False, sort_keys=True).encode("utf-8"))
    with _tts_cache_lock:
        _tts_cache_store[cache_key] = {
            "created_at": now,
            "last_access": now,
            "size_bytes": response_bytes,
            "response": dict(response),
        }
        cleanup = _tts_cache_cleanup_unlocked(now)
    return cleanup


def _tts_cache_stats_snapshot() -> TtsCacheStatsResponse:
    with _tts_cache_lock:
        entries = len(_tts_cache_store)
        size_bytes = _tts_cache_total_size_unlocked()
        return TtsCacheStatsResponse(
            enabled=bool(settings.TTS_CACHE_ENABLED),
            entries=entries,
            size_bytes=size_bytes,
            ttl_sec=int(settings.TTS_CACHE_TTL_SEC),
            max_entries=int(settings.TTS_CACHE_MAX_ENTRIES),
            max_bytes=int(settings.TTS_CACHE_MAX_BYTES),
            hits=int(_tts_cache_stats["hits"]),
            misses=int(_tts_cache_stats["misses"]),
            evictions_ttl=int(_tts_cache_stats["evictions_ttl"]),
            evictions_size=int(_tts_cache_stats["evictions_size"]),
        )


COMMON_ERROR_RESPONSES: dict[int | str, dict[str, Any]] = {
    status.HTTP_400_BAD_REQUEST: {
        "model": ApiErrorResponse,
        "description": "Ungültige Anfrage oder Grenzwert verletzt.",
    },
    status.HTTP_401_UNAUTHORIZED: {
        "model": ApiErrorResponse,
        "description": "Nicht authentifiziert.",
    },
    status.HTTP_403_FORBIDDEN: {
        "model": ApiErrorResponse,
        "description": "Zugriff verweigert.",
    },
    status.HTTP_429_TOO_MANY_REQUESTS: {
        "model": ApiErrorResponse,
        "description": "Rate-Limit überschritten.",
    },
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "model": ApiErrorResponse,
        "description": "Interner Serverfehler.",
    },
    status.HTTP_504_GATEWAY_TIMEOUT: {
        "model": ApiErrorResponse,
        "description": "Zeitüberschreitung bei Backend-Verarbeitung.",
    },
}

# Optional: Einfache In-Memory Rate-Limit Middleware (pro IP)
if settings.RATE_LIMIT_ENABLED or settings.TTS_RATE_LIMIT_ENABLED:
    import threading
    from collections import defaultdict, deque

    from starlette.middleware.base import BaseHTTPMiddleware

    class _RateLimiter(BaseHTTPMiddleware):
        def __init__(self, app: Any) -> None:
            super().__init__(app)
            self.lock = threading.Lock()
            self.window = float(settings.RATE_LIMIT_WINDOW_SEC)
            self.capacity = max(1, int(settings.RATE_LIMIT_REQUESTS_PER_MINUTE))
            self.burst = max(0, int(settings.RATE_LIMIT_BURST))
            self.tts_window = float(settings.TTS_RATE_LIMIT_WINDOW_SEC)
            self.tts_capacity = max(1, int(settings.TTS_RATE_LIMIT_REQUESTS_PER_MINUTE))
            self.tts_burst = max(0, int(settings.TTS_RATE_LIMIT_BURST))
            self.buckets: dict[str, deque[float]] = defaultdict(deque)

        def _resolve_limit(self, path: str) -> tuple[bool, float, int, int, str]:
            tts_paths = set(settings.TTS_RATE_LIMIT_PATHS)
            if settings.TTS_RATE_LIMIT_ENABLED and path in tts_paths:
                return True, self.tts_window, self.tts_capacity, self.tts_burst, "tts"
            if settings.RATE_LIMIT_ENABLED:
                return True, self.window, self.capacity, self.burst, "global"
            return False, self.window, self.capacity, self.burst, "none"

        async def dispatch(self, request: Request, call_next):
            if request.url.path in set(settings.RATE_LIMIT_EXEMPT_PATHS):
                return await call_next(request)

            enabled, window, capacity, burst, scope = self._resolve_limit(request.url.path)
            if not enabled:
                return await call_next(request)

            client_host = request.client.host if request.client else "unknown"
            if client_host in set(settings.RATE_LIMIT_TRUSTED_IPS):
                return await call_next(request)
            now = time.time()
            allow = True
            bucket_key = f"{scope}:{client_host}"

            with self.lock:
                q: deque[float] = self.buckets[bucket_key]
                cutoff = now - window
                while q and q[0] < cutoff:
                    q.popleft()
                limit = capacity + burst
                if len(q) >= limit:
                    allow = False
                else:
                    q.append(now)

            if not allow:
                headers = {
                    "Retry-After": str(int(window)),
                    "X-RateLimit-Limit": str(capacity + burst),
                    "X-RateLimit-Window": str(int(window)),
                }
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Rate limit exceeded. Bitte später erneut versuchen.",
                    headers=headers,
                )
            response = await call_next(request)
            try:
                q2: deque[float] = self.buckets[bucket_key]
                remaining = max(0, (capacity + burst) - len(q2))
                response.headers["X-RateLimit-Limit"] = str(capacity + burst)
                response.headers["X-RateLimit-Remaining"] = str(remaining)
                response.headers["X-RateLimit-Window"] = str(int(window))
            except Exception:
                pass
            return response

    app.add_middleware(_RateLimiter)

# CORS-Middleware hinzufügen
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.BACKEND_CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


@app.get("/health", status_code=status.HTTP_200_OK)
async def health_check() -> dict[str, Any]:
    """Gesundheitscheck für den API-Server."""
    return {"status": "ok", "time": time.time()}


@app.get("/version", status_code=status.HTTP_200_OK)
async def version_info() -> dict[str, Any]:
    """Gibt Version und Laufzeitinformationen der Anwendung zurück."""
    return {
        "app_name": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "git_sha": _os.getenv("GIT_SHA"),
        "build_time": _os.getenv("BUILD_TIME"),
        "python_version": _platform.python_version(),
        "fastapi_version": getattr(_fastapi, "__version__", None),
    }


def _tts_provider() -> str:
    return _tts_provider_instance.provider_id


def _extract_tts_token(request: Request) -> str | None:
    auth = request.headers.get("Authorization", "")
    if auth.lower().startswith("bearer "):
        token = auth[7:].strip()
        return token or None
    direct = request.headers.get(settings.TTS_AUTH_HEADER)
    return direct.strip() if isinstance(direct, str) and direct.strip() else None


def _require_tts_auth(request: Request) -> None:
    if not settings.TTS_AUTH_ENABLED:
        return

    provided = _extract_tts_token(request)
    if not provided:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="TTS token fehlt.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    expected = (settings.TTS_AUTH_TOKEN or "").strip()
    if not expected or provided != expected:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="TTS token ungueltig.",
        )


@app.get(
    "/tts/health",
    response_model=TtsHealthResponse,
    status_code=status.HTTP_200_OK,
    tags=["tts"],
    summary="TTS Health",
    responses=COMMON_ERROR_RESPONSES,
)
async def tts_health() -> TtsHealthResponse:
    """TTS-Mini-Service-Vertrag: Health-Status und Readiness-Flags."""
    return TtsHealthResponse(
        status="ok",
        provider=_tts_provider(),
        synthesize_ready=bool(_tts_provider_instance.supports_synthesis),
        cache_ready=bool(settings.TTS_CACHE_ENABLED),
    )


@app.get(
    "/tts/voices",
    response_model=TtsVoicesResponse,
    status_code=status.HTTP_200_OK,
    tags=["tts"],
    summary="TTS Voices",
    responses=COMMON_ERROR_RESPONSES,
)
async def tts_voices(req: Request) -> TtsVoicesResponse:
    """TTS-Mini-Service-Vertrag: verfügbare Stimmen (Dummy-Provider)."""
    # Step 4: minimal local auth contract for sensitive TTS endpoints.
    _require_tts_auth(req)
    provider = _tts_provider_instance.provider_id
    voices = _tts_provider_instance.voices()
    return TtsVoicesResponse(provider=provider, voices=voices)


@app.post(
    "/tts/synthesize",
    response_model=TtsSynthesizeResponse,
    status_code=status.HTTP_200_OK,
    tags=["tts"],
    summary="TTS Synthesize",
    responses=COMMON_ERROR_RESPONSES,
)
async def tts_synthesize(request: TtsSynthesizeRequest, req: Request) -> TtsSynthesizeResponse:
    """TTS-Mini-Service-Vertrag mit Cache.

    Reproduzierbare Metadatenbasis und klare Provider-Fallbacks inklusive.
    """
    _require_tts_auth(req)
    if len(request.text) > settings.REQUEST_MAX_INPUT_CHARS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                "Input zu lang: "
                + str(len(request.text))
                + " Zeichen (Limit "
                + str(settings.REQUEST_MAX_INPUT_CHARS)
                + ")."
            ),
        )

    digest_source = {
        "provider": _tts_provider(),
        "text": request.text,
        "voice": request.voice,
        "language": request.language,
        "output_format": request.output_format.value,
        "sample_rate_hz": request.sample_rate_hz,
        "settings": request.settings,
    }
    payload = _json.dumps(digest_source, ensure_ascii=False, sort_keys=True)
    request_hash = _hashlib.sha256(payload.encode("utf-8")).hexdigest()
    cache_key = _tts_cache_key_from_payload(payload)
    now = time.time()
    cached, cleanup_get = _tts_cache_get(cache_key, now)
    if cached is not None:
        cached_placeholder = bool(cached.get("is_placeholder", True))
        cached_status = "placeholder" if cached_placeholder else "ok"
        cached_detail = str(cached.get("detail") or "cached-response")
        return TtsSynthesizeResponse(
            status=cached_status,
            provider=_tts_provider(),
            output_format=request.output_format,
            mime_type=str(cached.get("mime_type", "audio/ogg")),
            is_placeholder=cached_placeholder,
            request_hash=request_hash,
            cache_key=cache_key,
            cache_hit=True,
            artifact_path=(
                str(cached.get("artifact_path"))
                if cached.get("artifact_path") is not None
                else None
            ),
            detail=(
                "Cache hit (removed_expired="
                + str(cleanup_get.get("removed_expired", 0))
                + ", removed_size="
                + str(cleanup_get.get("removed_size", 0))
                + "). "
                + cached_detail
            ),
        )

    try:
        provider_result = _tts_provider_instance.synthesize(request)
    except TtsProviderUnavailableError as exc:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="TTS provider unavailable (" + _tts_provider() + "): " + str(exc),
        ) from exc

    mime = provider_result.mime_type

    payload_to_cache = {
        "mime_type": mime,
        "request_hash": request_hash,
        "is_placeholder": bool(provider_result.is_placeholder),
        "artifact_path": provider_result.artifact_path,
        "detail": provider_result.detail,
    }
    cleanup_put = _tts_cache_put(cache_key, payload_to_cache, now)

    response_status = "placeholder" if provider_result.is_placeholder else "ok"

    return TtsSynthesizeResponse(
        status=response_status,
        provider=_tts_provider(),
        output_format=request.output_format,
        mime_type=mime,
        is_placeholder=bool(provider_result.is_placeholder),
        request_hash=request_hash,
        cache_key=cache_key,
        cache_hit=False,
        artifact_path=provider_result.artifact_path,
        detail=(
            "Cache miss (removed_expired="
            + str(cleanup_put.get("removed_expired", 0))
            + ", removed_size="
            + str(cleanup_put.get("removed_size", 0))
            + "). "
            + provider_result.detail
        ),
    )


@app.get(
    "/tts/cache/stats",
    response_model=TtsCacheStatsResponse,
    status_code=status.HTTP_200_OK,
    tags=["tts"],
    summary="TTS Cache Stats",
    responses=COMMON_ERROR_RESPONSES,
)
async def tts_cache_stats(req: Request) -> TtsCacheStatsResponse:
    _require_tts_auth(req)
    return _tts_cache_stats_snapshot()


@app.post(
    "/tts/cache/cleanup",
    response_model=TtsCacheCleanupResponse,
    status_code=status.HTTP_200_OK,
    tags=["tts"],
    summary="TTS Cache Cleanup",
    responses=COMMON_ERROR_RESPONSES,
)
async def tts_cache_cleanup(req: Request) -> TtsCacheCleanupResponse:
    _require_tts_auth(req)
    with _tts_cache_lock:
        cleanup = _tts_cache_cleanup_unlocked(time.time())
        entries = len(_tts_cache_store)
        size_bytes = _tts_cache_total_size_unlocked()
    return TtsCacheCleanupResponse(
        status="ok",
        removed_expired=int(cleanup.get("removed_expired", 0)),
        removed_size=int(cleanup.get("removed_size", 0)),
        entries=entries,
        size_bytes=size_bytes,
    )


# Einfache Middleware für Request-ID und JSON-Logs
@app.middleware("http")
async def request_context_mw(request: Request, call_next):
    rid = request.headers.get(settings.REQUEST_ID_HEADER) or request.headers.get("X-Request-Id")
    if not rid:
        rid = f"req-{int(time.time() * 1000)}"
    start = time.time()
    try:
        try:
            request.state.request_id = rid
        except Exception:
            pass
        response = _cast(Response, await call_next(request))
        duration_ms = int((time.time() - start) * 1000)
        if settings.LOG_JSON:
            logger.info(
                _json.dumps(
                    {
                        "event": "request",
                        "path": request.url.path,
                        "method": request.method,
                        "status": int(response.status_code),
                        "duration_ms": duration_ms,
                        "request_id": rid,
                    },
                    ensure_ascii=False,
                )
            )
        else:
            method = request.method
            path = request.url.path
            status_code = int(response.status_code)
            msg = (
                method
                + " "
                + path
                + " -> "
                + str(status_code)
                + " ["
                + str(duration_ms)
                + " ms] rid="
                + str(rid)
            )
            logger.info(msg)
        response.headers[settings.REQUEST_ID_HEADER] = rid
        return response
    except Exception as exc:
        duration_ms = int((time.time() - start) * 1000)
        if settings.LOG_JSON:
            logger.exception(
                _json.dumps(
                    {
                        "event": "error",
                        "path": request.url.path,
                        "request_id": rid,
                        "duration_ms": duration_ms,
                        "error": str(exc),
                    },
                    ensure_ascii=False,
                )
            )
        else:
            logger.exception(f"Fehler bei {request.url.path} rid={rid}: {exc}")
        if isinstance(exc, HTTPException):
            raw_headers = getattr(exc, "headers", None)
            headers: dict[str, str] = {settings.REQUEST_ID_HEADER: str(rid)}
            try:
                if isinstance(raw_headers, dict):
                    m: _Mapping[str, object] = _cast(_Mapping[str, object], raw_headers)
                    for key_obj, val_obj in m.items():
                        headers[str(key_obj)] = str(val_obj)
            except Exception:
                pass
            return JSONResponse(
                status_code=exc.status_code,
                content={"detail": exc.detail},
                headers=headers,
            )
        raise


def _get_content_from_message(m: ChatMessage | _Mapping[str, str]) -> str:
    """Extrahiert Nachrichteninhalte für ChatMessage- oder Mapping-Inputs."""
    if isinstance(m, ChatMessage):
        return m.content or ""
    if isinstance(m, _Mapping):
        try:
            mapping = _cast(_Mapping[str, str], m)
            return mapping.get("content", "") or ""
        except Exception:
            return ""
    content = getattr(m, "content", "")
    return str(content) if content is not None else ""


@app.post(
    "/chat",
    response_model=ChatResponse,
    tags=["chat"],
    summary="Chat Completion",
    responses=COMMON_ERROR_RESPONSES,
)
async def chat(request: ChatRequest, req: Request):
    try:
        _raw = await req.json()
        request_data: dict[str, Any] = {}
        if isinstance(_raw, dict):
            request_data = _cast(dict[str, Any], _raw)
        eval_mode = bool(request_data.get("eval_mode", False))
        unrestricted_mode = bool(request_data.get("unrestricted_mode", False))

        total_chars = 0
        for m in request.messages:
            total_chars += len(_get_content_from_message(m))
        if total_chars > settings.REQUEST_MAX_INPUT_CHARS:
            detail_msg = (
                "Input zu lang: "
                + str(total_chars)
                + " Zeichen (Limit "
                + str(settings.REQUEST_MAX_INPUT_CHARS)
                + ")."
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=detail_msg,
            )

        rid = getattr(req.state, "request_id", None)
        log_template = (
            "Chat-Anfrage erhalten mit %s Nachrichten, Eval-Modus: %s, "
            "Uneingeschränkter Modus: %s, rid=%s"
        )
        logger.info(
            log_template,
            len(request.messages),
            eval_mode,
            unrestricted_mode,
            rid,
        )

        response = await asyncio.wait_for(
            process_chat_request(
                request,
                eval_mode=eval_mode,
                unrestricted_mode=unrestricted_mode,
                client=None,
                request_id=rid,
            ),
            timeout=settings.REQUEST_TIMEOUT,
        )
        return response

    except TimeoutError as exc:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=("Zeitüberschreitung bei /chat nach " + str(settings.REQUEST_TIMEOUT) + "s."),
        ) from exc
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Fehler bei der Verarbeitung der Chat-Anfrage: %s", exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Interner Serverfehler: {exc!s}",
        ) from exc


@app.post(
    "/chat/stream",
    tags=["chat"],
    summary="Chat Stream (SSE)",
    responses=COMMON_ERROR_RESPONSES,
)
async def chat_stream(request: ChatRequest, req: Request):
    try:
        request_data = await req.json()
        eval_mode = request_data.get("eval_mode", False)
        unrestricted_mode = request_data.get("unrestricted_mode", False)
        total_chars = 0
        for m in request.messages:
            total_chars += len(_get_content_from_message(m))
        if total_chars > settings.REQUEST_MAX_INPUT_CHARS:
            detail_msg = (
                "Input zu lang: "
                + str(total_chars)
                + " Zeichen (Limit "
                + str(settings.REQUEST_MAX_INPUT_CHARS)
                + ")."
            )
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=detail_msg,
            )

        rid = getattr(req.state, "request_id", None)
        gen = await asyncio.wait_for(
            stream_chat_request(
                request,
                eval_mode=eval_mode,
                unrestricted_mode=unrestricted_mode,
                client=None,
                request_id=rid,
            ),
            timeout=settings.REQUEST_TIMEOUT,
        )
        return StreamingResponse(gen, media_type="text/event-stream")
    except TimeoutError as exc:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail=(
                "Zeitüberschreitung bei /chat/stream nach " + str(settings.REQUEST_TIMEOUT) + "s."
            ),
        ) from exc
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Fehler bei der Streaming-Chat-Anfrage: %s", exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Interner Serverfehler: {exc!s}",
        ) from exc


@app.get("/")
async def root():
    """Root-Endpunkt für einfache Gesundheitsprüfung."""
    return {"message": "CVN Agent API ist aktiv"}
