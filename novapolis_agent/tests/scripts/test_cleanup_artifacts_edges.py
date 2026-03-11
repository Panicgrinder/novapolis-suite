from __future__ import annotations

import contextlib
import io
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_iter_files_missing_dir_and_keep_name_matching(tmp_path: Path) -> None:
    from scripts import cleanup_artifacts as mod

    assert mod._iter_files(tmp_path / "missing") == []
    assert mod._matches_keep_name(Path("artifact_MARATHON.bin"), ("marathon",)) == "marathon"
    assert mod._matches_keep_name(Path("artifact.bin"), ("", "x")) is None


@pytest.mark.scripts
@pytest.mark.unit
def test_apply_cleanup_remove_empty_dirs(tmp_path: Path) -> None:
    from scripts import cleanup_artifacts as mod

    target = tmp_path / "outputs"
    f1 = target / "a" / "x.bin"
    f2 = target / "b" / "y.bin"
    f1.parent.mkdir(parents=True, exist_ok=True)
    f2.parent.mkdir(parents=True, exist_ok=True)
    f1.write_text("x", encoding="utf-8")
    f2.write_text("y", encoding="utf-8")

    decisions = mod.plan_artifact_cleanup(
        repo_root=tmp_path,
        targets=("outputs",),
        keep_latest=0,
        keep_names=(),
    )
    removed, kept = mod.apply_cleanup(decisions, dry_run=False, remove_empty_dirs=True)

    assert kept == 0
    assert removed == 2
    assert not f1.exists()
    assert not f2.exists()


@pytest.mark.scripts
@pytest.mark.unit
def test_main_dry_run_generates_report(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from scripts import cleanup_artifacts as mod

    rel_target = "outputs"
    out_file = tmp_path / rel_target / "run.bin"
    out_file.parent.mkdir(parents=True, exist_ok=True)
    out_file.write_text("x", encoding="utf-8")

    args = SimpleNamespace(
        repo_root=str(tmp_path),
        target=[rel_target],
        keep_latest=0,
        keep_name=["baseline"],
        dry_run=True,
        remove_empty_dirs=False,
        report=".tmp/results/reports/artifact_lifecycle_report.json",
    )
    monkeypatch.setattr(mod.argparse.ArgumentParser, "parse_args", lambda self: args)

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.main()

    assert rc == 0
    report = tmp_path / ".tmp" / "results" / "reports" / "artifact_lifecycle_report.json"
    assert report.exists()
    text_out = buf.getvalue()
    assert "[artifact-cleanup] report:" in text_out
    assert "dry_run:" in text_out
