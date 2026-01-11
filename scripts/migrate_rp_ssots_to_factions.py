#!/usr/bin/env python3
"""migrate_rp_ssots_to_factions.py

Moves RP SSOT markdown/json files into the faction folder structure:
  novapolis-rp/database-rp/01-factions/<faction>/<category>/...

Key behaviors:
- Builds a deterministic mapping based on frontmatter (`owner`, `affiliations`, etc.)
- Moves matching .md + .json sidecars together
- Updates JSON sidecar field `source` when present
- Rewrites Markdown links across database-rp so references keep working
- Updates database-rp/index.json to the new paths

Usage:
  & .\\.venv\\Scripts\\python.exe scripts\\migrate_rp_ssots_to_factions.py            # dry-run
  & .\\.venv\\Scripts\\python.exe scripts\\migrate_rp_ssots_to_factions.py --apply    # apply changes

Exit codes:
- 0 on success
- 2 on preflight conflict / unsafe state
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable

LOG_ENCODING = "utf-8"

KNOWN_FACTIONS = {
    "novapolis",
    "haendlerbund",
    "eisenkonklave",
    "schienenbund",
    "arkologie-a1",
    "schattenbund",
    "fluesterkollektiv",
}

CATEGORY_DIRS = ("02-characters", "03-locations", "04-inventory", "05-projects")

MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")


@dataclass(frozen=True)
class MoveItem:
    old: Path
    new: Path


def resolve_repo_root() -> Path:
    here = Path(__file__).resolve()
    return here.parent.parent.resolve()


def rp_root(repo_root: Path) -> Path:
    return repo_root / "novapolis-rp" / "database-rp"


def now_ts_for_paths() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def read_text(path: Path) -> str:
    return path.read_text(encoding=LOG_ENCODING, errors="replace")


def split_frontmatter(text: str) -> tuple[str | None, str]:
    if not text.startswith("---"):
        return None, text
    lines = text.splitlines(keepends=True)
    if not lines:
        return None, text
    fm_lines: list[str] = []
    end_idx: int | None = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
        fm_lines.append(lines[i])
    if end_idx is None:
        return "".join(fm_lines), ""
    fm = "".join(fm_lines)
    rest = "".join(lines[end_idx + 1 :])
    return fm, rest


def _parse_bracket_list(value: str) -> list[str]:
    inner = value.strip()
    if not (inner.startswith("[") and inner.endswith("]")):
        return []
    inner = inner[1:-1].strip()
    if not inner:
        return []
    parts = [p.strip() for p in inner.split(",")]
    out: list[str] = []
    for part in parts:
        item = part.strip().strip('"').strip("'")
        if item:
            out.append(item)
    return out


def parse_frontmatter(fm: str) -> dict[str, Any]:
    """Parse a tiny YAML subset used in RP docs.

    Supports:
      key: value
      key: [a, b]
      key:\n  - a\n  - b

    Values are returned as str or list[str].
    """

    lines = fm.splitlines()
    meta: dict[str, Any] = {}

    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if not m:
            i += 1
            continue
        key = m.group(1)
        value = m.group(2).strip()

        # bracket list
        if value.startswith("[") and value.endswith("]"):
            meta[key] = _parse_bracket_list(value)
            i += 1
            continue

        # block list
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
            if items:
                meta[key] = items
            i = j
            continue

        # scalar
        meta[key] = value.strip().strip('"').strip("'")
        i += 1

    return meta


def is_remote_link(link: str) -> bool:
    lowered = link.lower()
    return lowered.startswith(("http://", "https://", "mailto:"))


def strip_link_anchor(link: str) -> tuple[str, str]:
    """Return (path_part, anchor_part_including_hash_or_empty)."""

    if "#" not in link:
        return link, ""
    path_part, anchor = link.split("#", 1)
    return path_part, "#" + anchor


def canonical_rel(path: Path, base: Path) -> str:
    return path.relative_to(base).as_posix()


def pick_faction(category_dir: str, md_path: Path, meta: dict[str, Any]) -> str | None:
    owner = str(meta.get("owner") or "").strip()
    if owner in KNOWN_FACTIONS:
        return owner

    affiliations = meta.get("affiliations")
    if isinstance(affiliations, str):
        affiliations_list = [affiliations]
    elif isinstance(affiliations, list):
        affiliations_list = [str(x) for x in affiliations]
    else:
        affiliations_list = []

    candidates = [a for a in affiliations_list if a in KNOWN_FACTIONS]

    if len(candidates) == 1:
        return candidates[0]

    if len(candidates) == 2 and "novapolis" in candidates:
        # Prefer the non-Novapolis faction for dual membership.
        return candidates[0] if candidates[1] == "novapolis" else candidates[1]

    # Inventory: map by filename patterns (owner is usually present, but not always)
    if category_dir == "04-inventory":
        stem = md_path.stem.lower()
        if "haendlerbund" in stem:
            return "haendlerbund"
        if "schienenbund" in stem:
            return "schienenbund"
        if "novapolis" in stem:
            return "novapolis"
        if "arkologie" in stem:
            return "arkologie-a1"
        if "eiserne-enklave" in stem:
            return "eisenkonklave"

    # Projects: a few pragmatic heuristics
    if category_dir == "05-projects":
        cat = str(meta.get("category") or "").strip()
        slug = str(meta.get("slug") or "").strip()
        title = str(meta.get("title") or "").lower()

        if cat == "faction" and slug in KNOWN_FACTIONS:
            return slug

        deps = meta.get("dependencies")
        dep_list = [str(x) for x in deps] if isinstance(deps, list) else []
        if any(d == "novapolis-inventar" for d in dep_list):
            return "novapolis"

        if "karawan" in title or slug == "caravan_moves":
            return "haendlerbund"

        # Default: most early RP assets are Novapolis-centered.
        return "novapolis"

    # Locations: default to Novapolis if unknown (current RP map is Novapolis-centric)
    if category_dir == "03-locations":
        return "novapolis"

    # Characters: if ambiguous, default to Novapolis to minimize cross-link breakage.
    if category_dir == "02-characters":
        return "novapolis"

    return None


def iter_source_files(rp: Path) -> list[Path]:
    out: list[Path] = []
    for cat in CATEGORY_DIRS:
        out.extend(sorted((rp / cat).glob("*.md")))
    return out


def build_move_plan(repo_root: Path) -> tuple[list[MoveItem], dict[Path, Path], list[str]]:
    rp = rp_root(repo_root)
    moves: list[MoveItem] = []
    mapping: dict[Path, Path] = {}
    warnings: list[str] = []

    for md_path in iter_source_files(rp):
        text = read_text(md_path)
        fm, _rest = split_frontmatter(text)
        meta = parse_frontmatter(fm or "") if fm is not None else {}

        cat_dir = md_path.parent.name
        faction = pick_faction(cat_dir, md_path, meta)
        if not faction:
            warnings.append(f"Unassigned faction (kept in place): {canonical_rel(md_path, repo_root)}")
            continue

        if cat_dir == "05-projects" and str(meta.get("category") or "").strip() == "faction":
            dest_dir = rp / "01-factions" / faction
        else:
            dest_dir = rp / "01-factions" / faction / cat_dir

        dest_md = dest_dir / md_path.name
        moves.append(MoveItem(md_path, dest_md))
        mapping[md_path] = dest_md

        # Sidecar .json
        sidecar = md_path.with_suffix(".json")
        if sidecar.exists():
            dest_json = dest_md.with_suffix(".json")
            moves.append(MoveItem(sidecar, dest_json))
            mapping[sidecar] = dest_json

    # index.json itself is handled as a rewrite (not a move)
    return moves, mapping, warnings


def check_conflicts(moves: Iterable[MoveItem]) -> list[str]:
    conflicts: list[str] = []
    for item in moves:
        if item.new.exists() and item.new.resolve() != item.old.resolve():
            conflicts.append(f"Target exists: {item.new}")
    return conflicts


def apply_moves(moves: list[MoveItem]) -> None:
    # Ensure deterministic order: move deeper paths later doesn't matter much.
    for item in sorted(moves, key=lambda m: (len(str(m.old)), str(m.old))):
        ensure_dir(item.new.parent)
        shutil.move(str(item.old), str(item.new))


def rewrite_json_sources(repo_root: Path, mapping: dict[Path, Path]) -> int:
    """Update `source` in moved JSON sidecars."""

    rp = rp_root(repo_root)
    changed = 0
    for old_path, new_path in mapping.items():
        if new_path.suffix.lower() != ".json":
            continue
        if not new_path.exists():
            continue

        data = json.loads(read_text(new_path))
        src = data.get("source")
        if isinstance(src, str) and src.startswith("database-rp/"):
            # Convert old md path -> new md path if the source points at a moved md.
            old_md_rel = rp / Path(src.replace("database-rp/", ""))
            if old_md_rel in mapping:
                new_md_abs = mapping[old_md_rel]
                new_md_rel = canonical_rel(new_md_abs, rp)
                data["source"] = f"database-rp/{new_md_rel}"
                new_path.write_text(
                    json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                    encoding=LOG_ENCODING,
                )
                changed += 1
    return changed


def build_abs_mapping_for_links(mapping: dict[Path, Path]) -> dict[Path, Path]:
    # Use absolute normalized paths as keys.
    out: dict[Path, Path] = {}
    for old, new in mapping.items():
        out[old] = new
    return out


def iter_all_markdown_files(rp: Path) -> list[Path]:
    return sorted(p for p in rp.rglob("*.md") if p.is_file())


def rewrite_markdown_links(repo_root: Path, mapping: dict[Path, Path]) -> int:
    rp = rp_root(repo_root)

    old_to_new = build_abs_mapping_for_links(mapping)

    # For moved markdown files, we need the old location to resolve their existing links.
    moved_md_old_by_new: dict[Path, Path] = {
        new: old for old, new in mapping.items() if old.suffix.lower() == ".md"
    }

    changed_files = 0
    for md_file in iter_all_markdown_files(rp):
        content = read_text(md_file)
        old_file = moved_md_old_by_new.get(md_file)
        base_dir_for_resolution = (old_file.parent if old_file else md_file.parent)

        def repl(match: re.Match[str]) -> str:
            raw_link = match.group(1).strip()
            if not raw_link or is_remote_link(raw_link) or raw_link.startswith("#"):
                return match.group(0)

            link_body, anchor = strip_link_anchor(raw_link)
            link_body = link_body.split("?", 1)[0].strip()
            if not link_body:
                return match.group(0)
            if link_body.startswith("/"):
                return match.group(0)

            target_old_abs = (base_dir_for_resolution / link_body).resolve(strict=False)
            if target_old_abs not in old_to_new:
                return match.group(0)

            target_new_abs = old_to_new[target_old_abs]
            rel_new = os.path.relpath(target_new_abs, start=md_file.parent)
            rel_new = rel_new.replace("\\", "/")
            return match.group(0).replace(raw_link, rel_new + anchor)

        new_content = MD_LINK_RE.sub(repl, content)
        if new_content != content:
            md_file.write_text(new_content, encoding=LOG_ENCODING)
            changed_files += 1

    return changed_files


def rewrite_index_json(repo_root: Path, mapping: dict[Path, Path]) -> bool:
    rp = rp_root(repo_root)
    index_path = rp / "index.json"
    if not index_path.exists():
        return False

    data = json.loads(read_text(index_path))

    def rewrite_entry(entry: dict[str, Any]) -> None:
        for key in ("md", "json"):
            val = entry.get(key)
            if not isinstance(val, str) or not val.startswith("database-rp/"):
                continue
            old_abs = rp / Path(val.replace("database-rp/", ""))
            if old_abs in mapping:
                new_abs = mapping[old_abs]
                entry[key] = f"database-rp/{canonical_rel(new_abs, rp)}"

    # Known top-level arrays
    for section in ("chapters", "characters", "locations", "other"):
        items = data.get(section)
        if isinstance(items, list):
            for entry in items:
                if isinstance(entry, dict):
                    rewrite_entry(entry)

    index_path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding=LOG_ENCODING)
    return True


def write_report(repo_root: Path, moves: list[MoveItem], warnings: list[str]) -> Path:
    out_dir = repo_root / ".tmp" / "results" / "reports"
    ensure_dir(out_dir)
    ts = now_ts_for_paths()
    report_path = out_dir / f"migrate_rp_ssots_to_factions_{ts}.json"

    report = {
        "tool": "migrate_rp_ssots_to_factions",
        "ts": datetime.now().isoformat(timespec="seconds"),
        "moves": [
            {
                "from": str(m.old),
                "to": str(m.new),
            }
            for m in moves
        ],
        "counts": {
            "move_items": len(moves),
            "warnings": len(warnings),
        },
        "warnings": warnings,
    }
    report_path.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding=LOG_ENCODING)
    return report_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Apply changes (default is dry-run)")
    args = parser.parse_args()

    repo_root = resolve_repo_root()
    rp = rp_root(repo_root)

    moves, mapping, warnings = build_move_plan(repo_root)
    report_path = write_report(repo_root, moves, warnings)

    conflicts = check_conflicts(moves)
    if conflicts:
        print("STOP: Conflicts detected; aborting.")
        for c in conflicts[:50]:
            print(" -", c)
        print(f"Report: {report_path}")
        return 2

    print(f"Planned move items: {len(moves)}")
    if warnings:
        print(f"Warnings: {len(warnings)} (see report)")
    print(f"Report: {report_path}")

    if not args.apply:
        print("Dry-run only. Use --apply to execute.")
        return 0

    # Apply
    apply_moves(moves)

    # Post-move rewrites
    changed_sources = rewrite_json_sources(repo_root, mapping)
    changed_links = rewrite_markdown_links(repo_root, mapping)
    idx_changed = rewrite_index_json(repo_root, mapping)

    print("Done.")
    print(f"- JSON sources updated: {changed_sources}")
    print(f"- Markdown files with link rewrites: {changed_links}")
    print(f"- index.json updated: {idx_changed}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
