from __future__ import annotations

import asyncio
import json
from types import SimpleNamespace

import app.api.chat as chat_module
import pytest
from app.api.models import ChatRequest
from pytest import MonkeyPatch


def _make_fake_stream_client(chunks: list[str]):
    class _Resp:
        status_code = 200

        def raise_for_status(self):
            return None

        async def aiter_lines(self):
            for c in chunks:
                yield json.dumps({"message": {"content": c}})
            yield json.dumps({"done": True})

    class _CM:
        async def __aenter__(self):
            return _Resp()

        async def __aexit__(self, exc_type, exc, tb):
            return False

    class _Client:
        def __init__(self, *a, **k):
            pass

        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            return False

        def stream(self, *args, **kwargs):
            return _CM()

    return _Client()


@pytest.mark.streaming
@pytest.mark.api
def test_stream_chat_sends_sse_chunks_and_done(monkeypatch: MonkeyPatch) -> None:

    def fake_factory(*a, **k) -> object:
        return _make_fake_stream_client(["a", "b"])
    monkeypatch.setattr(chat_module.httpx, "AsyncClient", fake_factory)
    req = ChatRequest(messages=[{"role": "user", "content": "hi"}])
    agen = asyncio.run(chat_module.stream_chat_request(req))

    collected: list[str] = []

    async def _consume():
        async for s in agen:
            collected.append(s)

    asyncio.run(_consume())

    assert any("data: a" in s for s in collected)
    assert any("data: b" in s for s in collected)
    assert any(s.startswith("event: done") for s in collected)


@pytest.mark.streaming
@pytest.mark.unit
def test_stream_chat_emits_delta_on_rewrite(monkeypatch: MonkeyPatch) -> None:
    chunks = ["Hallo", " Welt"]

    class _Resp:
        status_code = 200

        def raise_for_status(self) -> None:
            return None

        async def aiter_lines(self):
            for c in chunks:
                yield json.dumps({"message": {"content": c}})
            yield json.dumps({"done": True})

    class _CM:
        async def __aenter__(self):
            return _Resp()

        async def __aexit__(self, exc_type, exc, tb):
            return False

    class _Client:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            return False

        def stream(self, *args, **kwargs):
            return _CM()

    captured_meta: dict[str, str] = {}

    def _fake_apply_post(text: str, *, mode: str, profile_id: str | None = None):
        captured_meta["text"] = text
        return SimpleNamespace(action="rewrite", text=text.upper())

    monkeypatch.setattr(chat_module, "apply_post", _fake_apply_post)
    monkeypatch.setattr(chat_module.httpx, "AsyncClient", lambda *a, **k: _Client())

    req = ChatRequest(messages=[{"role": "user", "content": "hi"}])
    agen = asyncio.run(chat_module.stream_chat_request(req))

    events: list[str] = []

    async def _consume() -> None:
        async for ev in agen:
            events.append(ev)

    asyncio.run(_consume())

    assert captured_meta["text"] == "Hallo Welt"
    assert any(ev.startswith("data: Hallo") for ev in events)
    assert any(ev.startswith("data:  Welt") for ev in events)
    policy_events = [ev for ev in events if ev.startswith("event: meta")]
    assert any("policy_post" in ev and "rewritten" in ev for ev in policy_events)
    assert any(ev.startswith("event: delta") and "HALLO WELT" in ev for ev in events)
    assert events[-1].startswith("event: done")


@pytest.mark.streaming
@pytest.mark.unit
def test_stream_chat_yields_error_and_done(monkeypatch: MonkeyPatch) -> None:
    class _CM:
        async def __aenter__(self):
            raise RuntimeError("boom")

        async def __aexit__(self, exc_type, exc, tb):
            return False

    class _Client:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            return False

        def stream(self, *args, **kwargs):
            return _CM()

    monkeypatch.setattr(
        chat_module, "apply_post", lambda text, **_: SimpleNamespace(action="allow")
    )
    monkeypatch.setattr(chat_module.httpx, "AsyncClient", lambda *a, **k: _Client())

    req = ChatRequest(messages=[{"role": "user", "content": "hi"}])
    agen = asyncio.run(chat_module.stream_chat_request(req))

    events: list[str] = []

    async def _consume() -> None:
        async for ev in agen:
            events.append(ev)

    asyncio.run(_consume())

    assert events[0].startswith("event: meta")
    assert any(ev.startswith("event: error") and "boom" in ev for ev in events)
    assert events[-1].startswith("event: done")


@pytest.mark.streaming
@pytest.mark.unit
def test_stream_chat_policy_block(monkeypatch: MonkeyPatch) -> None:
    async def _noop_compose(messages, session_id, **_):
        return messages

    monkeypatch.setattr(chat_module, "compose_with_memory", _noop_compose)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: SimpleNamespace(action="block"))
    monkeypatch.setattr(
        chat_module, "apply_post", lambda text, **k: SimpleNamespace(action="allow")
    )

    req = ChatRequest(messages=[{"role": "user", "content": "hi"}])
    agen = asyncio.run(chat_module.stream_chat_request(req))

    events: list[str] = []

    async def _consume() -> None:
        async for ev in agen:
            events.append(ev)

    asyncio.run(_consume())

    assert events[0].startswith("event: error")
    assert events[-1].startswith("event: done")


@pytest.mark.streaming
@pytest.mark.unit
def test_stream_chat_appends_memory(monkeypatch: MonkeyPatch) -> None:
    class _Resp:
        status_code = 200

        def raise_for_status(self) -> None:
            return None

        async def aiter_lines(self):
            yield json.dumps({"message": {"content": "Hi"}})
            yield json.dumps({"done": True})

    class _CM:
        async def __aenter__(self):
            return _Resp()

        async def __aexit__(self, exc_type, exc, tb):
            return False

    class _Client:
        async def __aenter__(self):
            return self

        async def __aexit__(self, exc_type, exc, tb):
            return False

        def stream(self, *args, **kwargs):
            return _CM()

    async def _noop_compose(messages, session_id, **_):
        return messages

    class _Store:
        def __init__(self) -> None:
            self.calls: list[tuple[str, str, str]] = []

        async def append(self, session_id: str, role: str, content: str) -> None:
            self.calls.append((session_id, role, content))

    store = _Store()

    monkeypatch.setattr(chat_module, "compose_with_memory", _noop_compose)
    monkeypatch.setattr(chat_module, "get_memory_store", lambda: store)
    monkeypatch.setattr(chat_module, "apply_pre", lambda *a, **k: None)
    monkeypatch.setattr(
        chat_module, "apply_post", lambda text, **k: SimpleNamespace(action="allow")
    )
    monkeypatch.setattr(chat_module.httpx, "AsyncClient", lambda *a, **k: _Client())
    monkeypatch.setattr(chat_module.settings, "SESSION_MEMORY_ENABLED", False, raising=False)
    monkeypatch.setattr(chat_module.settings, "MEMORY_ENABLED", True, raising=False)

    req = ChatRequest(
        messages=[{"role": "user", "content": "hi"}], options={"session_id": "sess-1"}
    )
    agen = asyncio.run(chat_module.stream_chat_request(req))

    async def _consume() -> None:
        async for _ in agen:
            pass

    asyncio.run(_consume())

    assert ("sess-1", "user", "hi") in store.calls
    assert any(call[1] == "assistant" and call[2] == "Hi" for call in store.calls)
