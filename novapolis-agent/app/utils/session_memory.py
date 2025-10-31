"""Einfache In-Memory Sitzungsverwaltung."""

from __future__ import annotations

from threading import RLock
from typing import Dict, List, Mapping


class SessionMemory:
    def __init__(self) -> None:
        self._by_id: Dict[str, List[Mapping[str, str]]] = {}
        self._lock = RLock()

    def get(self, session_id: str) -> List[Mapping[str, str]]:
        with self._lock:
            return list(self._by_id.get(session_id, []))

    def put_and_trim(
        self,
        session_id: str,
        messages: List[Mapping[str, str]],
        max_messages: int,
        max_chars: int,
    ) -> List[Mapping[str, str]]:
        with self._lock:
            current = self._by_id.get(session_id, [])
            current.extend(messages)
            if max_messages > 0 and len(current) > max_messages:
                current = current[-max_messages:]
            if max_chars > 0:
                while current and sum(len(str(m.get("content", ""))) for m in current) > max_chars:
                    current.pop(0)
            self._by_id[session_id] = current
            return list(current)


session_memory = SessionMemory()

__all__ = ["SessionMemory", "session_memory"]
