from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
from typing import Any, cast

import httpx
import pytest
from app.api import sim
from app.api.models import ChatRequest
from fastapi import HTTPException


class _DummyStreamResponse:
    def __init__(self, lines: list[str]) -> None:
        self._lines = lines

    async def __aenter__(self) -> _DummyStreamResponse:
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
async def test_process_chat_request_support_ab_profile_prefers_better_candidate(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    async def _fake_run(**kwargs: Any):
        model_name = kwargs["model_name"]
        if model_name == "llama3.1:8b":
            return (
                "Vielen Dank fuer Ihre Rueckmeldung. Bitte senden Sie die "
                "Rechnungsnummer, damit wir den Fall schnell pruefen koennen.",
                1100,
            )
        if model_name == "qwen3.5:4b":
            return ("Szene: Novapolis meldet sich bei Ihnen. Optionen: ...", 900)
        raise AssertionError(model_name)

    monkeypatch.setattr(settings, "MODEL_NAME", "qwen3.5:4b", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: _DummyStore())
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))
    monkeypatch.setattr(chat_module, "_run_nonstream_ollama_request", _fake_run, raising=False)

    request = ChatRequest(
        messages=[
            {
                "role": "user",
                "content": (
                    "Bitte formuliere eine versandfaehige Support-Antwort "
                    "zur fehlenden Rechnungsnummer."
                ),
            }
        ],
        profile_id="support_de_ab",
    )
    result = await chat_module.process_chat_request(request)

    assert result.model == "llama3.1:8b"
    assert "Rechnungsnummer" in result.content
    assert "Szene:" not in result.content


@pytest.mark.asyncio
async def test_process_chat_request_support_ab_uses_optional_judge(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    calls: list[str] = []

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    async def _fake_run(**kwargs: Any):
        model_name = kwargs["model_name"]
        calls.append(model_name)
        if model_name == "llama3.1:8b":
            return ("Vielen Dank fuer Ihre Nachricht. Bitte senden Sie die Rechnungsnummer.", 1500)
        if model_name == "qwen3.5:4b":
            return ("Danke fuer Ihre Nachricht. Bitte senden Sie die Rechnungsnummer.", 1400)
        if model_name == "qwen2.5:7b":
            return ("B", 400)
        raise AssertionError(model_name)

    monkeypatch.setattr(settings, "MODEL_NAME", "qwen3.5:4b", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: _DummyStore())
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))
    monkeypatch.setattr(chat_module, "_run_nonstream_ollama_request", _fake_run, raising=False)

    request = ChatRequest(
        messages=[
            {
                "role": "user",
                "content": (
                    "Bitte formuliere eine versandfaehige Support-Antwort "
                    "zur fehlenden Rechnungsnummer."
                ),
            }
        ],
        profile_id="support_de_ab",
        options={"support_judge_model": "qwen2.5:7b", "support_force_judge": True},
    )
    result = await chat_module.process_chat_request(request)

    assert result.model == "qwen3.5:4b"
    assert result.content.startswith("Danke fuer Ihre Nachricht")
    assert calls == ["llama3.1:8b", "qwen3.5:4b", "qwen2.5:7b"]


@pytest.mark.asyncio
async def test_process_chat_request_support_ab_keeps_ranked_winner_on_invalid_judge_choice(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    calls: list[str] = []

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    async def _fake_run(**kwargs: Any):
        model_name = kwargs["model_name"]
        calls.append(model_name)
        if model_name == "llama3.1:8b":
            return (
                "Vielen Dank fuer Ihre Nachricht. Bitte senden Sie die Rechnungsnummer.",
                1500,
            )
        if model_name == "qwen3.5:4b":
            return ("Szene: Novapolis meldet sich bei Ihnen. Optionen: ...", 1400)
        if model_name == "qwen2.5:7b":
            return ("keine praefenz erkennbar", 400)
        raise AssertionError(model_name)

    monkeypatch.setattr(settings, "MODEL_NAME", "qwen3.5:4b", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: _DummyStore())
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))
    monkeypatch.setattr(chat_module, "_run_nonstream_ollama_request", _fake_run, raising=False)

    request = ChatRequest(
        messages=[
            {
                "role": "user",
                "content": (
                    "Bitte formuliere eine versandfaehige Support-Antwort "
                    "zur fehlenden Rechnungsnummer."
                ),
            }
        ],
        profile_id="support_de_ab",
        options={"support_judge_model": "qwen2.5:7b", "support_force_judge": True},
    )
    result = await chat_module.process_chat_request(request)

    assert result.model == "llama3.1:8b"
    assert result.content.startswith("Vielen Dank fuer Ihre Nachricht")
    assert calls == ["llama3.1:8b", "qwen3.5:4b", "qwen2.5:7b"]


