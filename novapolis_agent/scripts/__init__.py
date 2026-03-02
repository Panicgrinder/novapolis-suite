"""Compatibility bridge for ``scripts`` imports in mixed test/workdir setups.

When tests run from ``novapolis_agent`` as cwd, ``import scripts`` can resolve
to ``novapolis_agent/scripts`` first. Expose the repository-root ``scripts``
directory on this package path so imports like
``from scripts import check_sim_epoch_assets`` stay stable in CI.
"""

from __future__ import annotations

from pathlib import Path

_here = Path(__file__).resolve().parent
_root_scripts = _here.parent.parent / "scripts"
if _root_scripts.exists():
    __path__.append(str(_root_scripts))
