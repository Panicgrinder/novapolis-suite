"""Compatibility package for script imports across monorepo scopes.

Historically, many tests imported modules as ``scripts.<name>`` while some
script modules live under ``novapolis_agent/scripts``. To keep imports stable,
we include both directories in this package's module search path.
"""

from __future__ import annotations

from pathlib import Path

# Allow resolving submodules from both:
# - <repo>/scripts
# - <repo>/novapolis_agent/scripts
_here = Path(__file__).resolve().parent
_agent_scripts = _here.parent / "novapolis_agent" / "scripts"
if _agent_scripts.exists():
    __path__.append(str(_agent_scripts))
