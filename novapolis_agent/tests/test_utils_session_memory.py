from __future__ import annotations

import pytest

from app.utils.session_memory import SessionMemory


@pytest.mark.unit
def test_session_memory_returns_copy() -> None:
    memory = SessionMemory()
    memory.put_and_trim("sid", [{"role": "user", "content": "eins"}], max_messages=10, max_chars=100)

    retrieved = memory.get("sid")
    retrieved.append({"role": "assistant", "content": "zwei"})

    assert memory.get("sid") == [{"role": "user", "content": "eins"}]


@pytest.mark.unit
def test_session_memory_trims_messages_and_characters() -> None:
    memory = SessionMemory()

    memory.put_and_trim("sid", [{"role": "user", "content": "eins"}], max_messages=2, max_chars=50)
    memory.put_and_trim("sid", [{"role": "assistant", "content": "zwei"}], max_messages=2, max_chars=50)
    memory.put_and_trim("sid", [{"role": "user", "content": "drei"}], max_messages=2, max_chars=50)

    assert [m["content"] for m in memory.get("sid")] == ["zwei", "drei"]

    memory.put_and_trim("sid", [{"role": "assistant", "content": "x" * 32}], max_messages=5, max_chars=10)
    assert memory.get("sid") == []
