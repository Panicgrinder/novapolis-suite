from __future__ import annotations

import importlib

import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
def test_tts_auth_disabled_allows_voices() -> None:
    import os

    os.environ["TTS_PROVIDER"] = "dummy"
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    resp = client.get("/tts/voices")
    assert resp.status_code == 200


@pytest.mark.api
@pytest.mark.unit
def test_tts_auth_enabled_missing_token_returns_401(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_AUTH_ENABLED", "true")
    monkeypatch.setenv("TTS_AUTH_TOKEN", "secret-token")
    monkeypatch.setenv("TTS_PROVIDER", "dummy")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    resp = client.get("/tts/voices")
    assert resp.status_code == 401


@pytest.mark.api
@pytest.mark.unit
def test_tts_auth_enabled_wrong_token_returns_403(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_AUTH_ENABLED", "true")
    monkeypatch.setenv("TTS_AUTH_TOKEN", "secret-token")
    monkeypatch.setenv("TTS_PROVIDER", "dummy")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    resp = client.get("/tts/voices", headers={"X-TTS-Token": "wrong"})
    assert resp.status_code == 403


@pytest.mark.api
@pytest.mark.unit
def test_tts_auth_enabled_valid_token_returns_200(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_AUTH_ENABLED", "true")
    monkeypatch.setenv("TTS_AUTH_TOKEN", "secret-token")
    monkeypatch.setenv("TTS_PROVIDER", "dummy")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    resp = client.get("/tts/voices", headers={"X-TTS-Token": "secret-token"})
    assert resp.status_code == 200


@pytest.mark.api
@pytest.mark.unit
def test_tts_auth_bearer_header_supported(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_AUTH_ENABLED", "true")
    monkeypatch.setenv("TTS_AUTH_TOKEN", "secret-token")
    monkeypatch.setenv("TTS_PROVIDER", "dummy")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    payload = {
        "text": "Hallo",
        "voice": "dummy-de",
        "language": "de",
        "output_format": "ogg",
        "sample_rate_hz": 22050,
        "settings": {},
    }
    resp = client.post(
        "/tts/synthesize",
        json=payload,
        headers={"Authorization": "Bearer secret-token"},
    )
    assert resp.status_code == 200
