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
        for m in matches:
            p = Path(m)
            if p.exists() and p.is_file():
                out.append(p)

    deduped = sorted(set(out))
    return deduped


def _normalize_failure(failure: str) -> str:
    text = failure.lower()
    if "erforderlicher begriff nicht gefunden" in text:
        return "term_inclusion"
    if "rpg" in text:
        return "rpg_style"
    if "sts-relevanz" in text:
        return "sts_relevance"
    if "languagetool" in text:
        return "languagetool_quality"
    if "keywords" in text:
        return "keywords"
    if "regex" in text:
        return "regex"
    return "other"


def summarize_files(files: list[Path]) -> dict[str, Any]:
    total = 0
    success = 0
    durations: list[int] = []
    fail_counter: Counter[str] = Counter()
    package_total: Counter[str] = Counter()
    package_fail: Counter[str] = Counter()
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

    pass_rate = (success / total) if total else 0.0

    severity = "beobachtung"
    if total == 0 or pass_rate < 0.75:
        severity = "blocker"
    elif pass_rate < 0.9:
        severity = "warnung"

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

    top_failed = [{"check": name, "count": count} for name, count in fail_counter.most_common(8)]

    avg_duration = int(sum(durations) / len(durations)) if durations else 0

    return {
        "summary": {
            "files": [p.as_posix() for p in files],
            "records": total,
            "success": success,
            "pass_rate": round(pass_rate, 4),
            "avg_duration_ms": avg_duration,
            "severity": severity,
        },
        "top_failed_checks": top_failed,
        "per_package": per_package,
        "run_meta": run_meta,
    }


def _build_markdown(report: dict[str, Any]) -> str:
    summary = report["summary"]
    lines: list[str] = []
    lines.append("# Marathon KPI Summary")
    lines.append("")
    lines.append("## Summary")
    lines.append(f"- Severity: {summary['severity']}")
    lines.append(f"- Records: {summary['records']}")
    lines.append(f"- Success: {summary['success']}")
    lines.append(f"- Pass rate: {summary['pass_rate']}")
    lines.append(f"- Avg duration ms: {summary['avg_duration_ms']}")
    lines.append("")
    lines.append("## Top Failed Checks")
    top_failed = report.get("top_failed_checks", [])
    if top_failed:
        for item in top_failed:
            lines.append(f"- {item['check']}: {item['count']}")
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Per Package")
    per_package = report.get("per_package", [])
    if per_package:
        for row in per_package:
            pkg_line = (
                f"- {row['package']}: total={row['total']}, "
                + f"failed={row['failed']}, pass_rate={row['pass_rate']}"
            )
            lines.append(pkg_line)
    else:
        lines.append("- none")
    lines.append("")
    lines.append("## Board Ready")
    lines.append("- Severity und Top-Fails direkt in TODO/DONELOG uebernehmen.")
    lines.append("- Bei severity=blocker priorisiert nachfassen.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize marathon eval KPIs")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root",
    )
    parser.add_argument(
        "--pattern",
        action="append",
        default=["novapolis_agent/eval/results/results_*_marathon*.jsonl"],
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
        default=".tmp/results/reports/marathon_kpi_summary.json",
        help="Relative JSON report output path",
    )
    parser.add_argument(
        "--report-md",
        default=".tmp/results/reports/marathon_kpi_summary.md",
        help="Relative Markdown report output path",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    files = _collect_result_files(repo_root, list(args.pattern), list(args.results_file))
    if not files:
        print("[marathon-kpi] ERROR no matching result files")
        return 2

    report = summarize_files(files)

    json_path = (repo_root / args.report_json).resolve()
    md_path = (repo_root / args.report_md).resolve()
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)

    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md_path.write_text(_build_markdown(report), encoding="utf-8", newline="\n")

    print("[marathon-kpi] done")
    print(f"  files: {len(files)}")
    print(f"  severity: {report['summary']['severity']}")
    print(f"  pass_rate: {report['summary']['pass_rate']}")
    print(f"  report_json: {json_path}")
    print(f"  report_md: {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
