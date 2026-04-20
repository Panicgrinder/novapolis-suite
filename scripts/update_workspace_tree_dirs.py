#!/usr/bin/env python3
"""
Generate active and forensic workspace tree snapshots at repo root.

Outputs:
- workspace_tree.txt        (active reader tree; filtered files + directories)
- workspace_tree_dirs.txt   (active reader directory summary)
- workspace_tree_full.txt   (forensic full tree)

Notes:
- Active snapshots skip local caches, venvs, generated outputs and heavy archive paths.
- The forensic snapshot preserves the complete root tree for audit/reference.
- Non-destructive; overwrites only the snapshot files above.
"""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

ACTIVE_SKIP_DIRS = {
    ".git",
    "__pycache__",
    ".mypy_cache",
    ".ruff_cache",
    ".pytest_cache",
    ".hypothesis",
    ".tox",
    "node_modules",
}
ACTIVE_SKIP_FILES = {
    ".coverage",
    ".env",
}
ACTIVE_SKIP_PREFIXES = (
    ".tmp",
    ".venv",
    "eval/results",
    "outputs",
    "Backups",
    "novapolis-dev/archive",
    "novapolis-dev/logs",
    "novapolis_agent/archive",
    "novapolis_agent/outputs",
    "novapolis_agent/tmp",
    "novapolis_agent/.tmp",
    "novapolis_agent/eval/results",
    "novapolis-rp/database-raw",
    "novapolis-rp/database-curated",
    "novapolis-sim/.godot",
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update workspace tree snapshots")
    parser.add_argument(
        "--mode",
        choices=("all", "active-tree", "active-dirs", "forensic-full"),
        default="all",
        help="Which snapshot set to generate",
    )
    return parser.parse_args(argv)


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


def normalize_rel(value: str) -> str:
    normalized = value.replace("\\", "/")
    if normalized in {".", "./", ""}:
        return ""
    if normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized.rstrip("/")


def matches_active_prefix(rel: str, prefix: str) -> bool:
    if rel == prefix:
        return True
    if not rel.startswith(prefix):
        return False
    suffix = rel[len(prefix) :]
    return suffix.startswith(("/", "-"))


def should_skip_active_dir(root: Path, dirpath: Path, dirname: str) -> bool:
    if dirname in ACTIVE_SKIP_DIRS:
        return True

    candidate = dirpath / dirname
    rel = normalize_rel(relpath(root, candidate))
    if not rel:
        return False
    return any(matches_active_prefix(rel, prefix) for prefix in ACTIVE_SKIP_PREFIXES)


def should_skip_active_file(root: Path, file_path: Path) -> bool:
    if file_path.name in ACTIVE_SKIP_FILES:
        return True

    rel = normalize_rel(relpath(root, file_path))
    if not rel:
        return False
    return any(matches_active_prefix(rel, prefix) for prefix in ACTIVE_SKIP_PREFIXES)


def write_active_dirs(root: Path, out_path: Path) -> None:
    lines: list[str] = []
    for dirpath, dirnames, _filenames in os.walk(root):
        rp = Path(dirpath)
        dirnames[:] = [d for d in dirnames if not should_skip_active_dir(root, rp, d)]
        rel = relpath(root, rp)
        if rel:
            lines.append(rel + "/")
    out_path.write_text("\n".join(sorted(lines)) + "\n", encoding="utf-8")


def write_active_tree(root: Path, out_path: Path) -> None:
    lines: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        rp = Path(dirpath)
        dirnames[:] = [d for d in dirnames if not should_skip_active_dir(root, rp, d)]
        rel_dir = relpath(root, rp)
        if rel_dir:
            lines.append(rel_dir + "/")
        for fn in sorted(filenames):
            p = rp / fn
            if p == out_path or should_skip_active_file(root, p):
                continue
            lines.append(relpath(root, p))
    out_path.write_text("\n".join(sorted(lines)) + "\n", encoding="utf-8")


def write_forensic_full(root: Path, out_path: Path) -> None:
    command = f"tree /A /F | Out-File -Encoding ascii '{out_path.name}'"
    completed = subprocess.run(
        ["pwsh", "-NoLogo", "-Command", command],
        cwd=root,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip() or "tree command failed"
        raise RuntimeError(message)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    root = repo_root()
    if args.mode in {"all", "active-dirs"}:
        write_active_dirs(root, root / "workspace_tree_dirs.txt")
    if args.mode in {"all", "active-tree"}:
        write_active_tree(root, root / "workspace_tree.txt")
    if args.mode in {"all", "forensic-full"}:
        write_forensic_full(root, root / "workspace_tree_full.txt")

    print(f"[workspace-tree] Updated mode={args.mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