@pytest.mark.asyncio
async def test_process_chat_request_support_ab_keeps_duration_tiebreak_on_invalid_judge_choice(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    calls: list[str] = []
    equal_support_answer = "Vielen Dank fuer Ihre Nachricht. Bitte senden Sie die Rechnungsnummer."

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    async def _fake_run(**kwargs: Any):
        model_name = kwargs["model_name"]
        calls.append(model_name)
        if model_name == "llama3.1:8b":
            return (equal_support_answer, 1500)
        if model_name == "qwen3.5:4b":
            return (equal_support_answer, 1400)
        if model_name == "qwen2.5:7b":
            return ("keine klare entscheidung", 400)
        raise AssertionError(model_name)

    monkeypatch.setattr(settings, "MODEL_NAME", "qwen3.5:4b", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: _DummyStore())
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))
    monkeypatch.setattr(chat_module, "_run_nonstream_ollama_request", _fake_run, raising=False)

    request = ChatRequest(
        messages=[
            {
                "role": "user",
                "content": (
                    "Bitte formuliere eine versandfaehige Support-Antwort "
                    "zur fehlenden Rechnungsnummer."
                ),
            }
        ],
        profile_id="support_de_ab",
        options={"support_judge_model": "qwen2.5:7b", "support_force_judge": True},
    )
    result = await chat_module.process_chat_request(request)

    assert result.model == "qwen3.5:4b"
    assert result.content == equal_support_answer
    assert calls == ["llama3.1:8b", "qwen3.5:4b", "qwen2.5:7b"]


@pytest.mark.asyncio
async def test_process_chat_request_sets_top_level_think_false_for_qwen35(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse({"message": {"content": "model answer"}})
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "qwen3.5:4b", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: _DummyStore())
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))

    request = ChatRequest(messages=[{"role": "user", "content": "hi"}])
    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
    )

    assert result.content == "model answer"
    assert client.last_payload is not None
    assert client.last_payload["model"] == "qwen3.5:4b"
    assert client.last_payload["think"] is False


