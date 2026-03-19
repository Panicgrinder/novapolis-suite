from __future__ import annotations

from types import SimpleNamespace
from typing import Any

import pytest
from app.api.models import ChatRequest


class _Store:
    def __init__(self) -> None:
        self.rows: list[tuple[str, str, str]] = []

    async def append(self, session_id: str, role: str, content: str) -> None:
        self.rows.append((session_id, role, content))


class _BoomClient:
    def stream(self, *args: Any, **kwargs: Any):
        raise RuntimeError("boom-stream")


@pytest.mark.asyncio
async def test_stream_exception_path_logs_json_and_aborted_memory(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    store = _Store()
    monkeypatch.setattr(chat_module.settings, "LOG_JSON", True, raising=False)
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(
        chat_module, "compose_with_memory", lambda messages, session_id: _id_async(messages)
    )
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({}, "http://ollama")
    )
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: store)

    req = ChatRequest(messages=[{"role": "user", "content": "u"}], options={"session_id": "sid-x"})
    agen = await chat_module.stream_chat_request(req, client=_BoomClient(), request_id="rid-x")
    chunks = [c async for c in agen]

    assert any(c.startswith("event: error") for c in chunks)
    assert chunks[-1].startswith("event: done")
    assert store.rows == [("sid-x", "user", "u\n<!-- aborted=true -->")]


def test_append_shadow_mode_event_open_failure_branch(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    warnings: list[str] = []
    monkeypatch.setattr(chat_module.settings, "SHADOW_MODE_LOGGING_ENABLED", True, raising=False)
    monkeypatch.setattr(
        chat_module.settings, "SHADOW_MODE_LOG_PATH", "tmp/forbidden/shadow.jsonl", raising=False
    )
    monkeypatch.setattr(
        chat_module.settings, "SHADOW_MODE_REDACT_PREVIEW_ENABLED", True, raising=False
    )
    monkeypatch.setattr(chat_module.logger, "warning", lambda msg, *args: warnings.append(str(msg)))

    from pathlib import Path

    monkeypatch.setattr(Path, "open", lambda *a, **k: (_ for _ in ()).throw(OSError("nope")))

    req = ChatRequest(messages=[{"role": "user", "content": "x"}], options={"shadow_mode": True})
    chat_module._append_shadow_mode_event(
        request=req,
        eval_mode=False,
        unrestricted_mode=False,
        request_id="rid-shadow",
        stream=False,
        messages=[{"role": "user", "content": "x"}],
        response_text="y",
        policy_post="allow",
    )

    assert warnings


@pytest.mark.asyncio
async def test_process_options_model_dump_non_mapping(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    class _Resp:
        status_code = 200

        def raise_for_status(self) -> None:
            return None

        def json(self) -> dict[str, object]:
            return {"message": {"content": "ok"}}

    class _Client:
        async def post(self, *args: Any, **kwargs: Any):
            return _Resp()

    monkeypatch.setattr(chat_module.settings, "SESSION_MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(
        chat_module, "compose_with_memory", lambda messages, session_id: _id_async(messages)
    )
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module, "apply_post", lambda text, **k: SimpleNamespace(action="allow")
    )
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({}, "http://ollama")
    )

    class _BadOptions:
        def model_dump(self):
            return []

    req = ChatRequest.model_construct(
        messages=[{"role": "user", "content": "q"}], options=_BadOptions()
    )
    resp = await chat_module.process_chat_request(req, client=_Client(), request_id="bad-opt")
    assert resp.content == "ok"


async def _id_async(messages: list[dict[str, str]]) -> list[dict[str, str]]:
    return list(messages)
