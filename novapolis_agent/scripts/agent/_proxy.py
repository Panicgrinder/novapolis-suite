from __future__ import annotations

from importlib import import_module
from types import ModuleType


def load(module: str) -> ModuleType:
    return import_module(module)
