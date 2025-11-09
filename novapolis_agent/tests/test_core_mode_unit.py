from __future__ import annotations

import pytest

from app.core import mode


@pytest.mark.unit
@pytest.mark.parametrize(
    "messages,expected",
    [
        ([], None),
        ([{"role": "assistant", "content": "Hallo"}], None),
        ([{"role": "user", "content": "Bitte neutral, ohne RPG"}], "general"),
        ([{"role": "user", "content": "Szene: In Novapolis"}], "rpg"),
    ],
)
def test_detect_requested_mode_from_messages(messages, expected):
    assert mode.detect_requested_mode_from_messages(messages) == expected


@pytest.mark.unit
def test_session_mode_store_expiry_and_eviction(monkeypatch: pytest.MonkeyPatch) -> None:
    store = mode.SessionModeStore(ttl_minutes=1, max_entries=2)
    store._max = 2  # force small capacity for eviction test
    clock = {"value": 1_000.0}

    def _fake_time() -> float:
        return clock["value"]

    monkeypatch.setattr(mode.time, "time", _fake_time)

    store.set("s1", "rpg")
    assert store.get("s1") == "rpg"

    clock["value"] += 61.0
    assert store.get("s1") is None

    clock["value"] = 2_000.0
    store.set("s1", "rpg")
    clock["value"] += 1.0
    store.set("s2", "general")
    clock["value"] += 1.0
    store.set("s3", "rpg")

    assert store.get("s1") is None
    assert store.get("s2") == "general"
    assert store.get("s3") == "rpg"


@pytest.mark.unit
def test_session_mode_store_ignores_missing_session() -> None:
    store = mode.SessionModeStore(ttl_minutes=5, max_entries=10)
    assert store.get(None) is None
    store.set(None, "rpg")
    assert store.get(None) is None


@pytest.mark.unit
def test_resolve_mode_detects_and_persists(monkeypatch: pytest.MonkeyPatch) -> None:
    store = mode.SessionModeStore(ttl_minutes=10, max_entries=10)
    monkeypatch.setattr(mode, "SESSION_MODES", store)

    result = mode.resolve_mode(
        session_id="abc",
        eval_mode=False,
        unrestricted_mode=False,
        messages=[{"role": "user", "content": "Optionen: Test"}],
        default_mode="general",
    )
    assert result == "rpg"
    assert store.get("abc") == "rpg"

    # Fallback to remembered mode when no hint is given
    result2 = mode.resolve_mode(
        session_id="abc",
        eval_mode=False,
        unrestricted_mode=False,
        messages=[],
        default_mode="rpg",
    )
    assert result2 == "rpg"


@pytest.mark.unit
def test_resolve_mode_flags_and_persist_toggle(monkeypatch: pytest.MonkeyPatch) -> None:
    store = mode.SessionModeStore(ttl_minutes=10, max_entries=10)
    monkeypatch.setattr(mode, "SESSION_MODES", store)

    assert (
        mode.resolve_mode(
            session_id="one",
            eval_mode=True,
            unrestricted_mode=False,
            messages=[],
            default_mode="rpg",
        )
        == "general"
    )

    assert (
        mode.resolve_mode(
            session_id="two",
            eval_mode=False,
            unrestricted_mode=True,
            messages=[],
            default_mode="general",
        )
        == "rpg"
    )

    mode.resolve_mode(
        session_id="three",
        eval_mode=False,
        unrestricted_mode=False,
        messages=[],
        default_mode="general",
        persist=False,
    )
    assert store.get("three") is None
