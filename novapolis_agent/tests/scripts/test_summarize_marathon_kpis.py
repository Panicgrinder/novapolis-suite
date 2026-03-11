from __future__ import annotations

import json
import sys
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


@pytest.mark.scripts
@pytest.mark.unit
def test_normalize_failure_variants() -> None:
    from scripts import summarize_marathon_kpis as mod

    assert mod._normalize_failure("Erforderlicher Begriff nicht gefunden") == "term_inclusion"
    assert mod._normalize_failure("RPG Stil passt nicht") == "rpg_style"
    assert mod._normalize_failure("STS-Relevanz zu niedrig") == "sts_relevance"
    assert mod._normalize_failure("LanguageTool meldet Regelverletzung") == "languagetool_quality"
    assert mod._normalize_failure("keywords_any nicht getroffen") == "keywords"
    assert mod._normalize_failure("Regex mismatch") == "regex"
    assert mod._normalize_failure("unbekannt") == "other"


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_result_files_deduplicates(tmp_path: Path) -> None:
    from scripts import summarize_marathon_kpis as mod

    f1 = tmp_path / "a_marathon.jsonl"
    f2 = tmp_path / "b_marathon.jsonl"
    f1.write_text("{}\n", encoding="utf-8")
    f2.write_text("{}\n", encoding="utf-8")

    files = mod._collect_result_files(
        tmp_path,
        patterns=["*_marathon.jsonl"],
        explicit_files=["a_marathon.jsonl"],
    )

    assert files == sorted({f1.resolve(), f2.resolve()})


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_2_without_matching_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from scripts import summarize_marathon_kpis as mod

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "summarize_marathon_kpis.py",
            "--repo-root",
            str(tmp_path),
            "--pattern",
            "no-match-*.jsonl",
        ],
    )

    rc = mod.main()
    assert rc == 2


@pytest.mark.scripts
@pytest.mark.unit
def test_main_writes_reports_on_success(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import summarize_marathon_kpis as mod

    results = tmp_path / "results_demo_marathon.jsonl"
    lines = [
        {"item_id": "a", "success": True, "source_package": "pkg", "duration_ms": 10},
        {
            "item_id": "b",
            "success": False,
            "failed_checks": ["Regex fehlgeschlagen"],
            "source_package": "pkg",
            "duration_ms": 20,
        },
    ]
    results.write_text(
        "\n".join(json.dumps(x, ensure_ascii=False) for x in lines) + "\n",
        encoding="utf-8",
    )

    report_json = ".tmp/results/reports/kpi_test.json"
    report_md = ".tmp/results/reports/kpi_test.md"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "summarize_marathon_kpis.py",
            "--repo-root",
            str(tmp_path),
            "--pattern",
            "results_*_marathon.jsonl",
            "--report-json",
            report_json,
            "--report-md",
            report_md,
        ],
    )

    rc = mod.main()
    assert rc == 0

    json_out = (tmp_path / report_json).resolve()
    md_out = (tmp_path / report_md).resolve()
    assert json_out.exists()
    assert md_out.exists()

    payload = json.loads(json_out.read_text(encoding="utf-8"))
    assert payload["summary"]["records"] == 2
    assert "Marathon KPI Summary" in md_out.read_text(encoding="utf-8")
