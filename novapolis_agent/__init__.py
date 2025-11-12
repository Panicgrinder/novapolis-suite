"""Novapolis Agent package shim for editable checkouts.

The runtime code lives under ``novapolis_agent/app``. Re-export everything so
``import novapolis_agent`` behaves like ``from novapolis_agent import app`` in
editable installs and packaged distributions.
"""

from importlib import import_module as _import_module
from types import ModuleType as _ModuleType

_app: _ModuleType = _import_module(".app", __name__)
__all__ = list(getattr(_app, "__all__", []))
globals().update({name: getattr(_app, name) for name in __all__})
app = _app
