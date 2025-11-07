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
    ".pytest_cache/",
    "novapolis_agent/.pytest_cache/",
    ".github/ISSUE_TEMPLATE/",
    "Backups/",
    # Canonical exception: this file intentionally has no YAML frontmatter
    ".github/copilot-instructions.md",
)


def should_skip(path: Path) -> bool:
    """Return True if the markdown file should be ignored."""
    posix = path.as_posix() + ("/" if path.is_dir() else "")
    return any(pattern in posix for pattern in SKIP_PATTERNS)


def parse_frontmatter_block(text: str) -> tuple[dict[str, str] | None, list[str]]:
    """Extract frontmatter dict and collect structural issues."""
    errors: list[str] = []
    # BOM explicitly flagged
    if text.startswith("\ufeff"):
        errors.append("BOM vor Frontmatter (erste Zeile)")
        # remove BOM for further checks
        text = text.lstrip("\ufeff")

    if not text.startswith("---\n"):
        errors.append("Erste Zeile ist nicht '---'")
        return None, errors

    end = text.find("\n---", 4)
    if end == -1:
        errors.append("Schließender Frontmatter-Delimiter fehlt ('---')")
        return None, errors

    block = text[4:end].splitlines()
    data: dict[str, str] = {}
    for line in block:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            errors.append("Ungültige Zeile in Frontmatter: ':' fehlt")
            return None, errors
        key, value = stripped.split(":", 1)
        data[key.strip()] = value.strip()
    return data, errors


def validate_frontmatter(path: Path) -> list[str]:
    """Return a list of validation error strings for a markdown file."""
    if should_skip(path):
        return []

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["Datei ist nicht UTF-8-dekodierbar"]

    data, struct_errors = parse_frontmatter_block(text)
    if struct_errors:
        return struct_errors
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
