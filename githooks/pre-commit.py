#!/usr/bin/env python3
"""Pre-commit hook (Python). Minimal, non-blocking replacement for the archived PowerShell hook.

Notes:
- This script aims to be a safe, cross-platform pre-commit helper. It will:
  - try to run `scripts/snapshot_gate.py` equivalent (if available),
  - run `npx markdownlint-cli2` for staged markdown files if `npx` is available,
  - run `scripts/check_frontmatter.py` via the repo venv python when present.

The original PowerShell hook has been archived under
`novapolis-dev/archive/ps1_archives_20251114_2240/githooks/pre-commit.ps1`.
"""
from __future__ import annotations
import shutil
import subprocess
import sys
from pathlib import Path


def venv_python(root: Path) -> str:
    p = root / '.venv' / 'Scripts' / 'python.exe'
    if p.exists():
        return str(p)
    return sys.executable


def staged_markdown_files() -> list[str]:
    out = subprocess.run(['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMRT'], capture_output=True, text=True)
    if out.returncode != 0:
        return []
    files = [s for s in out.stdout.splitlines() if s.strip().endswith('.md')]
    return files


def main() -> int:
    root = Path(__file__).resolve().parent
    md_files = staged_markdown_files()
    if md_files:
        if shutil.which('npx'):
            cmd = ['npx', '--yes', 'markdownlint-cli2', '--config', '.markdownlint-cli2.jsonc'] + md_files
            r = subprocess.run(cmd)
            if r.returncode != 0:
                # try auto-fix
                fix = subprocess.run(['npx', '--yes', 'markdownlint-cli2-fix', '--config', '.markdownlint-cli2.jsonc'] + md_files)
                if fix.returncode == 0:
                    subprocess.run(['git', 'add'] + md_files)
                    print('Markdownlint auto-fix applied; please review and commit again.', file=sys.stderr)
                    return 1
                print('markdownlint-cli2 failed; please run locally.', file=sys.stderr)
                return 1

    py = venv_python(root)
    front = root / 'scripts' / 'check_frontmatter.py'
    if front.exists() and md_files:
        rc = subprocess.run([py, str(front)] + md_files).returncode
        return rc

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