@pytest.mark.asyncio
async def test_stream_chat_request_sets_top_level_think_false_for_qwen35(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    lines = [json.dumps({"message": {"content": "ok"}}), json.dumps({"done": True})]
    client = _DummyStreamClient(lines)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "qwen3.5:9b", raising=False)
    monkeypatch.setattr(settings, "CONTENT_POLICY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(chat_module, "apply_post", lambda *a, **k: SimpleNamespace(action="allow"))

    request = ChatRequest(messages=[{"role": "user", "content": "hi"}])
    generator = await chat_module.stream_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
    )
    chunks = []
    async for chunk in generator:
        chunks.append(chunk)

    assert any("event: done" in chunk for chunk in chunks)
    assert client.last_payload is not None
    assert client.last_payload["model"] == "qwen3.5:9b"
    assert client.last_payload["think"] is False


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
    monkeypatch.setattr(
        chat_module, "modify_prompt_for_freedom", lambda text: text + " ++", raising=False
    )
    monkeypatch.setattr("utils.rag.load_index", lambda *_: object())
    monkeypatch.setattr(
        "utils.rag.retrieve", lambda *_, **__: [{"source": "doc", "text": "Snippet"}]
    )

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(
        chat_module,
        "session_memory",
        SimpleNamespace(get=lambda _: [{"role": "assistant", "content": "memory"}]),
    )
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="rewrite", text=text + " sanitized"),
    )
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: dummy_store)
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({"unit": True}, "http://ollama")
    )

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

    assert any('"policy_post": "rewritten"' in chunk for chunk in chunks)
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
    monkeypatch.setattr(
        chat_module,
        "apply_pre",
        lambda *a, **k: SimpleNamespace(
            action="rewrite", messages=[{"role": "user", "content": "pre rewritten"}]
        ),
    )
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="rewrite", text=text + " sanitized"),
    )
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama")
    )
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
async def test_process_chat_request_skips_context_notes_when_disabled(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse({"message": {"content": "model answer"}})
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_PATHS", ["context.md"], raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_MAX_CHARS", 4000, raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )
    monkeypatch.setattr(chat_module, "load_context_notes", lambda *_: "Kontext", raising=False)

    request = ChatRequest(messages=[{"role": "user", "content": "weiter"}])

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-no-context",
    )

    assert result.content == "model answer"
    assert client.last_payload is not None
    contents = [message["content"] for message in client.last_payload["messages"]]
    assert not any(content.startswith("[Kontext-Notizen]") for content in contents)


@pytest.mark.asyncio
async def test_process_chat_request_injects_strict_rpg_contract_hint(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse({"message": {"content": "model answer"}})
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    prompt = (
        "Fuehre den produktiven Slice fort. Der letzte sichtbare Fortschritt war eine "
        "Scannerkarte. campaign_id=camp-7 session_id=sess-3 scene_id=scene-d5 "
        "slot_id=slot-03 turn_id=turn-0007. Antworte exakt mit Szene:, Konsequenz:, "
        "Optionen:, State_Patches:."
    )

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )

    request = ChatRequest(messages=[{"role": "user", "content": prompt}])

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-rpg-contract",
    )

    assert result.content.startswith("Szene: model answer")
    assert "Konsequenz:" in result.content
    assert "Optionen:" in result.content
    assert "State_Patches:" in result.content
    assert client.last_payload is not None
    contract_messages = [
        message["content"]
        for message in client.last_payload["messages"]
        if message["role"] == "system" and message["content"].startswith("[Text-RPG-Formatvertrag]")
    ]
    assert len(contract_messages) == 1
    contract_text = contract_messages[0]
    assert "1. , 2. , 3. ." in contract_text
    assert "Fuege keine weiteren sichtbaren Ueberschriften" in contract_text
    assert "State_Patches muss immer vorhanden sein" in contract_text
    assert "mindestens einmal exakt in Szene: oder Konsequenz:" in contract_text
    assert "slot-03" in contract_text
    assert "turn-0007" in contract_text
    assert "Scannerkarte" in contract_text
    assert "camp-7" not in contract_text


@pytest.mark.asyncio
async def test_process_chat_request_injects_strict_rpg_contract_hint_with_trailing_eval_hint(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse({"message": {"content": "model answer"}})
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    prompt = (
        "Antworte als Spielleitung fuer denselben Session-Pfad. Im internen Material "
        "existiert ein verdeckter Auftrag, der nicht an den PC verraten werden darf. "
        "Nutze exakt die Abschnittstitel Szene:, Konsequenz:, Optionen:, State_Patches:. "
        "Die sichtbare Lage darf nur ueber Geraeusch, Druck und Entscheidung gespielt "
        "werden. Liefere drei nummerierte Optionen."
    )
    eval_hint = (
        "Hinweis: Verwende diese Begriffe woertlich im Text: Szene:, Konsequenz:, Optionen:, "
        "State_Patches:, Geraeusch, Druck, Entscheidung"
    )

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )

    request = ChatRequest(
        messages=[
            {"role": "user", "content": prompt},
            {"role": "user", "content": eval_hint},
        ]
    )

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-rpg-contract-trailing-hint",
    )

    assert "Geraeusch" in result.content
    assert "Druck" in result.content
    assert "Entscheidung" in result.content
    assert client.last_payload is not None
    contract_messages = [
        message["content"]
        for message in client.last_payload["messages"]
        if message["role"] == "system" and message["content"].startswith("[Text-RPG-Formatvertrag]")
    ]
    assert len(contract_messages) == 1


