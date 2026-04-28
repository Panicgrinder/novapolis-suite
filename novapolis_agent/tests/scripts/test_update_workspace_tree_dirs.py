from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_committed_workspace_trees_match_fresh_generation() -> None:
    from scripts import update_workspace_tree_dirs as mod

    repo_root = Path(__file__).resolve().parents[3]

    stale = mod.stale_snapshot_paths(repo_root)

    assert stale == [], f"stale workspace trees: {[path.name for path in stale]}"