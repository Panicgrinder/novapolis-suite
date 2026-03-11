from __future__ import annotations

import json
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_summarize_files_classifies_and_counts(tmp_path: Path) -> None:
    from scripts import summarize_marathon_kpis as mod

    results = tmp_path / "results_demo_marathon.jsonl"
    lines = [
        {
            "_meta": True,
            "timestamp": "20260310_1500",
            "enabled_checks": ["must_include", "rpg_style"],
        },
        {
            "item_id": "a",
            "success": False,
            "failed_checks": ["Erforderlicher Begriff nicht gefunden: 'X'"],
            "source_package": "pkg_a",
            "duration_ms": 100,
        },
        {
            "item_id": "b",
            "success": False,
            "failed_checks": ["STS-Relevanz zu niedrig (score=0.01)"],
            "source_package": "pkg_a",
            "duration_ms": 200,
        },
        {
            "item_id": "c",
            "success": True,
            "failed_checks": [],
            "source_package": "pkg_b",
            "duration_ms": 300,
        },
    ]
    payload = "\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n"
    results.write_text(payload, encoding="utf-8")

    report = mod.summarize_files([results])

    assert report["summary"]["records"] == 3
    assert report["summary"]["success"] == 1
    assert report["summary"]["severity"] in {"warnung", "blocker"}
    top = {x["check"]: x["count"] for x in report["top_failed_checks"]}
    assert top.get("term_inclusion", 0) == 1
    assert top.get("sts_relevance", 0) == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_build_markdown_contains_board_ready(tmp_path: Path) -> None:
    from scripts import summarize_marathon_kpis as mod

    report = {
        "summary": {
            "files": ["a.jsonl"],
            "records": 2,
            "success": 2,
            "pass_rate": 1.0,
            "avg_duration_ms": 123,
            "severity": "beobachtung",
        },
        "top_failed_checks": [],
        "per_package": [],
        "run_meta": [],
    }

    md = mod._build_markdown(report)
    assert "Board Ready" in md
    assert "Severity" in md
