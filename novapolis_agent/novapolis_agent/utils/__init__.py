"""Compatibility bridge for ``novapolis_agent.utils`` imports.

Utility modules live in ``novapolis_agent/utils`` (project root). Expose that
folder under the package path ``novapolis_agent.utils``.
"""

from __future__ import annotations

from pathlib import Path

_here = Path(__file__).resolve().parent
_project_utils = _here.parent.parent / "utils"
if _project_utils.exists():
    __path__.append(str(_project_utils))