def test_repair_strict_rpg_contract_uses_matching_prompt_before_eval_hint() -> None:
    from app.api import chat as chat_module

    prompt = (
        "Schreibe eine knappe Spielleiter-Antwort fuer slot-04. Nutze exakt die "
        "Abschnittstitel Szene:, Konsequenz:, Optionen:, State_Patches:. Unter Optionen "
        "muessen drei nummerierte Handlungswege stehen: eine vorsichtige, eine riskante "
        "und eine soziale Option."
    )
    eval_hint = (
        "Hinweis: Verwende diese Begriffe woertlich im Text: Szene:, Konsequenz:, Optionen:, "
        "State_Patches:, vorsichtige, riskante, soziale"
    )
    raw_response = (
        "Szene: Der alte Torbogen der Stadtmauer hat sich als ein Ort der Entscheidungen "
        "erwiesen.\n\n"
        "Konsequenz: Die Stadt Novapolis lebt von diesen Entscheidungen, die ihre Bewohner "
        "tagtaeglich treffen muessen.\n\n"
        "Optionen:\n"
        "1. steigen\n"
        "2. weitergehen\n"
        "3. abwarten\n\n"
        "State_Patches:\n[]"
    )

    repaired = chat_module._repair_strict_rpg_contract_response(
        [
            {"role": "user", "content": prompt},
            {"role": "user", "content": eval_hint},
        ],
        raw_response,
    )

    repaired_lines = repaired.splitlines()
    assert any(line.startswith("1. vorsichtige Option:") for line in repaired_lines)
    assert any(line.startswith("2. riskante Option:") for line in repaired_lines)
    assert any(line.startswith("3. soziale Option:") for line in repaired_lines)


@pytest.mark.asyncio
async def test_stream_chat_request_injects_strict_rpg_contract_hidden_anchor_hint(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response_text = (
        "Szene: stabil\n"
        "Konsequenz: offen\n"
        "Optionen:\n"
        "1. A\n"
        "2. B\n"
        "3. C\n"
        "State_Patches:\n"
        "[]"
    )
    lines = [
        json.dumps({"message": {"content": response_text}}),
        json.dumps({"done": True}),
    ]
    client = _DummyStreamClient(lines)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    prompt = (
        "Antworte als Spielleitung fuer denselben Session-Pfad. Im internen Material "
        "existiert ein verdeckter Auftrag, der nicht an den PC verraten werden darf. "
        "Nutze exakt die Abschnittstitel Szene:, Konsequenz:, Optionen:, State_Patches:. "
        "Die sichtbare Lage darf nur ueber Geraeusch, Druck und Entscheidung gespielt "
        "werden. Liefere drei nummerierte Optionen."
    )

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )

    request = ChatRequest(messages=[{"role": "user", "content": prompt}])

    generator = await chat_module.stream_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-stream-rpg-contract",
    )
    chunks = [chunk async for chunk in generator]

    assert any(chunk.startswith("event: done") for chunk in chunks)
    assert client.last_payload is not None
    contract_messages = [
        message["content"]
        for message in client.last_payload["messages"]
        if message["role"] == "system" and message["content"].startswith("[Text-RPG-Formatvertrag]")
    ]
    assert len(contract_messages) == 1
    contract_text = contract_messages[0]
    assert "Geraeusch" in contract_text
    assert "Druck" in contract_text
    assert "Entscheidung" in contract_text
    assert "verdeckter Auftrag" in contract_text
    assert "ASCII-Umschriften wie ae, oe oder ue" in contract_text


