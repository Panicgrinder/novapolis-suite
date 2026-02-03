#!/usr/bin/env python3
"""Build staging artifacts for pending RAW canvas exports.

- Reads novapolis-rp/database-curated/staging/manifest.json
- Filters entries with id starting 'pending-raw-canvas' and type 'raw-txt'
- Generates normalized + chunks/index via chunk_text.py
- Generates text stats per source file
- Updates manifest artifacts for processed entries
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST_PATH = REPO_ROOT / "novapolis-rp" / "database-curated" / "staging" / "manifest.json"
CURATION_DIR = REPO_ROOT / "novapolis-rp" / "coding" / "tools" / "curation"
STAGING_DIR = REPO_ROOT / "novapolis-rp" / "database-curated" / "staging"
REPORTS_DIR = STAGING_DIR / "reports"


def run_py(module: str, args: list[str]) -> None:
    cmd = [sys.executable, str(CURATION_DIR / module), *args]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if proc.returncode != 0:
        raise SystemExit(f"Command failed: {' '.join(cmd)} (exit {proc.returncode})")


def ensure_artifacts(entry: dict[str, Any], base_name: str) -> None:
    artifacts = entry.setdefault("artifacts", {})
    artifacts.setdefault("normalized", f"database-curated/staging/{base_name}.normalized.txt")
    artifacts.setdefault("chunksDir", f"database-curated/staging/chunks/{base_name}")
    artifacts.setdefault("index", f"database-curated/staging/chunks/{base_name}/index.json")
    reports = artifacts.setdefault("reports", {})
    reports.setdefault("textStats", f"database-curated/staging/reports/text-stats.{base_name}.md")


def main() -> int:
    if not MANIFEST_PATH.exists():
        print(f"manifest.json nicht gefunden: {MANIFEST_PATH}", file=sys.stderr)
        return 2

    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("manifest.json: Top-Level ist nicht Array", file=sys.stderr)
        return 3

    processed = 0
    for entry in data:
        entry_id = str(entry.get("id", ""))
        if not entry_id.startswith("pending-raw-canvas"):
            continue
        if entry.get("type") != "raw-txt":
            continue
        source = entry.get("source")
        if not source:
            continue

        src_path = REPO_ROOT / "novapolis-rp" / source.replace("/", "\\")
        if not src_path.exists():
            print(f"Warnung: Source fehlt: {source}", file=sys.stderr)
            continue

        base_name = src_path.stem
        ensure_artifacts(entry, base_name)

        normalized = STAGING_DIR / f"{base_name}.normalized.txt"
        index_path = STAGING_DIR / "chunks" / base_name / "index.json"
        stats_path = REPORTS_DIR / f"text-stats.{base_name}.md"

        # Chunk only if not already present
        if not (normalized.exists() and index_path.exists()):
            run_py("chunk_text.py", [str(src_path), str(STAGING_DIR)])

        # Stats if missing
        if not stats_path.exists():
            REPORTS_DIR.mkdir(parents=True, exist_ok=True)
            run_py(
                "text_stats.py",
                [str(src_path), "--out", str(stats_path)],
            )

        processed += 1

    manifest_text = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    MANIFEST_PATH.write_text(manifest_text, encoding="utf-8")
    print(f"OK: Canvas-Staging aktualisiert (entries: {processed})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
