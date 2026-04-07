from __future__ import annotations

import importlib

import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
@pytest.mark.parametrize(
    ("provider", "expected"),
    [
        ("dummy", "dummy"),
        ("null", "null"),
        ("coqui", "coqui"),
        ("ollama", "ollama"),
        ("openai", "openai"),
    ],
)
def test_tts_provider_health_switch(
    monkeypatch: pytest.MonkeyPatch, provider: str, expected: str
) -> None:
    monkeypatch.setenv("TTS_PROVIDER", provider)
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "false")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))

    client = TestClient(app_mod.app)
    resp = client.get("/tts/health")

    assert resp.status_code == 200
    assert resp.json()["provider"] == expected


@pytest.mark.api
@pytest.mark.unit
def test_tts_provider_coqui_runtime_uses_same_contract(
    monkeypatch: pytest.MonkeyPatch, tmp_path
) -> None:
    monkeypatch.setenv("TTS_PROVIDER", "coqui")
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RUNTIME_OUTPUT_DIR", str(tmp_path))

    providers_mod = importlib.reload(importlib.import_module("app.tts.providers"))

    def _fake_synthesis(**_kwargs):
        return b"OggS\x00\x01", "audio/ogg"

    monkeypatch.setattr(providers_mod, "_coqui_request_synthesis", _fake_synthesis)

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))

    client = TestClient(app_mod.app)
    payload = {
        "text": "Provider-Test",
        "voice": "dummy-de",
        "language": "de",
        "output_format": "ogg",
        "sample_rate_hz": 22050,
        "settings": {},
        "session_id": "sess-provider-1",
        "campaign_id": "camp-provider",
        "scene_id": "scene-provider",
        "slot_id": "slot-provider",
        "turn_id": "turn-provider",
        "channel": "ally",
    }
    resp = client.post("/tts/synthesize", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["provider"] == "coqui"
    assert data["status"] == "ok"
    assert data["is_placeholder"] is False
    assert data["artifact_path"]
    assert "sessions/sess-provider-1/ally/" in data["artifact_path"].replace("\\", "/")


@pytest.mark.api
@pytest.mark.unit
def test_tts_provider_coqui_unavailable_returns_503(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_PROVIDER", "coqui")
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "false")

    providers_mod = importlib.reload(importlib.import_module("app.tts.providers"))

    def _raise_unavailable(**_kwargs):
        raise providers_mod.TtsProviderUnavailableError("service down")

    monkeypatch.setattr(providers_mod, "_coqui_request_synthesis", _raise_unavailable)

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))

    client = TestClient(app_mod.app)
    payload = {
        "text": "Provider-Test",
        "voice": "coqui-default",
        "language": "de",
        "output_format": "ogg",
        "sample_rate_hz": 22050,
        "settings": {},
    }
    resp = client.post("/tts/synthesize", json=payload)

    assert resp.status_code == 503
    assert "provider unavailable" in resp.json().get("detail", "").lower()
