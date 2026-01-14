#!/usr/bin/env python3
"""Wrapper: checks_rp_consistency.py

Audits Novapolis RP SSOT data under `novapolis-rp/database-rp` for consistency.

Goals (pragmatic, repo-local):
- Detect duplicate frontmatter blocks (common corruption pattern)
- Detect missing H1 (ATX or Setext)
- Detect broken local Markdown links
- Detect missing/duplicate slugs (soft checks)
- Detect broken scene cross-references (characters/locations/inventoryRefs)

Outputs (under `/.tmp/results/reports/`):
- A detailed log
- A JSON report (machine-readable)
- A short Markdown receipt with YAML frontmatter

Usage:
  python scripts/checks_rp_consistency.py

Exit codes:
- 0: no errors (warnings allowed unless --strict)
- 1: errors found (or warnings with --strict)
"""

from __future__ import annotations

import argparse
import json
import re
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

LOG_ENCODING = "utf-8"


@dataclass(frozen=True)
class Finding:
    level: str  # ERROR | WARN
    code: str
    file: str
    message: str


ATX_H1_RE = re.compile(r"^#\s+\S", re.MULTILINE)
SETEXT_H1_UNDERLINE_RE = re.compile(r"^=\s*=+\s*$")
FRONTMATTER_START_RE = re.compile(r"\A---\s*\r?\n")

# Very conservative link matcher (ignores images, captures inline links).
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

# `slug: ...` (allow underscores and version suffixes; validate separately)
SLUG_LINE_RE = re.compile(r"^slug:\s*(.+?)\s*$", re.MULTILINE)

# Accept common repo patterns: kebab, snake, and mixed (minimal enforcement here).
SLUG_VALUE_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]*$")

# Some docs deliberately store the canonical title in frontmatter to satisfy
# markdownlint MD025/single-title. In that case we must not require a Markdown H1.
FRONTMATTER_TITLE_RE = re.compile(r"^title:\s*\S", re.MULTILINE)
FRONTMATTER_CANVAS_RE = re.compile(r"^canvas:\s*\S", re.MULTILINE)

# keys used by scene crossrefs
SCENE_LIST_KEYS = ("characters", "locations", "inventoryRefs")


def resolve_repo_root() -> Path:
    here = Path(__file__).resolve()
    return here.parent.parent.resolve()


def now_ts_for_paths() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def now_ts_frontmatter() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding=LOG_ENCODING, errors="replace")


