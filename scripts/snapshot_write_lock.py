#!/usr/bin/env python3
"""
Writes a fresh snapshot lock timestamp into ".snapshot.now" at repo root.
Used by snapshot_gate to verify fresh "stand:" frontmatter updates.

- Timestamp format: YYYY-MM-DD HH:mm (local time)
- Safe: Only writes/overwrites a small text file; no deletions.

Options:
  --file <path>   Optional alternative lock file path (default: <repo>/.snapshot.now)
  --print-only    Do not write; only print the timestamp (dry run)
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def repo_root() -> Path:
    try:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return Path(r.stdout.strip())
    except Exception:
        pass
    return Path.cwd()


def now_hm() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Write snapshot lock timestamp to .snapshot.now")
    p.add_argument("--file", dest="file", help="Lock file path", default=None)
    p.add_argument(
        "--print-only", dest="print_only", action="store_true", help="Dry run: print only"
    )
    args = p.parse_args(argv)

    root = repo_root()
    target = Path(args.file) if args.file else root / ".snapshot.now"
    ts = now_hm()

    if args.print_only:
        print(ts)
        return 0

    try:
        target.write_text(ts + "\n", encoding="utf-8")
        rel = str(target.relative_to(root)) if target.is_absolute() else str(target)
        print(f"[snapshot-write-lock] Wrote {ts} to {rel}")
        return 0
    except Exception as e:
        print(f"[snapshot-write-lock] ERROR: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
