#!/usr/bin/env python3
"""
Generate active and forensic workspace tree snapshots at repo root.

Outputs:
- workspace_tree.txt        (active reader tree; filtered files + directories)
- workspace_tree_dirs.txt   (active reader directory summary)
- workspace_tree_full.txt   (forensic full tree)

Notes:
- Active snapshots skip local caches, venvs, generated outputs and local repo metadata.
- The forensic snapshot preserves the full repo-visible tree for audit/reference.
- Policy: active tree snapshots keep tracked repo content visible and exclude only
    local machine-artifact and repo-metadata paths.
- Policy: the forensic snapshot is deterministic and excludes ignore-based machine
    volatility, so it can stay inside the default freshness gate.
- Non-destructive; overwrites only the snapshot files above.
"""

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path

ACTIVE_GITIGNORE_SKIP_DIRS = {
    "__pycache__",
    ".cache",
    ".export",
    ".hypothesis",
    ".import",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    "node_modules",
}
ACTIVE_GITIGNORE_SKIP_FILES = {
    ".coverage",
    ".env",
    "coverage.xml",
}
ACTIVE_GITIGNORE_SKIP_PREFIXES = (
    ".history",
    ".tmp",
    ".tmp-results",
    ".venv",
    "Backups",
    "TTS",
    "eval/results",
    "outputs",
    "novapolis_agent/.tmp",
    "novapolis_agent/data",
    "novapolis_agent/eval/results",
    "novapolis_agent/outputs",
    "novapolis_agent/tmp",
    "novapolis-sim/.godot",
    "novapolis-sim/.import",
    "novapolis-sim/exports",
)
ACTIVE_LOCAL_METADATA_SKIP_DIRS = {
    ".git",
    ".tox",
}
ACTIVE_SKIP_DIRS = ACTIVE_GITIGNORE_SKIP_DIRS | ACTIVE_LOCAL_METADATA_SKIP_DIRS
ACTIVE_SKIP_FILES = ACTIVE_GITIGNORE_SKIP_FILES
ACTIVE_SKIP_PREFIXES = ACTIVE_GITIGNORE_SKIP_PREFIXES
FORENSIC_LOCAL_METADATA_SKIP_DIRS = ACTIVE_LOCAL_METADATA_SKIP_DIRS


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


def build_active_dirs_text(root: Path) -> str:
    lines: list[str] = []
    for dirpath, dirnames, _filenames in os.walk(root):
        rp = Path(dirpath)
        dirnames[:] = [d for d in dirnames if not should_skip_active_dir(root, rp, d)]
        rel = relpath(root, rp)
        if rel:
            lines.append(rel + "/")
    return "\n".join(sorted(lines)) + "\n"


def build_active_tree_text(root: Path, out_path: Path) -> str:
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
    return "\n".join(sorted(lines)) + "\n"


def _git_visible_paths(root: Path) -> list[str]:
    completed = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=root,
        capture_output=True,
        text=False,
    )
    if completed.returncode != 0:
        message = completed.stderr.decode("utf-8", errors="replace").strip() or "git ls-files failed"
        raise RuntimeError(message)

    visible: set[str] = set()
    for raw in completed.stdout.split(b"\0"):
        if not raw:
            continue
        rel = normalize_rel(raw.decode("utf-8", errors="replace"))
        if not rel:
            continue
        root_name = rel.split("/", 1)[0]
        if root_name in FORENSIC_LOCAL_METADATA_SKIP_DIRS:
            continue
        visible.add(rel)
    return sorted(visible)


def _insert_render_path(tree: dict[str, object], rel: str) -> None:
    parts = rel.split("/")
    node = tree
    for part in parts[:-1]:
        dirs = node.setdefault("dirs", {})
        assert isinstance(dirs, dict)
        child = dirs.setdefault(part, {})
        assert isinstance(child, dict)
        node = child
    files = node.setdefault("files", set())
    assert isinstance(files, set)
    files.add(parts[-1])


def _render_tree_lines(node: dict[str, object], prefix: str = "") -> list[str]:
    files = sorted(str(name) for name in node.get("files", set()))
    dirs = node.get("dirs", {})
    assert isinstance(dirs, dict)
    entries: list[tuple[str, str]] = [(name, "file") for name in files]
    entries.extend((str(name), "dir") for name in sorted(dirs))

    lines: list[str] = []
    for index, (name, kind) in enumerate(entries):
        is_last = index == len(entries) - 1
        connector = "`-- " if is_last else "|-- "
        suffix = "/" if kind == "dir" else ""
        lines.append(f"{prefix}{connector}{name}{suffix}")
        if kind == "dir":
            child = dirs[name]
            assert isinstance(child, dict)
            child_prefix = prefix + ("    " if is_last else "|   ")
            lines.extend(_render_tree_lines(child, child_prefix))
    return lines


def build_forensic_full_text(root: Path) -> str:
    tree: dict[str, object] = {}
    for rel in _git_visible_paths(root):
        _insert_render_path(tree, rel)
    lines = ["Repo-visible PATH listing", "Root = .", "."]
    lines.extend(_render_tree_lines(tree))
    return "\n".join(lines) + "\n"


def write_active_dirs(root: Path, out_path: Path) -> None:
    out_path.write_text(build_active_dirs_text(root), encoding="utf-8")


def write_active_tree(root: Path, out_path: Path) -> None:
    out_path.write_text(build_active_tree_text(root, out_path), encoding="utf-8")


def write_forensic_full(root: Path, out_path: Path) -> None:
    out_path.write_text(build_forensic_full_text(root), encoding="utf-8")


def snapshot_outputs(root: Path) -> list[Path]:
    return [
        root / "workspace_tree.txt",
        root / "workspace_tree_dirs.txt",
        root / "workspace_tree_full.txt",
    ]


def expected_snapshot_text(root: Path, out_path: Path) -> str:
    if out_path.name == "workspace_tree_dirs.txt":
        return build_active_dirs_text(root)
    if out_path.name == "workspace_tree.txt":
        return build_active_tree_text(root, out_path)
    if out_path.name == "workspace_tree_full.txt":
        return build_forensic_full_text(root)
    raise ValueError(f"Unsupported snapshot path: {out_path}")


def stale_snapshot_paths(root: Path, *, include_forensic_full: bool = True) -> list[Path]:
    stale: list[Path] = []
    outputs = snapshot_outputs(root) if include_forensic_full else snapshot_outputs(root)[:2]
    for out_path in outputs:
        current = out_path.read_text(encoding="utf-8")
        expected = expected_snapshot_text(root, out_path)
        if current != expected:
            stale.append(out_path)
    return stale


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
