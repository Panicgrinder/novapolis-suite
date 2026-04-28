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


@pytest.mark.scripts
@pytest.mark.unit
def test_forensic_full_tree_is_not_part_of_default_freshness_gate() -> None:
    from scripts import update_workspace_tree_dirs as mod

    repo_root = Path(__file__).resolve().parents[3]

    outputs = mod.active_snapshot_outputs(repo_root)

    assert [path.name for path in outputs] == ["workspace_tree.txt", "workspace_tree_dirs.txt"]


@pytest.mark.scripts
@pytest.mark.unit
def test_active_tree_policy_mirrors_gitignored_machine_artifacts() -> None:
    from scripts import update_workspace_tree_dirs as mod

    assert {".cache", ".import", ".export"} <= mod.ACTIVE_GITIGNORE_SKIP_DIRS
    assert {".coverage", ".env", "coverage.xml"} <= mod.ACTIVE_GITIGNORE_SKIP_FILES
    assert {
        ".tmp",
        ".tmp-results",
        ".venv",
        ".history",
        "Backups",
        "eval/results",
        "outputs",
        "novapolis_agent/data",
        "novapolis_agent/outputs",
        "novapolis_agent/eval/results",
        "novapolis-sim/.godot",
        "novapolis-sim/.import",
        "novapolis-sim/exports",
    } <= set(mod.ACTIVE_GITIGNORE_SKIP_PREFIXES)


@pytest.mark.scripts
@pytest.mark.unit
def test_active_tree_policy_separates_reader_surface_only_extras() -> None:
    from scripts import update_workspace_tree_dirs as mod

    extras = set(mod.ACTIVE_READER_SURFACE_ONLY_PREFIXES)
    mirrored = set(mod.ACTIVE_GITIGNORE_SKIP_PREFIXES)

    assert {
        "novapolis-dev/archive",
        "novapolis-dev/logs",
        "novapolis_agent/archive",
        "novapolis-rp/database-raw",
        "novapolis-rp/database-curated",
    } <= extras
    assert extras.isdisjoint(mirrored)


@pytest.mark.scripts
@pytest.mark.unit
def test_should_skip_active_file_excludes_gitignored_module_coverage_xml(tmp_path: Path) -> None:
    from scripts import update_workspace_tree_dirs as mod

    target = tmp_path / "novapolis_agent" / "coverage.xml"

    assert mod.should_skip_active_file(tmp_path, target)