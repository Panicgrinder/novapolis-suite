from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_summarize_files_separates_blockers_and_observations(tmp_path: Path) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    results = tmp_path / "results_demo_gm_session.jsonl"
    lines = [
        {
            "_meta": True,
            "timestamp": "20260407_1216",
            "enabled_checks": ["must_include", "regex", "not_include"],
        },
        {
            "item_id": "eval-gm-1",
            "slug": "gm.session.continuity.v1",
            "category": "gm_session",
            "tags": ["gm", "blocker", "continuity"],
            "success": False,
            "failed_checks": ["Erforderlicher Begriff nicht gefunden: 'slot-03'"],
            "source_package": "rpg_gm_session_core.v1",
            "duration_ms": 100,
        },
        {
            "item_id": "eval-gm-2",
            "slug": "gm.session.option-quality.v1",
            "category": "gm_session",
            "tags": ["gm", "observation", "options"],
            "success": False,
            "failed_checks": ["Regex nicht erfüllt: '(?m)^3\\. '"],
            "source_package": "rpg_gm_session_core.v1",
            "duration_ms": 120,
        },
        {
            "item_id": "eval-gm-3",
            "slug": "gm.session.patch-validity.v1",
            "category": "gm_session",
            "tags": ["gm", "observation", "state_patches"],
            "success": True,
            "failed_checks": [],
            "source_package": "rpg_gm_session_core.v1",
            "duration_ms": 80,
        },
    ]
    results.write_text(
        "\n".join(json.dumps(entry, ensure_ascii=False) for entry in lines) + "\n",
        encoding="utf-8",
    )

    report = mod.summarize_files([results])

    assert report["summary"]["records"] == 3
    assert report["summary"]["blocker_failures"] == 1
    assert report["summary"]["observation_failures"] == 1
    assert report["summary"]["severity"] == "blocker"
    assert report["summary"]["enabled_checks"] == ["must_include", "not_include", "regex"]
    assert report["blocker_cases"][0]["slug"] == "gm.session.continuity.v1"


@pytest.mark.scripts
@pytest.mark.unit
def test_main_writes_gm_reports(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    results = tmp_path / "results_demo_gm_session.jsonl"
    results.write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "item_id": "eval-gm-1",
                        "slug": "gm.session.continuity.v1",
                        "category": "gm_session",
                        "tags": ["gm", "blocker"],
                        "success": False,
                        "failed_checks": ["Erforderlicher Begriff nicht gefunden: 'slot-03'"],
                        "source_package": "rpg_gm_session_core.v1",
                        "duration_ms": 30,
                    },
                    ensure_ascii=False,
                )
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "summarize_gm_eval_kpis.py",
            "--repo-root",
            str(tmp_path),
            "--pattern",
            "results_*_gm_session.jsonl",
            "--report-json",
            ".tmp/results/reports/gm_summary.json",
            "--report-md",
            ".tmp/results/reports/gm_summary.md",
        ],
    )

    rc = mod.main()
    assert rc == 0
    payload = json.loads(
        (tmp_path / ".tmp/results/reports/gm_summary.json").read_text(encoding="utf-8")
    )
    assert payload["summary"]["severity"] == "blocker"
    assert "GM Session KPI Summary" in (tmp_path / ".tmp/results/reports/gm_summary.md").read_text(
        encoding="utf-8"
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_main_accepts_explicit_results_file_without_pattern(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    results = tmp_path / "custom_gm_results.jsonl"
    results.write_text(
        json.dumps(
            {
                "item_id": "eval-gm-1",
                "slug": "gm.session.continuity.v1",
                "category": "gm_session",
                "tags": ["gm", "observation"],
                "success": True,
                "failed_checks": [],
                "source_package": "rpg_gm_session_core.v1",
                "duration_ms": 25,
            },
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "summarize_gm_eval_kpis.py",
            "--repo-root",
            str(tmp_path),
            "--results-file",
            "custom_gm_results.jsonl",
            "--report-json",
            ".tmp/results/reports/gm_summary_single.json",
            "--report-md",
            ".tmp/results/reports/gm_summary_single.md",
        ],
    )

    rc = mod.main()
    assert rc == 0
    payload = json.loads(
        (tmp_path / ".tmp/results/reports/gm_summary_single.json").read_text(encoding="utf-8")
    )
    assert payload["summary"]["records"] == 1
