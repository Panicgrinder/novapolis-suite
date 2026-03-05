"""Enforce stand freshness SLA for active Dev docs.

Thresholds:
- ACTIVE: <= 14 days
- REFERENCE: <= 60 days

Scope is derived from `novapolis-dev/docs/active-surface-index.md` table entries
with concrete file paths (no wildcard rows).
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ACTIVE_SURFACE_INDEX = "novapolis-dev/docs/active-surface-index.md"
STAND_FORMAT = "%Y-%m-%d %H:%M"
ROW_RE = re.compile(r"^\|\s*`(?P<path>[^`]+)`\s*\|\s*(?P<surface>ACTIVE|REFERENCE|HISTORICAL)\s*\|")


@dataclass(frozen=True)
class Finding:
    path: str
    reason: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check stand freshness for active dev docs")
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    parser.add_argument(
        "--active-days",
        type=int,
        default=14,
        help="Max age in days for ACTIVE docs",
    )
    parser.add_argument(
        "--reference-days", type=int, default=60, help="Max age in days for REFERENCE docs"
    )
    return parser.parse_args()


def parse_surface_rows(index_path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for raw in index_path.read_text(encoding="utf-8").splitlines():
        match = ROW_RE.match(raw.strip())
        if not match:
            continue
        rel = match.group("path").strip()
        surface = match.group("surface").strip()
        rows.append((rel, surface))
    return rows


def parse_stand_value(doc_path: Path) -> datetime | None:
    lines = doc_path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == "---":
            return None
        if line.startswith("stand:"):
            value = line.split(":", 1)[1].strip().strip("\"'")
            try:
                return datetime.strptime(value, STAND_FORMAT)
            except ValueError:
                return None
    return None


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    index_path = (repo_root / ACTIVE_SURFACE_INDEX).resolve()

    if not index_path.exists():
        print(f"FAIL: missing index file {ACTIVE_SURFACE_INDEX}")
        return 1

    now = datetime.now()
    rows = parse_surface_rows(index_path)

    checked = 0
    skipped = 0
    findings: list[Finding] = []

    for rel, surface in rows:
        if surface == "HISTORICAL":
            continue
        if "*" in rel:
            skipped += 1
            continue

        doc_path = (repo_root / rel).resolve()
        if not doc_path.exists() or not doc_path.is_file():
            findings.append(
                Finding(
                    rel,
                    "missing_file",
                    "path listed in active-surface-index missing",
                )
            )
            continue

        stand_dt = parse_stand_value(doc_path)
        if stand_dt is None:
            findings.append(
                Finding(
                    rel,
                    "invalid_or_missing_stand",
                    "stand not parseable as YYYY-MM-DD HH:mm",
                )
            )
            continue

        checked += 1
        age_days = int((now - stand_dt).total_seconds() // 86400)
        limit = args.active_days if surface == "ACTIVE" else args.reference_days
        if age_days > limit:
            findings.append(
                Finding(
                    rel,
                    "stale",
                    f"surface={surface}; age_days={age_days}; limit={limit}",
                )
            )

    print(f"checked_docs={checked}")
    print(f"skipped_wildcard_rows={skipped}")
    print(f"findings={len(findings)}")

    if findings:
        for finding in findings:
            print(f"FAIL|{finding.path}|{finding.reason}|{finding.detail}")
        return 1

    print(
        "PASS: stand freshness SLA satisfied "
        f"(ACTIVE<={args.active_days}d, REFERENCE<={args.reference_days}d)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