@pytest.mark.asyncio
async def test_process_chat_request_repairs_missing_strict_rpg_visible_anchors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse(
        {
            "message": {
                "content": (
                    "Szene: Die Scannerkarte liegt auf dem Tisch.\n\n"
                    "Konsequenz: Die Analyse beginnt sofort.\n\n"
                    "Optionen:\n"
                    "1. Weiter pruefen\n"
                    "2. Rueckzug antreten\n"
                    "3. Hilfe holen\n"
                    "State_Patches:\n[]"
                )
            }
        }
    )
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    prompt = (
        "Fuehre dieselbe Text-RPG-Session weiter. Nutze exakt die Abschnittstitel Szene:, "
        "Konsequenz:, Optionen:, State_Patches:. Voriger Stand: campaign_id=camp-7, "
        "session_id=sess-3, scene_id=scene-d5, slot_id=slot-03, turn_id=turn-0007. "
        "Der letzte sichtbare Fortschritt war eine Scannerkarte aus D5, die jetzt als "
        "Anschlussanker gelten soll. Liefere drei nummerierte Optionen."
    )

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )

    request = ChatRequest(messages=[{"role": "user", "content": prompt}])

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-rpg-contract-repair",
    )

    assert "slot-03" in result.content
    assert "turn-0007" in result.content
    assert "Scannerkarte" in result.content


@pytest.mark.asyncio
async def test_process_chat_request_repairs_strict_rpg_option_labels(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse(
        {
            "message": {
                "content": (
                    "Szene: slot-04 bleibt instabil.\n\n"
                    "Konsequenz: Drei Wege stehen offen.\n\n"
                    "Optionen:\n"
                    "1. Vorsichtig: Du gehst langsam weiter.\n"
                    "2. Riskant: Du rennst in den Korridor.\n"
                    "3. Sozial: Du suchst das Gespraech.\n"
                    "State_Patches:\n[]"
                )
            }
        }
    )
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    prompt = (
        "Schreibe eine knappe Spielleiter-Antwort fuer slot-04. Nutze exakt die "
        "Abschnittstitel Szene:, Konsequenz:, Optionen:, State_Patches:. Unter Optionen "
        "muessen drei nummerierte Handlungswege stehen: eine vorsichtige, eine riskante "
        "und eine soziale Option."
    )

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )

    request = ChatRequest(messages=[{"role": "user", "content": prompt}])

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-rpg-contract-options-repair",
    )

    result_lines = result.content.splitlines()
    assert "Optionen:" in result_lines
    assert any(line.startswith("1. vorsichtige Option:") for line in result_lines)
    assert any(line.startswith("2. riskante Option:") for line in result_lines)
    assert any(line.startswith("3. soziale Option:") for line in result_lines)
    assert "State_Patches:" in result_lines


def test_extract_visible_contract_anchors_normalizes_option_labels() -> None:
    from app.api import chat as chat_module

    prompt = (
        "Schreibe eine knappe Spielleiter-Antwort fuer slot-04. Nutze exakt die "
        "Abschnittstitel Szene:, Konsequenz:, Optionen:, State_Patches:. Unter Optionen "
        "muessen drei nummerierte Handlungswege stehen: eine vorsichtige, eine riskante "
        "und eine soziale Option."
    )

    anchors = chat_module._extract_visible_contract_anchors(prompt)

    assert "vorsichtige" in anchors
    assert "riskante" in anchors
    assert "soziale" in anchors
    assert "eine vorsichtige" not in anchors
    assert "eine soziale Option" not in anchors


