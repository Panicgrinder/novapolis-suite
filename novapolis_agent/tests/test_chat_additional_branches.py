from __future__ import annotations

import json
from types import SimpleNamespace
from typing import Any

import pytest
from app.api.models import ChatOptions, ChatRequest


class _FakeStreamResponse:
    def __init__(self, lines: list[str]) -> None:
        self._lines = lines

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool:
        return False

    def raise_for_status(self) -> None:
        return None

    async def aiter_lines(self):
        for line in self._lines:
            yield line


class _FakePostResponse:
    def __init__(self, payload: dict[str, Any]) -> None:
        self._payload = payload
        self.status_code = 200

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict[str, Any]:
        return self._payload


class _FakeAsyncClient:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.last_payload: dict[str, Any] | None = None

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool:
        return False

    def stream(self, method: str, url: str, json: dict[str, Any], headers: dict[str, Any]):
        self.last_payload = json
        # Include one raw line to trigger parser fallback branch.
        return _FakeStreamResponse(
            [
                "not-json-line",
                json_dumps({"message": {"content": "ok"}}),
                json_dumps({"done": True}),
            ]
        )

    async def post(self, url: str, json: dict[str, Any], headers: dict[str, Any]):
        self.last_payload = json
        return _FakePostResponse({"message": {"content": "post-answer"}})


def json_dumps(obj: Any) -> str:
    return json.dumps(obj, ensure_ascii=False)


@pytest.mark.asyncio
async def test_stream_chat_client_none_and_raw_line_fallback(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    monkeypatch.setattr(chat_module.httpx, "AsyncClient", _FakeAsyncClient)
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
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(chat_module.settings, "LOG_JSON", False, raising=False)

    req = ChatRequest(messages=[{"role": "user", "content": "hallo"}], options=ChatOptions())
    agen = await chat_module.stream_chat_request(req, client=None, request_id="r-stream")
    chunks = [c async for c in agen]

    assert any("data: not-json-line" in c for c in chunks)
    assert chunks[-1].startswith("event: done")


@pytest.mark.asyncio
async def test_stream_chat_apply_post_nameerror_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    monkeypatch.setattr(chat_module.httpx, "AsyncClient", _FakeAsyncClient)
    monkeypatch.setattr(
        chat_module, "compose_with_memory", lambda messages, session_id: _id_async(messages)
    )
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({}, "http://ollama")
    )
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)

    # First call raises NameError (text unresolved), fallback injects globals()["text"].
    def _nameerror_apply_post(*args: Any, **kwargs: Any):
        globals_dict = _nameerror_apply_post.__globals__
        if "text" not in globals_dict:
            raise NameError("text")
        return SimpleNamespace(action="rewrite", text=str(globals_dict["text"]) + "::rw")

    monkeypatch.setattr(chat_module, "apply_post", _nameerror_apply_post)

    req = ChatRequest(messages=[{"role": "user", "content": "hallo"}], options=ChatOptions())
    agen = await chat_module.stream_chat_request(req, client=None, request_id="r-ne")
    chunks = [c async for c in agen]

    assert any('"policy_post": "rewritten"' in c for c in chunks)
    assert any(c.startswith("event: delta") for c in chunks)


