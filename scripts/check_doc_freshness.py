"""Enforce freshness SLA for the workspace-leading documentation scope.

Thresholds:
- ACTIVE: <= 14 days
- REFERENCE: <= 60 days

Scope is derived from `novapolis-dev/docs/meta/doc-freshness-scope.md`.
Rows may use concrete file paths or globs and can choose one of three
freshness modes:
- frontmatter: parse `stand` from YAML frontmatter
- legacy-header: parse `stand:` from a historical top-of-file header block
- mtime: use filesystem modification time
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

DOC_FRESHNESS_SCOPE = "novapolis-dev/docs/meta/doc-freshness-scope.md"
STAND_FORMAT = "%Y-%m-%d %H:%M"
ROW_RE = re.compile(
    r"^\|\s*`(?P<path>[^`]+)`\s*\|\s*(?P<surface>ACTIVE|REFERENCE|HISTORICAL)\s*\|\s*(?P<mode>frontmatter|legacy-header|mtime)\s*\|\s*(?P<max_age_days>-|\d+)\s*\|"
)
GLOB_CHARS = "*?["


@dataclass(frozen=True)
class ScopeRow:
    pattern: str
    surface: str
    mode: str
    max_age_days: int | None


@dataclass(frozen=True)
class ScopeEntry:
    rel_path: str
    surface: str
    mode: str
    max_age_days: int | None


@dataclass(frozen=True)
class Finding:
    path: str
    reason: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check stand freshness for active dev docs")
    parser.add_argument("--repo-root", default=".", help="Repository root path")
    parser.add_argument(
        "--active-days",
        type=int,
        default=14,
        help="Max age in days for ACTIVE docs",
    )
    parser.add_argument(
        "--reference-days", type=int, default=60, help="Max age in days for REFERENCE docs"
    )
    return parser.parse_args()


def parse_scope_rows(scope_path: Path) -> list[ScopeRow]:
    rows: list[ScopeRow] = []
    for raw in scope_path.read_text(encoding="utf-8").splitlines():
        match = ROW_RE.match(raw.strip())
        if not match:
            continue
        rows.append(
            ScopeRow(
                pattern=match.group("path").strip(),
                surface=match.group("surface").strip(),
                mode=match.group("mode").strip(),
                max_age_days=(
                    None if match.group("max_age_days") == "-" else int(match.group("max_age_days"))
                ),
            )
        )
    return rows


def expand_scope_rows(
    repo_root: Path,
    rows: list[ScopeRow],
) -> tuple[list[ScopeEntry], list[Finding], int]:
    expanded: dict[str, ScopeEntry] = {}
    findings: list[Finding] = []
    expanded_glob_rows = 0

    for row in rows:
        if row.surface == "HISTORICAL":
            continue

        is_glob = any(char in row.pattern for char in GLOB_CHARS)
        if is_glob:
            matches = sorted(path for path in repo_root.glob(row.pattern) if path.is_file())
            expanded_glob_rows += 1
        else:
            matches = [(repo_root / row.pattern).resolve()]

        if not matches:
            findings.append(
                Finding(
                    row.pattern,
                    "missing_scope_match",
                    "scope row did not resolve to a file",
                )
            )
            continue

        for match in matches:
            rel = match.resolve().relative_to(repo_root).as_posix()
            current = expanded.get(rel)
            if current is None or (current.surface == "REFERENCE" and row.surface == "ACTIVE"):
                expanded[rel] = ScopeEntry(
                    rel_path=rel,
                    surface=row.surface,
                    mode=row.mode,
                    max_age_days=row.max_age_days,
                )

    return sorted(expanded.values(), key=lambda entry: entry.rel_path), findings, expanded_glob_rows


def parse_stand_value(doc_path: Path) -> datetime | None:
    lines = doc_path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        line = lines[i].strip()
        if line == "---":
            return None
        if line.startswith("stand:"):
            value = line.split(":", 1)[1].strip().strip("\"'")
            try:
                return datetime.strptime(value, STAND_FORMAT)
            except ValueError:
                return None
    return None


def parse_legacy_header_stand(doc_path: Path) -> datetime | None:
    for raw in doc_path.read_text(encoding="utf-8").splitlines()[:20]:
        line = raw.strip()
        if not line.startswith("stand:"):
            continue
        value = line.split(":", 1)[1].strip().strip("\"'")
        try:
            return datetime.strptime(value, STAND_FORMAT)
        except ValueError:
            return None
    return None


def resolve_freshness_timestamp(doc_path: Path, mode: str) -> datetime | None:
    if mode == "frontmatter":
        return parse_stand_value(doc_path)
    if mode == "legacy-header":
        return parse_legacy_header_stand(doc_path)
    if mode == "mtime":
        return datetime.fromtimestamp(doc_path.stat().st_mtime)
    return None


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    scope_path = (repo_root / DOC_FRESHNESS_SCOPE).resolve()

    if not scope_path.exists():
        print(f"FAIL: missing scope file {DOC_FRESHNESS_SCOPE}")
        return 1

    now = datetime.now()
    rows = parse_scope_rows(scope_path)
    entries, findings, expanded_glob_rows = expand_scope_rows(repo_root, rows)

    checked = 0

    for entry in entries:
        doc_path = (repo_root / entry.rel_path).resolve()
        if not doc_path.exists() or not doc_path.is_file():
            findings.append(
                Finding(
                    entry.rel_path,
                    "missing_file",
                    "scope path missing",
                )
            )
            continue

        freshness_dt = resolve_freshness_timestamp(doc_path, entry.mode)
        if freshness_dt is None:
            findings.append(
                Finding(
                    entry.rel_path,
                    "invalid_or_missing_freshness_marker",
                    f"mode={entry.mode} did not yield a freshness timestamp",
                )
            )
            continue

        checked += 1
        age_days = int((now - freshness_dt).total_seconds() // 86400)
        default_limit = args.active_days if entry.surface == "ACTIVE" else args.reference_days
        limit = entry.max_age_days if entry.max_age_days is not None else default_limit
        if age_days > limit:
            findings.append(
                Finding(
                    entry.rel_path,
                    "stale",
                    (
                        f"surface={entry.surface}; mode={entry.mode}; "
                        f"age_days={age_days}; limit={limit}"
                    ),
                )
            )

    print(f"scope_rows={len(rows)}")
    print(f"expanded_glob_rows={expanded_glob_rows}")
    print(f"checked_docs={checked}")
    print(f"findings={len(findings)}")

    if findings:
        for finding in findings:
            print(f"FAIL|{finding.path}|{finding.reason}|{finding.detail}")
        return 1

    print(
        "PASS: stand freshness SLA satisfied "
        f"(ACTIVE<={args.active_days}d, REFERENCE<={args.reference_days}d)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
