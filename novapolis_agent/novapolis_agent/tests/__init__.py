"""Compatibility bridge for ``novapolis_agent.tests`` imports during collection."""

from __future__ import annotations

from pathlib import Path

_here = Path(__file__).resolve().parent
_project_tests = _here.parent.parent / "tests"
if _project_tests.exists():
    __path__.append(str(_project_tests))
