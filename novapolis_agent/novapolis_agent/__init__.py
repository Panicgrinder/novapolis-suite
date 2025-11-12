"""Re-export public API symbols from :mod:`novapolis_agent.app`."""

from importlib import import_module as _import_module
from types import ModuleType as _ModuleType

_app: _ModuleType = _import_module(".app", __name__)
__all__ = list(getattr(_app, "__all__", []))
globals().update({name: getattr(_app, name) for name in __all__})
app = _app
