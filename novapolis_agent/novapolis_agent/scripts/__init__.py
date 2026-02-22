"""Compatibility bridge for ``novapolis_agent.scripts`` imports.

Script modules live in ``novapolis_agent/scripts`` (project root), while tests
and some legacy call sites import ``novapolis_agent.scripts.<module>``.
Expose that directory as this package path for stable imports.
"""

from __future__ import annotations

from pathlib import Path

_here = Path(__file__).resolve().parent
_project_scripts = _here.parent.parent / "scripts"
if _project_scripts.exists():
    __path__.append(str(_project_scripts))
