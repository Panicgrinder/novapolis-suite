from __future__ import annotations

import asyncio
import importlib
from collections.abc import Mapping
from types import SimpleNamespace
from typing import Any

import pytest
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.testclient import TestClient
from starlette.datastructures import Headers


def _load_app_main():
    return importlib.reload(importlib.import_module("app.main"))


def _tts_request(**overrides: Any):
    from app.api.tts_models import TtsSynthesizeRequest

    payload: dict[str, Any] = {
        "text": "Hallo Welt",
        "voice": "dummy-de",
        "language": "de",
        "output_format": "ogg",
        "sample_rate_hz": 22050,
        "settings": {},
    }
    payload.update(overrides)
    return TtsSynthesizeRequest(**payload)


class _BrokenMapping(Mapping[str, str]):
    def __iter__(self):
        return iter(["content"])

    def __len__(self) -> int:
        return 1

    def __getitem__(self, key: str) -> str:
        raise RuntimeError("broken")

    def get(self, key: str, default: str | None = None) -> str:
        raise RuntimeError("broken")


@pytest.mark.unit
def test_tts_contract_and_record_helpers_cover_inactive_and_missing_session(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    app_mod = _load_app_main()

    inactive = app_mod._tts_contract_fields(_tts_request())
    assert inactive["contract_version"] is None
    assert inactive["channel"] is None
    assert inactive["log_channels"] is None

    active_request = _tts_request(
        session_id="sess-1",
        campaign_id="camp-1",
        scene_id="scene-1",
        slot_id="slot-01",
        turn_id="turn-01",
        channel="pc",
    )
    active = app_mod._tts_contract_fields(active_request)
    assert active["contract_version"] == "text_rpg_session_v1"
    assert active["channel"] == "pc"
    assert active["log_channels"] == ["world", "pc", "ally", "sys"]

    assert (
        app_mod._record_tts_session_artifact(
            _tts_request(),
            provider="dummy",
            mime_type="audio/ogg",
            request_hash="abc",
            cache_key=None,
            cache_hit=False,
            artifact_path=None,
            is_placeholder=True,
            detail="none",
        )
        is None
    )

    recorded: list[tuple[str, object]] = []
    monkeypatch.setattr(
        app_mod._sim_api,
        "record_tts_artifact",
        lambda session_id, record: recorded.append((session_id, record)),
    )
    monkeypatch.setattr(app_mod._sim_api, "load_session_record", lambda _session_id: None)
    assert (
        app_mod._record_tts_session_artifact(
            active_request,
            provider="dummy",
            mime_type="audio/ogg",
            request_hash="abc",
            cache_key="cache",
            cache_hit=True,
            artifact_path="artifact.ogg",
            is_placeholder=False,
            detail="detail",
        )
        is None
    )
    assert recorded and recorded[0][0] == "sess-1"

    monkeypatch.setattr(
        app_mod._sim_api,
        "load_session_record",
        lambda _session_id: SimpleNamespace(artifact_paths={"tts_manifest": "manifest.jsonl"}),
    )
    assert (
        app_mod._record_tts_session_artifact(
            active_request,
            provider="dummy",
            mime_type="audio/ogg",
            request_hash="abc",
            cache_key="cache",
            cache_hit=False,
            artifact_path="artifact.ogg",
            is_placeholder=True,
            detail="detail",
        )
        == "manifest.jsonl"
    )


@pytest.mark.unit
def test_tts_cache_helpers_cover_disabled_expired_and_size_cleanup(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    app_mod = _load_app_main()

    app_mod._tts_cache_store.clear()
    app_mod._tts_cache_stats.update(
        {"hits": 0, "misses": 0, "evictions_ttl": 0, "evictions_size": 0}
    )
    monkeypatch.setattr(app_mod.settings, "TTS_CACHE_ENABLED", False, raising=False)
    assert app_mod._tts_cache_get("missing", 10.0) == (
        None,
        {"removed_expired": 0, "removed_size": 0},
    )
    assert app_mod._tts_cache_put(
        "key",
        {
            "mime_type": "audio/ogg",
            "request_hash": "hash",
            "is_placeholder": True,
            "artifact_path": None,
            "detail": "detail",
        },
        10.0,
    ) == {"removed_expired": 0, "removed_size": 0}

    monkeypatch.setattr(app_mod.settings, "TTS_CACHE_ENABLED", True, raising=False)
    monkeypatch.setattr(app_mod.settings, "TTS_CACHE_TTL_SEC", 5, raising=False)
    monkeypatch.setattr(app_mod.settings, "TTS_CACHE_MAX_ENTRIES", 1, raising=False)
    monkeypatch.setattr(app_mod.settings, "TTS_CACHE_MAX_BYTES", 1, raising=False)

    app_mod._tts_cache_store.update(
        {
            "expired": {
                "created_at": 1.0,
                "last_access": 1.0,
                "size_bytes": 2,
                "response": {
                    "mime_type": "audio/ogg",
                    "request_hash": "a",
                    "is_placeholder": True,
                    "artifact_path": None,
                    "detail": "expired",
                },
            },
            "fresh": {
                "created_at": 9.0,
                "last_access": 2.0,
                "size_bytes": 2,
                "response": {
                    "mime_type": "audio/ogg",
                    "request_hash": "b",
                    "is_placeholder": False,
                    "artifact_path": "artifact",
                    "detail": "fresh",
                },
            },
        }
    )

    cleanup = app_mod._tts_cache_cleanup_unlocked(10.0)
    assert cleanup["removed_expired"] == 1
    assert cleanup["removed_size"] >= 1
    assert app_mod._tts_cache_total_size_unlocked() == 0

    app_mod._tts_cache_store["expired-only"] = {
        "created_at": 1.0,
        "last_access": 1.0,
        "size_bytes": 1,
        "response": {
            "mime_type": "audio/ogg",
            "request_hash": "c",
            "is_placeholder": True,
            "artifact_path": None,
            "detail": "expired",
        },
    }
    monkeypatch.setattr(app_mod.time, "time", lambda: 10.0)
    cleanup_with_now_default = app_mod._tts_cache_cleanup_unlocked()
    assert cleanup_with_now_default["removed_expired"] == 1


@pytest.mark.unit
def test_tts_cache_helpers_cover_put_hit_snapshot_and_hash() -> None:
    app_mod = _load_app_main()

    app_mod.settings.TTS_CACHE_ENABLED = True
    app_mod.settings.TTS_CACHE_TTL_SEC = 300
    app_mod.settings.TTS_CACHE_MAX_ENTRIES = 10
    app_mod.settings.TTS_CACHE_MAX_BYTES = 100000

    app_mod._tts_cache_store.clear()
    app_mod._tts_cache_stats.update(
        {"hits": 0, "misses": 0, "evictions_ttl": 0, "evictions_size": 0}
    )

    payload = {
        "mime_type": "audio/ogg",
        "request_hash": "hash-1",
        "is_placeholder": False,
        "artifact_path": "artifact.ogg",
        "detail": "detail",
    }
    cleanup = app_mod._tts_cache_put("cache-key", payload, 10.0)
    assert cleanup == {"removed_expired": 0, "removed_size": 0}
    assert app_mod._tts_cache_store["cache-key"]["created_at"] == 10.0

    cached, cached_cleanup = app_mod._tts_cache_get("cache-key", 12.0)
    assert cached == payload
    assert cached_cleanup == {"removed_expired": 0, "removed_size": 0}
    assert app_mod._tts_cache_store["cache-key"]["last_access"] == 12.0

    key_a = app_mod._tts_cache_key_from_payload("same-payload")
    key_b = app_mod._tts_cache_key_from_payload("same-payload")
    assert key_a == key_b

    snapshot = app_mod._tts_cache_stats_snapshot()
    assert snapshot.entries == 1
    assert snapshot.hits == 1
    assert snapshot.misses == 0
    assert snapshot.size_bytes > 0


@pytest.mark.unit
def test_tts_auth_and_token_extract_cover_direct_and_bearer_paths(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    app_mod = _load_app_main()
    monkeypatch.setattr(app_mod.settings, "TTS_AUTH_HEADER", "X-TTS-Token", raising=False)

    request = Request(
        {
            "type": "http",
            "headers": [(b"authorization", b"Bearer abc")],
        }
    )
    assert app_mod._extract_tts_token(request) == "abc"

    direct_request = Request(
        {
            "type": "http",
            "headers": [(b"x-tts-token", b"direct-secret")],
        }
    )
    assert app_mod._extract_tts_token(direct_request) == "direct-secret"

    monkeypatch.setattr(app_mod.settings, "TTS_AUTH_ENABLED", True, raising=False)
    monkeypatch.setattr(app_mod.settings, "TTS_AUTH_TOKEN", "secret", raising=False)
    with pytest.raises(HTTPException) as missing_exc:
        app_mod._require_tts_auth(Request({"type": "http", "headers": []}))
    assert missing_exc.value.status_code == 401

    with pytest.raises(HTTPException) as invalid_exc:
        app_mod._require_tts_auth(direct_request)
    assert invalid_exc.value.status_code == 403

    valid_request = Request(
        {
            "type": "http",
            "headers": [(b"x-tts-token", b"secret")],
        }
    )
    app_mod._require_tts_auth(valid_request)


@pytest.mark.unit
def test_get_content_and_basic_info_helpers_cover_mapping_and_attr_paths(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    app_mod = _load_app_main()
    from app.api.models import ChatMessage

    assert app_mod._get_content_from_message(ChatMessage(role="user", content="hi")) == "hi"
    assert app_mod._get_content_from_message({"content": "mapped"}) == "mapped"
    assert app_mod._get_content_from_message(_BrokenMapping()) == ""
    assert app_mod._get_content_from_message(SimpleNamespace(content=None)) == ""
    assert app_mod._get_content_from_message(SimpleNamespace(content=123)) == "123"

    monkeypatch.setenv("GIT_SHA", "gitsha")
    monkeypatch.setenv("BUILD_TIME", "buildtime")
    version = asyncio.run(app_mod.version_info())
    assert version["git_sha"] == "gitsha"
    assert version["build_time"] == "buildtime"
    assert asyncio.run(app_mod.health_check())["status"] == "ok"
    assert asyncio.run(app_mod.root())["message"] == "CVN Agent API ist aktiv"


@pytest.mark.unit
def test_request_context_middleware_json_and_http_exception_paths(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    app_mod = _load_app_main()
    monkeypatch.setattr(app_mod.settings, "LOG_JSON", True, raising=False)
    monkeypatch.setattr(app_mod.settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)

    logged: list[str] = []
    monkeypatch.setattr(app_mod.logger, "info", lambda message: logged.append(str(message)))
    monkeypatch.setattr(app_mod.logger, "exception", lambda message: logged.append(str(message)))

    request = Request(
        {
            "type": "http",
            "method": "GET",
            "path": "/demo",
            "headers": Headers({"X-Request-ID": "rid-1"}).raw,
            "client": ("127.0.0.1", 1234),
            "scheme": "http",
            "server": ("testserver", 80),
        }
    )

    async def _ok_call(_request: Request) -> Response:
        return Response(content="ok", status_code=204)

    response = asyncio.run(app_mod.request_context_mw(request, _ok_call))
    assert response.headers["X-Request-ID"] == "rid-1"
    assert any('"event": "request"' in entry for entry in logged)

    async def _boom_call(_request: Request) -> Response:
        raise HTTPException(status_code=418, detail="teapot", headers={"X-Extra": "1"})

    error_response = asyncio.run(app_mod.request_context_mw(request, _boom_call))
    assert error_response.status_code == 418
    assert error_response.headers["X-Request-ID"] == "rid-1"
    assert error_response.headers["X-Extra"] == "1"


@pytest.mark.unit
def test_request_context_middleware_covers_state_assignment_failure_and_plain_exception(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    app_mod = _load_app_main()
    monkeypatch.setattr(app_mod.settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(app_mod.settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)

    logged: list[str] = []
    monkeypatch.setattr(app_mod.logger, "exception", lambda message: logged.append(str(message)))

    class _BrokenState:
        def __setattr__(self, name: str, value: object) -> None:
            raise RuntimeError("no state")

    request = SimpleNamespace(
        headers={},
        url=SimpleNamespace(path="/broken"),
        method="GET",
        state=_BrokenState(),
        client=None,
    )

    async def _ok_call(_request: object) -> Response:
        return Response(content="ok", status_code=200)

    response = asyncio.run(app_mod.request_context_mw(request, _ok_call))
    assert response.headers["X-Request-ID"].startswith("req-")

    class _BrokenHeaders(dict[str, str]):
        def items(self):
            raise RuntimeError("bad headers")

    async def _http_exc_call(_request: object) -> Response:
        raise HTTPException(status_code=409, detail="conflict", headers=_BrokenHeaders())

    http_response = asyncio.run(app_mod.request_context_mw(request, _http_exc_call))
    assert http_response.status_code == 409
    assert http_response.headers["X-Request-ID"].startswith("req-")

    async def _runtime_call(_request: object) -> Response:
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError, match="boom"):
        asyncio.run(app_mod.request_context_mw(request, _runtime_call))
    assert any("Fehler bei /broken rid=req-" in entry for entry in logged)


@pytest.mark.api
@pytest.mark.unit
def test_rate_limiter_scope_cors_and_endpoint_edge_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    with pytest.MonkeyPatch.context() as local:
        local.setenv("RATE_LIMIT_ENABLED", "false")
        local.setenv("TTS_RATE_LIMIT_ENABLED", "true")
        local.setenv("TTS_RATE_LIMIT_REQUESTS_PER_MINUTE", "1")
        local.setenv("TTS_RATE_LIMIT_BURST", "0")
        local.setenv("TTS_RATE_LIMIT_WINDOW_SEC", "60")
        local.setenv("TTS_RATE_LIMIT_PATHS", '["/tts/voices"]')
        local.setenv("RATE_LIMIT_TRUSTED_IPS", '["trusted-host"]')
        local.setenv("BACKEND_CORS_ORIGINS", '["http://example.test"]')
        local.setenv("TTS_AUTH_ENABLED", "false")
        local.setenv("REQUEST_MAX_INPUT_CHARS", "5")
        local.setenv("REQUEST_TIMEOUT", "0.01")

        importlib.reload(importlib.import_module("app.core.settings"))
        app_mod = _load_app_main()

        assert any(m.cls.__name__ == "CORSMiddleware" for m in app_mod.app.user_middleware)

        limiter = app_mod._RateLimiter(FastAPI())

        async def _ok_call(_request: Request):
            return Response(content="ok", status_code=204)

        tts_request = Request(
            {
                "type": "http",
                "method": "GET",
                "path": "/tts/voices",
                "headers": [],
                "client": ("client-a", 1234),
                "scheme": "http",
                "server": ("testserver", 80),
            }
        )
        response = asyncio.run(limiter.dispatch(tts_request, _ok_call))
        assert response.headers["X-RateLimit-Limit"] == "1"

        with pytest.raises(HTTPException) as rate_exc:
            asyncio.run(limiter.dispatch(tts_request, _ok_call))
        assert rate_exc.value.status_code == 429

        trusted_request = Request(
            {
                "type": "http",
                "method": "GET",
                "path": "/tts/voices",
                "headers": [],
                "client": ("trusted-host", 1234),
                "scheme": "http",
                "server": ("testserver", 80),
            }
        )
        assert asyncio.run(limiter.dispatch(trusted_request, _ok_call)).status_code == 204

        class _BrokenResponse:
            status_code = 200

            class _Headers(dict[str, str]):
                def __setitem__(self, key: str, value: str) -> None:
                    raise RuntimeError("no headers")

            headers = _Headers()

        async def _broken_headers_call(_request: Request):
            return _BrokenResponse()

        broken_response = asyncio.run(
            limiter.dispatch(
                Request(
                    {
                        "type": "http",
                        "method": "GET",
                        "path": "/other",
                        "headers": [],
                        "client": ("client-b", 1234),
                        "scheme": "http",
                        "server": ("testserver", 80),
                    }
                ),
                _broken_headers_call,
            )
        )
        assert broken_response.status_code == 200

        client = TestClient(app_mod.app)
        assert client.get("/").status_code == 200

        too_long_chat = client.post(
            "/chat", json={"messages": [{"role": "user", "content": "abcdef"}]}
        )
        assert too_long_chat.status_code == 400

        too_long_tts = client.post(
            "/tts/synthesize",
            json={
                "text": "abcdef",
                "voice": "dummy-de",
                "language": "de",
                "output_format": "ogg",
                "sample_rate_hz": 22050,
                "settings": {},
            },
        )
        assert too_long_tts.status_code == 400

        from app.api.models import ChatRequest, ChatResponse

        async def _chat_ok(request: ChatRequest, **_kwargs: Any) -> ChatResponse:
            return ChatResponse(content="ok", model="unit")

        async def _stream_timeout(*_args: Any, **_kwargs: Any) -> Any:
            await asyncio.sleep(0.05)
            return iter(())

        async def _stream_boom(*_args: Any, **_kwargs: Any) -> Any:
            raise RuntimeError("stream kaputt")

        local.setattr(app_mod, "process_chat_request", _chat_ok)
        ok_chat = client.post("/chat", json={"messages": [{"role": "user", "content": "hi"}]})
        assert ok_chat.status_code == 200

        local.setattr(app_mod, "stream_chat_request", _stream_timeout)
        timeout_resp = client.post(
            "/chat/stream", json={"messages": [{"role": "user", "content": "hi"}]}
        )
        assert timeout_resp.status_code == 504

        local.setattr(app_mod, "stream_chat_request", _stream_boom)
        boom_resp = client.post(
            "/chat/stream", json={"messages": [{"role": "user", "content": "hi"}]}
        )
        assert boom_resp.status_code == 500

    importlib.reload(importlib.import_module("app.core.settings"))
    importlib.reload(importlib.import_module("app.main"))
