"""Kompatibilitätsschicht für Legacy-Imports ``from utils.*``.

Dieses Paket reicht die Module aus ``novapolis_agent.utils`` weiter, damit
bestehende Importpfade ohne Anpassungen funktionieren.
"""

from importlib import import_module
import sys
from types import ModuleType
from typing import Iterable

_BASE_PACKAGE = "novapolis_agent.utils"
_module = sys.modules[__name__]

def _expose(submodules: Iterable[str]) -> None:
    """Registriert die genannten Untermodule unter dem Legacy-Namen."""

    for name in submodules:
        target = import_module(f"{_BASE_PACKAGE}.{name}")
        setattr(_module, name, target)
        sys.modules[f"{__name__}.{name}"] = target


_expose(
    (
        "context_notes",
        "eval_cache",
        "eval_utils",
        "rag",
        "time_utils",
    )
)

