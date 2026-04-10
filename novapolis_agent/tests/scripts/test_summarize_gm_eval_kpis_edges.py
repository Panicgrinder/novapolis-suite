from __future__ import annotations

import json
import runpy
import sys
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
@pytest.mark.parametrize(
    ("failure", "expected"),
    [
        ("Erforderlicher Begriff nicht gefunden: 'slot-03'", "term_inclusion"),
        ("Unerwuenschter Begriff gefunden: leak", "reveal_leak"),
        ("Regex nicht erfuellt", "format"),
        ("RPG style verletzt", "rpg_style"),
        ("keywords_any failed", "keywords"),
        ("Ausfuehrungsfehler: boom", "execution"),
        ("etwas anderes", "other"),
    ],
)
def test_normalize_failure_maps_expected_buckets(failure: str, expected: str) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    assert mod._normalize_failure(failure) == expected


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_result_files_merges_explicit_and_pattern_matches(tmp_path: Path) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    explicit = tmp_path / "explicit.jsonl"
    pattern_match = tmp_path / "results_demo_gm_session.jsonl"
    explicit.write_text("{}\n", encoding="utf-8")
    pattern_match.write_text("{}\n", encoding="utf-8")

    files = mod._collect_result_files(
        tmp_path,
        patterns=["results_*_gm_session.jsonl"],
        explicit_files=["explicit.jsonl", "missing.jsonl"],
    )

    assert files == [explicit.resolve(), pattern_match.resolve()]


