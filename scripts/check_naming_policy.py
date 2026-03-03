"""Validate naming policy rules in active SSOT/doc scopes.

Outputs findings as: Datei:Zeile:Regel:Wert
Exit code is non-zero only when hard failures are present.
"""

from __future__ import annotations

import argparse
import fnmatch
import re
from dataclasses import dataclass
from pathlib import Path

DEFAULT_INCLUDE: tuple[str, ...] = (
    ".github",
    "novapolis-dev/docs",
    "README.md",
    "WORKSPACE_INDEX.md",
    "WORKSPACE_STATUS.md",
    "DONELOG.md",
    "todo.root.md",
)

DEFAULT_EXCLUDE_GLOBS: tuple[str, ...] = (
    ".git/**",
    ".venv/**",
    "Backups/**",
    "outputs/**",
    ".tmp/**",
    ".tmp-results/**",
    "novapolis-dev/archive/**",
    "novapolis-rp/database-raw/**",
    "novapolis-rp/database-curated/staging/**",
    "novapolis_agent/eval/results/**",
)

TEXT_SUFFIXES: tuple[str, ...] = (
    ".md",
    ".txt",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".py",
)

FILENAME_ALLOWED_RE = re.compile(r"^[A-Za-z0-9._-]+$")
SLUG_RE = re.compile(r"^[a-z0-9]+(?:[-_][a-z0-9]+)*$")
RULE_ID_RE = re.compile(r"^(R|E)-[A-Z0-9]+(?:-[A-Z0-9]+)*$")
REASON_CODE_RE = re.compile(r"^RC-[a-z0-9_]+$")


@dataclass(frozen=True)
class Finding:
    file: Path
    line: int
    rule: str
    value: str
    severity: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check naming policy conformance in active docs")
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    parser.add_argument(
        "--include", action="append", default=None, help="Include file/folder relative to repo root"
    )
    parser.add_argument(
        "--exclude-glob",
        action="append",
        default=None,
        help="Exclude glob relative to repo root",
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

        candidates = [target] if target.is_file() else [p for p in target.rglob("*") if p.is_file()]
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


def parse_frontmatter(lines: list[str]) -> tuple[dict[str, str], int, int]:
    if not lines or lines[0].strip() != "---":
        return {}, -1, -1
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            data: dict[str, str] = {}
            for raw in lines[1:i]:
                if ":" not in raw:
                    continue
                key, value = raw.split(":", 1)
                data[key.strip()] = value.strip()
            return data, 1, i + 1
    return {}, -1, -1


def validate_file(path: Path, repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    rel = path.relative_to(repo_root)
    rel_posix = rel.as_posix()

    name = path.name
    if not FILENAME_ALLOWED_RE.match(name):
        findings.append(Finding(rel, 1, "NP-NAME-001", name, "hard"))

    if rel_posix.startswith(".github/instructions/") and not name.endswith(".instructions.md"):
        findings.append(Finding(rel, 1, "NP-NAME-002", name, "hard"))

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        findings.append(Finding(rel, 1, "NP-NAME-099", "binary-or-invalid-utf8", "warn"))
        return findings

    lines = text.splitlines()
    frontmatter, fm_start, fm_end = parse_frontmatter(lines)
    if fm_start != -1 and "slug" in frontmatter:
        slug = frontmatter["slug"].strip("\"'")
        if slug and not SLUG_RE.match(slug):
            findings.append(Finding(rel, fm_start + 1, "NP-NAME-010", slug, "hard"))

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if "id:" in stripped and "priority:" in stripped:
            match = re.search(r"id:\s*([A-Za-z0-9-]+)", stripped)
            if match:
                value = match.group(1)
                # Only validate namespace-form where the field actually looks like a rule ID.
                if value.startswith(("R-", "E-")) and not RULE_ID_RE.match(value):
                    findings.append(Finding(rel, idx, "NP-NAME-020", value, "hard"))

        for match in re.finditer(r"\bRC-[A-Za-z0-9_]+\b", line):
            code = match.group(0)
            if not REASON_CODE_RE.match(code):
                findings.append(Finding(rel, idx, "NP-NAME-030", code, "hard"))

        if "tags:" in stripped and fm_end != -1 and idx <= fm_end:
            if not ("[" in stripped and "]" in stripped):
                findings.append(Finding(rel, idx, "NP-NAME-040", stripped, "warn"))

    return findings


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    includes = list(args.include) if args.include else list(DEFAULT_INCLUDE)
    excludes = list(args.exclude_glob) if args.exclude_glob else list(DEFAULT_EXCLUDE_GLOBS)

    files = iter_text_files(repo_root, includes, excludes)
    findings: list[Finding] = []
    for path in files:
        findings.extend(validate_file(path, repo_root))

    hard = [f for f in findings if f.severity == "hard"]
    warn = [f for f in findings if f.severity == "warn"]

    print(f"checked_files={len(files)}")
    print(f"hard_findings={len(hard)}")
    print(f"warn_findings={len(warn)}")

    for finding in findings:
        prefix = finding.rule if finding.severity == "hard" else f"W-{finding.rule}"
        print(f"{finding.file.as_posix()}:{finding.line}:{prefix}:{finding.value}")

    if hard:
        return 1
    print("PASS: naming policy checks passed for active scope")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
