#!/usr/bin/env python3
"""Diagnostics helper: small, read-only summary used in CI/workspace checks.

Replaces the archived PowerShell `scripts/diagnostics.ps1` with a Python variant.
"""
from __future__ import annotations
import hashlib
from pathlib import Path


def file_hash(path: Path) -> str:
    h = hashlib.sha256()
    data = path.read_bytes()
    h.update(data)
    return h.hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parent
    cleanup = root / 'cleanup_workspace_files.ps1'
    cleanup_hash = file_hash(cleanup) if cleanup.exists() else '<missing>'
    root_count = len(list(root.glob('*.code-workspace')))
    recurse_count = len(list(root.rglob('*.code-workspace')))
    print({
        'RootWorkspaceCount': root_count,
        'RecursiveWorkspaceCount': recurse_count,
        'CleanupScriptSha256': cleanup_hash,
    })
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
