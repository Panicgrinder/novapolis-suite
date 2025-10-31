from __future__ import annotations

from typing import Any, Callable, Dict, Optional, Tuple

try:
    from app.core.settings import settings
except Exception:  # pragma: no cover
    settings = None  # type: ignore[assignment]

ToolFunc = Callable[[Dict[str, Any]], Dict[str, Any]]

_REGISTRY: Dict[str, ToolFunc] = {}


def register_tool(name: str, func: ToolFunc) -> None:
    if not isinstance(name, str) or not name:
        raise ValueError("tool name must be non-empty string")
    _REGISTRY[name] = func


def list_tools() -> Tuple[str, ...]:
    return tuple(sorted(_REGISTRY.keys()))


def is_allowed(name: str) -> bool:
    if settings is None:
        return False
    if not getattr(settings, "TOOLS_ENABLED", False):
        return False
    whitelist = getattr(settings, "TOOLS_WHITELIST", [])
    if isinstance(whitelist, (list, tuple)):
        return name in whitelist
    return False


def call_tool(name: str, args: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
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


def _calc_add(args: Dict[str, Any]) -> Dict[str, Any]:
    a = float(args.get("a", 0))
    b = float(args.get("b", 0))
    return {"result": float(a + b)}


register_tool("calc_add", _calc_add)

__all__ = [
    "register_tool",
    "list_tools",
    "call_tool",
    "is_allowed",
]
