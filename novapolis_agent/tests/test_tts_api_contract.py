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
def test_tts_health_contract(monkeypatch: pytest.MonkeyPatch) -> None:
    client = _client_without_tts_auth(monkeypatch)
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
        "session_id": "sess-tts-1",
        "campaign_id": "camp-tts",
        "scene_id": "scene-a",
        "slot_id": "slot-01",
        "turn_id": "turn-01",
        "channel": "pc",
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
    assert data["contract_version"] == "text_rpg_session_v1"
    assert data["session_id"] == "sess-tts-1"
    assert data["campaign_id"] == "camp-tts"
    assert data["scene_id"] == "scene-a"
    assert data["slot_id"] == "slot-01"
    assert data["turn_id"] == "turn-01"
    assert data["channel"] == "pc"
    assert data["log_channels"] == ["world", "pc", "ally", "sys"]
    assert data["tts_manifest_path"].endswith("tts_manifest.jsonl")
