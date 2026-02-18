from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_FILE = ROOT / "single-root-todo.md"

EXCLUDE_DIRS = {
    ".git",
    ".venv",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    "node_modules",
}

EXCLUDE_FILES = {
    OUT_FILE.name.lower(),
}


def is_todo_file(path: Path) -> bool:
    name = path.name.lower()
    return name.endswith(".md") and "todo" in name


def iter_todo_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        rel_parts = set(path.relative_to(root).parts)
        if rel_parts & EXCLUDE_DIRS:
            continue
        if path.name.lower() in EXCLUDE_FILES:
            continue
        if is_todo_file(path):
            files.append(path)
    return sorted(files, key=lambda item: str(item.relative_to(root)).lower())


def main() -> int:
    todo_files = iter_todo_files(ROOT)

    lines: list[str] = [
        "# Zusammengeführte TODOs",
        "",
        f"_Quelle: {len(todo_files)} Dateien im Workspace_",
        "",
    ]

    for file_path in todo_files:
        rel_path = file_path.relative_to(ROOT).as_posix()
        content = file_path.read_text(encoding="utf-8", errors="replace").strip()
        lines.extend(
            [
                f"## {rel_path}",
                "",
                content if content else "_(leer)_",
                "",
                "---",
                "",
            ]
        )

    OUT_FILE.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"[OK] Merge abgeschlossen: {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
