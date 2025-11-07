from __future__ import annotations

import importlib
import json
from pathlib import Path

import pytest


def _load_module():
    return importlib.import_module("scripts.reports.generate_consistency_report")


@pytest.mark.scripts
@pytest.mark.unit
def test_generate_consistency_report_creates_report(tmp_path: Path, monkeypatch: "pytest.MonkeyPatch", capsys: "pytest.CaptureFixture[str]") -> None:
    mod = _load_module()

    out_root = tmp_path / "reports"
    monkeypatch.setattr(mod, "REPORTS_ROOT", str(out_root))
    monkeypatch.setattr(mod, "timestamp", lambda: "20251107_1200")
    monkeypatch.setattr(mod, "run_audit_workspace", lambda: "line1\nline2")

    exit_code = mod.main()

    captured = capsys.readouterr().out
    report_dir = out_root / "20251107_1200"
    params_path = report_dir / "params.txt"
    report_path = report_dir / "report.md"

    assert exit_code == 0
    assert f"Konsistenz-Report erzeugt: {report_dir}" in captured
    assert params_path.exists() and report_path.exists()

    params = json.loads(params_path.read_text(encoding="utf-8"))
    assert params["timestamp"] == "20251107_1200"
    assert params["source"].endswith("generate_consistency_report.py")
    assert params["tools"] == ["scripts/audit_workspace.py"]

    report_text = report_path.read_text(encoding="utf-8")
    assert "# Konsistenz-Report" in report_text
    assert "- line1" in report_text
    assert "- line2" in report_text


@pytest.mark.scripts
@pytest.mark.unit
def test_generate_consistency_report_write_files_empty(tmp_path: Path, monkeypatch: "pytest.MonkeyPatch") -> None:
    mod = _load_module()

    report_dir = tmp_path / "empty"
    report_dir.mkdir(parents=True, exist_ok=True)

    params = {"timestamp": "20250101_0000"}
    mod.write_files(str(report_dir), params, "")

    report_text = (report_dir / "report.md").read_text(encoding="utf-8")
    assert "(keine Ausgabe)" in report_text
