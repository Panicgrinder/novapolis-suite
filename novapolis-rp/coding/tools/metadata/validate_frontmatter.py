#!/usr/bin/env python3
"""
Validate YAML Front Matter across Markdown canvases.
Rules (agreed schema):
- Required for all: title(str), category(enum), slug(str kebab-case ASCII),
    version(str) und last_updated(ISO-8601 mit TZ)
- Always present (may be empty arrays): tags[], affiliations[], locations[], dependencies[]
- Optional: last_change(str)
- Category specifics:
    - scene: characters[] (non-empty), locations[] (non-empty)
    - character: affiliations[] (non-empty; ["none"] allowed)
    - location: affiliations[] (non-empty; ["none"] allowed)
- Reference checks:
    - dependencies: each slug must exist in repo
    - scene.characters: each slug must exist in repo

Exit code non-zero on errors. Prints concise summary and first N errors per file.
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

ROOT = Path(os.getcwd()).resolve()
FRONTMATTER_MAX_LINES = 200
ALLOWED_CATEGORIES = {"admin", "canon", "character", "location", "inventory", "project", "scene"}

# Nur diese Verzeichnisse validieren
VALIDATE_DIRS = [ROOT / "database-rp"]

SKIP_DIRS = {
    "node_modules",
    ".git",
    ".venv",
    ".vscode",
    ".idea",
    ".DS_Store",
    "database-raw/99-exports",
}


def relp(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


def should_skip_dir(d: Path) -> bool:
    rp = relp(d)
    # nur unterhalb erlaubter Wurzeln prüfen
    if not any(rp == relp(base) or rp.startswith(relp(base) + "/") for base in VALIDATE_DIRS):
        return True
    for s in SKIP_DIRS:
        if rp == s or rp.startswith(s + "/"):
            return True
    # verschachtelte node_modules vermeiden
    if "node_modules" in rp.split("/"):
        return True
    return False


def parse_bracket_list(val: str) -> list[str]:
    inner = val.strip().strip("[]").strip()
    if not inner:
        return []
    return [x.strip().strip("\"'") for x in inner.split(",") if x.strip()]


def parse_front_matter(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    if not lines:
        return data
    start = None
    for idx, ln in enumerate(lines[:FRONTMATTER_MAX_LINES]):
        if ln.strip() == "---":
            start = idx
            break
        if ln.strip().startswith("#") and idx < 5:
            return {}
        if ln.strip():
            if idx < 5:
                return {}
    if start is None:
        return {}
    end = None
    for j in range(start + 1, min(len(lines), start + FRONTMATTER_MAX_LINES)):
        if lines[j].strip() == "---":
            end = j
            break
    if end is None:
        return {}
    i = start + 1
    while i < end:
        line = lines[i].rstrip("\n")
        if not line.strip():
            i += 1
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            k = key.strip()
            v = val.strip()
            if v == "":
                items: list[str] = []
                j = i + 1
                while j < end:
                    nxt = lines[j].rstrip("\n")
                    if not nxt.strip():
                        j += 1
                        continue
                    if nxt.lstrip().startswith("- "):
                        tok = nxt.split("- ", 1)[1].strip().strip("'\"")
                        items.append(tok)
                        j += 1
                        continue
                    if ":" in nxt:
                        break
                    break
                data[k] = items
                i = j
                continue
            else:
                if v.startswith("[") and v.endswith("]"):
                    data[k] = parse_bracket_list(v)
                else:
                    data[k] = v.strip().strip("'\"")
        i += 1
    return data


def is_kebab(s: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", s))


def is_iso8601_tz(s: str) -> bool:
    # Basic check: 2025-10-28T18:05:00+01:00
    return bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}[+-]\d{2}:\d{2}", s))


def collect_slugs() -> dict[str, str]:
    slugs: dict[str, str] = {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        d = Path(dirpath)
        if should_skip_dir(d):
            dirnames[:] = []
            continue
        for fname in filenames:
            if not fname.lower().endswith(".md"):
                continue
            md_path = d / fname
            lines = md_path.read_text(encoding="utf-8", errors="ignore").splitlines()
            fm = parse_front_matter(lines)
            slug = fm.get("slug") if isinstance(fm.get("slug"), str) else None
            if slug:
                slugs[slug] = relp(md_path)
    return slugs


def validate_file(md_path: Path, slugs_index: dict[str, str]) -> list[str]:
    errs: list[str] = []
    lines = md_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    fm = parse_front_matter(lines)
    ctx = relp(md_path)

    def req_str(key: str) -> str | None:
        v = fm.get(key)
        if isinstance(v, str) and v.strip():
            return v.strip()
        errs.append(f"{ctx}: missing/empty '{key}'")
        return None

    def arr(key: str) -> list[str]:
        v = fm.get(key)
        if isinstance(v, list):
            return [str(x).strip() for x in v if str(x).strip()]
        # ensure presence but allow empty
        return []

    req_str("title")
    category = req_str("category")
    slug = req_str("slug")
    req_str("version")
    last_updated = req_str("last_updated")

    if category and category not in ALLOWED_CATEGORIES:
        errs.append(f"{ctx}: invalid category '{category}'")

    if slug and not is_kebab(slug):
        errs.append(f"{ctx}: slug not kebab-case ASCII '{slug}'")

    if last_updated and not is_iso8601_tz(last_updated):
        errs.append(f"{ctx}: last_updated not ISO-8601 with TZ '{last_updated}'")

    tags = arr("tags")
    affiliations = arr("affiliations")
    locations = arr("locations")
    dependencies = arr("dependencies")

    # category specifics
    if category == "scene":
        chars = arr("characters")
        if not chars:
            errs.append(f"{ctx}: scene requires non-empty 'characters'[]")
        if not locations:
            errs.append(f"{ctx}: scene requires non-empty 'locations'[]")
        else:
            for c in chars:
                if c not in slugs_index:
                    errs.append(f"{ctx}: scene character slug not found: '{c}'")
    if category == "character":
        if not affiliations:
            errs.append(f"{ctx}: character requires 'affiliations'[] (use ['none'] if none)")
    if category == "location":
        if not affiliations:
            errs.append(f"{ctx}: location requires 'affiliations'[] (use ['none'] if none)")

    for dep in dependencies:
        if dep not in slugs_index:
            errs.append(f"{ctx}: dependency slug not found: '{dep}'")

    # Ensure always-present arrays are at least declared in FM (no mutation here;
    # the enricher normalizes JSON afterwards)
    for key, _val in (
        ("tags", tags),
        ("affiliations", affiliations),
        ("locations", locations),
        ("dependencies", dependencies),
    ):
        if key not in fm:
            errs.append(f"{ctx}: missing array field '{key}' (can be empty: [])")

    return errs


def main() -> int:
    slugs_index = collect_slugs()
    errors: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        d = Path(dirpath)
        if should_skip_dir(d):
            dirnames[:] = []
            continue
        for fname in filenames:
            if not fname.lower().endswith(".md"):
                continue
            md_path = d / fname
            errors.extend(validate_file(md_path, slugs_index))
    if errors:
        # Limit per print to avoid flooding, but still return full count
        print("Front Matter validation FAILED")
        for msg in errors[:200]:
            print("- ", msg)
        print(f"Total errors: {len(errors)}")
        return 1
    print("Front Matter validation PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