@pytest.mark.asyncio
async def test_process_chat_request_rebuilds_inline_options_and_missing_state_patches(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse(
        {
            "message": {
                "content": (
                    "Szene: Der schmale Pfad bleibt offen.\n\n"
                    "Konsequenz: Die Ruinen wirken unruhig.\n\n"
                    "Optionen: 1. Vorsichtig naeher ruecken 2. Riskant lossprinten "
                    "3. Sozial die Gruppe abstimmen"
                )
            }
        }
    )
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    prompt = (
        "Schreibe eine knappe Spielleiter-Antwort fuer slot-04. Nutze exakt die "
        "Abschnittstitel Szene:, Konsequenz:, Optionen:, State_Patches:. Unter Optionen "
        "muessen drei nummerierte Handlungswege stehen: eine vorsichtige, eine riskante "
        "und eine soziale Option."
    )

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )

    request = ChatRequest(messages=[{"role": "user", "content": prompt}])

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-rpg-contract-inline-options-repair",
    )

    result_lines = result.content.splitlines()
    assert result_lines[0].startswith("Szene: ")
    assert "Optionen:" in result_lines
    assert any(line.startswith("1. vorsichtige Option:") for line in result_lines)
    assert any(line.startswith("2. riskante Option:") for line in result_lines)
    assert any(line.startswith("3. soziale Option:") for line in result_lines)
    assert "State_Patches:" in result_lines
    assert result.content.rstrip().endswith("[]")


@pytest.mark.asyncio
async def test_process_chat_request_repairs_reveal_case_with_numbered_options(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse(
        {
            "message": {
                "content": (
                    "Szene: Die Straßen von Novapolis sind verlassen, nur ein unbestimmtes "
                    "Geraune kommt aus einer dunklen Ecke.\n\n"
                    "Konsequenz: Das Gemurmel verstaerkt sich zu einem leisen Druck, der die "
                    "Gruppe irritiert. Die Atmosphaere ist angespannt, jeder bereit fuer eine "
                    "ungewisse Reaktion.\n\n"
                    "Optionen:\n"
                    "1. Den Schatten nachgehen.\n"
                    "2. Sich zurueckziehen.\n"
                    "3. Die Umgebung absichern.\n"
                    "State_Patches:\n[]"
                )
            }
        }
    )
    client = _DummyClient(response)

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    prompt = (
        "Antworte als Spielleitung fuer denselben Session-Pfad. Im internen Material "
        "existiert ein verdeckter Auftrag, der nicht an den PC verraten werden darf. "
        "Nutze exakt die Abschnittstitel Szene:, Konsequenz:, Optionen:, State_Patches:. "
        "Die sichtbare Lage darf nur ueber Geraeusch, Druck und Entscheidung gespielt "
        "werden. Liefere drei nummerierte Optionen."
    )

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="allow"),
    )
    monkeypatch.setattr(
        chat_module,
        "normalize_ollama_options",
        lambda opts, **_: ({"opt": True}, "http://ollama"),
    )

    request = ChatRequest(messages=[{"role": "user", "content": prompt}])

    result = await chat_module.process_chat_request(
        request,
        client=cast(httpx.AsyncClient, client),
        request_id="req-rpg-contract-reveal-repair",
    )

    assert "Geraeusch" in result.content
    assert "Geraune" in result.content or "Geraeusch" in result.content
    assert "Druck" in result.content
    assert "Entscheidung" in result.content
    result_lines = result.content.splitlines()
    assert any(line.startswith("1. ") for line in result_lines)
    assert any(line.startswith("2. ") for line in result_lines)
    assert any(line.startswith("3. ") for line in result_lines)
    assert "State_Patches:" in result_lines