@pytest.mark.asyncio
async def test_process_chat_client_none_path(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    monkeypatch.setattr(chat_module.httpx, "AsyncClient", _FakeAsyncClient)
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
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(chat_module.settings, "LOG_JSON", True, raising=False)

    req = ChatRequest(messages=[{"role": "user", "content": "frage"}], options=ChatOptions())
    resp = await chat_module.process_chat_request(req, client=None, request_id="r-post")
    assert resp.content == "post-answer"


async def _id_async(messages: list[dict[str, str]]) -> list[dict[str, str]]:
    return list(messages)


class _CaptureStreamClient:
    def __init__(self, lines: list[str]) -> None:
        self._lines = lines
        self.last_payload: dict[str, Any] | None = None

    def stream(self, method: str, url: str, json: dict[str, Any], headers: dict[str, Any]):
        self.last_payload = json
        return _FakeStreamResponse(self._lines)


@pytest.mark.asyncio
async def test_stream_context_rag_and_prompt_freedom_exceptions(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    client = _CaptureStreamClient(
        [json_dumps({"message": {"content": "x"}}), json_dumps({"done": True})]
    )
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
    monkeypatch.setattr(
        chat_module,
        "modify_prompt_for_freedom",
        lambda *_: (_ for _ in ()).throw(RuntimeError("x")),
    )
    monkeypatch.setattr(
        chat_module, "load_context_notes", lambda *_: (_ for _ in ()).throw(RuntimeError("n"))
    )
    monkeypatch.setattr(chat_module.settings, "CONTENT_POLICY_ENABLED", True, raising=False)
    monkeypatch.setattr(chat_module.settings, "CONTEXT_NOTES_ENABLED", True, raising=False)
    monkeypatch.setattr(chat_module.settings, "RAG_ENABLED", True, raising=False)
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(chat_module.settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(
        "utils.rag.load_index", lambda *_: (_ for _ in ()).throw(FileNotFoundError("no"))
    )

    req = ChatRequest(messages=[{"role": "user", "content": "q"}], options={"canvas_count": 3})
    agen = await chat_module.stream_chat_request(req, client=client, request_id="ctx-rag")
    chunks = [c async for c in agen]

    assert chunks[-1].startswith("event: done")
    assert client.last_payload is not None
    msgs = client.last_payload["messages"]
    assert any(m.get("content", "").startswith("Canvas geladen:") for m in msgs)


@pytest.mark.asyncio
async def test_stream_session_memory_injection_from_dict_options(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    client = _CaptureStreamClient(
        ["", json_dumps({"message": {"content": "ok"}}), json_dumps({"done": True})]
    )
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
    monkeypatch.setattr(chat_module.settings, "SESSION_MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(
        chat_module,
        "session_memory",
        SimpleNamespace(get=lambda sid: [{"role": "assistant", "content": "mem"}]),
    )

    req = ChatRequest(messages=[{"role": "user", "content": "q"}], options={"session_id": "s1"})
    agen = await chat_module.stream_chat_request(req, client=client, request_id="mem-stream")
    _ = [c async for c in agen]

    assert client.last_payload is not None
    contents = [m.get("content", "") for m in client.last_payload["messages"]]
    assert "mem" in contents


@pytest.mark.asyncio
async def test_process_policy_pre_block_soft_fails_and_continues(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    monkeypatch.setattr(chat_module.httpx, "AsyncClient", _FakeAsyncClient)
    monkeypatch.setattr(
        chat_module, "compose_with_memory", lambda messages, session_id: _id_async(messages)
    )
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="block"))
    monkeypatch.setattr(
        chat_module, "apply_post", lambda text, **k: SimpleNamespace(action="allow")
    )
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({}, "http://ollama")
    )
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)

    req = ChatRequest(messages=[{"role": "user", "content": "frage"}], options=ChatOptions())
    resp = await chat_module.process_chat_request(req, client=None, request_id="pre-block")
    assert resp.content == "post-answer"


@pytest.mark.asyncio
async def test_process_session_memory_injection_from_dict_options(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    client = _FakeAsyncClient()
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
    monkeypatch.setattr(chat_module.settings, "SESSION_MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(
        chat_module,
        "session_memory",
        SimpleNamespace(get=lambda sid: [{"role": "assistant", "content": "hist"}]),
    )

    req = ChatRequest(
        messages=[{"role": "user", "content": "frage"}], options={"session_id": "sid-2"}
    )
    resp = await chat_module.process_chat_request(req, client=client, request_id="mem-post")

    assert resp.content == "post-answer"
    assert client.last_payload is not None
    assert any(m.get("content") == "hist" for m in client.last_payload["messages"])
