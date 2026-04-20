from __future__ import annotations

import subprocess
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_sync_markdown_paths_updates_frontmatter_values(tmp_path: Path) -> None:
    from scripts import sync_docs_after_checks as mod

    target = tmp_path / "README.md"
    target.write_text(
        "---\n" "stand: 2026-04-18 01:00\n" "update: Beispiel\n" "checks: alt\n" "---\n\n" "Text\n",
        encoding="utf-8",
    )

    updated = mod.sync_markdown_paths(
        [target],
        stand_value="2026-04-18 02:04",
        checks_value=(
            "scripts/run_checks_and_report.py overall=PASS; "
            "report=.tmp/results/reports/checks_report_20260417_071110.md; "
            "snapshot-lock PASS (2026-04-18 02:04)"
        ),
    )

    content = target.read_text(encoding="utf-8")
    assert updated == [target]
    assert "stand: 2026-04-18 02:04" in content
    assert "snapshot-lock PASS (2026-04-18 02:04)" in content


@pytest.mark.scripts
@pytest.mark.unit
def test_resolve_report_uses_latest_markdown_report(tmp_path: Path) -> None:
    from scripts import sync_docs_after_checks as mod

    report_dir = tmp_path / ".tmp" / "results" / "reports"
    report_dir.mkdir(parents=True)
    older = report_dir / "checks_report_20260417_060000.md"
    latest = report_dir / "checks_report_20260417_071110.md"
    older.write_text("---\nchecks: overall=PASS; markdownlint=PASS\n---\n", encoding="utf-8")
    latest.write_text(
        "---\nchecks: overall=PASS; markdownlint=PASS; pytest=PASS\n---\n",
        encoding="utf-8",
    )

    resolved, headline, report_ref = mod.resolve_report(tmp_path, "latest")

    assert resolved == latest.resolve()
    assert headline == "overall=PASS; markdownlint=PASS; pytest=PASS"
    assert report_ref == ".tmp/results/reports/checks_report_20260417_071110.md"


@pytest.mark.scripts
@pytest.mark.unit
def test_main_runs_todo_index_sync_for_active_board(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from scripts import sync_docs_after_checks as mod

    board = tmp_path / "novapolis-dev" / "docs" / "todo.dev.md"
    board.parent.mkdir(parents=True)
    board.write_text(
        "---\n"
        "stand: 2026-04-18 01:45\n"
        "update: offen\n"
        "checks: alt\n"
        "---\n\n"
        "- [ ] Punkt\n",
        encoding="utf-8",
    )
    index_path = tmp_path / "novapolis-dev" / "docs" / "todo.index.md"
    index_path.write_text(
        "---\n" "stand: 2026-04-18 01:45\n" "update: offen\n" "checks: alt\n" "---\n\n" "Index\n",
        encoding="utf-8",
    )
    report_dir = tmp_path / ".tmp" / "results" / "reports"
    report_dir.mkdir(parents=True)
    report = report_dir / "checks_report_20260417_071110.md"
    report.write_text(
        "---\nchecks: overall=PASS; markdownlint=PASS; pytest=PASS\n---\n",
        encoding="utf-8",
    )

    commands: list[list[str]] = []

    def fake_refresh_snapshot_lock(_repo_root: Path, _python_exec: Path) -> str:
        return "2026-04-18 02:04"

    def fake_run_python_subprocess(
        python_exec: Path,
        script_path: Path,
        *args: str,
        cwd: Path,
    ) -> subprocess.CompletedProcess[str]:
        commands.append([str(python_exec), str(script_path), *args])
        return subprocess.CompletedProcess(
            [str(script_path), *args],
            0,
            "PASS: TODO index sync policy satisfied\n",
            "",
        )

    monkeypatch.setattr(mod, "refresh_snapshot_lock", fake_refresh_snapshot_lock)
    monkeypatch.setattr(mod, "run_python_subprocess", fake_run_python_subprocess)
    monkeypatch.setattr(
        mod.checks_runner,
        "resolve_python",
        lambda _repo_root: tmp_path / ".venv" / "Scripts" / "python.exe",
    )

    rc = mod.main(
        [
            "--repo-root",
            str(tmp_path),
            "--report",
            "latest",
            "--files",
            "novapolis-dev/docs/todo.dev.md",
        ]
    )

    assert rc == 0
    assert any("check_todo_index_sync.py" in " ".join(command) for command in commands)
    assert "stand: 2026-04-18 02:04" in board.read_text(encoding="utf-8")
    assert "snapshot-lock PASS (2026-04-18 02:04)" in index_path.read_text(encoding="utf-8")
