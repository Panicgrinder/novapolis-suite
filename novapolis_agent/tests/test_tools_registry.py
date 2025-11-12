from __future__ import annotations

import types
from typing import Any, cast

import pytest
from app.tools import registry


@pytest.fixture(autouse=True)
def clean_registry(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(registry, "_REGISTRY", {})


@pytest.mark.unit
def test_register_tool_validates_name() -> None:
    with pytest.raises(ValueError):
        registry.register_tool("", lambda _: {})
    with pytest.raises(ValueError):
        registry.register_tool(cast(Any, 123), lambda _: {})

    registry.register_tool("alpha", lambda _: {})
    assert registry.list_tools() == ("alpha",)


@pytest.mark.unit
def test_is_allowed_respects_settings(monkeypatch: pytest.MonkeyPatch) -> None:
    registry.register_tool("beta", lambda _: {})
    monkeypatch.setattr(registry, "settings", None)
    assert registry.is_allowed("beta") is False

    config = types.SimpleNamespace(TOOLS_ENABLED=False, TOOLS_WHITELIST=["beta"])
    monkeypatch.setattr(registry, "settings", config)
    assert registry.is_allowed("beta") is False

    config_enabled = types.SimpleNamespace(TOOLS_ENABLED=True, TOOLS_WHITELIST=["beta"])
    monkeypatch.setattr(registry, "settings", config_enabled)
    assert registry.is_allowed("beta") is True


@pytest.mark.unit
def test_call_tool_covers_error_paths(monkeypatch: pytest.MonkeyPatch) -> None:
    called = {}

    def ok_tool(args: dict[str, Any]) -> dict[str, Any]:
        called.update(args)
        return {"value": args.get("value", 0) * 2}

    def bad_tool(_: dict[str, Any]) -> Any:
        return "oops"

    def boom_tool(_: dict[str, Any]) -> dict[str, Any]:
        raise RuntimeError("boom")

    registry.register_tool("ok", ok_tool)
    registry.register_tool("bad", bad_tool)
    registry.register_tool("boom", boom_tool)

    config = types.SimpleNamespace(TOOLS_ENABLED=True, TOOLS_WHITELIST=["ok"])
    monkeypatch.setattr(registry, "settings", config)

    assert registry.call_tool("unknown") == {"ok": False, "error": "unknown tool: unknown"}
    assert registry.call_tool("bad") == {"ok": False, "error": "tool not allowed: bad"}

    config.TOOLS_WHITELIST.append("bad")
    result = registry.call_tool("ok", {"value": 3})
    assert result == {"ok": True, "data": {"value": 6}}
    assert called == {"value": 3}

    assert registry.call_tool("bad") == {"ok": False, "error": "tool returned non-dict"}

    config.TOOLS_WHITELIST.append("boom")
    assert "boom" in registry.call_tool("boom")["error"]
