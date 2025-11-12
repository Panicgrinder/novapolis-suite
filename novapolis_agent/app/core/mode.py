from __future__ import annotations

import threading
import time
from typing import Any, Literal

Mode = Literal["rpg", "general"]


def detect_requested_mode_from_messages(messages: list[dict[str, Any]]) -> Mode | None:
    if not messages:
        return None
    text = " ".join(
        str(m.get("content", "")) for m in messages if str(m.get("role", "")).lower() == "user"
    ).lower()
    if any(
        key in text
        for key in ["novapolis", "chronistin", "/roll", "szene:", "konsequenz:", "optionen:"]
    ):
        return "rpg"
    if any(
        key in text
        for key in ["neutral", "sachlich", "ohne rpg", "kein rpg", "allgemein", "keine persona"]
    ):
        return "general"
    return None


class SessionModeStore:
    def __init__(self, ttl_minutes: int, max_entries: int):
        self._ttl = max(1, int(ttl_minutes)) * 60
        self._max = max(100, int(max_entries))
        self._store: dict[str, tuple[Mode, float]] = {}
        self._lock = threading.Lock()

    def get(self, sid: str | None) -> Mode | None:
        if not sid:
            return None
        now = time.time()
        with self._lock:
            entry = self._store.get(sid)
            if not entry:
                return None
            mode, ts = entry
            if now - ts > self._ttl:
                self._store.pop(sid, None)
                return None
            return mode

    def set(self, sid: str | None, mode: Mode) -> None:
        if not sid:
            return
        now = time.time()
        with self._lock:
            if len(self._store) >= self._max:
                oldest_key = min(self._store.items(), key=lambda kv: kv[1][1])[0]
                self._store.pop(oldest_key, None)
            self._store[sid] = (mode, now)


try:
    from app.core.settings import settings as _settings

    _ttl = getattr(_settings, "AUTO_MODE_MEMORY_TTL_MIN", 120)
    _max = getattr(_settings, "AUTO_MODE_MEMORY_MAX", 1000)
except Exception:  # pragma: no cover
    _ttl, _max = 120, 1000

SESSION_MODES = SessionModeStore(ttl_minutes=_ttl, max_entries=_max)


def resolve_mode(
    *,
    session_id: str | None,
    eval_mode: bool,
    unrestricted_mode: bool,
    messages: list[dict[str, Any]],
    default_mode: Mode,
    persist: bool = True,
) -> Mode:
    if unrestricted_mode:
        mode: Mode = "rpg"
    elif eval_mode:
        mode = "general"
    else:
        detected = detect_requested_mode_from_messages(messages)
        if detected is not None:
            mode = detected
        else:
            remembered = SESSION_MODES.get(session_id)
            mode = remembered if remembered else default_mode

    if persist and session_id:
        SESSION_MODES.set(session_id, mode)
    return mode


__all__ = [
    "Mode",
    "detect_requested_mode_from_messages",
    "SessionModeStore",
    "SESSION_MODES",
    "resolve_mode",
]
