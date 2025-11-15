#!/usr/bin/env python3
"""
YAML-driven tagging pipeline for chat chunks.

- Parses Markdown front-matter from database-rp/** to build a lexicon (by_slug, aliases).
- Tags chunk files line-by-line with semantic labels based on slugs/aliases.
-
CLI:
  python coding/tools/curation/tag_chunks_from_yaml.py \
    --yaml-root "database-rp" \
    --chunks-root "database-curated/staging/chunks/chat-export (1)" \
    --out-root "database-curated/reviewed/chat-export (1)" \
    --range 019-016 [--dry-run] [--alias-file aliases.json]

Implementation details:
 - Tries to import PyYAML; if unavailable, falls back to a minimal front-matter parser.
 - Streaming line processing to keep memory footprint low.
 - Writes index_review.json, unresolved.json and a warnings log under reports/.

Note: This script is designed to be Windows-friendly (paths with spaces/parentheses) via pathlib.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    yaml = None  # Fallback parser will be used


# ----------------------------- Utilities / Data ----------------------------- #


@dataclass
class LexEntry:
    slug: str
    category: str
    title: str


@dataclass
class Lexicon:
    by_slug: dict[str, LexEntry]
    aliases: dict[str, str]  # alias token (case as provided) -> slug
    unresolved_dependencies: set[str]
    alias_collisions: dict[str, set[str]]
    redirects: dict[str, str]
    deprecated: set[str]


FRONTMATTER_START = re.compile(r"^---\s*$")
FRONTMATTER_END = re.compile(r"^---\s*$")


def read_frontmatter(md_path: Path) -> dict | None:
    """Read the first YAML front-matter block from a Markdown file.

    Returns a dict or None if no front-matter present. Tries yaml.safe_load if
    PyYAML is available; otherwise uses a minimal parser supporting:
      - key: value
      - key: [a, b, c]
      - simple dash lists:
            key:
              - a
              - b
    """
    try:
        text = md_path.read_text(encoding="utf-8")
    except Exception:
        return None

    lines = text.splitlines()
    if not lines or not FRONTMATTER_START.match(lines[0]):
        return None

    # Find end marker
    block_lines: list[str] = []
    for i in range(1, len(lines)):
        if FRONTMATTER_END.match(lines[i]):
            block_lines = lines[1:i]
            break
    if not block_lines:
        return None

    block = "\n".join(block_lines)
    if yaml is not None:
        try:
            data = yaml.safe_load(block)
            return data if isinstance(data, dict) else None
        except Exception:
            pass

    # Minimal fallback parser
    result: dict[str, object] = {}
    key: str | None = None
    pending_list: list[str] | None = None
    for raw in block_lines:
        line = raw.rstrip()
        if not line:
            continue
        if re.match(r"^[A-Za-z0-9_\-]+:\s*\[", line):
            # key: [a, b, c]
            k, v = line.split(":", 1)
            arr = v.strip()
            try:
                arr_json = arr.replace("'", '"')
                result[k.strip()] = json.loads(arr_json)
            except Exception:
                # crude split fallback
                inner = arr.strip().lstrip("[").rstrip("]")
                result[k.strip()] = [s.strip() for s in inner.split(",") if s.strip()]
            key = None
            pending_list = None
            continue
        m = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if m:
            key = m.group(1).strip()
            rest = m.group(2).strip()
            if rest == "":
                # maybe a dash list follows
                pending_list = []
                result[key] = pending_list
            else:
                result[key] = rest
                pending_list = None
            continue
        if pending_list is not None:
            m2 = re.match(r"^-\s*(.*)$", line)
            if m2:
                pending_list.append(m2.group(1).strip())
    return result


def is_short_location_slug(slug: str) -> bool:
    # "short" like c6, d5, a12; keep conservative
    return bool(re.match(r"^[a-z]\d{1,2}$", slug))


def build_word_safe_regex(
    token: str, *, alnum_dash_underscore: bool = True, case_sensitive: bool = True
) -> re.Pattern:
    """Build word-safe regex for token with negative look-arounds.

    For slugs: (?<![A-Za-z0-9_-])token(?![A-Za-z0-9_-])
    For multiword aliases: (?<!\\w)Alias\\ Name(?!\\w)
    """
    cls = r"[A-Za-z0-9_-]" if alnum_dash_underscore else r"\w"
    pattern = rf"(?<!{cls}){re.escape(token)}(?!{cls})"
    flags = 0 if case_sensitive else re.IGNORECASE
    return re.compile(pattern, flags)


def build_lexicon(yaml_root: Path, extra_aliases: dict[str, str] | None = None) -> Lexicon:
    by_slug: dict[str, LexEntry] = {}
    title_by_slug: dict[str, str] = {}
    category_by_slug: dict[str, str] = {}
    primary_locs: set[str] = set()
    last_seens: set[str] = set()
    deps_all: set[str] = set()

    # 1) First pass: read all front-matter
    for md_path in yaml_root.rglob("*.md"):
        fm = read_frontmatter(md_path)
        if not fm or not isinstance(fm, dict):
            continue
        slug = str(fm.get("slug", "")).strip().lower()
        title = str(fm.get("title", slug)).strip()
        category = str(fm.get("category", "unknown")).strip().lower()
        if not slug:
            continue
        by_slug[slug] = LexEntry(slug=slug, category=category, title=title)
        title_by_slug[slug] = title
        category_by_slug[slug] = category

        pl = fm.get("primary_location")
        if isinstance(pl, str) and pl.strip():
            primary_locs.add(pl.strip().lower())
        ls = fm.get("last_seen")
        if isinstance(ls, str) and ls.strip():
            last_seens.add(ls.strip().lower())
        deps = fm.get("dependencies")
        if isinstance(deps, list):
            for d in deps:
                if isinstance(d, str) and d.strip():
                    deps_all.add(d.strip().lower())

    # 2) Ensure referenced locations exist in by_slug (category location if unknown)
    for loc_slug in sorted(primary_locs | last_seens):
        if loc_slug not in by_slug:
            by_slug[loc_slug] = LexEntry(slug=loc_slug, category="location", title=loc_slug.upper())

    # Force-add canonical entries if missing
    if "c6-nord" not in by_slug:
        by_slug["c6-nord"] = LexEntry(slug="c6-nord", category="location", title="C6 Nord")
    if "mission-c6-nord" not in by_slug:
        by_slug["mission-c6-nord"] = LexEntry(
            slug="mission-c6-nord", category="mission", title="Mission C6-Nord (Sealed room)"
        )

    # 3) Build aliases: title-basierte Zuordnungen, Case-Varianten für kurze
    # Location-Slugs sowie erste/letzte Tokens aus Titeln
    aliases: dict[str, str] = {}
    alias_collisions: dict[str, set[str]] = defaultdict(set)

    def add_alias(alias: str, slug: str) -> None:
        existing = aliases.get(alias)
        if existing and existing != slug:
            alias_collisions[alias].update({existing, slug})
        else:
            aliases[alias] = slug

    for s, entry in by_slug.items():
        if entry.title:
            add_alias(entry.title, s)
            # Expand first/last tokens from multi-word titles as aliases (both cases)
            parts = [p for p in re.split(r"\s+", entry.title.strip()) if p]
            if len(parts) >= 2:
                first, last = parts[0], parts[-1]
                for token in {first, last, first.lower(), last.lower()}:
                    add_alias(token, s)
        if entry.category == "location" and is_short_location_slug(entry.slug):
            add_alias(entry.slug.upper(), entry.slug)
            add_alias(entry.slug.lower(), entry.slug)

    if extra_aliases:
        for k, v in extra_aliases.items():
            if not isinstance(k, str) or not isinstance(v, str):
                continue
            add_alias(k, v.lower())

    # Add requested aliases/redirects for C6-Nord; canonicalize N7 -> c6-nord
    add_alias("C6-Nord", "c6-nord")
    add_alias("C6 Nord", "c6-nord")
    add_alias("N7", "c6-nord")
    add_alias("n7", "c6-nord")
    add_alias("Mission C6-Nord", "mission-c6-nord")
    add_alias("C6-Nord Mission", "mission-c6-nord")

    # 4) Unresolved dependencies
    unresolved = {d for d in deps_all if d not in by_slug}

    redirects = {"n7": "c6-nord"}
    deprecated = {"n7"}

    return Lexicon(
        by_slug=by_slug,
        aliases=aliases,
        unresolved_dependencies=unresolved,
        alias_collisions=alias_collisions,
        redirects=redirects,
        deprecated=deprecated,
    )


# ------------------------------ Tagging logic ------------------------------- #


def detect_time_anchor(line: str) -> bool:
    if re.search(r"\b\d{4}-\d{2}-\d{2}\b", line):
        return True
    if re.search(r"\b\d{1,2}:\d{2}\b", line):
        return True
    if re.search(r"\b(Tag|Woche)\s+\d+\b", line, flags=re.IGNORECASE):
        return True
    return False


def detect_fact_candidate(line: str) -> bool:
    units = r"m|km|kwh|t|%|°c"
    if re.search(rf"\b(\d+[\.,]?\d*)\s*({units})\b", line, flags=re.IGNORECASE):
        return True
    if re.search(
        r"\b(ist|sind|hat|haben|beträgt)\b.{0,40}\b\d+[\.,]?\d*\b", line, flags=re.IGNORECASE
    ):
        return True
    return False


def categorize(slug: str, lex: Lexicon) -> str:
    entry = lex.by_slug.get(slug)
    cat = (entry.category if entry else "unknown").lower()
    if cat == "character":
        return "CHAR"
    if cat == "location":
        return "LOC"
    if cat == "project":
        return "PROJ"
    if cat == "mission":
        return "MISSION"
    return "ENT"


def build_patterns(lex: Lexicon) -> tuple[dict[str, re.Pattern], dict[str, tuple[str, re.Pattern]]]:
    # slug patterns: lowercase on lowercase copy of the line, word-safe
    slug_patterns: dict[str, re.Pattern] = {
        slug: build_word_safe_regex(slug, alnum_dash_underscore=True, case_sensitive=False)
        for slug in lex.by_slug.keys()
    }
    # alias patterns: case-sensitive on original line; use \w class for multiword
    alias_patterns: dict[str, tuple[str, re.Pattern]] = {}
    for alias, slug in lex.aliases.items():
        # Special-case: N7 alias is handled via canonicalization with metro-disambiguation
        if alias.lower() == "n7":
            continue
        # Heuristic: if alias contains space, use \w class; else alnum/dash/underscore
        use_word = " " in alias
        pat = build_word_safe_regex(alias, alnum_dash_underscore=not use_word, case_sensitive=True)
        alias_patterns[alias] = (slug, pat)
    return slug_patterns, alias_patterns


# ------------------------------ New heuristics ------------------------------ #

METRO_TERMS = {
    "metro",
    "ubahn",
    "u-bahn",
    "bahn",
    "station",
    "haltestelle",
    "linie",
    "strecke",
    "gleis",
    "zug",
    "fahrplan",
}
NOTE_PREFIXES = [
    "Anmerkung:",
    "Achtung",
    "Hinweis:",
    "TODO:",
    "Todo:",
    "-",
    "*",
    "•",
    "1)",
    "1.",
    "#",
    ">",
]
EVENT_TOKENS = {
    "ankunft",
    "abmarsch",
    "evakuierung",
    "besprechung",
    "fund",
    "unfall",
    "störung",
    "start",
    "stopp",
    "prüfbericht",
    "sichtprüfung",
    "freigabe",
    "sperre",
}
MISSION_TERMS = {
    "versiegelt",
    "gesperrt",
    "quarantäne",
    "untersuchung",
    "siegel",
    "seal",
    "abgesperrt",
    "sperrzone",
    "sperrbereich",
}

SECTOR_CODE_RE = re.compile(r"(?<![A-Za-z0-9])([A-HJ-NR-Z])(\d)(?![A-Za-z0-9])")
N7_RE = build_word_safe_regex("n7", alnum_dash_underscore=True, case_sensitive=False)


def is_note_line(line: str) -> bool:
    stripped = line.lstrip()
    for p in NOTE_PREFIXES:
        if stripped.lower().startswith(p.lower()):
            return True
    return False


def is_metro_context(lines: list[str], idx: int) -> bool:
    # Look ±3 lines window for metro terms
    start = max(0, idx - 3)
    end = min(len(lines), idx + 4)
    window = "\n".join(lines[start:end]).lower()
    return any(t in window for t in METRO_TERMS)


def process_chunk_file(
    in_path: Path,
    out_path: Path,
    lex: Lexicon,
    slug_patterns: dict[str, re.Pattern],
    alias_patterns: dict[str, tuple[str, re.Pattern]],
    *,
    dry_run: bool,
    warnings: list[str],
) -> dict[str, object]:
    lines_total = 0
    chars_total = 0
    tag_counts = Counter()
    slug_counter = Counter()
    canon_n7_count = 0

    # Co-occurrence tracking (location slugs)
    locs_per_line: list[set[str]] = []

    if not dry_run:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        fout = out_path.open("w", encoding="utf-8", newline="\n")
    else:
        fout = None

    try:
        with in_path.open("r", encoding="utf-8", errors="ignore") as fin:
            all_lines = [ln.rstrip("\n") for ln in fin]
            for i, line in enumerate(all_lines):
                line_lower = line.lower()
                lines_total += 1
                chars_total += len(line)

                found_slugs: set[str] = set()
                # slug matches on lowercased line
                for slug, pat in slug_patterns.items():
                    if pat.search(line_lower):
                        found_slugs.add(slug)

                # alias matches on original line
                for _alias, (slug, pat) in alias_patterns.items():
                    if pat.search(line):
                        found_slugs.add(slug)

                # 2) Canonicalize N7 -> c6-nord if not metro context
                if N7_RE.search(line) and not is_metro_context(all_lines, i):
                    found_slugs.add("c6-nord")
                    canon_n7_count += 1

                # 4) Sector code fallback for locations
                for m in SECTOR_CODE_RE.finditer(line):
                    code = (m.group(1) + m.group(2)).lower()
                    if code not in lex.by_slug:
                        # Insert minimal entry and alias
                        lex.by_slug[code] = LexEntry(
                            slug=code, category="location", title=(m.group(1) + m.group(2)).upper()
                        )
                        slug_patterns[code] = build_word_safe_regex(
                            code, alnum_dash_underscore=True, case_sensitive=False
                        )
                    found_slugs.add(code)

                # categorize and order
                grouped: dict[str, list[str]] = {
                    "CHAR": [],
                    "LOC": [],
                    "PROJ": [],
                    "MISSION": [],
                    "ENT": [],
                }
                for slug in sorted(found_slugs):
                    kind = categorize(slug, lex)
                    grouped[kind].append(slug)
                    slug_counter[slug] += 1
                    tag_counts[kind] += 1

                tags: list[str] = []
                for key in ["CHAR", "LOC", "PROJ", "MISSION", "ENT"]:
                    for slug in grouped[key]:
                        tags.append(f"[{key}:{slug}]")

                # Heuristics
                time_flag = detect_time_anchor(line)
                if time_flag:
                    tags.append("[TIME]")
                    tag_counts["TIME"] += 1
                if detect_fact_candidate(line):
                    tags.append("[FACT?]")
                    tag_counts["FACT?"] += 1

                # 5) Minimal [EVENT] heuristic
                if any(tok in line_lower for tok in EVENT_TOKENS):
                    tags.append("[EVENT]")
                    tag_counts["EVENT"] += 1

                # 3) [NOTE] tagging and warning suppression awareness
                note_flag = is_note_line(line)
                if note_flag:
                    tags.append("[NOTE]")
                    tag_counts["NOTE"] += 1

                # Warnings: LOC only (no other entity tag)
                if (
                    grouped["LOC"]
                    and not (
                        grouped["CHAR"] or grouped["PROJ"] or grouped["MISSION"] or grouped["ENT"]
                    )
                    and not note_flag
                ):
                    warnings.append(f"{in_path.name}:{lines_total} LOC-only line: {line}")

                # 8) Mission tagging for C6-Nord with context terms in ±3 lines window
                if ("c6-nord" in found_slugs) and any(
                    t in "\n".join(all_lines[max(0, i - 3) : min(len(all_lines), i + 4)]).lower()
                    for t in MISSION_TERMS
                ):
                    # append mission tag if not present
                    mission_tag = "[MISSION:mission-c6-nord]"
                    if mission_tag not in tags:
                        tags.append(mission_tag)
                        tag_counts["MISSION"] += 1

                out_line = line if not tags else f"{line} {' '.join(tags)}"
                if not dry_run and fout is not None:
                    fout.write(out_line + "\n")

                # Track locations per line for suggestions
                locs_per_line.append(set(grouped["LOC"]))
    finally:
        if fout is not None:
            fout.close()

    # Co-occurrence alias suggestions (report-only) for 'n7'
    alias_suggestions: list[dict[str, object]] = []
    if locs_per_line:
        total = 0
        hits: Counter = Counter()
        # Consider 'n7' co-occurrence with other locs within ±2 lines
        for i, locs in enumerate(locs_per_line):
            if "n7" in locs or "c6-nord" in locs:
                start = max(0, i - 2)
                end = min(len(locs_per_line), i + 3)
                neighborhood = set().union(*locs_per_line[start:end])
                for loc in neighborhood:
                    if loc != "n7":
                        total += 1
                        hits[loc] += 1
        if total >= 10 and hits:
            cand, count = hits.most_common(1)[0]
            share = count / max(1, total)
            if share >= 0.7:
                alias_suggestions.append(
                    {"source": "n7", "candidate": cand, "total": total, "hits": count}
                )

    top_slugs = slug_counter.most_common(10)
    return {
        "file": in_path.name,
        "lines": lines_total,
        "chars": chars_total,
        "tag_counts": dict(tag_counts),
        "top_slugs": [{"slug": s, "count": c} for s, c in top_slugs],
        "canonicalized_n7": canon_n7_count,
        "alias_suggestions": alias_suggestions,
    }


def parse_range(spec: str) -> list[int]:
    m = re.match(r"^(\d{3})\s*-\s*(\d{3})$", spec.strip())
    if not m:
        raise ValueError("--range must be like 019-016")
    a = int(m.group(1))
    b = int(m.group(2))
    step = -1 if a > b else 1
    return list(range(a, b + step, step))


def load_optional_alias_file(path: Path | None) -> dict[str, str] | None:
    if not path:
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            return {str(k): str(v).lower() for k, v in data.items()}
    except Exception:
        pass
    return None


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    # Allow --self-test without other required args
    if "--self-test" in argv:
        return self_test()

    ap = argparse.ArgumentParser(
        description="Tag chat chunk files based on YAML front-matter lexicon."
    )
    ap.add_argument(
        "--yaml-root",
        default="database-rp",
        help="Root folder containing Markdown with YAML front-matter",
    )
    ap.add_argument(
        "--chunks-root", required=True, help="Root folder of chunk files 'part-XYZ.txt'"
    )
    ap.add_argument("--out-root", required=True, help="Output root for tagged files and indexes")
    ap.add_argument(
        "--range", required=True, help="Inclusive range like 019-016 (ascending or descending)"
    )
    ap.add_argument(
        "--alias-file", default=None, help="Optional JSON alias file mapping alias->slug"
    )
    ap.add_argument(
        "--dry-run", action="store_true", help="Print per-file summary without writing outputs"
    )
    # Keep --self-test for help text parity, though it's intercepted above
    ap.add_argument("--self-test", action="store_true", help="Run minimal self-tests and exit")
    ap.add_argument(
        "--retag-in",
        default=None,
        help="File or directory with .tagged.txt to re-tag with new heuristics",
    )
    ap.add_argument("--retag-out", default=None, help="Output directory for re-tagged files")

    args = ap.parse_args(argv)

    yaml_root = Path(args.yaml_root)
    chunks_root = Path(args.chunks_root)
    out_root = Path(args.out_root)
    out_root.mkdir(parents=True, exist_ok=True)

    try:
        indices = parse_range(args.range)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return 2

    extra_aliases = load_optional_alias_file(Path(args.alias_file)) if args.alias_file else None
    lex = build_lexicon(yaml_root, extra_aliases)
    slug_patterns, alias_patterns = build_patterns(lex)

    # Prepare outputs
    index_path = out_root / "index_review.json"
    unresolved_path = out_root / "unresolved.json"
    lexicon_dump_path = out_root / "lexicon.json"
    reports_dir = Path("reports")
    reports_dir.mkdir(parents=True, exist_ok=True)
    try:
        # Python 3.11+: timezone-aware UTC
        from datetime import UTC  # type: ignore

        ts = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    except Exception:
        ts = datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
    log_path = reports_dir / f"tagging-{ts}.log"

    # Load existing index if present
    index_data: dict[str, object] = {"files": {}, "updated_at": ts}
    if index_path.exists():
        try:
            index_data = json.loads(index_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    per_file_summaries = []
    warnings: list[str] = []

    # Retag mode: apply subset of rules a/b/c on existing tagged files
    if args.retag_in:
        in_target = Path(args.retag_in)
        out_dir = Path(args.retag_out) if args.retag_out else out_root
        out_dir.mkdir(parents=True, exist_ok=True)
        candidates: list[Path] = []
        if in_target.is_dir():
            candidates = sorted(in_target.glob("*.tagged.txt"))
        elif in_target.is_file():
            candidates = [in_target]
        else:
            print(f"Error: --retag-in not found: {in_target}", file=sys.stderr)
            return 2
        for in_file in candidates:
            with in_file.open("r", encoding="utf-8", errors="ignore") as f:
                lines = [ln.rstrip("\n") for ln in f]
            updated: list[str] = []
            for i, line in enumerate(lines):
                # Preserve existing tags but avoid duplicates
                current = line
                base_text = line
                # Heuristic a) N7 canonicalization (non-metro)
                if N7_RE.search(base_text) and not is_metro_context(lines, i):
                    if "[LOC:c6-nord]" not in base_text:
                        current = (
                            base_text
                            + (" " if not base_text.endswith(" ") else "")
                            + "[LOC:c6-nord]"
                        )
                    else:
                        current = base_text
                # Heuristic b) NOTE tagging
                if is_note_line(base_text) and "[NOTE]" not in current:
                    current = current + " [NOTE]"
                # Heuristic c) Mission tagging with context
                window = "\n".join(lines[max(0, i - 3) : min(len(lines), i + 4)]).lower()
                if ("c6-nord" in base_text.lower() or "[LOC:c6-nord]" in current.lower()) and any(
                    t in window for t in MISSION_TERMS
                ):
                    if "[MISSION:mission-c6-nord]" not in current:
                        current = current + " [MISSION:mission-c6-nord]"
                updated.append(current)
            out_file = out_dir / in_file.name
            out_file.write_text("\n".join(updated) + "\n", encoding="utf-8")
        # Write unresolved + alias collisions + suggestions passthrough (empty here)
        unresolved_payload = {
            "unresolved_dependencies": sorted(lex.unresolved_dependencies),
            "alias_collisions": {k: sorted(list(v)) for k, v in lex.alias_collisions.items()},
            "unknown_tokens": [],
            "alias_suggestions": [],
        }
        try:
            unresolved_path = out_root / "unresolved.json"
            unresolved_path.write_text(
                json.dumps(unresolved_payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except Exception:
            pass
        # Also dump lexicon for traceability
        try:
            lex_dump = {
                "by_slug": {
                    s: {"category": e.category, "title": e.title} for s, e in lex.by_slug.items()
                },
                "aliases": lex.aliases,
                "redirects": lex.redirects,
                "deprecated": sorted(list(lex.deprecated)),
            }
            (out_root / "lexicon.json").write_text(
                json.dumps(lex_dump, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        except Exception:
            pass
        return 0

    canon_total = 0
    for idx in indices:
        xyz = f"{idx:03d}"
        # Support both 'part-XYZ.txt' and '* .part-XYZ.txt' file name styles
        in_path = chunks_root / f"part-{xyz}.txt"
        if not in_path.exists():
            # search for '*.part-XYZ.txt'
            candidates = list(chunks_root.glob(f"*.part-{xyz}.txt"))
            if candidates:
                in_path = candidates[0]
            else:
                print(f"Warning: missing input for index {xyz} under {chunks_root}")
                continue
        out_path = out_root / f"part-{xyz}.tagged.txt"
        summary = process_chunk_file(
            in_path,
            out_path,
            lex,
            slug_patterns,
            alias_patterns,
            dry_run=args.dry_run,
            warnings=warnings,
        )
        per_file_summaries.append(summary)
        canon_total += int(summary.get("canonicalized_n7", 0))
        if not args.dry_run:
            # Update index
            files = index_data.setdefault("files", {})  # type: ignore
            if isinstance(files, dict):
                files[summary["file"]] = {
                    "lines": summary["lines"],
                    "chars": summary["chars"],
                    "tag_counts": summary["tag_counts"],
                    "top_slugs": summary["top_slugs"],
                }

    # Write unresolved + alias collisions
    # Aggregate alias suggestions from per-file summaries
    alias_suggestions_all: list[dict[str, object]] = []
    for s in per_file_summaries:
        alias_suggestions_all.extend(s.get("alias_suggestions", []))
    # Deduplicate suggestions by (source,candidate)
    seen_pairs = set()
    alias_suggestions_unique = []
    for item in alias_suggestions_all:
        key = (item.get("source"), item.get("candidate"))
        if key not in seen_pairs:
            seen_pairs.add(key)
            alias_suggestions_unique.append(item)

    unresolved_payload = {
        "unresolved_dependencies": sorted(lex.unresolved_dependencies),
        "alias_collisions": {k: sorted(list(v)) for k, v in lex.alias_collisions.items()},
        "unknown_tokens": [],  # optional heuristic placeholder
        "alias_suggestions": alias_suggestions_unique,
    }

    # Output / Logs
    if args.dry_run:
        print(
            json.dumps(
                {"summaries": per_file_summaries, **unresolved_payload},
                ensure_ascii=False,
                indent=2,
            )
        )
    else:
        # index, unresolved, lexicon, log
        index_data["updated_at"] = ts
        try:
            index_path.write_text(
                json.dumps(index_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        except Exception as e:
            print(f"Error writing {index_path}: {e}", file=sys.stderr)

        try:
            unresolved_path.write_text(
                json.dumps(unresolved_payload, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except Exception as e:
            print(f"Error writing {unresolved_path}: {e}", file=sys.stderr)

        try:
            # Optional lexicon dump
            lex_dump = {
                "by_slug": {
                    s: {"category": e.category, "title": e.title} for s, e in lex.by_slug.items()
                },
                "aliases": lex.aliases,
                "redirects": lex.redirects,
                "deprecated": sorted(list(lex.deprecated)),
            }
            lexicon_dump_path.write_text(
                json.dumps(lex_dump, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        except Exception as e:
            print(f"Error writing {lexicon_dump_path}: {e}", file=sys.stderr)

        # Write warnings and a short summary of canonicalizations
        try:
            log_lines = []
            if warnings:
                log_lines.extend(warnings)
            log_lines.append(f"Canonicalized N7→c6-nord total: {canon_total}")
            if log_lines:
                log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
        except Exception as e:
            print(f"Error writing {log_path}: {e}", file=sys.stderr)

    return 0


# ------------------------------- Self tests -------------------------------- #


def self_test() -> int:
    # Regex builder tests
    pat = build_word_safe_regex("c6", alnum_dash_underscore=True, case_sensitive=False)
    assert pat.search("C6 ist in Ordnung")
    assert pat.search(" abc c6 ")
    assert not pat.search("c67")
    assert not pat.search("xc6y")

    # Alias mapping tests
    # Simulate two entries: Ronja Kerschner (character), c6 (location)
    tmp_root = Path("__tmp_test__")
    try:
        tmp_root.mkdir(exist_ok=True)
        (tmp_root / "a.md").write_text(
            """---
