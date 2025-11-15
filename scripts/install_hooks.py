#!/usr/bin/env python3
"""Install Git hooks from `githooks/` into `.git/hooks`.

Replaces the archived PowerShell `scripts/install_hooks.ps1`.
"""
from __future__ import annotations
import shutil
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    src = root / 'githooks'
    dst = root / '.git' / 'hooks'
    if not dst.exists():
        print('.git/hooks not found; please run inside a git repo', file=sys.stderr)
        return 1

    for item in src.iterdir():
        if item.is_file():
            target = dst / item.name
            shutil.copy2(item, target)
            # ensure executable on *nix
            try:
                target.chmod(target.stat().st_mode | 0o111)
            except Exception:
                pass

    print('Installed local git hooks from githooks/ to .git/hooks')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
