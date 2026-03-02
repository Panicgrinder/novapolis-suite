"""Kompatibilitätsschicht für app.core.memory."""

from app.core import memory as _impl
from app.core.memory import *  # noqa: F403

# Legacy tests patch `novapolis_agent.app.core.memory.settings` directly.
settings = _impl.settings