title: Ronja Kerschner
category: character
slug: ronja-kerschner
---
Body
""",
            encoding="utf-8",
        )
        (tmp_root / "b.md").write_text(
            """---
title: C6
category: location
slug: c6
---
Body
""",
            encoding="utf-8",
        )
        lex = build_lexicon(tmp_root)
        # Title alias
        assert lex.aliases.get("Ronja Kerschner") == "ronja-kerschner"
        # Short location uppercase alias
        assert lex.aliases.get("C6") == "c6"

        # Heuristic a) N7 non-metro → [LOC:c6-nord]
        # Prepare minimal patterns
        slug_patterns, alias_patterns = build_patterns(lex)
        # a) N7 non-metro → tagged
        chunk = tmp_root / "part-000.txt"
        chunk.write_text("Wir gehen zu N7 heute.\n", encoding="utf-8")
        out = tmp_root / "part-000.tagged.txt"
        warnings: list[str] = []
        _ = process_chunk_file(
            chunk, out, lex, slug_patterns, alias_patterns, dry_run=False, warnings=warnings
        )
        text = out.read_text(encoding="utf-8")
        assert "[LOC:c6-nord]" in text
        # b) N7 with U-Bahn → not tagged
        chunkm = tmp_root / "part-000m.txt"
        chunkm.write_text("U-Bahn Linie - N7 ist nur ein Hinweis.\n", encoding="utf-8")
        outm = tmp_root / "part-000m.tagged.txt"
        warningsm: list[str] = []
        _ = process_chunk_file(
            chunkm, outm, lex, slug_patterns, alias_patterns, dry_run=False, warnings=warningsm
        )
        textm = outm.read_text(encoding="utf-8")
        assert "[LOC:c6-nord]" not in textm

        # c) Sector codes E3 / F1 → [LOC:e3], [LOC:f1]
        sec_lines = ["Sichtung in E3.", "Weiter nach F1."]
        chunk2 = tmp_root / "part-001.txt"
        chunk2.write_text("\n".join(sec_lines) + "\n", encoding="utf-8")
        out2 = tmp_root / "part-001.tagged.txt"
        warnings2: list[str] = []
        _ = process_chunk_file(
            chunk2, out2, lex, slug_patterns, alias_patterns, dry_run=False, warnings=warnings2
        )
        text2 = out2.read_text(encoding="utf-8")
        assert "[LOC:e3]" in text2.splitlines()[0]
        assert "[LOC:f1]" in text2.splitlines()[1]

        # d) NOTE lines suppress LOC-only warning
        note_lines = ["Hinweis: C6."]
        chunk3 = tmp_root / "part-002.txt"
        chunk3.write_text("\n".join(note_lines) + "\n", encoding="utf-8")
        out3 = tmp_root / "part-002.tagged.txt"
        warnings3: list[str] = []
        _ = process_chunk_file(
            chunk3, out3, lex, slug_patterns, alias_patterns, dry_run=False, warnings=warnings3
        )
        assert any("[NOTE]" in ln for ln in out3.read_text(encoding="utf-8").splitlines())
        assert len(warnings3) == 0

        # e) Mission rule: C6-Nord with versiegelt → [MISSION:mission-c6-nord]
        mission_lines = ["C6-Nord wurde versiegelt."]
        chunk4 = tmp_root / "part-003.txt"
        chunk4.write_text("\n".join(mission_lines) + "\n", encoding="utf-8")
        out4 = tmp_root / "part-003.tagged.txt"
        warnings4: list[str] = []
        _ = process_chunk_file(
            chunk4, out4, lex, slug_patterns, alias_patterns, dry_run=False, warnings=warnings4
        )
        assert "[MISSION:mission-c6-nord]" in out4.read_text(encoding="utf-8")
    finally:
        # cleanup
        try:
            for p in tmp_root.glob("*.md"):
                p.unlink(missing_ok=True)
            for p in tmp_root.glob("part-*.txt"):
                p.unlink(missing_ok=True)
            for p in tmp_root.glob("part-*.tagged.txt"):
                p.unlink(missing_ok=True)
            tmp_root.rmdir()
        except Exception:
            pass
    print("Self-test: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
