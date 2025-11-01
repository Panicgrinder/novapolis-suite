"""Novapolis Agent package shim for editable checkouts.

The runtime code lives under ``novapolis_agent/app``.  Re-export everything so
``import novapolis_agent`` behaves the same as ``from novapolis_agent import
app`` in editable installs and packaged distributions.
"""

from .app import *  # noqa: F401,F403

try:
    from .app import __all__ as __all__  # type: ignore[attr-defined]
except ImportError:
    __all__ = []
