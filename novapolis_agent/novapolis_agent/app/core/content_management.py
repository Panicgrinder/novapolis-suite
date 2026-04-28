"""Kompatibilitätsschicht für app.core.content_management."""

from __future__ import annotations

from typing import Any

from app.core import content_management as _impl


def _export(name: str) -> Any:
    return getattr(_impl, name)


# Keep explicit bindings so type checkers can resolve module attributes.
PostResult = _export("PostResult")
PreResult = _export("PreResult")
check_content_allowed = _export("check_content_allowed")
compact = _export("compact")
create_unrestricted_prompt = _export("create_unrestricted_prompt")
limit_sentences = _export("limit_sentences")
modify_prompt_for_freedom = _export("modify_prompt_for_freedom")
neutralize = _export("neutralize")
split_sentences = _export("split_sentences")
trim_length = _export("trim_length")

# Legacy tests patch `novapolis_agent.app.core.content_management.settings` directly.
settings: Any = getattr(_impl, "settings", None)


def _call_with_legacy_settings(*args, method_name: str, **kwargs):  # type: ignore[no-untyped-def]
    original_settings = getattr(_impl, "settings", None)
    _impl.settings = settings
    try:
        method = getattr(_impl, method_name)
        return method(*args, **kwargs)
    finally:
        _impl.settings = original_settings


def apply_pre(*args, **kwargs):  # type: ignore[no-untyped-def]
    return _call_with_legacy_settings(*args, method_name="apply_pre", **kwargs)


def apply_post(*args, **kwargs):  # type: ignore[no-untyped-def]
    return _call_with_legacy_settings(*args, method_name="apply_post", **kwargs)


__all__ = [
    "PostResult",
    "PreResult",
    "apply_post",
    "apply_pre",
    "check_content_allowed",
    "compact",
    "create_unrestricted_prompt",
    "limit_sentences",
    "modify_prompt_for_freedom",
    "neutralize",
    "settings",
    "split_sentences",
    "trim_length",
]
