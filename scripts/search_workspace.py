#!/usr/bin/env python3

"""Search workspace files for terms and optionally include markdown `stand` values."""

from __future__ import annotations

import argparse
import fnmatch
import re
from collections.abc import Iterable
from pathlib import Path, PurePosixPath

DEFAULT_EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "node_modules",
    "__pycache__",
    ".tmp",
    ".tmp-results",
    ".tmp-datasets",
    "novapolis-dev/archive",
    "Backups",
    "outputs",
    "novapolis_agent/outputs",
    "novapolis_agent/eval/results",
}

DEFAULT_TEXT_SUFFIXES = {
    ".md",
    ".txt",
    ".py",
    ".yml",
    ".yaml",
    ".json",
    ".toml",
    ".ini",
    ".cfg",
    ".ps1",
    ".sh",
    ".js",
    ".ts",
    ".gd",
}

DEFAULT_TEXT_FILENAMES = {
    ".gitignore",
    ".gitattributes",
    ".editorconfig",
}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Durchsucht Dateien im Workspace nach Suchbegriffen. "
            "Optional kann der Frontmatter-Stand aus Markdown-Dateien ausgegeben werden."
        )
    )
    parser.add_argument("terms", nargs="*", help="Suchbegriffe (bei --regex: Regex-Ausdrücke)")
    parser.add_argument("--terms-file", help="Datei mit einem Suchbegriff pro Zeile")
    parser.add_argument(
        "--glob",
        default="**/*",
        help="Glob-Pattern relativ zum Repo-Root (Standard: **/*)",
    )
    parser.add_argument(
        "--case-sensitive",
        action="store_true",
        help="Suche case-sensitive statt case-insensitive",
    )
    parser.add_argument(
        "--regex",
        action="store_true",
        help="Interpretiert Suchbegriffe als Regex statt Literal-Text",
    )
    parser.add_argument(
        "--with-stand",
        action="store_true",
        help="Gibt pro Treffer zusätzlich den `stand`-Wert der Datei aus (falls vorhanden)",
    )
    parser.add_argument(
        "--all-files",
        action="store_true",
        help="Scannt auch Dateien mit nicht-typischen Text-Endungen",
    )
    parser.add_argument(
        "--exclude-dir",
        action="append",
        default=[],
        help="Zusätzlicher auszuschließender Verzeichnispräfix (relativ, mehrfach nutzbar)",
    )
    parser.add_argument(
        "--exclude-glob",
        action="append",
        default=[],
        help="Zusätzliches Glob-Pattern für auszuschließende Pfade (relativ, mehrfach nutzbar)",
    )
    parser.add_argument(
        "--max-hits",
        type=int,
        default=0,
        help="Maximale Trefferzahl (0 = unbegrenzt)",
    )
    return parser.parse_args()


def load_terms(args: argparse.Namespace) -> list[str]:
    terms: list[str] = [t for t in args.terms if t.strip()]
    if args.terms_file:
        term_file = Path(args.terms_file)
        if not term_file.is_absolute():
            term_file = repo_root() / term_file
        raw = term_file.read_text(encoding="utf-8", errors="ignore").splitlines()
        terms.extend(
            line.strip() for line in raw if line.strip() and not line.strip().startswith("#")
        )
    unique = list(dict.fromkeys(terms))
    if not unique:
        raise SystemExit("Fehler: Keine Suchbegriffe angegeben (terms oder --terms-file).")
    return unique


def is_excluded(rel_path: str, exclude_dirs: set[str]) -> bool:
    rel_low = rel_path.lower()
    rel_parts = {part.lower() for part in PurePosixPath(rel_path).parts}
    for prefix in exclude_dirs:
        pref_low = prefix.lower().strip("/")
        if "/" in pref_low:
            if rel_low == pref_low or rel_low.startswith(pref_low + "/"):
                return True
            continue
        if pref_low in rel_parts:
            return True
    return False


def is_text_candidate(path: Path, include_all: bool) -> bool:
    if include_all:
        return True
    if path.name in DEFAULT_TEXT_FILENAMES:
        return True
    return path.suffix.lower() in DEFAULT_TEXT_SUFFIXES


def compile_patterns(
    terms: Iterable[str],
    use_regex: bool,
    case_sensitive: bool,
) -> list[tuple[str, re.Pattern[str]]]:
    flags = 0 if case_sensitive else re.IGNORECASE
    compiled: list[tuple[str, re.Pattern[str]]] = []
    for term in terms:
        pattern = term if use_regex else re.escape(term)
        compiled.append((term, re.compile(pattern, flags=flags)))
    return compiled


def extract_stand(lines: list[str]) -> str | None:
    if not lines:
        return None

    probe = lines[:80]
    for line in probe:
        match = re.match(r"^stand:\s*(.+)$", line.strip(), flags=re.IGNORECASE)
        if match:
            return match.group(1).strip()

    for line in probe:
        match = re.match(r"^Stand:\s*(.+)$", line.strip())
        if match:
            return match.group(1).strip()
    return None


def search_file(
    path: Path,
    rel: str,
    patterns: list[tuple[str, re.Pattern[str]]],
    with_stand: bool,
) -> list[tuple[str, str]]:
    try:
        content = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return []

    lines = content.splitlines()
    stand = extract_stand(lines) if with_stand and path.suffix.lower() == ".md" else None

    hits: list[tuple[str, str]] = []
    for line_no, text in enumerate(lines, start=1):
        matched_terms = [term for term, regex in patterns if regex.search(text)]
        if not matched_terms:
            continue
        for term in matched_terms:
            stand_part = f" | stand={stand}" if stand else ""
            hits.append((term, f"{rel}:{line_no}: [{term}]{stand_part} | {text.strip()}"))
    return hits


def main() -> int:
    args = parse_args()
    terms = load_terms(args)
    patterns = compile_patterns(terms, use_regex=args.regex, case_sensitive=args.case_sensitive)

    root = repo_root()
    exclude_dirs = set(DEFAULT_EXCLUDE_DIRS)
    exclude_dirs.update(p.strip().replace("\\", "/") for p in args.exclude_dir if p.strip())
    exclude_globs = [p.strip().replace("\\", "/") for p in args.exclude_glob if p.strip()]

    scanned_files = 0
    hit_files = 0
    total_hits = 0
    per_term: dict[str, int] = {term: 0 for term in terms}
    max_reached = False

    for path in sorted(root.glob(args.glob)):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if is_excluded(rel, exclude_dirs):
            continue
        if any(fnmatch.fnmatch(rel, pattern) for pattern in exclude_globs):
            continue
        if not is_text_candidate(path, args.all_files):
            continue

        scanned_files += 1
        hits = search_file(path, rel, patterns, with_stand=args.with_stand)
        if not hits:
            continue

        hit_files += 1
        for term, hit in hits:
            print(hit)
            per_term[term] += 1
            total_hits += 1
            if args.max_hits > 0 and total_hits >= args.max_hits:
                max_reached = True
                break
        if max_reached:
            break

    print("---")
    if max_reached:
        print(f"max_hits_reached={args.max_hits}")
    print(f"scanned_files={scanned_files}")
    print(f"hit_files={hit_files}")
    print(f"total_hits={total_hits}")
    for term in terms:
        print(f"hits[{term}]={per_term[term]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
