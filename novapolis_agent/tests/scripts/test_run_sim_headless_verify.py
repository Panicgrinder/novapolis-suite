from __future__ import annotations

from pathlib import Path

import pytest

from scripts import run_sim_headless_verify as mod


@pytest.mark.scripts
@pytest.mark.unit
def test_resolve_godot_executable_uses_running_process_fallback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    godot_exe = tmp_path / "Godot_v4.6.1-stable_win64.exe"
    godot_exe.write_text("stub", encoding="utf-8")

    monkeypatch.delenv("GODOT_BIN", raising=False)
    monkeypatch.setattr(mod.shutil, "which", lambda name: None)
    monkeypatch.setattr(mod, "_resolve_running_godot_process_path", lambda: godot_exe)

    resolved = mod._resolve_godot_executable(None)

    assert resolved == godot_exe.resolve()


@pytest.mark.scripts
@pytest.mark.unit
def test_main_dry_run_reports_resolved_process_fallback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo_root = tmp_path / "repo"
    (repo_root / "novapolis-sim").mkdir(parents=True)
    godot_exe = tmp_path / "Godot_v4.6.1-stable_win64.exe"
    godot_exe.write_text("stub", encoding="utf-8")

    monkeypatch.delenv("GODOT_BIN", raising=False)
    monkeypatch.setattr(mod.shutil, "which", lambda name: None)
    monkeypatch.setattr(mod, "_resolve_running_godot_process_path", lambda: godot_exe)

    rc = mod.main(["--repo-root", str(repo_root), "--dry-run"])
    out = capsys.readouterr().out

    assert rc == 0
    assert str(godot_exe.resolve()) in out
