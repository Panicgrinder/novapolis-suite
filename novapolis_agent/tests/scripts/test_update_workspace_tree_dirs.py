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
def test_forensic_full_tree_is_part_of_default_freshness_gate() -> None:
    from scripts import update_workspace_tree_dirs as mod

    repo_root = Path(__file__).resolve().parents[3]

    outputs = mod.snapshot_outputs(repo_root)

    assert [path.name for path in outputs] == [
        "workspace_tree.txt",
        "workspace_tree_dirs.txt",
        "workspace_tree_full.txt",
    ]


@pytest.mark.scripts
@pytest.mark.unit
def test_forensic_full_tree_excludes_ignore_based_machine_volatility() -> None:
    from scripts import update_workspace_tree_dirs as mod

    repo_root = Path(__file__).resolve().parents[3]
    forensic = mod.build_forensic_full_text(repo_root)

    assert ".snapshot.now" not in forensic
    assert ".venv/" not in forensic
    assert "coverage.xml" not in forensic
    assert "workspace_tree_full.txt" in forensic


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
def test_active_tree_policy_keeps_tracked_repo_content_visible() -> None:
    from scripts import update_workspace_tree_dirs as mod

    repo_root = Path(__file__).resolve().parents[3]
    active_tree = mod.build_active_tree_text(repo_root, repo_root / "workspace_tree.txt")
    active_dirs = mod.build_active_dirs_text(repo_root)
    active_tree_lines = {line.replace("\\", "/") for line in active_tree.splitlines()}
    active_dir_lines = {line.replace("\\", "/") for line in active_dirs.splitlines()}

    assert {
        "novapolis-dev/archive/todo.dev.archive.md",
        "novapolis-rp/database-raw/99-exports/raw-export-policy.md",
        "novapolis-rp/database-curated/staging/staging-workflow.md",
    } <= active_tree_lines
    assert {
        "novapolis-dev/archive/",
        "novapolis-rp/database-raw/99-exports/",
        "novapolis-rp/database-curated/staging/",
    } <= active_dir_lines


@pytest.mark.scripts
@pytest.mark.unit
def test_should_skip_active_file_excludes_gitignored_module_coverage_xml(tmp_path: Path) -> None:
    from scripts import update_workspace_tree_dirs as mod

    target = tmp_path / "novapolis_agent" / "coverage.xml"

    assert mod.should_skip_active_file(tmp_path, target)