#!/usr/bin/env python3
"""
Generate workspace tree snapshots (dirs + full) at repo root.

Outputs:
- workspace_tree_dirs.txt   (directories only)
- workspace_tree.txt        (files and directories, compact)

Notes:
- Skips common virtualenv and cache dirs.
- Non-destructive; overwrites only the snapshot files above.
"""
from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

SKIP_DIRS = {".git", ".venv", "__pycache__", ".mypy_cache", ".ruff_cache", ".pytest_cache"}


def repo_root() -> Path:
    try:
        r = subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True)
        if r.returncode == 0 and r.stdout.strip():
            return Path(r.stdout.strip())
    except Exception:
        pass
    return Path.cwd()


def relpath(root: Path, p: Path) -> str:
    try:
        return str(p.relative_to(root))
    except Exception:
        return str(p)


def write_dirs_only(root: Path, out_path: Path) -> None:
    lines: list[str] = []
    for dirpath, dirnames, _filenames in os.walk(root):
        rp = Path(dirpath)
        # prune skip dirs in-place
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel = relpath(root, rp)
        if rel:
            lines.append(rel + "/")
    out_path.write_text("\n".join(sorted(lines)) + "\n", encoding="utf-8")


def write_full_tree(root: Path, out_path: Path) -> None:
    lines: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        rp = Path(dirpath)
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        rel_dir = relpath(root, rp)
        if rel_dir:
            lines.append(rel_dir + "/")
        for fn in sorted(filenames):
            p = rp / fn
            # skip our own outputs
            if p == out_path:
                continue
            lines.append(relpath(root, p))
    out_path.write_text("\n".join(sorted(lines)) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    _ = argparse.ArgumentParser(description="Update workspace tree snapshots").parse_args(argv)
    root = repo_root()
    write_dirs_only(root, root / "workspace_tree_dirs.txt")
    write_full_tree(root, root / "workspace_tree.txt")
    print("[workspace-tree] Updated workspace_tree_dirs.txt and workspace_tree.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
