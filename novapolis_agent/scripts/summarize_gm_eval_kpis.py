#!/usr/bin/env python
from __future__ import annotations

import argparse
import glob
import json
from collections import Counter
from pathlib import Path
from typing import Any


def _collect_result_files(
    repo_root: Path,
    patterns: list[str],
    explicit_files: list[str],
) -> list[Path]:
    out: list[Path] = []

    for rel in explicit_files:
        p = (repo_root / rel).resolve()
        if p.exists() and p.is_file():
            out.append(p)

    for pat in patterns:
        matches = glob.glob(str((repo_root / pat).resolve()), recursive=True)
        for match in matches:
            p = Path(match)
            if p.exists() and p.is_file():
                out.append(p)

    return sorted(set(out))


def _normalize_failure(failure: str) -> str:
    text = failure.lower()
    if "erforderlicher begriff nicht gefunden" in text:
        return "term_inclusion"
    if "unerwuenschter begriff gefunden" in text:
        return "reveal_leak"
    if "regex" in text:
        return "format"
    if "rpg" in text:
        return "rpg_style"
    if "keywords" in text:
        return "keywords"
    if "ausfuehrungsfehler" in text:
        return "execution"
    return "other"


def _normalize_tags(raw_tags: Any) -> list[str]:
    if not isinstance(raw_tags, list):
        return []
    tags: list[str] = []
    for entry in raw_tags:
        if isinstance(entry, str):
            tag = entry.strip().lower()
            if tag:
                tags.append(tag)
    return tags


def _case_bucket(tags: list[str]) -> str:
    tag_set = set(tags)
    if {"blocker", "gm:blocker", "severity:blocker"} & tag_set:
        return "blocker"
    return "observation"


def summarize_files(files: list[Path]) -> dict[str, Any]:
    total = 0
    success = 0
    durations: list[int] = []
    fail_counter: Counter[str] = Counter()
    package_total: Counter[str] = Counter()
    package_fail: Counter[str] = Counter()
    enabled_checks: set[str] = set()
    blocker_cases: list[dict[str, Any]] = []
    observation_cases: list[dict[str, Any]] = []
    run_meta: list[dict[str, Any]] = []

    for file_path in files:
        with file_path.open("r", encoding="utf-8") as handle:
            for raw in handle:
                line = raw.strip()
                if not line:
                    continue
                obj = json.loads(line)

                if isinstance(obj, dict) and obj.get("_meta") is True:
                    run_meta.append(obj)
                    meta_checks = obj.get("enabled_checks")
                    if isinstance(meta_checks, list):
                        for entry in meta_checks:
                            if isinstance(entry, str) and entry.strip():
                                enabled_checks.add(entry.strip())
                    continue

                if not isinstance(obj, dict):
                    continue

                total += 1
                ok = bool(obj.get("success"))
                if ok:
                    success += 1

                dur = obj.get("duration_ms")
                if isinstance(dur, int) and dur >= 0:
                    durations.append(dur)

                pkg = str(obj.get("source_package") or "unknown")
                package_total[pkg] += 1
                if not ok:
                    package_fail[pkg] += 1

                failed_checks = obj.get("failed_checks")
                if isinstance(failed_checks, list):
                    for entry in failed_checks:
                        if isinstance(entry, str):
                            fail_counter[_normalize_failure(entry)] += 1

                if ok:
                    continue

                tags = _normalize_tags(obj.get("tags"))
                case = {
                    "item_id": str(obj.get("item_id") or ""),
                    "slug": str(obj.get("slug") or ""),
                    "category": str(obj.get("category") or ""),
                    "package": pkg,
                    "tags": tags,
                    "failed_checks": [
                        entry for entry in (failed_checks or []) if isinstance(entry, str)
                    ],
                }
                if _case_bucket(tags) == "blocker":
                    blocker_cases.append(case)
                else:
                    observation_cases.append(case)

    pass_rate = (success / total) if total else 0.0
    severity = "beobachtung"
    if blocker_cases or total == 0:
        severity = "blocker"
    elif observation_cases or pass_rate < 0.9:
        severity = "warnung"

    avg_duration = int(sum(durations) / len(durations)) if durations else 0
    top_failed = [{"check": name, "count": count} for name, count in fail_counter.most_common(8)]

    per_package: list[dict[str, Any]] = []
    for pkg, pkg_total in sorted(package_total.items()):
        pkg_fail = int(package_fail.get(pkg, 0))
        pkg_rate = (pkg_total - pkg_fail) / pkg_total if pkg_total else 0.0
        per_package.append(
            {
                "package": pkg,
                "total": pkg_total,
                "failed": pkg_fail,
                "pass_rate": round(pkg_rate, 4),
            }
        )

    return {
        "summary": {
            "files": [p.as_posix() for p in files],
            "records": total,
            "success": success,
            "pass_rate": round(pass_rate, 4),
            "avg_duration_ms": avg_duration,
            "severity": severity,
            "blocker_failures": len(blocker_cases),
            "observation_failures": len(observation_cases),
            "enabled_checks": sorted(enabled_checks),
        },
        "top_failed_checks": top_failed,
        "per_package": per_package,
        "blocker_cases": blocker_cases,
        "observation_cases": observation_cases,
        "run_meta": run_meta,
    }


