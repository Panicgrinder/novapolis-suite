#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

MISSING_TERM_RE = re.compile(r"Erforderlicher Begriff nicht gefunden: '([^']+)'")


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            if isinstance(raw, dict):
                rows.append(raw)
    return rows


def _as_top_pairs(counter: Counter[str], top_n: int = 5) -> list[list[Any]]:
    return [[k, v] for k, v in counter.most_common(top_n)]


def build_summary(results_path: Path) -> dict[str, Any]:
    rows = _load_jsonl(results_path)
    meta = next((r for r in rows if r.get("_meta") is True), {})
    items = [r for r in rows if r.get("_meta") is not True]

    total = len(items)
    passes = sum(1 for r in items if bool(r.get("success")))
    pass_rate = round((passes / total) * 100.0, 2) if total else 0.0

    failed_checks_counter: Counter[str] = Counter()
    missing_terms_counter: Counter[str] = Counter()

    for row in items:
        failed_checks = row.get("failed_checks") or []
        for msg in failed_checks:
            text = str(msg)
            failed_checks_counter[text] += 1
            m = MISSING_TERM_RE.search(text)
            if m:
                missing_terms_counter[m.group(1).strip().lower()] += 1

    return {
        "result_file": str(results_path).replace("\\", "/"),
        "run_id": meta.get("run_id"),
        "timestamp": meta.get("timestamp"),
        "total": total,
        "passes": passes,
        "pass_rate": pass_rate,
        "top_failed_checks": _as_top_pairs(failed_checks_counter, top_n=5),
        "top_missing_terms": _as_top_pairs(missing_terms_counter, top_n=5),
    }


def _pairs_to_map(pairs: list[list[Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for p in pairs:
        if isinstance(p, list) and len(p) == 2:
            out[str(p[0])] = int(p[1])
    return out


def compare_to_baseline(
    baseline: dict[str, Any],
    current: dict[str, Any],
    warn_pass_drop: float,
    blocker_pass_drop: float,
    warn_fail_increase: int,
    blocker_fail_increase: int,
) -> dict[str, Any]:
    baseline_pass = float(baseline.get("pass_rate", 0.0))
    current_pass = float(current.get("pass_rate", 0.0))
    pass_rate_delta = round(current_pass - baseline_pass, 2)

    b_failed = _pairs_to_map(baseline.get("top_failed_checks", []))
    c_failed = _pairs_to_map(current.get("top_failed_checks", []))

    combined_keys = sorted(set(b_failed.keys()) | set(c_failed.keys()))
    failed_check_deltas: list[dict[str, Any]] = []
    max_fail_increase = 0
    for key in combined_keys:
        before = int(b_failed.get(key, 0))
        after = int(c_failed.get(key, 0))
        delta = after - before
        if delta > max_fail_increase:
            max_fail_increase = delta
        failed_check_deltas.append(
            {
                "check": key,
                "baseline": before,
                "current": after,
                "delta": delta,
            }
        )

    status = "ok"
    reasons: list[str] = []

    if pass_rate_delta <= -blocker_pass_drop:
        status = "blocker"
        reasons.append(
            f"pass_rate_delta={pass_rate_delta} <= -{blocker_pass_drop}"
        )
    elif pass_rate_delta <= -warn_pass_drop:
        status = "warning"
        reasons.append(f"pass_rate_delta={pass_rate_delta} <= -{warn_pass_drop}")

    if max_fail_increase >= blocker_fail_increase:
        status = "blocker"
        reasons.append(
            f"max_failed_check_increase={max_fail_increase} >= {blocker_fail_increase}"
        )
    elif max_fail_increase >= warn_fail_increase and status != "blocker":
        status = "warning"
        reasons.append(
            f"max_failed_check_increase={max_fail_increase} >= {warn_fail_increase}"
        )

    return {
        "status": status,
        "reasons": reasons,
        "pass_rate_delta": pass_rate_delta,
        "failed_check_deltas": failed_check_deltas,
    }


def _write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build eval drift report against monthly baseline")
    parser.add_argument("--current", required=True, help="Current results_*.jsonl path")
    parser.add_argument("--baseline", required=True, help="Monthly baseline JSON path")
    parser.add_argument("--out", required=True, help="Drift report output JSON path")
    parser.add_argument("--month", required=True, help="Baseline month label, e.g. 2026-02")
    parser.add_argument("--set-baseline", action="store_true", help="Write/overwrite baseline from current")
    parser.add_argument("--warn-pass-drop", type=float, default=2.0)
    parser.add_argument("--blocker-pass-drop", type=float, default=5.0)
    parser.add_argument("--warn-fail-increase", type=int, default=3)
    parser.add_argument("--blocker-fail-increase", type=int, default=8)
    args = parser.parse_args()

    current_path = Path(args.current)
    baseline_path = Path(args.baseline)
    out_path = Path(args.out)

    current_summary = build_summary(current_path)

    if args.set_baseline:
        baseline_payload = {
            "schema": "eval_drift_baseline.v1",
            "month": args.month,
            "kpi": current_summary,
        }
        _write_json(baseline_path, baseline_payload)
        print(f"Baseline written: {baseline_path}")

    if not baseline_path.exists():
        raise FileNotFoundError(
            f"Baseline file not found: {baseline_path}. Use --set-baseline first."
        )

    baseline_payload = json.loads(baseline_path.read_text(encoding="utf-8"))
    baseline_summary = baseline_payload.get("kpi", {})

    comparison = compare_to_baseline(
        baseline=baseline_summary,
        current=current_summary,
        warn_pass_drop=args.warn_pass_drop,
        blocker_pass_drop=args.blocker_pass_drop,
        warn_fail_increase=args.warn_fail_increase,
        blocker_fail_increase=args.blocker_fail_increase,
    )

    report = {
        "schema": "eval_drift_report.v1",
        "month": args.month,
        "thresholds": {
            "warn_pass_drop": args.warn_pass_drop,
            "blocker_pass_drop": args.blocker_pass_drop,
            "warn_fail_increase": args.warn_fail_increase,
            "blocker_fail_increase": args.blocker_fail_increase,
        },
        "baseline": {
            "file": str(baseline_path).replace("\\", "/"),
            "kpi": baseline_summary,
        },
        "current": current_summary,
        "comparison": comparison,
    }
    _write_json(out_path, report)

    print(f"Drift report written: {out_path}")
    print(
        "status="
        + str(comparison.get("status"))
        + ", pass_rate_delta="
        + str(comparison.get("pass_rate_delta"))
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
