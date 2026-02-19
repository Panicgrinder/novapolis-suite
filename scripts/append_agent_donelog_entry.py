#!/usr/bin/env python3

"""Append a single entry to novapolis_agent/docs/DONELOG.txt.

Format: timestamp | author | message
"""

from __future__ import annotations

import argparse
import os
from datetime import datetime
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Append a single entry to novapolis_agent/docs/DONELOG.txt "
            "(timestamp | author | message)."
        )
    )
    parser.add_argument(
        "--message",
        required=True,
        help="Entry message (required).",
    )
    parser.add_argument(
        "--author",
        default="",
        help="Author name (optional; defaults to USERNAME/USER).",
    )
    parser.add_argument(
        "--path",
        default="",
        help=(
            "Optional DONELOG path override "
            "(defaults to repo-root/novapolis_agent/docs/DONELOG.txt)."
        ),
    )
    args = parser.parse_args()

    message = (args.message or "").strip()
    if not message:
        raise SystemExit("DONELOG message is required.")

    author = (args.author or "").strip()
    if not author:
        author = (
            os.environ.get("USERNAME") or os.environ.get("USER") or "unknown"
        ).strip() or "unknown"

    if args.path:
        donelog_path = Path(args.path)
    else:
        donelog_path = _repo_root() / "novapolis_agent" / "docs" / "DONELOG.txt"

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")
    line = f"{ts} | {author} | {message}\n"

    donelog_path.parent.mkdir(parents=True, exist_ok=True)
    with donelog_path.open("a", encoding="utf-8", newline="\n") as f:
        f.write(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
