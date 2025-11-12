from __future__ import annotations

from collections.abc import Callable
from typing import TYPE_CHECKING, Any, cast

__runtime_settings_any: object | None = None
try:
    from app.core.settings import settings as __rs

    __runtime_settings_any = __rs
except Exception:  # pragma: no cover
    pass

if TYPE_CHECKING:
    from app.core.settings import Settings as SettingsType
else:  # pragma: no cover - only for typing
    SettingsType = Any  # type: ignore[assignment]

_settings: SettingsType | None = cast(SettingsType | None, __runtime_settings_any)
settings: SettingsType | None = _settings

ToolFunc = Callable[[dict[str, Any]], dict[str, Any]]

_REGISTRY: dict[str, ToolFunc] = {}


def register_tool(name: str, func: ToolFunc) -> None:
    if not isinstance(name, str) or not name:
        raise ValueError("tool name must be non-empty string")
    _REGISTRY[name] = func


def list_tools() -> tuple[str, ...]:
    return tuple(sorted(_REGISTRY.keys()))


def is_allowed(name: str) -> bool:
    if settings is None:
        return False
    if not getattr(settings, "TOOLS_ENABLED", False):
        return False
    whitelist = getattr(settings, "TOOLS_WHITELIST", [])
    if isinstance(whitelist, list | tuple):
        return name in whitelist
    return False


def call_tool(name: str, args: dict[str, Any] | None = None) -> dict[str, Any]:
    if name not in _REGISTRY:
        return {"ok": False, "error": f"unknown tool: {name}"}
    if not is_allowed(name):
        return {"ok": False, "error": f"tool not allowed: {name}"}
    func = _REGISTRY[name]
    try:
        result = func(dict(args or {}))
        if not isinstance(result, dict):
            return {"ok": False, "error": "tool returned non-dict"}
        return {"ok": True, "data": result}
    except Exception as exc:
        return {"ok": False, "error": str(exc)}


def _calc_add(args: dict[str, Any]) -> dict[str, Any]:
    a = float(args.get("a", 0))
    b = float(args.get("b", 0))
    return {"result": float(a + b)}


register_tool("calc_add", _calc_add)

__all__ = [
    "register_tool",
    "list_tools",
    "call_tool",
    "is_allowed",
    "settings",
]

settings_instance = settings
