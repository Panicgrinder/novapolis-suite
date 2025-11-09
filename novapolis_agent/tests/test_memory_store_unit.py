from __future__ import annotations

import asyncio
from pathlib import Path

import pytest

from app.core import memory


@pytest.mark.asyncio
async def test_inmemory_store_trims_turns_and_chars(monkeypatch: pytest.MonkeyPatch) -> None:
    store = memory.InMemoryStore()
    monkeypatch.setattr(memory.settings, "MEMORY_MAX_TURNS", 2, raising=False)
    monkeypatch.setattr(memory.settings, "MEMORY_MAX_CHARS", 8, raising=False)

    await store.append("s", "user", "1234")
    await store.append("s", "assistant", "5678")
    await store.append("s", "user", "abcd")

    window = await store.get_window("s", max_chars=50, max_turns=5)
    assert len(window) == 2
    assert window[-1]["content"] == "abcd"

    limited = await store.get_window("s", max_chars=4, max_turns=5)
    assert limited == [{"role": "user", "content": "abcd"}]

    trimmed_out = await store.get_window("s", max_chars=3, max_turns=5)
    assert trimmed_out == []

    await store.clear("s")
    assert await store.get_window("s", max_chars=10, max_turns=5) == []


@pytest.mark.asyncio
async def test_jsonl_store_persists_and_filters(tmp_path: Path) -> None:
    store = memory.JsonlStore(base_dir=tmp_path)

    await store.append("sess", "user", "hello")
    await store.append("sess", "assistant", "world")

    # Inject a malformed line to cover error handling
    path = store._path("sess")
    path.write_text(path.read_text(encoding="utf-8") + "{bad json}\n", encoding="utf-8")

    window = await store.get_window("sess", max_chars=20, max_turns=5)
    assert len(window) == 2

    trimmed = await store.get_window("sess", max_chars=5, max_turns=5)
    assert len(trimmed) == 1

    await store.clear("sess")
    assert not path.exists()


@pytest.mark.asyncio
async def test_compose_with_memory_variants(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    monkeypatch.setattr(memory, "_STORE", None, raising=False)
    monkeypatch.setattr(memory.settings, "MEMORY_ENABLED", True, raising=False)
    monkeypatch.setattr(memory.settings, "MEMORY_STORE", "jsonl", raising=False)
    monkeypatch.setattr(memory.settings, "MEMORY_DIR", tmp_path, raising=False)

    result = await memory.compose_with_memory([{"role": "user", "content": "hi"}], "sess-1")
    assert isinstance(result, list)

    immediate = await memory.compose_with_memory([{"role": "user", "content": "hi"}], None)
    assert immediate == [{"role": "user", "content": "hi"}]

    # Disable memory -> should return copy of messages immediately
    monkeypatch.setattr(memory.settings, "MEMORY_ENABLED", False, raising=False)
    out = await memory.compose_with_memory([{"role": "user", "content": "hi"}], "sess-1")
    assert out == [{"role": "user", "content": "hi"}]

    # Error path: make get_window raise
    monkeypatch.setattr(memory, "get_memory_store", lambda: _FailingStore(), raising=False)
    monkeypatch.setattr(memory.settings, "MEMORY_ENABLED", True, raising=False)
    fallback = await memory.compose_with_memory([{"role": "user", "content": "hi"}], "sess-2")
    assert fallback == [{"role": "user", "content": "hi"}]


class _FailingStore(memory.MemoryStore):
    async def append(self, session_id: str, role: str, content: str) -> None:  # pragma: no cover - not used
        raise RuntimeError

    async def get_window(self, session_id: str, max_chars: int, max_turns: int):
        raise RuntimeError("fail")

    async def clear(self, session_id: str) -> None:  # pragma: no cover - not used
        raise RuntimeError