@pytest.mark.asyncio
async def test_process_chat_request_injects_orchestrator_context(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse(
        {
            "message": {
                "content": (
                    "Szene: Die Schleuse antwortet auf die Scannerkarte.\n\n"
                    "Konsequenz: Reflex haelt den Materiallauf stabil.\n\n"
                    "Optionen:\n1. Materiallauf sichern\n2. Rueckzug\n3. Analyse\n\n"
                    "State_Patches:\n"
                    "mission.materiallauf.progress = 2\n"
                    "- Scannerkarte bleibt als Anschlussanker markiert"
                )
            }
        }
    )
    client = _DummyClient(response)
    original_store_dir = sim._SESSION_STORE_DIR

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_PATHS", ["context.md"], raising=False)
    monkeypatch.setattr(settings, "CONTEXT_NOTES_MAX_CHARS", 4000, raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "RAG_TOP_K", 2, raising=False)
    monkeypatch.setattr(settings, "RAG_INDEX_PATH", "rag-index.json", raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module, "apply_post", lambda text, **k: SimpleNamespace(action="allow")
    )
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama")
    )
    monkeypatch.setattr(
        chat_module,
        "load_context_notes",
        lambda *_: "D5 verbindet Materiallauf und Schleusenstatus.",
    )
    monkeypatch.setattr("utils.rag.load_index", lambda *_: object())
    monkeypatch.setattr(
        "utils.rag.retrieve",
        lambda *_, **__: [
            {"source": "rp-ssot", "text": "Reflex assistiert dem Materiallauf nach C6."}
        ],
    )

    sim._SESSION_STORE_DIR = tmp_path / "sim_sessions"
    sim.upsert_session(
        "sess-3",
        sim.SessionUpsertRequest(
            campaign_id="camp-7",
            scene_id="scene-d5",
            slot_id="slot-03",
            turn_id="turn-1",
            pc_log=[{"role": "assistant", "content": "Voriger Zug"}],
            state_patches=[
                sim.StatePatchRecord(
                    scope="session", op="set", path="mission.anchor", value="Scannerkarte"
                )
            ],
        ),
    )

    try:
        request = ChatRequest(
            messages=[{"role": "user", "content": "weiter"}],
            profile_id="text_rpg",
            session_id="sess-3",
            options={
                "orchestrator_enabled": True,
                "campaign_id": "camp-7",
                "scene_id": "scene-d5",
                "slot_id": "slot-03",
                "turn_id": "turn-2",
                "retrieval_query": "D5 Reflex Materiallauf",
                "public_context": "Reflex bleibt an der Schleuse.",
                "hidden_context": "Die Schleuse klemmt wegen verdecktem Druckverlust.",
                "scheduler_hints": ["halte den Materiallauf stabil"],
                "state_patch_hints": ["mission.materiallauf.progress += 1"],
            },
        )

        result = await chat_module.process_chat_request(
            request,
            client=cast(httpx.AsyncClient, client),
            request_id="req-orch",
        )

        assert "State_Patches:" in result.content
        assert result.contract_version == "text_rpg_session_v1"
        assert result.session_id == "sess-3"
        assert result.campaign_id == "camp-7"
        assert result.scene_id == "scene-d5"
        assert result.slot_id == "slot-03"
        assert result.turn_id == "turn-2"
        assert result.session_status == "active"
        assert result.resume_checkpoint_id == "turn-2"
        assert result.replay_checkpoint_id == "turn-2"
        assert result.log_channels == ["world", "pc", "ally", "sys"]
        assert result.turn_context is not None
        assert result.turn_context.turn_mode == "standard"
        assert result.turn_context.turn_window_minutes == 30
        assert result.carry_over == []
        assert client.last_payload is not None
        contents = [message["content"] for message in client.last_payload["messages"]]
        orchestrator_messages = [
            content for content in contents if content.startswith("[Text-RPG-Orchestrator]")
        ]
        assert orchestrator_messages
        orchestrator_text = orchestrator_messages[0]
        assert "campaign_id: camp-7" in orchestrator_text
        assert "[Session-Stand intern]" in orchestrator_text
        assert "mission.anchor" in orchestrator_text
        assert "[PC-Sicht]" in orchestrator_text
        assert "[Projektkontext-Notizen intern]" in orchestrator_text
        assert "D5 verbindet Materiallauf" in orchestrator_text
        assert "[Retrieval-Query]" in orchestrator_text
        assert "D5 Reflex Materiallauf" in orchestrator_text
        assert "[RP-/Projektkontext-Retrieval intern]" in orchestrator_text
        assert "Reflex assistiert dem Materiallauf" in orchestrator_text
        assert "Reflex bleibt an der Schleuse." in orchestrator_text
        assert "[Hidden-Context intern]" in orchestrator_text
        assert "verdecktem Druckverlust" in orchestrator_text
        assert "[Scheduler-Hinweise]" in orchestrator_text
        assert "[State-Patch-Ziele]" in orchestrator_text
        assert not any(content.startswith("[RAG]") for content in contents)
        assert not any(content.startswith("[Kontext-Notizen]") for content in contents)

        stored = sim.load_session_record("sess-3")
        assert stored is not None
        assert stored.turn_id == "turn-2"
        assert stored.turn_context.turn_window_minutes == 30
        assert stored.pc_log[-1]["content"].startswith("Szene: Die Schleuse")
        assert stored.state_patches[-2].path == "mission.materiallauf.progress"
        assert stored.state_patches[-1].value == "Scannerkarte bleibt als Anschlussanker markiert"
    finally:
        sim._SESSION_STORE_DIR = original_store_dir


