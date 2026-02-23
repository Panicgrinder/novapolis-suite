from __future__ import annotations

import importlib

import pytest
from fastapi.testclient import TestClient


@pytest.mark.api
@pytest.mark.unit
def test_openapi_includes_chat_and_tts_contract_paths() -> None:
    app_mod = importlib.import_module("app.main")
    client = TestClient(app_mod.app)

    resp = client.get("/openapi.json")
    assert resp.status_code == 200
    spec = resp.json()

    assert "/chat" in spec["paths"]
    assert "/chat/stream" in spec["paths"]
    assert "/tts/health" in spec["paths"]
    assert "/tts/voices" in spec["paths"]
    assert "/tts/synthesize" in spec["paths"]

    chat_post = spec["paths"]["/chat"]["post"]
    tts_post = spec["paths"]["/tts/synthesize"]["post"]

    # Step 3 contract: explicit error codes and OpenAPI as technical SSOT
    for code in ["400", "429", "500", "504"]:
        assert code in chat_post["responses"]
        assert code in tts_post["responses"]


@pytest.mark.api
@pytest.mark.unit
def test_stream_input_limit_matches_chat_limit(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("REQUEST_MAX_INPUT_CHARS", "10")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))

    client = TestClient(app_mod.app)
    payload = {"messages": [{"role": "user", "content": "abcdefghijk"}]}
    resp = client.post("/chat/stream", json=payload)

    assert resp.status_code == 400
    assert "Input zu lang" in resp.json().get("detail", "")


@pytest.mark.api
@pytest.mark.unit
def test_chat_timeout_returns_504(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("REQUEST_TIMEOUT", "0.01")

    importlib.reload(importlib.import_module("app.core.settings"))
    app_mod = importlib.reload(importlib.import_module("app.main"))

    from typing import Any

    async def slow_call(*_a: Any, **_k: Any):
        import asyncio

        await asyncio.sleep(0.05)
        return {"content": "late", "model": "x"}

    monkeypatch.setattr(app_mod, "process_chat_request", slow_call)

    client = TestClient(app_mod.app)
    payload = {"messages": [{"role": "user", "content": "hi"}]}
    resp = client.post("/chat", json=payload)

    assert resp.status_code == 504
    assert "Zeitüberschreitung" in resp.json().get("detail", "")
