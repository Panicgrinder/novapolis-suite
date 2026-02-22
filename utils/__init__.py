"""Compatibility bridge for legacy imports like ``utils.time_utils``.

Utility modules live in ``novapolis_agent/utils``. We expose that directory via
this package path so imports resolve without eager side effects.
"""

from __future__ import annotations

from pathlib import Path

_here = Path(__file__).resolve().parent
_agent_utils = _here.parent / "novapolis_agent" / "utils"
if _agent_utils.exists():
    __path__.append(str(_agent_utils))
