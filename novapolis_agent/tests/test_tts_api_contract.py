from __future__ import annotations

from typing import Any

import pytest
from app.main import app
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
def test_tts_health_contract() -> None:
    client = TestClient(app)
    resp = client.get("/tts/health")
    assert resp.status_code == 200
    data: dict[str, Any] = resp.json()
    assert data["status"] == "ok"
    assert data["provider"] == "dummy"
    assert isinstance(data["synthesize_ready"], bool)


@pytest.mark.api
@pytest.mark.unit
def test_tts_voices_contract() -> None:
    client = TestClient(app)
    resp = client.get("/tts/voices")
    assert resp.status_code == 200
    data: dict[str, Any] = resp.json()
    assert data["provider"] == "dummy"
    assert isinstance(data["voices"], list)
    assert len(data["voices"]) >= 1


@pytest.mark.api
@pytest.mark.unit
def test_tts_synthesize_contract() -> None:
    client = TestClient(app)
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
