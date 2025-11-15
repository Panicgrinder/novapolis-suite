"""Simple YAML frontmatter validator for Markdown files."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path

REQUIRED_KEYS = ("stand", "update", "checks")
TIMESTAMP_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")
AUTO_FIX_OPENING_DELIMITER = True
SKIP_PATTERNS = (
    ".venv/",
    "novapolis_agent/eval/results/",
    "novapolis_agent/outputs/",
    "outputs/",
    "novapolis-rp/database-raw/",
    "novapolis-rp/.pytest_cache/",
    ".pytest_cache/",
    "novapolis_agent/.pytest_cache/",
    "node_modules/",
    ".github/ISSUE_TEMPLATE/",
    "Backups/",
    # Canonical exception: this file intentionally has no YAML frontmatter
    ".github/copilot-instructions.md",
)


def should_skip(path: Path) -> bool:
    """Return True if the markdown file should be ignored."""
    posix = path.as_posix() + ("/" if path.is_dir() else "")
    return any(pattern in posix for pattern in SKIP_PATTERNS)


def ensure_opening_delimiter(path: Path, text: str) -> tuple[str, bool]:
    """Ensure the frontmatter starts with '---' and trim leading blank lines."""
    bom_prefix = "\ufeff" if text.startswith("\ufeff") else ""
    body = text[len(bom_prefix) :]
    if body.startswith("---\n"):
        return text, False

    stripped = body.lstrip("\r\n")
    removed_blank_lines = len(stripped) != len(body)
    if stripped.startswith("---\n"):
        return bom_prefix + stripped, removed_blank_lines

    # Detect likely frontmatter content (keys within first few lines)
    candidate_lines = stripped.splitlines()
    window = candidate_lines[:6]
    has_keys = sum(
        any(line.strip().startswith(f"{key}:") for line in window)
        for key in ("stand", "update", "checks")
    )
    if has_keys < 2:
        return text, False

    fixed = bom_prefix + "---\n" + stripped
    return fixed, True


def replace_frontmatter_value(text: str, key: str, value: str) -> tuple[str, bool]:
    """Replace or insert a key within the frontmatter block."""
    if not text.startswith("---\n"):
        return text, False

    end = text.find("\n---", 4)
    if end == -1:
        return text, False

    block = text[4:end]
    lines = block.splitlines()
    key_prefix = f"{key}:"
    replaced = False
    new_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(key_prefix):
            new_lines.append(f"{key}: {value}")
            replaced = True
        else:
            new_lines.append(line)
    if not replaced:
        new_lines.insert(0, f"{key}: {value}")

    new_block = "\n".join(new_lines)
    if new_block == block:
        return text, False

    return text[:4] + new_block + text[end:], True


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


def validate_frontmatter(path: Path, touch: bool = False) -> list[str]:
    """Return a list of validation error strings for a markdown file."""
    if should_skip(path):
        return []

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return ["Datei ist nicht UTF-8-dekodierbar"]

    if AUTO_FIX_OPENING_DELIMITER:
        fixed_text, changed = ensure_opening_delimiter(path, text)
        if changed:
            path.write_text(fixed_text, encoding="utf-8")
            text = fixed_text
            print(f"{path}: fehlender Frontmatter-Delimiter ergänzt")

    data, struct_errors = parse_frontmatter_block(text)
    if struct_errors:
        return struct_errors
    if data is None:
        return ["Frontmatter fehlt oder ist unvollständig"]

    if touch:
        new_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        updated_text, changed = replace_frontmatter_value(text, "stand", new_timestamp)
        if changed:
            path.write_text(updated_text, encoding="utf-8")
            text = updated_text
            data["stand"] = new_timestamp
            print(f"{path}: 'stand' auf {new_timestamp} aktualisiert")

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
    parser.add_argument(
        "--touch",
        action="store_true",
        help="Aktualisiert 'stand' auf den aktuellen Zeitpunkt (YYYY-MM-DD HH:MM).",
    )
    args = parser.parse_args()

    errors_found = False
    for entry in args.paths:
        if entry.is_dir():
            candidates = sorted(p for p in entry.rglob("*.md") if not should_skip(p))
        else:
            candidates = [entry]
        for md_file in candidates:
            issues = validate_frontmatter(md_file, touch=args.touch)
            if issues:
                errors_found = True
                for issue in issues:
                    print(f"{md_file}: {issue}")
    return 1 if errors_found else 0


if __name__ == "__main__":
    sys.exit(main())
