from __future__ import annotations

import asyncio
import json
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Deque, Dict, List, Mapping, Optional

from .settings import settings


@dataclass
class _Turn:
    role: str
    content: str

    def to_message(self) -> Dict[str, str]:
        return {"role": self.role, "content": self.content}


class MemoryStore:
    async def append(self, session_id: str, role: str, content: str) -> None:
        raise NotImplementedError

    async def get_window(self, session_id: str, max_chars: int, max_turns: int) -> List[Dict[str, str]]:
        raise NotImplementedError

    async def clear(self, session_id: str) -> None:
        raise NotImplementedError


class InMemoryStore(MemoryStore):
    def __init__(self) -> None:
        self._by_id: Dict[str, Deque[_Turn]] = {}
        self._locks: Dict[str, asyncio.Lock] = {}
        self._global_lock = asyncio.Lock()

    async def _ensure_lock(self, session_id: str) -> asyncio.Lock:
        async with self._global_lock:
            lock = self._locks.get(session_id)
            if lock is None:
                lock = asyncio.Lock()
                self._locks[session_id] = lock
            return lock

    async def append(self, session_id: str, role: str, content: str) -> None:
        lock = await self._ensure_lock(session_id)
        async with lock:
            queue: Optional[Deque[_Turn]] = self._by_id.get(session_id)
            if queue is None:
                queue = deque[_Turn]()
                self._by_id[session_id] = queue
            queue.append(_Turn(role=role, content=content))
            max_turns = max(0, int(getattr(settings, "MEMORY_MAX_TURNS", 20)))
            if max_turns > 0:
                while len(queue) > max_turns:
                    queue.popleft()
            max_chars = max(0, int(getattr(settings, "MEMORY_MAX_CHARS", 8000)))
            if max_chars > 0:
                while queue and sum(len(turn.content) for turn in queue) > max_chars:
                    queue.popleft()

    async def get_window(self, session_id: str, max_chars: int, max_turns: int) -> List[Dict[str, str]]:
        lock = await self._ensure_lock(session_id)
        async with lock:
            queue: Optional[Deque[_Turn]] = self._by_id.get(session_id)
            if not queue:
                return []
            items: List[_Turn] = list(queue)
        items = items[-max_turns:] if max_turns > 0 else items
        while items and max_chars > 0 and sum(len(t.content) for t in items) > max_chars:
            items.pop(0)
        return [turn.to_message() for turn in items]

    async def clear(self, session_id: str) -> None:
        lock = await self._ensure_lock(session_id)
        async with lock:
            self._by_id.pop(session_id, None)


class JsonlStore(MemoryStore):
    def __init__(self, base_dir: Path) -> None:
        self.base_dir = base_dir
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self._locks: Dict[str, asyncio.Lock] = {}
        self._global_lock = asyncio.Lock()

    async def _ensure_lock(self, session_id: str) -> asyncio.Lock:
        async with self._global_lock:
            lock = self._locks.get(session_id)
            if lock is None:
                lock = asyncio.Lock()
                self._locks[session_id] = lock
            return lock

    def _path(self, session_id: str) -> Path:
        safe = "".join(ch for ch in session_id if ch.isalnum() or ch in ("-", "_"))
        return self.base_dir / f"session_{safe}.jsonl"

    async def append(self, session_id: str, role: str, content: str) -> None:
        lock = await self._ensure_lock(session_id)
        async with lock:
            path = self._path(session_id)
            line = json.dumps({"role": role, "content": content}, ensure_ascii=False)
            with path.open("a", encoding="utf-8") as handle:
                handle.write(line + "\n")

    async def get_window(self, session_id: str, max_chars: int, max_turns: int) -> List[Dict[str, str]]:
        lock = await self._ensure_lock(session_id)
        async with lock:
            path = self._path(session_id)
            if not path.exists():
                return []
            try:
                with path.open("r", encoding="utf-8") as handle:
                    lines = handle.readlines()
            except Exception:
                return []
        turns: List[_Turn] = []
        for line in lines[-max_turns:]:
            try:
                obj = json.loads(line)
                role = str(obj.get("role", "user"))
                content = str(obj.get("content", ""))
                turns.append(_Turn(role=role, content=content))
            except Exception:
                continue
        while turns and max_chars > 0 and sum(len(t.content) for t in turns) > max_chars:
            turns.pop(0)
        return [turn.to_message() for turn in turns]

    async def clear(self, session_id: str) -> None:
        lock = await self._ensure_lock(session_id)
        async with lock:
            path = self._path(session_id)
            try:
                if path.exists():
                    path.unlink()
            except Exception:
                pass


_STORE: Optional[MemoryStore] = None


def get_memory_store() -> MemoryStore:
    global _STORE
    if _STORE is not None:
        return _STORE
    try:
        if not getattr(settings, "MEMORY_ENABLED", True):
            _STORE = InMemoryStore()
            return _STORE
        store_kind = getattr(settings, "MEMORY_STORE", "inmemory")
        if store_kind == "jsonl":
            _STORE = JsonlStore(base_dir=getattr(settings, "MEMORY_DIR", Path(".data/memory")))
        else:
            _STORE = InMemoryStore()
        return _STORE
    except Exception:
        _STORE = InMemoryStore()
        return _STORE


async def compose_with_memory(
    messages: List[Mapping[str, str]],
    session_id: Optional[str],
    *,
    max_chars: Optional[int] = None,
    max_turns: Optional[int] = None,
) -> List[Dict[str, str]]:
    if not session_id or not getattr(settings, "MEMORY_ENABLED", True):
        return [dict(message) for message in messages]
    try:
        store = get_memory_store()
        mc = max_chars if isinstance(max_chars, int) else int(getattr(settings, "MEMORY_MAX_CHARS", 8000))
        mt = max_turns if isinstance(max_turns, int) else int(getattr(settings, "MEMORY_MAX_TURNS", 20))
        window = await store.get_window(session_id, max_chars=mc, max_turns=mt)
        composed: List[Dict[str, str]] = list(window) + [dict(message) for message in messages]
        while composed and mc > 0 and sum(len(str(m.get("content", ""))) for m in composed) > mc:
            composed.pop(0)
        return composed
    except Exception:
        return [dict(message) for message in messages]


__all__ = [
    "MemoryStore",
    "InMemoryStore",
    "JsonlStore",
    "get_memory_store",
    "compose_with_memory",
]