def has_h1(text: str) -> bool:
    if ATX_H1_RE.search(text):
        return True
    # Setext H1: a non-empty line followed by a line of '='
    lines = text.splitlines()
    for idx in range(len(lines) - 1):
        title = lines[idx].strip()
        underline = lines[idx + 1].strip()
        if title and SETEXT_H1_UNDERLINE_RE.match(underline):
            return True
    return False


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return (frontmatter_text_or_none, rest_text).

    Frontmatter is recognized only when the file starts with `---`.
    """

    if not FRONTMATTER_START_RE.search(text):
        return None, text

    # Find the *next* delimiter line `---`.
    lines = text.splitlines(keepends=True)
    if not lines:
        return None, text

    # First line is '---\n' (or '---\r\n')
    fm_lines: list[str] = []
    end_idx: int | None = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
        fm_lines.append(lines[i])

    if end_idx is None:
        # malformed frontmatter
        return "".join(fm_lines), ""  # treat as fm, no rest

    fm = "".join(fm_lines)
    rest = "".join(lines[end_idx + 1 :])
    return fm, rest


def has_duplicate_frontmatter(rest_text: str) -> bool:
    return rest_text.lstrip().startswith("---\n") or rest_text.lstrip().startswith("---\r\n")


def has_frontmatter_doc_title(frontmatter: str) -> bool:
    return bool(
        FRONTMATTER_TITLE_RE.search(frontmatter) or FRONTMATTER_CANVAS_RE.search(frontmatter)
    )


def parse_bracket_list(value: str) -> list[str]:
    inner = value.strip()
    if not (inner.startswith("[") and inner.endswith("]")):
        return []
    inner = inner[1:-1].strip()
    if not inner:
        return []
    parts = [p.strip() for p in inner.split(",")]
    cleaned: list[str] = []
    for part in parts:
        p = part.strip().strip('"').strip("'")
        if p:
            cleaned.append(p)
    return cleaned


def parse_frontmatter_lists(frontmatter: str) -> dict[str, list[str]]:
    """Parse a minimal subset of YAML/JSON-ish list values.

    Supports:
      key: [a, b]
      key: ["a", "b"]
      key:\n  - a\n  - b
    """

    lines = frontmatter.splitlines()
    out: dict[str, list[str]] = {}

    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not m:
            i += 1
            continue

        key = m.group(1)
        if key not in SCENE_LIST_KEYS:
            i += 1
            continue

        value = m.group(2).strip()
        if value.startswith("[") and value.endswith("]"):
            out[key] = parse_bracket_list(value)
            i += 1
            continue

        if value == "":
            items: list[str] = []
            j = i + 1
            while j < len(lines):
                li = lines[j]
                mm = re.match(r"^\s*-\s*(.+?)\s*$", li)
                if not mm:
                    break
                item = mm.group(1).strip().strip('"').strip("'")
                if item:
                    items.append(item)
                j += 1
            out[key] = items
            i = j
            continue

        # fallback: single scalar is treated as singleton list
        out[key] = [value.strip().strip('"').strip("'")]
        i += 1

    return out


def clean_frontmatter_scalar(raw: str) -> str:
    return raw.strip().strip('"').strip("'")


def extract_frontmatter_slug(frontmatter: str) -> str | None:
    m = SLUG_LINE_RE.search(frontmatter)
    if not m:
        return None
    slug = clean_frontmatter_scalar(m.group(1))
    return slug or None


def build_slug_index(files: list[Path]) -> tuple[set[str], set[str], dict[str, str]]:
    """Return (slug_set, stem_set, stem_to_slug).

    - slug_set is derived from each file's frontmatter `slug:`.
    - stem_set uses the filename stem as a fallback/diagnostic.
    - stem_to_slug is best-effort and used for error messages.
    """

    slug_set: set[str] = set()
    stem_set: set[str] = set()
    stem_to_slug: dict[str, str] = {}

    for p in files:
        stem_set.add(p.stem)
        text = read_text(p)
        fm, _rest = split_frontmatter(text)
        if fm is None:
            continue
        slug = extract_frontmatter_slug(fm)
        if slug:
            slug_set.add(slug)
            stem_to_slug[p.stem] = slug

    return slug_set, stem_set, stem_to_slug


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def iter_local_links(text: str) -> list[str]:
    links: list[str] = []
    for raw in MD_LINK_RE.findall(text):
        link = raw.strip()
        if not link:
            continue
        # strip surrounding angle brackets
        if link.startswith("<") and link.endswith(">"):
            link = link[1:-1].strip()
        links.append(link)
    return links


def is_remote_link(link: str) -> bool:
    lowered = link.lower()
    return lowered.startswith(("http://", "https://", "mailto:"))


def resolve_link_target(file_path: Path, link: str) -> Path | None:
    """Resolve a markdown link target to a filesystem path (if local).

    - ignores pure anchors (#...)
    - strips anchors and query strings
    """

    if link.startswith("#"):
        return None

    link = link.split("#", 1)[0].split("?", 1)[0].strip()
    if not link:
        return None

    # Windows paths in markdown are not expected here; treat as relative.
    if link.startswith("/"):
        # repo-relative
        return None

    return (file_path.parent / link).resolve()


def audit_rp(
    repo_root: Path,
    rp_root: Path,
    strict: bool,
    log_path: Path,
) -> tuple[dict[str, Any], int]:
    start = time.perf_counter()

    allow_no_h1 = {
        (rp_root / "00-admin" / "system-prompt.md").resolve(),
    }

    allow_no_slug = {
        # Template file uses placeholder slugs intentionally.
        (rp_root / "00-admin" / "schema-header-templates.md").resolve(),
    }

    findings: list[Finding] = []
    md_files = iter_markdown_files(rp_root)

    slugs: dict[str, list[str]] = {}
    missing_frontmatter: list[str] = []
    missing_slug: list[str] = []

    scenes_dir = (rp_root / "06-scenes").resolve()

    # pre-index for scene crossrefs (slug-only)
    char_files = list((rp_root / "02-characters").glob("*.md")) + list(
        (rp_root / "01-factions").glob("*/02-characters/*.md")
    )
    loc_files = list((rp_root / "03-locations").glob("*.md")) + list(
        (rp_root / "01-factions").glob("*/03-locations/*.md")
    )
    inv_files = list((rp_root / "04-inventory").glob("*.md")) + list(
        (rp_root / "01-factions").glob("*/04-inventory/*.md")
    )

    idx_char, idx_char_stem, idx_char_stem_to_slug = build_slug_index(char_files)
    idx_loc, idx_loc_stem, idx_loc_stem_to_slug = build_slug_index(loc_files)
    idx_inv, idx_inv_stem, idx_inv_stem_to_slug = build_slug_index(inv_files)

    with log_path.open("w", encoding=LOG_ENCODING) as lh:
        lh.write(f"RepoRoot: {repo_root}\n")
        lh.write(f"RPRoot: {rp_root}\n")
        lh.write(f"Files: {len(md_files)}\n\n")

        for file_path in md_files:
            rel = file_path.relative_to(repo_root).as_posix()
            text = read_text(file_path)

            fm, rest = split_frontmatter(text)
            if fm is None:
                missing_frontmatter.append(rel)
            else:
                if fm == "" and text.startswith("---"):
                    findings.append(
                        Finding(
                            "ERROR",
                            "FM_UNTERMINATED",
                            rel,
                            "Frontmatter starts but no closing '---' found",
                        )
                    )
                if has_duplicate_frontmatter(rest):
                    findings.append(
                        Finding(
                            "ERROR",
                            "FM_DUPLICATE",
                            rel,
                            "Duplicate frontmatter block detected",
                        )
                    )

                if file_path.resolve() not in allow_no_slug:
                    m = SLUG_LINE_RE.search(fm)
                    if not m:
                        missing_slug.append(rel)
                    else:
                        raw_slug = m.group(1).strip().strip('"').strip("'")
                        if not raw_slug:
                            missing_slug.append(rel)
                        elif "<" in raw_slug or ">" in raw_slug:
                            # Placeholder in frontmatter (templates) or unfinished doc.
                            findings.append(
                                Finding(
                                    "WARN",
                                    "SLUG_PLACEHOLDER",
                                    rel,
                                    f"slug looks like a placeholder: {raw_slug}",
                                )
                            )
                        elif not SLUG_VALUE_RE.match(raw_slug):
                            findings.append(
                                Finding(
                                    "WARN",
                                    "SLUG_INVALID",
                                    rel,
                                    f"slug contains unexpected characters: {raw_slug}",
                                )
                            )
                        else:
                            slugs.setdefault(raw_slug, []).append(rel)

                # H1 requirement: only when the doc doesn't provide a title in frontmatter.
                if (
                    file_path not in allow_no_h1
                    and not has_frontmatter_doc_title(fm)
                    and not has_h1(text)
                ):
                    findings.append(
                        Finding(
                            "ERROR",
                            "MD_H1_MISSING",
                            rel,
                            "Missing H1 heading (ATX '# ' or Setext '=')",
                        )
                    )

                # scene crossrefs
                if file_path.resolve().parent == scenes_dir:
                    lists = parse_frontmatter_lists(fm)
                    for c in lists.get("characters", []):
                        if not c:
                            continue
                        if c in idx_char:
                            continue
                        if c in idx_char_stem:
                            expected = idx_char_stem_to_slug.get(c)
                            hint = f" (expected slug: {expected})" if expected else ""
                            findings.append(
                                Finding(
                                    "ERROR",
                                    "XREF_CHAR_NON_SLUG",
                                    rel,
                                    f"character ref must be slug, not filename-stem: {c}{hint}",
                                )
                            )
                        else:
                            findings.append(
                                Finding(
                                    "ERROR",
                                    "XREF_CHAR_MISSING",
                                    rel,
                                    f"character ref not found: {c}",
                                )
                            )
                    for loc in lists.get("locations", []):
                        if not loc:
                            continue
                        if loc in idx_loc:
                            continue
                        if loc in idx_loc_stem:
                            expected = idx_loc_stem_to_slug.get(loc)
                            hint = f" (expected slug: {expected})" if expected else ""
                            findings.append(
                                Finding(
                                    "ERROR",
                                    "XREF_LOC_NON_SLUG",
                                    rel,
                                    f"location ref must be slug, not filename-stem: {loc}{hint}",
                                )
                            )
                        else:
                            findings.append(
                                Finding(
                                    "ERROR",
                                    "XREF_LOC_MISSING",
                                    rel,
                                    f"location ref not found: {loc}",
                                )
                            )
                    for iref in lists.get("inventoryRefs", []):
                        if not iref:
                            continue
                        if iref in idx_inv:
                            continue
                        if iref in idx_inv_stem:
                            expected = idx_inv_stem_to_slug.get(iref)
                            hint = f" (expected slug: {expected})" if expected else ""
                            findings.append(
                                Finding(
                                    "ERROR",
                                    "XREF_INV_NON_SLUG",
                                    rel,
                                    f"inventory ref must be slug, not filename-stem: {iref}{hint}",
                                )
                            )
                        else:
                            findings.append(
                                Finding(
                                    "ERROR",
                                    "XREF_INV_MISSING",
                                    rel,
                                    f"inventory ref not found: {iref}",
                                )
                            )

            # broken local links (skip remote)
            for link in iter_local_links(text):
                if is_remote_link(link):
                    continue
                target = resolve_link_target(file_path, link)
                if target is None:
                    continue
                # Only validate links that look like files or folders.
                # Keep it simple: ignore non-existent anchors-only and empty.
                if not target.exists():
                    findings.append(
                        Finding(
                            "ERROR",
                            "LINK_BROKEN",
                            rel,
                            f"broken link target: {link}",
                        )
                    )

        # derive slug duplicates as WARN (doesn't always mean wrong, but is risky)
        for slug, files in sorted(slugs.items()):
            if len(files) > 1:
                msg = f"Duplicate slug '{slug}' in {len(files)} files"
                for f in files:
                    findings.append(Finding("WARN", "SLUG_DUPLICATE", f, msg))

        if missing_frontmatter:
            findings.append(
                Finding(
                    "WARN",
                    "FM_MISSING",
                    str(rp_root.relative_to(repo_root).as_posix()),
                    f"{len(missing_frontmatter)} files without YAML frontmatter",
                )
            )

        if missing_slug:
            findings.append(
                Finding(
                    "WARN",
                    "SLUG_MISSING",
                    str(rp_root.relative_to(repo_root).as_posix()),
                    f"{len(missing_slug)} files with frontmatter but missing 'slug:'",
                )
            )

        # Log summary
        errors = [f for f in findings if f.level == "ERROR"]
        warns = [f for f in findings if f.level == "WARN"]
        lh.write(f"Errors: {len(errors)}\n")
        lh.write(f"Warnings: {len(warns)}\n\n")
        for f in errors[:200]:
            lh.write(f"ERROR {f.code} {f.file}: {f.message}\n")
        if len(errors) > 200:
            lh.write(f"... truncated ({len(errors) - 200} more errors)\n")
        if warns:
            lh.write("\nWARNINGS (first 200):\n")
            for f in warns[:200]:
                lh.write(f"WARN {f.code} {f.file}: {f.message}\n")
            if len(warns) > 200:
                lh.write(f"... truncated ({len(warns) - 200} more warnings)\n")

    duration_ms = int((time.perf_counter() - start) * 1000)
    errors = [f for f in findings if f.level == "ERROR"]
    warns = [f for f in findings if f.level == "WARN"]

    report: dict[str, Any] = {
        "tool": "checks_rp_consistency",
        "ts": datetime.now().isoformat(timespec="seconds"),
        "repo_root": str(repo_root),
        "rp_root": str(rp_root),
        "files_scanned": len(md_files),
        "duration_ms": duration_ms,
        "counts": {
            "errors": len(errors),
            "warnings": len(warns),
            "missing_frontmatter": len(missing_frontmatter),
            "missing_slug": len(missing_slug),
        },
        "missing_frontmatter": missing_frontmatter,
        "missing_slug": missing_slug,
        "findings": [f.__dict__ for f in findings],
    }

    exit_code = 0
    if errors:
        exit_code = 1
    elif strict and warns:
        exit_code = 1

    return report, exit_code


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Fail (exit 1) when warnings exist",
    )
    args = parser.parse_args()

    repo_root = resolve_repo_root()
    rp_root = repo_root / "novapolis-rp" / "database-rp"

    ts = now_ts_for_paths()
    out_dir = repo_root / ".tmp" / "results" / "reports"
    ensure_dir(out_dir)

    log_path = out_dir / f"checks_rp_consistency_{ts}.log"
    json_path = out_dir / f"rp_consistency_report_{ts}.json"
    receipt_path = out_dir / f"checks_rp_consistency_postflight_{ts}.md"

    report, exit_code = audit_rp(repo_root, rp_root, args.strict, log_path)

    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False) + "\n",
        encoding=LOG_ENCODING,
    )

    with receipt_path.open("w", encoding=LOG_ENCODING) as rf:
        rf.write("---\n")
        rf.write(f"stand: {now_ts_frontmatter()}\n")
        rf.write("update: RP database-rp consistency audit\n")
        rf.write("checks: report + log created\n")
        rf.write("---\n\n")
        rf.write("RP Consistency Audit\n")
        rf.write("====================\n\n")
        rf.write(f"Scope: {rp_root.as_posix()}\n\n")
        rf.write(f"Log: {log_path.as_posix()}\n")
        rf.write(f"Report (JSON): {json_path.as_posix()}\n\n")
        rf.write("Summary\n")
        rf.write("-------\n\n")
        rf.write(f"- files_scanned: {report['files_scanned']}\n")
        rf.write(f"- errors: {report['counts']['errors']}\n")
        rf.write(f"- warnings: {report['counts']['warnings']}\n")
        rf.write(f"- missing_frontmatter: {report['counts']['missing_frontmatter']}\n")
        rf.write(f"- missing_slug: {report['counts']['missing_slug']}\n")

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