def _build_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines: list[str] = []
    lines.append("# GM Session KPI Summary")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Severity: {summary['severity']}")
    lines.append(f"- Records: {summary['records']}")
    lines.append(f"- Success: {summary['success']}")
    lines.append(f"- Pass rate: {summary['pass_rate']}")
    lines.append(f"- Blocker-Faelle: {summary['blocker_failures']}")
    lines.append(f"- Beobachtungen: {summary['observation_failures']}")
    lines.append(f"- Avg duration ms: {summary['avg_duration_ms']}")
    lines.append("")
    lines.append("## Enabled Checks")
    if summary.get("enabled_checks"):
        for check in summary["enabled_checks"]:
            lines.append(f"- {check}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Blocker Cases")
    if report.get("blocker_cases"):
        for case in report["blocker_cases"]:
            lines.append(
                f"- {case['item_id']} ({case['slug'] or case['package']}): "
                + ", ".join(case["failed_checks"])
            )
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Observation Cases")
    if report.get("observation_cases"):
        for case in report["observation_cases"]:
            lines.append(
                f"- {case['item_id']} ({case['slug'] or case['package']}): "
                + ", ".join(case["failed_checks"])
            )
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Top Failed Checks")
    if report.get("top_failed_checks"):
        for item in report["top_failed_checks"]:
            lines.append(f"- {item['check']}: {item['count']}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Board Ready")
    lines.append("- Blocker-Faelle direkt in das Agent-Board rueckspiegeln.")
    lines.append("- Beobachtungen gesammelt triagieren und erst danach naechste Produkt-Gates schliessen.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize GM session eval KPIs")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root",
    )
    parser.add_argument(
        "--pattern",
        action="append",
        default=["novapolis_agent/eval/results/results_*_gm_session*.jsonl"],
        help="Relative glob pattern for result files",
    )
    parser.add_argument(
        "--results-file",
        action="append",
        default=[],
        help="Explicit relative results file",
    )
    parser.add_argument(
        "--report-json",
        default=".tmp/results/reports/gm_session_kpi_summary.json",
        help="Relative JSON report output path",
    )
    parser.add_argument(
        "--report-md",
        default=".tmp/results/reports/gm_session_kpi_summary.md",
        help="Relative Markdown report output path",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    files = _collect_result_files(repo_root, list(args.pattern), list(args.results_file))
    if not files:
        print("[gm-session-kpi] ERROR no matching result files")
        return 2

    report = summarize_files(files)

    json_path = (repo_root / args.report_json).resolve()
    md_path = (repo_root / args.report_md).resolve()
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(_build_markdown(report), encoding="utf-8", newline="\n")

    print("[gm-session-kpi] done")
    print(f"  files: {len(files)}")
    print(f"  severity: {report['summary']['severity']}")
    print(f"  blocker_failures: {report['summary']['blocker_failures']}")
    print(f"  observation_failures: {report['summary']['observation_failures']}")
    print(f"  report_json: {json_path}")
    print(f"  report_md: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())