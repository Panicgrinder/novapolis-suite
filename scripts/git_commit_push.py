#!/usr/bin/env python3
"""Non-interactive helper to run a guarded git add/commit/push sequence.

This is a conservative replacement for the archived `scripts/git_commit_push.ps1`.
It intentionally requires explicit flags for non-interactive use to avoid accidental
destructive pushes.
"""
from __future__ import annotations
import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd, **kwargs):
    print('>', ' '.join(cmd))
    return subprocess.run(cmd, **kwargs)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument('--commit', action='store_true', help='Perform add+commit')
    p.add_argument('--push', action='store_true', help='Perform push after commit')
    p.add_argument('--message', type=str, default=None)
    args = p.parse_args()

    # Dry-run status first
    run(['git', 'status', '--short', '--branch'])

    if not args.commit:
        print('No commit requested; exiting (safe mode).')
        return 0

    if not args.message:
        print('ERROR: --message required to create a commit in non-interactive mode', file=sys.stderr)
        return 2

    # dry-run add
    run(['git', 'add', '--all', '--dry-run'])
    # apply
    rc = run(['git', 'add', '--all']).returncode
    if rc != 0:
        return rc
    rc = run(['git', 'commit', '-m', args.message]).returncode
    if rc != 0:
        return rc

    if args.push:
        rc = run(['git', 'push']).returncode
        return rc

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
