#!/usr/bin/env python
"""Liefert kompakte Prozent-Auswertung der letzten Eval-Runs als JSON."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Summarize latest eval runs")
    parser.add_argument("--count", type=int, default=3, help="Anzahl letzter Runs")
    parser.add_argument(
        "--results-dir",
        type=str,
        default="",
        help="Optionales eval/results Verzeichnis",
    )
    return parser.parse_args()


def _infer_results_dir(path_hint: str) -> Path:
    if path_hint:
        return Path(path_hint)
    project_root = Path(__file__).resolve().parents[1]
    return project_root / "eval" / "results"


def _file_timestamp(file_name: str) -> str:
    stem = Path(file_name).stem
    if not stem.startswith("results_"):
        return "n/a"
    parts = stem.split("_")
    if len(parts) < 3:
        return "n/a"
    date_part = parts[1]
    time_part = parts[2]
    if len(date_part) != 8 or len(time_part) != 4:
        return "n/a"
    return f"{date_part[0:4]}-{date_part[4:6]}-{date_part[6:8]} {time_part[0:2]}:{time_part[2:4]}"


def _summarize_result_file(path: Path) -> dict[str, Any]:
    total = 0
    success = 0
    durations: list[float] = []

    with path.open("r", encoding="utf-8") as handle:
        for raw_line in handle:
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except Exception:
                continue
            if not isinstance(payload, dict):
                continue
            if bool(payload.get("_meta", False)):
                continue

            total += 1
            if bool(payload.get("success", False)):
                success += 1

            duration_value = payload.get("duration_ms")
            if isinstance(duration_value, (int, float)):
                durations.append(float(duration_value))

    failed = max(0, total - success)
    success_rate = 0.0
    if total > 0:
        success_rate = round((success / total) * 100.0, 1)

    avg_ms = 0.0
    if durations:
        avg_ms = round(sum(durations) / len(durations), 1)

    return {
        "file": path.name,
        "timestamp": _file_timestamp(path.name),
        "items": total,
        "success": success,
        "failed": failed,
        "success_rate_percent": success_rate,
        "avg_duration_ms": avg_ms,
    }


def main() -> int:
    args = _parse_args()
    count = max(1, int(args.count))
    results_dir = _infer_results_dir(args.results_dir)

    if not results_dir.exists() or not results_dir.is_dir():
        print(json.dumps({"ok": True, "runs": []}, ensure_ascii=True, separators=(",", ":")))
        return 0

    files = sorted(results_dir.glob("results_*.jsonl"), key=lambda p: p.stat().st_mtime, reverse=True)
    runs = [_summarize_result_file(path) for path in files[:count]]

    print(json.dumps({"ok": True, "runs": runs}, ensure_ascii=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
