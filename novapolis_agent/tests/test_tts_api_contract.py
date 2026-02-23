from __future__ import annotations

import importlib
from typing import Any

import pytest
from fastapi.testclient import TestClient


def _client_without_tts_auth(monkeypatch: pytest.MonkeyPatch) -> TestClient:
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")
    monkeypatch.setenv("TTS_PROVIDER", "dummy")
    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    return TestClient(app_mod.app)


@pytest.mark.api
@pytest.mark.unit
def test_tts_health_contract() -> None:
    app_mod = importlib.import_module("app.main")
    client = TestClient(app_mod.app)
    resp = client.get("/tts/health")
    assert resp.status_code == 200
    data: dict[str, Any] = resp.json()
    assert data["status"] == "ok"
    assert data["provider"] == "dummy"
    assert isinstance(data["synthesize_ready"], bool)


@pytest.mark.api
@pytest.mark.unit
def test_tts_voices_contract(monkeypatch: pytest.MonkeyPatch) -> None:
    client = _client_without_tts_auth(monkeypatch)
    resp = client.get("/tts/voices")
    assert resp.status_code == 200
    data: dict[str, Any] = resp.json()
    assert data["provider"] == "dummy"
    assert isinstance(data["voices"], list)
    assert len(data["voices"]) >= 1


@pytest.mark.api
@pytest.mark.unit
def test_tts_synthesize_contract(monkeypatch: pytest.MonkeyPatch) -> None:
    client = _client_without_tts_auth(monkeypatch)
    payload = {
        "text": "Hallo Welt",
        "voice": "dummy-de",
        "language": "de",
        "output_format": "ogg",
        "sample_rate_hz": 22050,
        "settings": {"temperature": 0.0},
    }
    resp = client.post("/tts/synthesize", json=payload)
    assert resp.status_code == 200
    data: dict[str, Any] = resp.json()
    assert data["status"] == "placeholder"
    assert data["is_placeholder"] is True
    assert data["output_format"] == "ogg"
    assert data["mime_type"] == "audio/ogg"
    assert isinstance(data["request_hash"], str)
    assert len(data["request_hash"]) == 64
