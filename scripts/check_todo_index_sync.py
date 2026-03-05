"""Enforce TODO index sync when TODO boards are modified.

Rule: if any active TODO markdown file changes, then
`novapolis-dev/docs/todo.index.md` must change in the same change set.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

ACTIVE_TODO_FILES = {
    "todo.root.md",
    "novapolis-dev/docs/todo.dev.md",
    "novapolis-dev/docs/todo.rp.md",
    "novapolis-dev/docs/todo.sim.md",
    "novapolis-dev/docs/todo.agent-board.md",
}
TODO_INDEX_FILE = "novapolis-dev/docs/todo.index.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check TODO index sync policy")
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    return parser.parse_args()


def parse_status_line(line: str) -> str | None:
    if not line:
        return None
    payload = line[3:] if len(line) >= 4 else ""
    if not payload:
        return None
    if " -> " in payload:
        payload = payload.split(" -> ", 1)[1]
    return payload.strip().replace("\\", "/")


def changed_files(repo_root: Path) -> list[str]:
    cmd = ["git", "status", "--porcelain", "--untracked-files=all"]
    completed = subprocess.run(
        cmd,
        cwd=str(repo_root),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if completed.returncode != 0:
        stderr = (completed.stderr or "").strip()
        raise RuntimeError(stderr or "git status failed")

    result: list[str] = []
    for raw in completed.stdout.splitlines():
        path = parse_status_line(raw)
        if path:
            result.append(path)
    return result


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()

    try:
        changed = changed_files(repo_root)
    except FileNotFoundError:
        print("FAIL: git executable not found")
        return 1
    except RuntimeError as exc:
        print(f"FAIL: unable to read git status ({exc})")
        return 1

    todo_changed = sorted(path for path in changed if path in ACTIVE_TODO_FILES)
    index_changed = TODO_INDEX_FILE in changed

    print(f"changed_files={len(changed)}")
    print(f"todo_changed={len(todo_changed)}")
    print(f"todo_index_changed={index_changed}")

    if not todo_changed:
        print("PASS: no active TODO board changes detected")
        return 0

    for path in todo_changed:
        print(f"TODO_CHANGED|{path}")

    if not index_changed:
        print(
            "FAIL: active TODO file changed without matching todo.index.md sync "
            f"({TODO_INDEX_FILE})"
        )
        return 1

    print("PASS: TODO index sync policy satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
