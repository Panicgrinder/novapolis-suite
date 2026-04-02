from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_snapshot_gate_checks_changed_markdown_even_without_stand_diff(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import snapshot_gate as mod

    monkeypatch.delenv("SNAPSHOT_GATE_BYPASS", raising=False)
    monkeypatch.setattr(mod, "get_repo_root", lambda: tmp_path)
    monkeypatch.setattr(mod.os, "chdir", lambda _path: None)
    monkeypatch.setattr(mod, "now_ts", lambda: "2026-03-27 15:52")
    monkeypatch.setattr(mod, "read_snapshot_lock", lambda _root: "2026-03-27 15:52")
    monkeypatch.setattr(mod, "get_staged_files", lambda: ["docs/example.md"])
    monkeypatch.setattr(
        mod,
        "get_staged_content",
        lambda _path: "---\nstand: 2026-03-27 14:30\nupdate: stale\nchecks: none\n---\nbody\n",
    )
    monkeypatch.setattr(mod, "is_stand_changed_in_diff", lambda _path: False, raising=False)
    monkeypatch.setattr(
        mod,
        "run",
        lambda cmd, cwd=None: SimpleNamespace(returncode=0, stdout=str(tmp_path), stderr=""),
    )

    rc = mod.main()
    out = capsys.readouterr().out

    assert rc == 1
    assert "docs/example.md" in out
    assert "Snapshot-Anforderung nicht erfüllt" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_pre_commit_runs_snapshot_gate_after_other_gates(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from scripts import pre_commit as mod

    calls: list[str] = []

    monkeypatch.setattr(mod, "repo_root", lambda: tmp_path)
    monkeypatch.setattr(mod, "capture_lines", lambda argv, cwd: ["docs/example.md"])
    monkeypatch.setattr(mod, "enforce_agent_donelog_if_needed", lambda root, staged_all: None)
    monkeypatch.setattr(mod, "markdownlint", lambda root, staged_md: calls.append("markdownlint"))
    monkeypatch.setattr(
        mod,
        "frontmatter_check",
        lambda root, staged_md: calls.append("frontmatter"),
    )
    monkeypatch.setattr(
        mod,
        "run_rp_hard_gates_if_needed",
        lambda root, staged_all: calls.append("rp"),
    )
    monkeypatch.setattr(mod, "run_snapshot_gate", lambda root: calls.append("snapshot"))

    rc = mod.main()

    assert rc == 0
    assert calls == ["markdownlint", "frontmatter", "rp", "snapshot"]
