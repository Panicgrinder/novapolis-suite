#!/usr/bin/env python3
"""
Central Hybrid Index Builder (append-only)
- Scans database-rp for Markdown files with matching sidecar JSON.
- Maintains central index at database-rp/index.json with structure:
  {
    "project": "Novapolis-RP",
    "version": "2.0",
    "chapters": [],
    "characters": [],
    "locations": [],
    "other": [],
    "last_update": "ISO-8601 timestamp"
  }
Rules:
- Do not overwrite existing entries; only append new ones.
- Preserve folder hierarchy; do not modify Markdown.
Options:
  --dry-run   Print actions only
  --root PATH Root directory (default: cwd)
  --rp PATH   RP base dir relative to root (default: database-rp)
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import UTC, datetime
from pathlib import Path

DEFAULT_INDEX = {
    "project": "Novapolis-RP",
    "version": "2.0",
    "chapters": [],
    "characters": [],
    "locations": [],
    "other": [],
    "last_update": "",
}

CATEGORY_MAP = {
    "02-characters": "characters",
    "03-locations": "locations",
    "06-scenes": "chapters",
}


def parse_args():
    p = argparse.ArgumentParser(description="Build/append central hybrid index.")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--root", type=str, default=os.getcwd())
    p.add_argument("--rp", type=str, default="database-rp")
    return p.parse_args()


def load_index(index_path: Path) -> dict:
    if not index_path.exists():
        return DEFAULT_INDEX.copy()
    try:
        return json.loads(index_path.read_text(encoding="utf-8") or "{}")
    except Exception:
        # if unreadable, keep a safe baseline and append-only
        return DEFAULT_INDEX.copy()


def save_index(index_path: Path, data: dict, dry: bool) -> None:
    data["last_update"] = datetime.now(UTC).isoformat()
    if dry:
        print(f"DRY: would save index -> {index_path}")
        return
    index_path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def entry_exists(arr: list[dict], md_rel: str, json_rel: str) -> bool:
    for e in arr:
        if e.get("md") == md_rel or e.get("json") == json_rel:
            return True
    return False


def main():
    args = parse_args()
    root = Path(args.root).resolve()
    rp_dir = (root / args.rp).resolve()
    index_path = rp_dir / "index.json"

    index = load_index(index_path)
    # Ensure required arrays exist
    for k in ("chapters", "characters", "locations", "other"):
        if k not in index or not isinstance(index[k], list):
            index[k] = []

    added = 0

    # Walk RP directory only
    for dirpath, _dirnames, filenames in os.walk(rp_dir):
        dpath = Path(dirpath)
        for fname in filenames:
            if not fname.lower().endswith(".md"):
                continue
            md_path = dpath / fname
            json_path = md_path.with_suffix(".json")
            if not json_path.exists():
                continue

            # Relatives from repo root
            md_rel = md_path.relative_to(root).as_posix()
            json_rel = json_path.relative_to(root).as_posix()

            # Pick category by 1st-level under rp_dir
            rel_from_rp = md_path.relative_to(rp_dir).as_posix()
            first_seg = rel_from_rp.split("/", 1)[0] if "/" in rel_from_rp else rel_from_rp
            cat = CATEGORY_MAP.get(first_seg, "other")

            arr = index.get(cat, index["other"])
            if entry_exists(arr, md_rel, json_rel):
                continue

            entry = {"md": md_rel, "json": json_rel}
            arr.append(entry)
            added += 1

    save_index(index_path, index, args.dry_run)
    print(f"Hybrid index: added={added}, path={index_path.relative_to(root).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
