"""Compatibility bridge for ``novapolis_agent.agents`` imports."""

from __future__ import annotations

from pathlib import Path

_here = Path(__file__).resolve().parent
_project_agents = _here.parent.parent / "agents"
if _project_agents.exists():
    __path__.append(str(_project_agents))