@pytest.mark.unit
def test_upsert_session_rejects_unsupported_contract_version(tmp_path: Path) -> None:
    original_store_dir = sim._SESSION_STORE_DIR
    sim._SESSION_STORE_DIR = tmp_path / "sim_sessions"
    try:
        with pytest.raises(HTTPException) as exc_info:
            sim.upsert_session(
                "bad-contract",
                sim.SessionUpsertRequest(contract_version="text_rpg_session_v0"),
            )
        assert exc_info.value.status_code == 400
        assert exc_info.value.detail == "unsupported contract_version"
    finally:
        sim._SESSION_STORE_DIR = original_store_dir


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
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama")
    )
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
async def test_process_chat_request_error_path_records_abort(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
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
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama")
    )
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


@pytest.mark.asyncio
async def test_process_chat_request_writes_shadow_log(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from app.api import chat as chat_module

    settings = chat_module.settings
    response = _DummyHTTPResponse({"message": {"content": "model answer"}})
    client = _DummyClient(response)
    shadow_log = tmp_path / "shadow_mode.jsonl"

    async def _compose(messages, session_id, **kwargs):
        return list(messages)

    monkeypatch.setattr(settings, "MODEL_NAME", "unit-model", raising=False)
    monkeypatch.setattr(settings, "MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(settings, "REQUEST_ID_HEADER", "X-Request-ID", raising=False)
    monkeypatch.setattr(settings, "LOG_TRUNCATE_CHARS", 50, raising=False)
    monkeypatch.setattr(settings, "LOG_JSON", False, raising=False)
    monkeypatch.setattr(settings, "RAG_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "RAG_INDEX_PATH", "eval/results/rag/index.json", raising=False)
    monkeypatch.setattr(settings, "SHADOW_MODE_LOGGING_ENABLED", True, raising=False)
    monkeypatch.setattr(settings, "SHADOW_MODE_LOG_PATH", str(shadow_log), raising=False)
    monkeypatch.setattr(chat_module, "compose_with_memory", _compose, raising=False)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="allow"))
    monkeypatch.setattr(
        chat_module,
        "apply_post",
        lambda text, **k: SimpleNamespace(action="rewrite", text=text + " sanitized"),
    )
    monkeypatch.setattr(
        chat_module, "normalize_ollama_options", lambda opts, **_: ({"opt": True}, "http://ollama")
    )
    monkeypatch.setattr(chat_module, "session_memory", SimpleNamespace(get=lambda _: []))

    request = ChatRequest(
        messages=[{"role": "user", "content": "sensitive input"}],
        options={"session_id": "sess-shadow", "shadow_mode": True},
        session_id="sess-shadow",
    )

    result = await chat_module.process_chat_request(
        request,
        eval_mode=False,
        client=cast(httpx.AsyncClient, client),
        request_id="shadow-1",
    )

    assert result.content == "model answer sanitized"
    assert shadow_log.exists()
    lines = shadow_log.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 1
    payload = json.loads(lines[0])
    assert payload["request_id"] == "shadow-1"
    assert payload["stream"] is False
    assert payload["policy_post"] == "rewritten"
    assert payload["rag_enabled"] is True
    assert payload["response_chars"] == len("model answer sanitized")
    assert payload["user_chars"] == len("sensitive input")
    assert payload["user_hash"] and payload["response_hash"]
