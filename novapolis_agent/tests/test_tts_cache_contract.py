from __future__ import annotations

import importlib
from typing import Any

import pytest
from fastapi.testclient import TestClient


def _payload(text: str) -> dict[str, Any]:
    return {
        "text": text,
        "voice": "dummy-de",
        "language": "de",
        "output_format": "ogg",
        "sample_rate_hz": 22050,
        "settings": {"temperature": 0.0},
    }


@pytest.mark.api
@pytest.mark.unit
def test_tts_cache_hit_miss_and_deterministic_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_CACHE_ENABLED", "true")
    monkeypatch.setenv("TTS_CACHE_TTL_SEC", "300")
    monkeypatch.setenv("TTS_CACHE_MAX_ENTRIES", "10")
    monkeypatch.setenv("TTS_CACHE_MAX_BYTES", "100000")
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "false")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    r1 = client.post("/tts/synthesize", json=_payload("Hallo Cache"))
    assert r1.status_code == 200
    d1 = r1.json()
    assert d1["cache_hit"] is False

    r2 = client.post("/tts/synthesize", json=_payload("Hallo Cache"))
    assert r2.status_code == 200
    d2 = r2.json()
    assert d2["cache_hit"] is True
    assert d2["cache_key"] == d1["cache_key"]

    scoped_payload = _payload("Hallo Cache")
    scoped_payload["session_id"] = "sess-cache-a"
    scoped_payload["channel"] = "pc"
    r3 = client.post("/tts/synthesize", json=scoped_payload)
    assert r3.status_code == 200
    d3 = r3.json()
    assert d3["cache_hit"] is False
    assert d3["cache_key"] != d1["cache_key"]
    assert d3["tts_manifest_path"].endswith("tts_manifest.jsonl")


@pytest.mark.api
@pytest.mark.unit
def test_tts_cache_size_limit_evicts_oldest(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_CACHE_ENABLED", "true")
    monkeypatch.setenv("TTS_CACHE_TTL_SEC", "300")
    monkeypatch.setenv("TTS_CACHE_MAX_ENTRIES", "1")
    monkeypatch.setenv("TTS_CACHE_MAX_BYTES", "100000")
    monkeypatch.setenv("TTS_AUTH_ENABLED", "false")
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "false")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    a1 = client.post("/tts/synthesize", json=_payload("A"))
    assert a1.status_code == 200
    b1 = client.post("/tts/synthesize", json=_payload("B"))
    assert b1.status_code == 200

    # A wurde durch max_entries=1 verdrängt -> erneuter MISS
    a2 = client.post("/tts/synthesize", json=_payload("A"))
    assert a2.status_code == 200
    assert a2.json()["cache_hit"] is False


@pytest.mark.api
@pytest.mark.unit
def test_tts_cache_cleanup_and_stats_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TTS_CACHE_ENABLED", "true")
    monkeypatch.setenv("TTS_CACHE_TTL_SEC", "300")
    monkeypatch.setenv("TTS_CACHE_MAX_ENTRIES", "10")
    monkeypatch.setenv("TTS_CACHE_MAX_BYTES", "100000")
    monkeypatch.setenv("TTS_AUTH_ENABLED", "true")
    monkeypatch.setenv("TTS_AUTH_TOKEN", "secret-token")
    monkeypatch.setenv("RATE_LIMIT_ENABLED", "false")
    monkeypatch.setenv("TTS_RATE_LIMIT_ENABLED", "false")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))
    client = TestClient(app_mod.app)

    headers = {"X-TTS-Token": "secret-token"}

    s1 = client.get("/tts/cache/stats", headers=headers)
    assert s1.status_code == 200
    d1 = s1.json()
    assert d1["enabled"] is True

    client.post("/tts/synthesize", json=_payload("cleanup"), headers=headers)

    c = client.post("/tts/cache/cleanup", headers=headers)
    assert c.status_code == 200
    dc = c.json()
    assert dc["status"] == "ok"
    assert isinstance(dc["entries"], int)
