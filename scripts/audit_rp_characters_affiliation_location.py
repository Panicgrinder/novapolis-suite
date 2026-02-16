"""Audit RP character affiliation and location fields.

Purpose
-------
Checks all faction character markdown files under
`novapolis-rp/database-rp/01-factions/*/02-characters/` for:
- `affiliations` contains the owning faction slug
- presence of `primary_location`
- presence of `last_seen`

Additionally reports whether each faction has at least one probable
leadership character based on conservative keyword matching in the
character file body/frontmatter.

Outputs
-------
- Markdown report: `.tmp/results/reports/character_affiliation_location_audit_YYYYMMDD_HHMM.md`
- JSON report: `.tmp/results/reports/character_affiliation_location_audit_YYYYMMDD_HHMM.json`
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

LEADERSHIP_RE = re.compile(
    r"fraktionsleitung|fuehrungsfigur|führungsfigur|kommandant|anführer|anfuehrer|"
    r"sicherheitsoffizier|stellvertretung\s*\(.*leitung|leitung\s*\(",
    re.IGNORECASE,
)


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text

    block = text[4:end].splitlines()
    body = text[end + 4 :]
    data: dict[str, str] = {}
    for line in block:
        s = line.strip()
        if not s or s.startswith("#") or ":" not in s:
            continue
        key, value = s.split(":", 1)
        data[key.strip()] = value.strip()
    return data, body


def parse_list_value(raw: str | None) -> list[str]:
    if raw is None:
        return []
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        parts = [p.strip().strip('"').strip("'") for p in inner.split(",")]
        return [p for p in parts if p]

    if "," in raw:
        parts = [p.strip().strip('"').strip("'") for p in raw.split(",")]
        return [p for p in parts if p]

    return [raw.strip().strip('"').strip("'")] if raw else []


@dataclass
class CharacterAuditRow:
    faction: str
    file: str
    slug: str
    affiliations: list[str]
    affiliation_ok: bool
    primary_location: str | None
    last_seen: str | None
    missing_fields: list[str]
    leadership_candidate: bool


def collect_character_files(base: Path) -> list[Path]:
    files = sorted(base.glob("*/02-characters/*.md"))
    out: list[Path] = []
    for p in files:
        name = p.name.lower()
        if name == "readme.md":
            continue
        if name.startswith("person-index"):
            continue
        out.append(p)
    return out


def build_rows(files: list[Path], root: Path) -> list[CharacterAuditRow]:
    rows: list[CharacterAuditRow] = []
    for path in files:
        text = path.read_text(encoding="utf-8", errors="replace")
        fm, body = parse_frontmatter(text)
        category = (fm.get("category") or "").strip().lower()
        if category and category != "character":
            continue

        faction = path.parts[-3]  # .../01-factions/<faction>/02-characters/<file>
        slug = (fm.get("slug") or "").strip()
        affiliations = parse_list_value(fm.get("affiliations"))
        primary_location = (fm.get("primary_location") or "").strip() or None
        last_seen = (fm.get("last_seen") or "").strip() or None

        missing: list[str] = []
        if not affiliations:
            missing.append("affiliations")
        if not primary_location:
            missing.append("primary_location")
        if not last_seen:
            missing.append("last_seen")

        affiliation_ok = faction in affiliations if affiliations else False

        leadership_candidate = bool(LEADERSHIP_RE.search(text) or LEADERSHIP_RE.search(body))

        rows.append(
            CharacterAuditRow(
                faction=faction,
                file=str(path.relative_to(root).as_posix()),
                slug=slug,
                affiliations=affiliations,
                affiliation_ok=affiliation_ok,
                primary_location=primary_location,
                last_seen=last_seen,
                missing_fields=missing,
                leadership_candidate=leadership_candidate,
            )
        )
    return rows


def summarize(rows: list[CharacterAuditRow]) -> dict[str, Any]:
    by_faction: dict[str, dict[str, Any]] = {}
    for row in rows:
        bucket = by_faction.setdefault(
            row.faction,
            {
                "total_characters": 0,
                "affiliation_mismatches": 0,
                "missing_primary_location": 0,
                "missing_last_seen": 0,
                "leadership_candidates": 0,
                "files_with_issues": [],
            },
        )
        bucket["total_characters"] += 1
        if not row.affiliation_ok:
            bucket["affiliation_mismatches"] += 1
        if row.primary_location is None:
            bucket["missing_primary_location"] += 1
        if row.last_seen is None:
            bucket["missing_last_seen"] += 1
        if row.leadership_candidate:
            bucket["leadership_candidates"] += 1
        if row.missing_fields or not row.affiliation_ok:
            bucket["files_with_issues"].append(row.file)

    return by_faction


def ensure_all_factions(summary: dict[str, Any], base: Path) -> dict[str, Any]:
    for faction_dir in sorted(p for p in base.iterdir() if p.is_dir()):
        faction = faction_dir.name
        summary.setdefault(
            faction,
            {
                "total_characters": 0,
                "affiliation_mismatches": 0,
                "missing_primary_location": 0,
                "missing_last_seen": 0,
                "leadership_candidates": 0,
                "files_with_issues": [],
            },
        )
    return summary


def write_markdown_report(
    *,
    out_path: Path,
    rows: list[CharacterAuditRow],
    summary: dict[str, Any],
) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    ts = dt.datetime.now().strftime("%Y-%m-%d %H:%M")

    lines: list[str] = [
        "---",
        f"stand: {ts}",
        "update: Character-Audit (Zugehoerigkeit/Standortfelder) erstellt.",
        "checks: scripts/audit_rp_characters_affiliation_location.py RUN",
        "---",
        "",
        "RP Character Audit (Affiliation + Locations)",
        "==========================================",
        "",
        "Fraktions-Summary",
        "-----------------",
        "",
        "| Fraktion | Chars | Affiliation-Mismatch | Missing primary_location | ",
        "| Missing last_seen | Leadership-Kandidaten |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
    ]

    for faction in sorted(summary.keys()):
        s = summary[faction]
        lines.append(
            f"| {faction} | {s['total_characters']} | {s['affiliation_mismatches']} | "
            f"{s['missing_primary_location']} | {s['missing_last_seen']} | "
            f"{s['leadership_candidates']} |"
        )

    lines += [
        "",
        "Details (nur Auffaelligkeiten)",
        "------------------------------",
        "",
    ]

    issue_rows = [r for r in rows if (r.missing_fields or not r.affiliation_ok)]
    if not issue_rows:
        lines.append("- Keine Auffaelligkeiten gefunden.")
    else:
        for row in issue_rows:
            lines.append(f"- {row.file}")
            lines.append(f"  - faction: {row.faction}")
            lines.append(f"  - slug: {row.slug or '(leer)'}")
            lines.append(f"  - affiliations: {row.affiliations}")
            lines.append(f"  - affiliation_ok: {row.affiliation_ok}")
            primary_location = row.primary_location or "(leer)"
            lines.append(f"  - primary_location: {primary_location}")
            lines.append(f"  - last_seen: {row.last_seen if row.last_seen else '(leer)'}")
            lines.append(f"  - missing_fields: {row.missing_fields}")

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base",
        default="novapolis-rp/database-rp/01-factions",
        help="Base path containing faction folders.",
    )
    parser.add_argument(
        "--out-prefix",
        default="character_affiliation_location_audit",
        help="Output filename prefix for report artifacts.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    base = root / args.base
    if not base.exists():
        raise SystemExit(f"Base path not found: {base}")

    files = collect_character_files(base)
    rows = build_rows(files, root)
    summary = summarize(rows)
    summary = ensure_all_factions(summary, base)

    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir = root / ".tmp" / "results" / "reports"
    md_path = out_dir / f"{args.out_prefix}_{stamp}.md"
    json_path = out_dir / f"{args.out_prefix}_{stamp}.json"

    write_markdown_report(out_path=md_path, rows=rows, summary=summary)
    json_payload = {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "base": str(base.as_posix()),
        "summary": summary,
        "rows": [asdict(r) for r in rows],
    }
    json_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(json_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    print("RP Character Audit completed")
    print(f"Markdown report: {md_path.as_posix()}")
    print(f"JSON report: {json_path.as_posix()}")
    print("\nFaction summary:")
    for faction in sorted(summary.keys()):
        s = summary[faction]
        print(
            f"- {faction}: chars={s['total_characters']}, "
            f"affiliation_mismatch={s['affiliation_mismatches']}, "
            f"missing_primary_location={s['missing_primary_location']}, "
            f"missing_last_seen={s['missing_last_seen']}, "
            f"leadership_candidates={s['leadership_candidates']}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
