#!/usr/bin/env python3

"""Build a machine-readable review sample from shadow-mode logs.

Output is JSONL so humans or AI evaluators can fill `verdict` and `rationale`.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


@dataclass(frozen=True)
class Event:
    ts: int
    request_id: str | None
    stream: bool
    mode: str
    policy_post: str
    user_hash: str
    response_hash: str
    user_preview_redacted: str
    response_preview_redacted: str

    @property
    def key(self) -> tuple[str | None, bool, str, str]:
        return (self.request_id, self.stream, self.user_hash, self.response_hash)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _load_events(path: Path) -> list[Event]:
    rows: list[Event] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        obj = json.loads(line)
        rows.append(
            Event(
                ts=int(obj.get("ts", 0) or 0),
                request_id=obj.get("request_id"),
                stream=bool(obj.get("stream", False)),
                mode=str(obj.get("mode", "default")),
                policy_post=str(obj.get("policy_post", "")).strip().lower(),
                user_hash=str(obj.get("user_hash", "")),
                response_hash=str(obj.get("response_hash", "")),
                user_preview_redacted=str(obj.get("user_preview_redacted", "")),
                response_preview_redacted=str(obj.get("response_preview_redacted", "")),
            )
        )
    return rows


def _dedupe_latest(events: list[Event]) -> list[Event]:
    latest: dict[tuple[str | None, bool, str, str], Event] = {}
    for event in sorted(events, key=lambda e: e.ts):
        latest[event.key] = event
    return sorted(latest.values(), key=lambda e: e.ts, reverse=True)


def _suggested_verdict(policy_post: str) -> str:
    return "accept" if policy_post == "allow" else "revise"


def main() -> int:
    parser = argparse.ArgumentParser(description="Build shadow review sample JSONL.")
    parser.add_argument("--log", default=".tmp/results/logs/shadow_mode.jsonl", help="Shadow log")
    parser.add_argument(
        "--out",
        default=".tmp/results/reviews/shadow_review_sample.jsonl",
        help="Output JSONL for review",
    )
    parser.add_argument("--sample-size", type=int, default=20)
    args = parser.parse_args()

    root = _repo_root()
    log_path = Path(args.log) if Path(args.log).is_absolute() else (root / args.log)
    out_path = Path(args.out) if Path(args.out).is_absolute() else (root / args.out)

    if not log_path.exists():
        raise SystemExit(f"shadow log missing: {log_path}")

    events = _dedupe_latest(_load_events(log_path))
    sample = events[: max(0, args.sample_size)]

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8", newline="\n") as handle:
        for idx, ev in enumerate(sample, start=1):
            payload = {
                "sample_id": f"shadow-{idx:04d}",
                "ts": ev.ts,
                "request_id": ev.request_id,
                "stream": ev.stream,
                "mode": ev.mode,
                "policy_post": ev.policy_post,
                "user_hash": ev.user_hash,
                "response_hash": ev.response_hash,
                "user_preview_redacted": ev.user_preview_redacted,
                "response_preview_redacted": ev.response_preview_redacted,
                "suggested_verdict": _suggested_verdict(ev.policy_post),
                "verdict": "",
                "rationale": "",
            }
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")

    print(f"sample={len(sample)}")
    print(f"out={out_path}")
    print(f"generated_at={datetime.now().strftime('%Y-%m-%d %H:%M')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
