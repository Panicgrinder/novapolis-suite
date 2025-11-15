#!/usr/bin/env python3
"""
GPT Hybrid Metadata Generator (Python)
- Scans the workspace for all .md files
- For each .md, creates a sibling .json with the same base name if missing
- Preserves folder hierarchy, does not touch Markdown content
- JSON scaffold shape:
  {
    "chapter": "",
    "characters": [],
    "location": "",
    "tags": [],
    "source": "relative/path/to/file.md"
  }
Options:
  --dry-run    Only print actions, do not write files
  --overwrite  Overwrite existing .json files (default: False)
  --root PATH  Root directory to scan (default: cwd)
"""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

SKIP_DIRS = {
    "node_modules",
    ".git",
    ".venv",
    ".vscode",
    ".idea",
    ".DS_Store",
    "database-raw/99-exports",
}


def parse_args():
    p = argparse.ArgumentParser(description="Generate JSON metadata next to Markdown files.")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--overwrite", action="store_true")
    p.add_argument("--root", type=str, default=os.getcwd())
    return p.parse_args()


def should_skip_dir(root: Path, d: Path) -> bool:
    rel = d.relative_to(root).as_posix() if d != root else ""
    if not rel:
        return False
    for skip in SKIP_DIRS:
        if rel == skip or rel.startswith(skip + "/"):
            return True
    return False


def md_to_json_path(md_path: Path) -> Path:
    return md_path.with_suffix(".json")


def main():
    args = parse_args()
    root = Path(args.root).resolve()

    written = 0
    exists = 0
    errors = 0

    for dirpath, dirnames, filenames in os.walk(root):
        # mutate dirnames to skip unwanted dirs
        dpath = Path(dirpath)
        if should_skip_dir(root, dpath):
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if not should_skip_dir(root, dpath / d)]

        for fname in filenames:
            if not fname.lower().endswith(".md"):
                continue
            md_path = dpath / fname
            json_path = md_to_json_path(md_path)

            try:
                if json_path.exists() and not args.overwrite:
                    exists += 1
                    continue
                scaffold = {
                    "chapter": "",
                    "characters": [],
                    "location": "",
                    "tags": [],
                    "source": md_path.relative_to(root).as_posix(),
                }
                if args.dry_run:
                    print(f"DRY: would write {json_path}")
                    continue
                json_path.write_text(json.dumps(scaffold, indent=2) + "\n", encoding="utf-8")
                written += 1
            except Exception as e:
                errors += 1
                print(f"ERROR {md_path}: {e}")

    print(f"Hybrid metadata: written={written}, exists={exists}, errors={errors}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
