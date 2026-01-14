#!/usr/bin/env python3
"""Check tag coverage between RP staging reports.

Goal:
- Ensure that tags referenced in
  novapolis-rp/database-curated/staging/reports/uncertainties.md
  are present as [FACT] tags in
  novapolis-rp/database-curated/staging/reports/resolved.md

This is a lightweight guard against "verify-first" drift.

Exit codes:
- 0: OK (no missing tags)
- 2: Missing tags detected
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_UNCERTAINTIES = (
    REPO_ROOT / "novapolis-rp" / "database-curated" / "staging" / "reports" / "uncertainties.md"
)
DEFAULT_RESOLVED = (
    REPO_ROOT / "novapolis-rp" / "database-curated" / "staging" / "reports" / "resolved.md"
)


FACT_TAG_RE = re.compile(r"\[FACT\]\s+\[([^\]]+)\]")

# Heuristic for tags used in staging reports.
# Includes:
# - Letters/digits
# - Hyphen
# - Unicode arrow used in a few tags (SYSTEM→REFLEX, D5-98→100)
TAG_TOKEN_RE = re.compile(r"^[A-Z0-9][A-Z0-9\-→]*$")


def parse_fact_tags(resolved_text: str) -> set[str]:
    return {m.group(1).strip() for m in FACT_TAG_RE.finditer(resolved_text)}


def parse_referenced_tags(uncertainties_text: str) -> tuple[set[str], list[str]]:
    """Extract referenced tags from parenthetical lists in uncertainties.

    Returns:
      (tags, raw_lines)
    where raw_lines are the lines where we detected parentheses, for debugging.
    """

    tags: set[str] = set()
    lines_with_lists: list[str] = []

    for line in uncertainties_text.splitlines():
        if "(" not in line or ")" not in line:
            continue

        # We only care about the "... (A/B/C)." style lists.
        # Grab the *last* parenthetical group on the line.
        m = re.search(r"\(([^)]*)\)\s*\.?\s*$", line)
        if not m:
            continue

        inside = m.group(1)
        if "/" not in inside:
            continue

        lines_with_lists.append(line.strip())
        for token in inside.split("/"):
            token = token.strip()
            if not token:
                continue

            # Accept either exact tags or simple wildcard forms like ARKO-*.
            if token.endswith("*") and " " not in token:
                tags.add(token)
                continue

            if TAG_TOKEN_RE.match(token):
                tags.add(token)

    return tags, lines_with_lists


def is_covered(token: str, fact_tags: set[str]) -> bool:
    if token.endswith("*"):
        prefix = token[:-1]
        return any(t.startswith(prefix) for t in fact_tags)
    return token in fact_tags


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check that tags referenced in uncertainties.md are covered as [FACT] in resolved.md."
        ),
    )
    parser.add_argument(
        "--uncertainties",
        type=Path,
        default=DEFAULT_UNCERTAINTIES,
        help="Path to uncertainties.md (default: RP staging uncertainties).",
    )
    parser.add_argument(
        "--resolved",
        type=Path,
        default=DEFAULT_RESOLVED,
        help="Path to resolved.md (default: RP staging resolved).",
    )
    parser.add_argument(
        "--show-lines",
        action="store_true",
        help="Print the source lines from uncertainties that contained tag lists.",
    )

    args = parser.parse_args(argv)

    uncertainties_path: Path = args.uncertainties
    resolved_path: Path = args.resolved

    if not uncertainties_path.exists():
        raise SystemExit(f"Missing file: {uncertainties_path}")
    if not resolved_path.exists():
        raise SystemExit(f"Missing file: {resolved_path}")

    uncertainties_text = uncertainties_path.read_text(encoding="utf-8")
    resolved_text = resolved_path.read_text(encoding="utf-8")

    fact_tags = parse_fact_tags(resolved_text)
    referenced, lines_with_lists = parse_referenced_tags(uncertainties_text)

    missing = sorted(t for t in referenced if not is_covered(t, fact_tags))

    print(f"resolved FACT tags: {len(fact_tags)}")
    print(f"uncertainties referenced tags: {len(referenced)}")

    if args.show_lines and lines_with_lists:
        print("\nSource lines (uncertainties):")
        for line in lines_with_lists:
            print(f"- {line}")

    if missing:
        print("\nMissing tag coverage:")
        for t in missing:
            print(f"- {t}")
        return 2

    print("\nOK: All referenced tags are covered.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