@pytest.mark.scripts
@pytest.mark.unit
def test_normalize_tags_case_bucket_and_markdown_without_failures(tmp_path: Path) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    assert mod._normalize_tags("not-a-list") == []
    assert mod._normalize_tags([" GM ", "", 1]) == ["gm"]
    assert mod._case_bucket(["gm", "blocker"]) == "blocker"
    assert mod._case_bucket(["gm", "observation"]) == "observation"

    report = {
        "summary": {
            "severity": "beobachtung",
            "records": 0,
            "success": 0,
            "pass_rate": 0.0,
            "blocker_failures": 0,
            "observation_failures": 0,
            "avg_duration_ms": 0,
            "enabled_checks": [],
        },
        "blocker_cases": [],
        "observation_cases": [],
        "top_failed_checks": [],
    }

    markdown = mod._build_markdown(report)
    assert "- none" in markdown


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_result_files_and_summary_cover_remaining_false_branches(tmp_path: Path) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    ignored_dir = tmp_path / "results_dir_gm_session.jsonl"
    ignored_dir.mkdir()
    matched = tmp_path / "results_case_gm_session.jsonl"
    matched.write_text(
        "\n".join(
            [
                json.dumps({"_meta": True, "enabled_checks": "not-a-list"}),
                json.dumps(
                    {
                        "item_id": "eval-gm-block",
                        "slug": "",
                        "category": "gm_session",
                        "tags": ["gm:blocker"],
                        "success": False,
                        "failed_checks": "not-a-list",
                        "source_package": "pkg.blocker",
                        "duration_ms": 5,
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    files = mod._collect_result_files(tmp_path, ["results_*_gm_session.jsonl"], [])
    assert files == [matched]

    report = mod.summarize_files(files)
    assert report["summary"]["enabled_checks"] == []
    assert report["blocker_cases"][0]["failed_checks"] == list("not-a-list")

    markdown = mod._build_markdown(report)
    assert "## Enabled Checks" in markdown
    assert "- none" in markdown
    assert "eval-gm-block (pkg.blocker):" in markdown


@pytest.mark.scripts
@pytest.mark.unit
def test_build_markdown_lists_enabled_checks(tmp_path: Path) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    report = {
        "summary": {
            "severity": "warnung",
            "records": 1,
            "success": 1,
            "pass_rate": 1.0,
            "blocker_failures": 0,
            "observation_failures": 0,
            "avg_duration_ms": 12,
            "enabled_checks": ["must_include", "no_leak"],
        },
        "blocker_cases": [],
        "observation_cases": [],
        "top_failed_checks": [],
    }

    markdown = mod._build_markdown(report)
    assert "- must_include" in markdown
    assert "- no_leak" in markdown


@pytest.mark.scripts
@pytest.mark.unit
def test_summarize_files_with_meta_only_marks_blocker(tmp_path: Path) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    results = tmp_path / "results_meta_gm_session.jsonl"
    results.write_text(
        json.dumps({"_meta": True, "enabled_checks": ["must_include"]}) + "\n", encoding="utf-8"
    )

    report = mod.summarize_files([results])

    assert report["summary"]["records"] == 0
    assert report["summary"]["severity"] == "blocker"
    assert report["summary"]["enabled_checks"] == ["must_include"]


@pytest.mark.scripts
@pytest.mark.unit
def test_summarize_files_handles_blank_lines_non_dict_records_and_warnung(tmp_path: Path) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    results = tmp_path / "results_warn_gm_session.jsonl"
    results.write_text(
        "\n".join(
            [
                json.dumps({"_meta": True, "enabled_checks": ["", 1]}),
                "",
                json.dumps([1, 2, 3]),
                json.dumps(
                    {
                        "item_id": "eval-gm-2",
                        "slug": "gm.session.warn.v1",
                        "category": "gm_session",
                        "tags": ["gm", "observation"],
                        "success": False,
                        "failed_checks": ["Regex nicht erfuellt", 1],
                        "source_package": "rpg_gm_session_core.v1",
                        "duration_ms": -1,
                    },
                    ensure_ascii=False,
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    report = mod.summarize_files([results])

    assert report["summary"]["severity"] == "warnung"
    assert report["summary"]["enabled_checks"] == []
    assert report["observation_cases"][0]["failed_checks"] == ["Regex nicht erfuellt"]

    markdown = mod._build_markdown(report)
    assert "## Observation Cases" in markdown
    assert "gm.session.warn.v1" in markdown
    assert "- format: 1" in markdown


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_2_when_no_results_match(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    monkeypatch.setattr(
        sys,
        "argv",
        [
            "summarize_gm_eval_kpis.py",
            "--repo-root",
            str(tmp_path),
            "--pattern",
            "missing*.jsonl",
        ],
    )

    assert mod.main() == 2


@pytest.mark.scripts
@pytest.mark.unit
def test_main_uses_default_pattern_when_no_args_given(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from scripts import summarize_gm_eval_kpis as mod

    results_dir = tmp_path / "novapolis_agent" / "eval" / "results"
    results_dir.mkdir(parents=True)
    result_file = results_dir / "results_20260409_gm_session.jsonl"
    result_file.write_text(
        json.dumps(
            {
                "item_id": "eval-gm-1",
                "slug": "gm.session.ok.v1",
                "category": "gm_session",
                "tags": ["gm"],
                "success": True,
                "failed_checks": [],
                "source_package": "rpg_gm_session_core.v1",
                "duration_ms": 10,
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
            "--report-json",
            ".tmp/results/reports/default.json",
            "--report-md",
            ".tmp/results/reports/default.md",
        ],
    )

    assert mod.main() == 0
    assert (tmp_path / ".tmp" / "results" / "reports" / "default.json").exists()
    assert (tmp_path / ".tmp" / "results" / "reports" / "default.md").exists()


@pytest.mark.scripts
@pytest.mark.unit
def test_module_main_executes_via_runpy(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "summarize_gm_eval_kpis.py"
    results_dir = tmp_path / "novapolis_agent" / "eval" / "results"
    results_dir.mkdir(parents=True)
    (results_dir / "results_demo_gm_session.jsonl").write_text(
        json.dumps(
            {
                "item_id": "eval-gm-1",
                "slug": "gm.session.ok.v1",
                "category": "gm_session",
                "tags": ["gm"],
                "success": True,
                "failed_checks": [],
                "source_package": "rpg_gm_session_core.v1",
                "duration_ms": 12,
            },
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "summarize_gm_eval_kpis.py",
            "--repo-root",
            str(tmp_path),
            "--report-json",
            ".tmp/results/reports/runpy.json",
            "--report-md",
            ".tmp/results/reports/runpy.md",
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        runpy.run_path(str(script_path), run_name="__main__")

    assert exc_info.value.code == 0
