from __future__ import annotations

from pathlib import Path

import pytest


def _touch_with_mtime(path: Path, mtime: float) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("x", encoding="utf-8")
    path.touch()
    import os

    os.utime(path, (mtime, mtime))


@pytest.mark.scripts
@pytest.mark.unit
def test_plan_and_dry_run_keeps_named_and_latest(tmp_path: Path) -> None:
    from scripts import cleanup_artifacts as mod

    t = tmp_path / "novapolis_agent" / "eval" / "results"
    _touch_with_mtime(t / "results_01.jsonl", 100)
    _touch_with_mtime(t / "results_02.jsonl", 200)
    _touch_with_mtime(t / "results_baseline_old.jsonl", 50)

    decisions = mod.plan_artifact_cleanup(
        repo_root=tmp_path,
        targets=("novapolis_agent/eval/results",),
        keep_latest=1,
        keep_names=("baseline",),
    )

    keep_paths = {d.path.name for d in decisions if d.action == "keep"}
    remove_paths = {d.path.name for d in decisions if d.action == "remove"}

    assert "results_02.jsonl" in keep_paths
    assert "results_baseline_old.jsonl" in keep_paths
    assert "results_01.jsonl" in remove_paths

    removed_count, _ = mod.apply_cleanup(decisions, dry_run=True)
    assert removed_count == 0
    assert (t / "results_01.jsonl").exists()


@pytest.mark.scripts
@pytest.mark.unit
def test_apply_cleanup_removes_non_kept(tmp_path: Path) -> None:
    from scripts import cleanup_artifacts as mod

    t = tmp_path / "outputs"
    _touch_with_mtime(t / "run_a.bin", 100)
    _touch_with_mtime(t / "run_b.bin", 200)

    decisions = mod.plan_artifact_cleanup(
        repo_root=tmp_path,
        targets=("outputs",),
        keep_latest=1,
        keep_names=(),
    )

    removed_count, _ = mod.apply_cleanup(decisions, dry_run=False)
    assert removed_count == 1
    assert (t / "run_b.bin").exists()
    assert not (t / "run_a.bin").exists()
