"""Check active workspace files for non-portable absolute path patterns.

This check intentionally targets active docs/config/code paths and excludes
audit/forensics/artifact areas where absolute paths are allowed by governance.
"""

from __future__ import annotations

import argparse
import fnmatch
import re
from dataclasses import dataclass
from pathlib import Path

DEFAULT_INCLUDE: tuple[str, ...] = (
    ".github",
    ".vscode",
    "scripts",
    "README.md",
    "WORKSPACE_INDEX.md",
    "todo.root.md",
    "novapolis-dev/README.md",
    "novapolis-dev/docs",
    "novapolis_agent/README.md",
    "novapolis_agent/scripts",
    "novapolis-rp/README.md",
    "novapolis-sim/README.md",
    "packages/README.md",
)

DEFAULT_EXCLUDE_GLOBS: tuple[str, ...] = (
    ".git/**",
    ".venv/**",
    "Backups/**",
    "outputs/**",
    ".tmp/**",
    ".tmp-results/**",
    "novapolis-dev/archive/**",
    "novapolis-rp/database-curated/staging/**",
    "novapolis_agent/eval/results/**",
    "DONELOG.md",
    "WORKSPACE_STATUS.md",
    "novapolis-dev/docs/donelog.md",
    "novapolis_agent/docs/DONELOG.txt",
)

TEXT_SUFFIXES: tuple[str, ...] = (
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".py",
    ".ps1",
    ".psm1",
    ".cmd",
    ".bat",
)

PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("drive-abs", re.compile(r"(?i)\b[A-Z]:[\\/][^\s'\"`<>|]+")),
    ("unc", re.compile(r"\\\\[A-Za-z0-9._$ -]+\\[^\s'\"`<>|]+")),
    ("file-uri", re.compile(r"(?i)file:///[^\s'\"`<>|]+|file://[^\s'\"`<>|]+")),
)


@dataclass(frozen=True)
class Finding:
    file: Path
    line: int
    kind: str
    value: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check for non-portable absolute paths.")
    parser.add_argument("--repo-root", default=".", help="Repository root path.")
    parser.add_argument(
        "--include", action="append", default=None, help="Include path (file or directory)."
    )
    parser.add_argument(
        "--exclude-glob",
        action="append",
        default=None,
        help="Exclude glob pattern relative to repo root.",
    )
    return parser.parse_args()


def is_excluded(rel_posix: str, exclude_globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel_posix, pattern) for pattern in exclude_globs)


def iter_text_files(repo_root: Path, includes: list[str], exclude_globs: list[str]) -> list[Path]:
    files: list[Path] = []
    seen: set[Path] = set()
    for entry in includes:
        target = (repo_root / entry).resolve()
        if not target.exists():
            continue
        if target.is_file():
            candidates = [target]
        else:
            candidates = [p for p in target.rglob("*") if p.is_file()]
        for path in candidates:
            rel = path.relative_to(repo_root).as_posix()
            if is_excluded(rel, exclude_globs):
                continue
            if path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if path in seen:
                continue
            seen.add(path)
            files.append(path)
    files.sort()
    return files


def scan_file(path: Path, repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    rel_path = path.relative_to(repo_root).as_posix()
    if rel_path == "scripts/check_portable_paths.py":
        return findings
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return findings

    is_json_like = path.suffix.lower() in {".json"}

    for index, line in enumerate(text.splitlines(), start=1):
        for kind, pattern in PATTERNS:
            for match in pattern.finditer(line):
                value = match.group(0)
                if kind == "unc":
                    # In JSON, UNC paths are escaped as \\\\server\\share; ignore double-backslash
                    # sequences that only represent normal path separators.
                    if is_json_like and not value.startswith("\\\\\\\\"):
                        continue
                    # Avoid partial matches inside templated task/setting expressions.
                    start = match.start()
                    if start > 0:
                        prev = line[start - 1]
                        if prev.isalnum() or prev in "}_$":
                            continue
                    # Root-relative escaped paths like \\.venv are not UNC shares.
                    if value.startswith("\\\\."):
                        continue
                findings.append(
                    Finding(
                        file=path.relative_to(repo_root),
                        line=index,
                        kind=kind,
                        value=value,
                    )
                )
    return findings


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    includes = list(args.include) if args.include else list(DEFAULT_INCLUDE)
    exclude_globs = list(args.exclude_glob) if args.exclude_glob else list(DEFAULT_EXCLUDE_GLOBS)

    files = iter_text_files(repo_root, includes, exclude_globs)
    findings: list[Finding] = []
    for path in files:
        findings.extend(scan_file(path, repo_root))

    print(f"checked_files={len(files)}")
    print(f"findings={len(findings)}")

    if findings:
        for finding in findings:
            print(
                f"FAIL|{finding.file.as_posix()}:{finding.line}|{finding.kind}|{finding.value}",
            )
        return 1

    print("PASS: no non-portable absolute path patterns in active scope")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
