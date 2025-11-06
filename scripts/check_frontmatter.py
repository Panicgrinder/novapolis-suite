"""Simple YAML frontmatter validator for Markdown files."""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REQUIRED_KEYS = ("stand", "update", "checks")
TIMESTAMP_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")
SKIP_PATTERNS = (
    ".venv/",
    "novapolis_agent/eval/results/",
    "novapolis_agent/outputs/",
    "outputs/",
    "novapolis-rp/database-raw/",
    "novapolis-rp/.pytest_cache/",
    "Backups/",
)


def should_skip(path: Path) -> bool:
    """Return True if the markdown file should be ignored."""
    posix = path.as_posix() + ("/" if path.is_dir() else "")
    return any(pattern in posix for pattern in SKIP_PATTERNS)


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    """Extract a minimal frontmatter dict or None if absent."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return None

    if not text.startswith("---\n"):
        return None

    end = text.find("\n---", 4)
    if end == -1:
        return None

    block = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in block:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            return None
        key, value = stripped.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def validate_frontmatter(path: Path) -> list[str]:
    """Return a list of validation error strings for a markdown file."""
    if should_skip(path):
        return []

    data = parse_frontmatter(path)
    if data is None:
        return ["Frontmatter fehlt oder ist unvollständig"]

    errors: list[str] = []
    for key in REQUIRED_KEYS:
        value = data.get(key)
        if value is None or not value:
            errors.append(f"Schlüssel '{key}' fehlt oder ist leer")
    stand_value = data.get("stand")
    if stand_value and not TIMESTAMP_PATTERN.match(stand_value):
        errors.append("'stand' entspricht nicht dem Format YYYY-MM-DD HH:MM")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[Path.cwd()],
        help="Dateien oder Verzeichnisse, die geprüft werden sollen.",
    )
    args = parser.parse_args()

    errors_found = False
    for entry in args.paths:
        if entry.is_dir():
            candidates = sorted(p for p in entry.rglob("*.md") if not should_skip(p))
        else:
            candidates = [entry]
        for md_file in candidates:
            issues = validate_frontmatter(md_file)
            if issues:
                errors_found = True
                for issue in issues:
                    print(f"{md_file}: {issue}")
    return 1 if errors_found else 0


if __name__ == "__main__":
    sys.exit(main())
