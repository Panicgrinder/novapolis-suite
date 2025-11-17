"""
Ersatz für `scripts/rotate_backups.ps1` als Python-Skript.
Ein sehr kleines Rotationstool: behalte N neueste Backups, verschiebe ältere in `Backups/archive/`.

Usage:
    python -m scripts.rotate_backups
"""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKUPS = ROOT / "Backups"
ARCHIVE = BACKUPS / "archive"
KEEP = 5


def main() -> int:
    if not BACKUPS.exists():
        print("No Backups/ directory found — nothing to rotate.")
        return 0
    files = sorted(
        [p for p in BACKUPS.iterdir() if p.is_file()], key=lambda p: p.stat().st_mtime, reverse=True
    )
    to_archive = files[KEEP:]
    if not to_archive:
        print(f"No files older than top {KEEP} to archive.")
        return 0
    ARCHIVE.mkdir(parents=True, exist_ok=True)
    for p in to_archive:
        dest = ARCHIVE / p.name
        print(f"Archiving {p.name} -> {dest}")
        shutil.move(str(p), str(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
