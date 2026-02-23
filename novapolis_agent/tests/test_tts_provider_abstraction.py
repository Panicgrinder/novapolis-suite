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
def test_tts_provider_coqui_scaffold_uses_same_contract(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_PROVIDER", "coqui")
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "false")

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
    }
    resp = client.post("/tts/synthesize", json=payload)

    assert resp.status_code == 200
    data = resp.json()
    assert data["provider"] == "coqui"
    assert data["is_placeholder"] is True
    assert "scaffold" in data["detail"].lower()
