"""Enforce TODO index sync when TODO boards are modified.

Rule: if any active TODO markdown file changes, then
`novapolis-dev/docs/todo.index.md` must change in the same change set.
"""

from __future__ import annotations

import argparse
import re
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
INDEX_COUNT_PATTERN = re.compile(r"-\s+(?P<name>.+?)\(offen:\s*(?P<count>\d+)\)")
CHECKBOX_OPEN_PATTERN = re.compile(r"^\s*-\s*\[ \]\s+", re.MULTILINE)
CONTRADICTION_PATTERN = re.compile(r"keine\s+offen", re.IGNORECASE)

BOARD_LABELS = {
    "novapolis-dev/docs/todo.dev.md": "dev",
    "novapolis-dev/docs/todo.rp.md": "rp",
    "novapolis-dev/docs/todo.sim.md": "sim",
    "novapolis-dev/docs/todo.agent-board.md": "agent",
}

INDEX_KEYWORDS = {
    "dev": "Dev-Module",
    "rp": "RP-Module",
    "agent": "Agent-Module",
    "sim": "Sim-Module",
}


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


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def parse_index_counts(index_text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for line in index_text.splitlines():
        match = INDEX_COUNT_PATTERN.search(line)
        if not match:
            continue
        name = match.group("name")
        count = int(match.group("count"))
        for key, marker in INDEX_KEYWORDS.items():
            if marker in name:
                counts[key] = count
    return counts


def open_checkbox_count(board_text: str) -> int:
    return len(CHECKBOX_OPEN_PATTERN.findall(board_text))


def has_contradiction(board_text: str, open_count: int) -> bool:
    return open_count > 0 and bool(CONTRADICTION_PATTERN.search(board_text))


def oldest_open_item(board_text: str) -> str:
    for line in board_text.splitlines():
        if CHECKBOX_OPEN_PATTERN.search(line):
            return line.strip()
    return "none"


def latest_change_timestamp(repo_root: Path, rel_path: str) -> str:
    cmd = ["git", "log", "-1", "--format=%cs %H", "--", rel_path]
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
        return "unknown"
    value = (completed.stdout or "").strip()
    return value or "unknown"


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

    index_path = repo_root / TODO_INDEX_FILE
    if not index_path.exists():
        print(f"FAIL: missing index file: {TODO_INDEX_FILE}")
        return 1

    index_text = read_text(index_path)
    index_counts = parse_index_counts(index_text)

    diagnostics_fail = False
    for board_path, key in BOARD_LABELS.items():
        board_file = repo_root / board_path
        if not board_file.exists():
            print(f"WARN: missing board file: {board_path}")
            continue

        board_text = read_text(board_file)
        open_count = open_checkbox_count(board_text)
        index_count = index_counts.get(key)
        contradiction = has_contradiction(board_text, open_count)
        oldest_open = oldest_open_item(board_text)
        latest_change = latest_change_timestamp(repo_root, board_path)

        print(f"BOARD|{key}|open={open_count}|index={index_count}")
        print(f"BOARD_META|{key}|latest_change={latest_change}|oldest_open={oldest_open}")

        if contradiction:
            diagnostics_fail = True
            print(
                f"FAIL: contradiction in {board_path} (contains 'keine offen*' but has open checkboxes)"
            )

        if index_count is None:
            diagnostics_fail = True
            print(f"FAIL: missing index count for board key '{key}' in {TODO_INDEX_FILE}")
            continue

        if index_count != open_count:
            diagnostics_fail = True
            print(
                f"FAIL: count mismatch for {board_path}: index={index_count} actual_open={open_count}"
            )

    if not todo_changed:
        if diagnostics_fail:
            return 1
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

    if diagnostics_fail:
        return 1

    print("PASS: TODO index sync policy satisfied")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
