#!/usr/bin/env python3
"""
Safe cleanup wrapper (Python) for a few known root artifacts.

Behavior:
- Default is WhatIf (no changes). Use --apply to actually move files.
- Instead of deleting, moves targets into Backups/<stamp>/ preserving name.

Targets (root-level only, conservative):
- *.code-workspace
- README.md.bak
- lint.out / lint.out.*

This is a minimal, safe replacement for the old cleanup_workspace_files.ps1.
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
from collections.abc import Iterable
from datetime import datetime
from pathlib import Path

ROOT_TARGETS = [
    "*.code-workspace",
    "README.md.bak",
    "lint.out",
    "lint.out.*",
]


def repo_root() -> Path:
    try:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return Path(r.stdout.strip())
    except Exception:
        pass
    return Path.cwd()


def glob_many(base: Path, patterns: Iterable[str]) -> list[Path]:
    out: list[Path] = []
    for pat in patterns:
        out.extend(base.glob(pat))
    return out


def stamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description="Safe cleanup (WhatIf by default)")
    ap.add_argument("--apply", action="store_true", help="Apply changes (move files)")
    args = ap.parse_args(argv)

    root = repo_root()
    candidates = [p for p in glob_many(root, ROOT_TARGETS) if p.exists() and p.is_file()]

    if not candidates:
        print("[cleanup] Nothing to do.")
        return 0

    if not args.apply:
        print("[cleanup][WhatIf] Would move these files to Backups/:")
        for p in candidates:
            print(f" - {p.name}")
        print("Use --apply to perform the move.")
        return 0

    dest_dir = root / "Backups" / f"cleanup-{stamp()}"
    dest_dir.mkdir(parents=True, exist_ok=True)

    moved = 0
    for p in candidates:
        try:
            target = dest_dir / p.name
            shutil.move(str(p), str(target))
            print(f"[cleanup] Moved {p.name} -> {target.relative_to(root)}")
            moved += 1
        except Exception as e:
            print(f"[cleanup] ERROR moving {p}: {e}")

    print(f"[cleanup] Done. Moved {moved} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
