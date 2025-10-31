from __future__ import annotations

import json as _json
import logging
import os as _os
import platform as _platform
import time
from typing import Any, Dict, Mapping as _Mapping, Union as _Union, cast as _cast

import fastapi as _fastapi
from fastapi import FastAPI, HTTPException, Request, Response, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, StreamingResponse

from .api.chat import process_chat_request, stream_chat_request
from .api.models import ChatMessage, ChatRequest, ChatResponse
from .core.settings import settings

# Logger-Konfiguration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPI-App erstellen
app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    version=settings.PROJECT_VERSION,
)

# Optional: Einfache In-Memory Rate-Limit Middleware (pro IP)
if settings.RATE_LIMIT_ENABLED:
    from collections import defaultdict, deque
    import threading
    from typing import Deque

    from starlette.middleware.base import BaseHTTPMiddleware

    class _RateLimiter(BaseHTTPMiddleware):
        def __init__(self, app: Any) -> None:
            super().__init__(app)
            self.lock = threading.Lock()
            self.window = float(settings.RATE_LIMIT_WINDOW_SEC)
            self.capacity = max(1, int(settings.RATE_LIMIT_REQUESTS_PER_MINUTE))
            self.burst = max(0, int(settings.RATE_LIMIT_BURST))
            self.buckets: Dict[str, Deque[float]] = defaultdict(deque)

        async def dispatch(self, request: Request, call_next):
            if request.url.path in set(settings.RATE_LIMIT_EXEMPT_PATHS):
                return await call_next(request)

            client_host = request.client.host if request.client else "unknown"
            if client_host in set(settings.RATE_LIMIT_TRUSTED_IPS):
                return await call_next(request)
            now = time.time()
            allow = True

            with self.lock:
                q: Deque[float] = self.buckets[client_host]
                cutoff = now - self.window
                while q and q[0] < cutoff:
                    q.popleft()
                limit = self.capacity + self.burst
                if len(q) >= limit:
                    allow = False
                else:
                    q.append(now)

            if not allow:
                headers = {
                    "Retry-After": str(int(self.window)),
                    "X-RateLimit-Limit": str(self.capacity + self.burst),
                    "X-RateLimit-Window": str(int(self.window)),
                }
                raise HTTPException(
                    status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                    detail="Rate limit exceeded. Bitte später erneut versuchen.",
                    headers=headers,
                )
            response = await call_next(request)
            try:
                q2: Deque[float] = self.buckets[client_host]
                remaining = max(0, (self.capacity + self.burst) - len(q2))
                response.headers["X-RateLimit-Limit"] = str(self.capacity + self.burst)
                response.headers["X-RateLimit-Remaining"] = str(remaining)
                response.headers["X-RateLimit-Window"] = str(int(self.window))
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
async def health_check() -> Dict[str, Any]:
    """Gesundheitscheck für den API-Server."""
    return {"status": "ok", "time": time.time()}


@app.get("/version", status_code=status.HTTP_200_OK)
async def version_info() -> Dict[str, Any]:
    """Gibt Version und Laufzeitinformationen der Anwendung zurück."""
    return {
        "app_name": settings.PROJECT_NAME,
        "version": settings.PROJECT_VERSION,
        "git_sha": _os.getenv("GIT_SHA"),
        "build_time": _os.getenv("BUILD_TIME"),
        "python_version": _platform.python_version(),
        "fastapi_version": getattr(_fastapi, "__version__", None),
    }


# Einfache Middleware für Request-ID und JSON-Logs
@app.middleware("http")
async def request_context_mw(request: Request, call_next):
    rid = request.headers.get(settings.REQUEST_ID_HEADER) or request.headers.get("X-Request-Id")
    if not rid:
        rid = f"req-{int(time.time()*1000)}"
    start = time.time()
    try:
        try:
            setattr(request.state, "request_id", rid)
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
            logger.info(
                f"{request.method} {request.url.path} -> {int(response.status_code)} [{duration_ms} ms] rid={rid}"
            )
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
            headers: Dict[str, str] = {settings.REQUEST_ID_HEADER: str(rid)}
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


def _get_content_from_message(m: _Union[ChatMessage, _Mapping[str, str]]) -> str:
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


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, req: Request):
    try:
        _raw = await req.json()
        request_data: Dict[str, Any] = {}
        if isinstance(_raw, dict):
            request_data = _cast(Dict[str, Any], _raw)
        eval_mode = bool(request_data.get("eval_mode", False))
        unrestricted_mode = bool(request_data.get("unrestricted_mode", False))

        total_chars = 0
        for m in request.messages:
            total_chars += len(_get_content_from_message(m))
        if total_chars > settings.REQUEST_MAX_INPUT_CHARS:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Input zu lang: {total_chars} Zeichen (Limit {settings.REQUEST_MAX_INPUT_CHARS}).",
            )

        rid = getattr(req.state, "request_id", None)
        logger.info(
            "Chat-Anfrage erhalten mit %s Nachrichten, Eval-Modus: %s, Uneingeschränkter Modus: %s, rid=%s",
            len(request.messages),
            eval_mode,
            unrestricted_mode,
            rid,
        )

        response = await process_chat_request(
            request,
            eval_mode=eval_mode,
            unrestricted_mode=unrestricted_mode,
            client=None,
            request_id=rid,
        )
        return response

    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Fehler bei der Verarbeitung der Chat-Anfrage: %s", exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Interner Serverfehler: {str(exc)}",
        ) from exc


@app.post("/chat/stream")
async def chat_stream(request: ChatRequest, req: Request):
    try:
        request_data = await req.json()
        eval_mode = request_data.get("eval_mode", False)
        unrestricted_mode = request_data.get("unrestricted_mode", False)
        rid = getattr(req.state, "request_id", None)
        gen = await stream_chat_request(
            request,
            eval_mode=eval_mode,
            unrestricted_mode=unrestricted_mode,
            client=None,
            request_id=rid,
        )
        return StreamingResponse(gen, media_type="text/event-stream")
    except HTTPException:
        raise
    except Exception as exc:
        logger.exception("Fehler bei der Streaming-Chat-Anfrage: %s", exc)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Interner Serverfehler: {str(exc)}",
        ) from exc


@app.get("/")
async def root():
    """Root-Endpunkt für einfache Gesundheitsprüfung."""
    return {"message": "CVN Agent API ist aktiv"}
