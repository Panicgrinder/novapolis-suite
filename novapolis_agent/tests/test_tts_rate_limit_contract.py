from __future__ import annotations

import importlib
from typing import Any

import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
def test_tts_rate_limit_blocks_second_request(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "true")
    monkeypatch.setenv("TTS_RATE_LIMIT_REQUESTS_PER_MINUTE", "1")
    monkeypatch.setenv("TTS_RATE_LIMIT_BURST", "0")
    monkeypatch.setenv("TTS_RATE_LIMIT_WINDOW_SEC", "60")
    monkeypatch.setenv("RATE_LIMIT_TRUSTED_IPS", "[]")
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))

    client = TestClient(app_mod.app)
    r1 = client.get("/tts/voices")
    assert r1.status_code == 200

    r2 = client.get("/tts/voices")
    assert r2.status_code == 429
    assert r2.headers.get("Retry-After") is not None
    assert r2.headers.get("X-RateLimit-Limit") == "1"


@pytest.mark.api
@pytest.mark.unit
def test_tts_rate_limit_does_not_throttle_chat(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "true")
    monkeypatch.setenv("TTS_RATE_LIMIT_REQUESTS_PER_MINUTE", "1")
    monkeypatch.setenv("TTS_RATE_LIMIT_BURST", "0")
    monkeypatch.setenv("TTS_RATE_LIMIT_WINDOW_SEC", "60")
    monkeypatch.setenv("RATE_LIMIT_TRUSTED_IPS", "[]")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))

    async def _ok_chat(*_a: Any, **_k: Any) -> dict[str, str]:
        return {"content": "ok", "model": "dummy"}

    monkeypatch.setattr(app_mod, "process_chat_request", _ok_chat)

    client = TestClient(app_mod.app)
    payload = {"messages": [{"role": "user", "content": "hi"}]}

    c1 = client.post("/chat", json=payload)
    c2 = client.post("/chat", json=payload)

    assert c1.status_code == 200
    assert c2.status_code == 200
