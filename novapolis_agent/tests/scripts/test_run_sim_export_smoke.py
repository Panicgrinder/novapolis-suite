from __future__ import annotations

import json
from pathlib import Path

import pytest

from scripts import run_sim_export_smoke as mod


@pytest.mark.scripts
@pytest.mark.unit
def test_export_smoke_fails_when_exe_missing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    repo_root = tmp_path / "repo"
    repo_root.mkdir()

    rc = mod.main(["--repo-root", str(repo_root)])

    assert rc == 2
    payload = json.loads(capsys.readouterr().out)
    assert payload["error"] == "export executable missing"


@pytest.mark.scripts
@pytest.mark.unit
def test_export_smoke_reports_existing_artifacts_without_launch(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    repo_root = tmp_path / "repo"
    export_dir = repo_root / "novapolis-sim" / "exports" / "windows"
    export_dir.mkdir(parents=True)
    export_exe = export_dir / "NovapolisSim.exe"
    export_exe.write_text("stub", encoding="utf-8")
    (export_dir / "NovapolisSim.pck").write_text("stub", encoding="utf-8")

    rc = mod.main(["--repo-root", str(repo_root)])

    assert rc == 0
    payload = json.loads(capsys.readouterr().out)
    assert payload["ok"] is True
    assert payload["companions"] == ["NovapolisSim.pck"]
