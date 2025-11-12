from __future__ import annotations

import importlib
import json
from pathlib import Path

import pytest


def _load_module():
    return importlib.import_module("scripts.todo_gather")


@pytest.mark.scripts
@pytest.mark.unit
def test_todo_gather_prints_summary(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    mod = _load_module()

    tmp_project = tmp_path / "project"
    eval_dir = tmp_project / "eval" / "results"
    eval_dir.mkdir(parents=True, exist_ok=True)

    rows = [
        {"id": "a", "success": True, "rpg_mode": False, "duration_ms": 120, "package": "pack1"},
        {"id": "b", "success": False, "rpg_mode": True, "duration_ms": 80, "package": "pack2"},
        {"id": "c", "success": True, "rpg_mode": True, "duration_ms": 200, "package": "pack1"},
    ]
    results_file = eval_dir / "results_20251031.jsonl"
    results_file.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")

    summaries_dir = eval_dir / "summaries"

    monkeypatch.setattr(mod, "PROJECT_ROOT", str(tmp_project))
    monkeypatch.setattr(mod, "RESULTS_DIR", str(eval_dir))
    monkeypatch.setattr(mod, "SUMMARIES_DIR", str(summaries_dir))
    monkeypatch.setattr(
        mod,
        "feature_status",
        lambda: {
            "caching_integrated": False,
            "caching_available": True,
            "fine_tune_pipeline_available": True,
            "curate_dataset_available": True,
        },
    )

    exit_code = mod.main([])

    captured = capsys.readouterr().out
    assert exit_code == 0
    assert "TODO-Status" in captured
    assert "Tests: 2/3" in captured
    assert "RPG-Anteil" in captured
    assert "Fehlgeschlagene IDs" in captured


@pytest.mark.scripts
@pytest.mark.unit
def test_todo_gather_write_md(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    mod = _load_module()

    tmp_project = tmp_path / "project"
    eval_dir = tmp_project / "eval" / "results"
    eval_dir.mkdir(parents=True, exist_ok=True)

    summaries_dir = eval_dir / "summaries"

    monkeypatch.setattr(mod, "PROJECT_ROOT", str(tmp_project))
    monkeypatch.setattr(mod, "RESULTS_DIR", str(eval_dir))
    monkeypatch.setattr(mod, "SUMMARIES_DIR", str(summaries_dir))
    monkeypatch.setattr(mod, "latest_results", lambda: None)
    monkeypatch.setattr(
        mod,
        "feature_status",
        lambda: {
            "caching_integrated": False,
            "caching_available": False,
            "fine_tune_pipeline_available": False,
            "curate_dataset_available": False,
        },
    )

    utils_time = importlib.import_module("utils.time_utils")
    monkeypatch.setattr(utils_time, "now_compact", lambda: "20251107_1215")

    exit_code = mod.main(["--write-md"])

    captured = capsys.readouterr().out
    expected_file = summaries_dir / "todo_status_20251107_1215.md"

    assert exit_code == 0
    assert expected_file.exists()
    assert "Report gespeichert" in captured
    assert "# TODO-Status" in expected_file.read_text(encoding="utf-8")
