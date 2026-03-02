"""Kompatibilitätsschicht für app.core.content_management."""

from app.core import content_management as _impl
from app.core.content_management import *  # noqa: F403

# Legacy tests patch `novapolis_agent.app.core.content_management.settings` directly.
settings = _impl.settings


def apply_pre(*args, **kwargs):  # type: ignore[no-untyped-def]
    _impl.settings = settings
    return _impl.apply_pre(*args, **kwargs)


def apply_post(*args, **kwargs):  # type: ignore[no-untyped-def]
    _impl.settings = settings
    return _impl.apply_post(*args, **kwargs)
