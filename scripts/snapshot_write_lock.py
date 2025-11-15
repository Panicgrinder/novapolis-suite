#!/usr/bin/env python3
"""Write a .snapshot.now lock file with local timestamp (used by snapshot_gate).

Replaces the archived PowerShell script.
"""
from __future__ import annotations
from datetime import datetime
from pathlib import Path


def main() -> int:
    repo_root = None
    try:
        import subprocess
        out = subprocess.run(['git', 'rev-parse', '--show-toplevel'], capture_output=True, text=True)
        if out.returncode == 0:
            repo_root = Path(out.stdout.strip())
    except Exception:
        pass

    if repo_root is None:
        repo_root = Path.cwd()

    ts = datetime.now().strftime('%Y-%m-%d %H:%M')
    lock_path = repo_root / '.snapshot.now'
    lock_path.write_text(ts)
    print(f"[snapshot-lock] wrote {ts} to {lock_path}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
