from __future__ import annotations

import json
from types import SimpleNamespace
from typing import Any, cast

import httpx
import pytest
from fastapi import HTTPException

from app.api.models import ChatRequest


class _DummyStreamResponse:
    def __init__(self, lines: list[str]) -> None:
        self._lines = lines

    async def __aenter__(self) -> "_DummyStreamResponse":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> bool:
        return False

    def raise_for_status(self) -> None:
        return None

    async def aiter_lines(self):
        for line in self._lines:
            yield line


class _DummyStreamClient:
    def __init__(self, lines: list[str]) -> None:
        self._lines = lines
        self.last_payload: dict[str, Any] | None = None
        self.last_headers: dict[str, Any] | None = None

    def stream(self, method: str, url: str, json: dict[str, Any], headers: dict[str, Any]):
        self.last_payload = json
        self.last_headers = headers
        return _DummyStreamResponse(self._lines)


class _DummyStore:
    def __init__(self) -> None:
        self.records: list[tuple[str, str, str]] = []

    async def append(self, session_id: str, role: str, content: str) -> None:
        self.records.append((session_id, role, content))


class _DummyHTTPResponse:
    def __init__(self, payload: dict[str, Any]) -> None:
        self._payload = payload
        self.status_code = 200

    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict[str, Any]:
        return self._payload


class _DummyClient:
    def __init__(self, response: _DummyHTTPResponse) -> None:
        self._response = response
        self.last_payload: dict[str, Any] | None = None
        self.last_headers: dict[str, Any] | None = None

    async def post(self, url: str, json: dict[str, Any], headers: dict[str, Any]):
        self.last_payload = json
        self.last_headers = headers
        return self._response


class _FailingClient:
    async def post(self, *args: Any, **kwargs: Any):
        raise RuntimeError("network down")


@pytest.mark.asyncio
async def test_stream_chat_enriches_messages_and_rewrites(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    dummy_store = _DummyStore()
    lines = [
        json.dumps({"message": {"content": "hello"}}),
        json.dumps({"message": {"content": " world"}}),
        json.dumps({"done": True}),
    ]
    client = _DummyStreamClient(lines)

    monkeypatch.setattr(settings, "CONTENT_POLICY_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_PATHS", ["context.md"], raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_MAX_CHARS", 4000, raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "RAG_TOP_K", 1, raising=False)
    monkeypatch.setattr(settings, "RAG_INDEX_PATH", "rag-index.json", raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)

    monkeypatch.setattr(chat_module, "load_context_notes", lambda *_: "Kontext", raising=False)
    monkeypatch.setattr(chat_module, "modify_prompt_for_freedom", lambda text: text + " ++", raising=False)
    monkeypatch.setattr("utils.rag.load_index", lambda *_: object())
    monkeypatch.setattr("utils.rag.retrieve", lambda *_, **__: [{"source": "doc", "text": "Snippet"}])

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: [{"role": "assistant", "content": "memory"}]))
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda text, **k: SimpleNamespace(action="rewrite", text=text + " sanitized"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: dummy_store)
    monkeypatch.setattr(chat_module, "normalize_ollama_options", lambda opts, **_: ({"unit": True}, "http://ollama"))

    request = ChatRequest(
        messages=[{"role": "user", "content": "Hallo?"}],
        options={"session_id": "sess-1"},
        session_id="sess-1",
    )

    generator = await chat_module.stream_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-7",
    )
    chunks = [chunk async for chunk in generator]

    assert any("\"policy_post\": \"rewritten\"" in chunk for chunk in chunks)
    assert any("hello world sanitized" in chunk for chunk in chunks if "event: delta" in chunk)
    assert dummy_store.records == [
        ("sess-1", "user", "Hallo?"),
        ("sess-1", "assistant", "hello world sanitized"),
    ]
    assert client.last_payload is not None
    contents = [msg["content"] for msg in client.last_payload["messages"]]
    assert any(content.startswith("[RAG]") for content in contents)
    assert any(content.startswith("[Kontext-Notizen]") for content in contents)
    assert any(content == "memory" for content in contents)
    assert client.last_headers and client.last_headers["X-Request-ID"] == "req-7"


@pytest.mark.asyncio
async def test_stream_chat_policy_block(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "CONTENT_POLICY_ENABLED", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="block"))

    request = ChatRequest(messages=[{"role": "user", "content": "block me"}])

    generator = await chat_module.stream_chat_request(request, request_id="blocked")
    chunks = [chunk async for chunk in generator]

    assert chunks[0].startswith("event: error") and "policy_block" in chunks[0]
    assert chunks[-1].startswith("event: done")


@pytest.mark.asyncio
async def test_process_chat_request_rewrite_and_memory(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    dummy_store = _DummyStore()
    response = _DummyHTTPResponse({"message": {"content": "model answer"}})
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="rewrite", messages=[{"role": "user", "content": "pre rewritten"}]))
    monkeypatch.setattr(chat_module, "apply_post", lambda text, **k: SimpleNamespace(action="rewrite", text=text + " sanitized"))
    monkeypatch.setattr(chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: dummy_store)
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))

    request = ChatRequest(
        messages=[{"role": "user", "content": "original"}],
        options={"session_id": "sess-2"},
        session_id="sess-2",
    )

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-9",
    )

    assert result.content == "model answer sanitized"
    assert dummy_store.records == [
        ("sess-2", "user", "pre rewritten"),
        ("sess-2", "assistant", "model answer sanitized"),
    ]
    assert client.last_payload is not None
    assert client.last_payload["messages"][0]["content"] == "pre rewritten"


@pytest.mark.asyncio
async def test_process_chat_request_policy_post_block(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse({"message": {"content": "ignored"}})
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="block"))
    monkeypatch.setattr(chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: _DummyStore())
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))

    request = ChatRequest(
        messages=[{"role": "user", "content": "halt"}],
        options={"session_id": "sess-block"},
        session_id="sess-block",
    )

    with pytest.raises(HTTPException):
        await chat_module.process_chat_request(
            request,
            client=cast(httpx.AsyncClient, client),
        )


@pytest.mark.asyncio
async def test_process_chat_request_error_path_records_abort(monkeypatch: pytest.MonkeyPatch) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    dummy_store = _DummyStore()

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: dummy_store)
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))

    request = ChatRequest(
        messages=[{"role": "user", "content": "fail please"}],
        options={"session_id": "sess-err"},
        session_id="sess-err",
    )

    failing = _FailingClient()
    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, failing),
        request_id="err-1",
    )

    assert "Entschuldigung" in result.content
    assert dummy_store.records == [
        ("sess-err", "user", "fail please\n<!-- aborted=true -->"),
    ]
