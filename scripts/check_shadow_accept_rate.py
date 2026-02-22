#!/usr/bin/env python3

"""Check shadow-mode acceptance rate and emit a small report.

Two modes are supported:
- policy-proxy: Accept when policy_post == "allow"; otherwise Revise.
- review-file: load manual labels from a JSONL file and compute exact rates.
"""

from __future__ import annotations

import argparse
import json
from collections.abc import Iterable
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class ShadowEvent:
    ts: int
    request_id: str | None
    stream: bool
    user_hash: str
    response_hash: str
    policy_post: str

    @property
    def key(self) -> tuple[str | None, bool, str, str]:
        return (self.request_id, self.stream, self.user_hash, self.response_hash)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_events(path: Path) -> list[ShadowEvent]:
    if not path.exists():
        raise FileNotFoundError(f"Shadow log not found: {path}")

    events: list[ShadowEvent] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        events.append(
            ShadowEvent(
                ts=int(obj.get("ts", 0) or 0),
                request_id=obj.get("request_id"),
                stream=bool(obj.get("stream", False)),
                user_hash=str(obj.get("user_hash", "")),
                response_hash=str(obj.get("response_hash", "")),
                policy_post=str(obj.get("policy_post", "")).strip().lower(),
            )
        )
    return events


def _dedupe_latest(events: Iterable[ShadowEvent]) -> list[ShadowEvent]:
    latest: dict[tuple[str | None, bool, str, str], ShadowEvent] = {}
    for event in sorted(events, key=lambda e: e.ts):
        latest[event.key] = event
    return sorted(latest.values(), key=lambda e: e.ts, reverse=True)


def _load_manual_labels(path: Path) -> dict[tuple[str | None, bool, str, str], tuple[str, str]]:
    labels: dict[tuple[str | None, bool, str, str], tuple[str, str]] = {}
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        obj = json.loads(raw)
        verdict = str(obj.get("verdict", "")).strip().lower()
        suggested = str(obj.get("suggested_verdict", "")).strip().lower()
        key = (
            obj.get("request_id"),
            bool(obj.get("stream", False)),
            str(obj.get("user_hash", "")),
            str(obj.get("response_hash", "")),
        )
        labels[key] = (verdict, suggested)
    return labels


def _policy_proxy_verdict(event: ShadowEvent) -> str:
    return "accept" if event.policy_post == "allow" else "revise"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check shadow-mode acceptance rate.")
    parser.add_argument(
        "--log",
        default=".tmp/results/logs/shadow_mode.jsonl",
        help="Path to shadow-mode JSONL log.",
    )
    parser.add_argument(
        "--mode",
        choices=["policy-proxy", "review-file"],
        default="policy-proxy",
        help="How verdicts are generated.",
    )
    parser.add_argument(
        "--review-file",
        default="",
        help="Manual review JSONL file (required in review-file mode).",
    )
    parser.add_argument(
        "--fallback-suggested",
        action="store_true",
        help=(
            "In review-file mode, use suggested_verdict when verdict is empty. "
            "Useful for AI bootstrap runs."
        ),
    )
    parser.add_argument("--sample-size", type=int, default=20, help="Max events to score.")
    parser.add_argument("--min-sample", type=int, default=8, help="Minimum events for pass.")
    parser.add_argument("--target", type=float, default=80.0, help="Accept-rate target in percent.")
    parser.add_argument(
        "--out",
        default="",
        help="Optional output markdown report path. Defaults to .tmp/results/reports/.",
    )
    args = parser.parse_args()

    root = _repo_root()
    log_path = Path(args.log) if Path(args.log).is_absolute() else (root / args.log)
    events = _dedupe_latest(_load_events(log_path))
    sample = events[: max(0, args.sample_size)]

    verdicts: list[str] = []
    missing_labels = 0
    used_suggested = 0

    if args.mode == "review-file":
        if not args.review_file:
            raise SystemExit("--review-file is required in review-file mode")
        review_path = Path(args.review_file)
        if not review_path.is_absolute():
            review_path = root / review_path
        labels = _load_manual_labels(review_path)
        for event in sample:
            pair = labels.get(event.key)
            if pair is None:
                missing_labels += 1
                continue
            verdict, suggested = pair
            if verdict in {"accept", "revise", "reject"}:
                verdicts.append(verdict)
                continue
            if args.fallback_suggested and suggested in {"accept", "revise", "reject"}:
                verdicts.append(suggested)
                used_suggested += 1
                continue
            missing_labels += 1
    else:
        verdicts = [_policy_proxy_verdict(event) for event in sample]

    total = len(verdicts)
    accept = sum(1 for v in verdicts if v == "accept")
    revise = sum(1 for v in verdicts if v == "revise")
    reject = sum(1 for v in verdicts if v == "reject")
    accept_rate = (accept / total * 100.0) if total else 0.0

    passed = total >= args.min_sample and accept_rate >= args.target and missing_labels == 0
    status = "PASS" if passed else "FAIL"

    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = (
        Path(args.out)
        if args.out
        else root / ".tmp" / "results" / "reports" / f"shadow_accept_report_{now}.md"
    )
    if not report_path.is_absolute():
        report_path = root / report_path
    report_path.parent.mkdir(parents=True, exist_ok=True)

    report_lines = [
        "---",
        f"stand: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "update: Shadow-Mode Stichprobe (Accept-Rate Gate)",
        f"checks: status={status}; mode={args.mode}; sample={total}; target={args.target:.1f}%",
        "---",
        "",
        "Shadow Accept Gate",
        "=================",
        "",
        f"- Status: **{status}**",
        f"- Mode: `{args.mode}`",
        f"- Sample scored: `{total}` (min required `{args.min_sample}`)",
        f"- Accept rate: `{accept_rate:.2f}%` (target `{args.target:.1f}%`)",
        f"- Verdicts: accept={accept}, revise={revise}, reject={reject}",
        f"- Missing labels: `{missing_labels}`",
        f"- Suggested fallback used: `{used_suggested}`",
        f"- Source log: `{log_path}`",
    ]
    report_path.write_text("\n".join(report_lines) + "\n", encoding="utf-8")

    print(f"status={status}")
    print(f"sample={total}")
    print(f"accept_rate={accept_rate:.2f}")
    print(f"report={report_path}")

    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
