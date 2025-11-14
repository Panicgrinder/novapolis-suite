#!/usr/bin/env python3
"""
Builds curated staging reports (text-stats + delta reports) based on staging/manifest.json.

Behavior:
- Reads novapolis-rp/database-curated/staging/manifest.json (array of entries)
- For each entry, resolves input files from database-raw/99-exports/
- Regenerates:
  * text-stats.md for the three inputs (A, B, RAW)
  * delta A: A vs B
  * delta B: A vs RAW
  * delta C: B vs RAW
- Writes outputs with UTF-8 + LF and exactly one trailing newline via the curation tools.

Assumptions:
- manifest.artifacts.reports has keys: textStats, deltaA, deltaB, deltaC
- manifest.source points to A (e.g., chat-export (1).txt)
- B is usually the sibling chat-export.txt in the same folder
- RAW file is discovered under database-raw/99-exports/ as RAW-chat-export-*.txt;
  we prefer one whose timestamp includes the HH-MM hint embedded in the delta filename (e.g., RAW-02-54)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]  # .../Main
RAW_DIR = REPO_ROOT / "novapolis-rp" / "database-raw" / "99-exports"
CURATION_DIR = REPO_ROOT / "novapolis-rp" / "coding" / "tools" / "curation"


def find_b_path(a_path: Path) -> Path | None:
    # Common pattern: A = chat-export (1).txt, B = chat-export.txt in same dir
    if a_path.name == "chat-export (1).txt":
        cand = a_path.parent / "chat-export.txt"
        return cand if cand.exists() else None
    # Fallback: try to strip " (1)" from filename
    name = a_path.stem.replace(" (1)", "") + a_path.suffix
    cand = a_path.parent / name
    return cand if cand.exists() else None


def find_raw_from_hint(hhmm: str | None) -> Path | None:
    raws = sorted(RAW_DIR.glob("RAW-chat-export-*.txt"))
    if not raws:
        return None
    if hhmm:
        # Match like '02-54' → look for 'T02-54' in filename
        token = f"T{hhmm}"
        for p in raws:
            if token in p.name:
                return p
    # Fallback: first (oldest) for stability
    return raws[0]


def extract_hhmm_from_delta_name(delta_out: Path) -> str | None:
    # e.g., delta-chat-export-1_vs_RAW-02-54.md → '02-54'
    m = re.search(r"RAW-([0-9]{2}-[0-9]{2})", delta_out.stem)
    return m.group(1) if m else None


def run_py(module: str, args: list[str]) -> None:
    cmd = [sys.executable, str(CURATION_DIR / module), *args]
    proc = subprocess.run(cmd, cwd=str(REPO_ROOT))
    if proc.returncode != 0:
        raise SystemExit(f"Command failed: {' '.join(cmd)} (exit {proc.returncode})")


def regen_for_entry(entry: dict[str, Any]) -> None:
    artifacts = entry.get("artifacts") or {}
    reports = artifacts.get("reports") or {}
    # Resolve inputs
    a_rel = entry.get("source")
    if not a_rel:
        return
    a_path = REPO_ROOT / "novapolis-rp" / a_rel.replace("/", os.sep)
    if not a_path.exists():
        # Some manifests may have root-relative without 'novapolis-rp/' prefix
        a_path = REPO_ROOT / a_rel.replace("/", os.sep)
    b_path = find_b_path(a_path)
    hhmm = extract_hhmm_from_delta_name(REPO_ROOT / "novapolis-rp" / (reports.get("deltaB") or ""))
    raw_path = find_raw_from_hint(hhmm)

    # Build text-stats if all inputs present
    if a_path and b_path and raw_path and reports.get("textStats"):
        out_stats = REPO_ROOT / "novapolis-rp" / reports["textStats"].replace("/", os.sep)
        run_py(
            "text_stats.py",
            [
                str(a_path.relative_to(REPO_ROOT)),
                str(b_path.relative_to(REPO_ROOT)),
                str(raw_path.relative_to(REPO_ROOT)),
                "--out",
                str(out_stats.relative_to(REPO_ROOT)),
            ],
        )

    # Delta A: A vs B
    if a_path and b_path and reports.get("deltaA"):
        out_a = REPO_ROOT / "novapolis-rp" / reports["deltaA"].replace("/", os.sep)
        run_py(
            "delta_report.py",
            [
                str(a_path.relative_to(REPO_ROOT)),
                str(b_path.relative_to(REPO_ROOT)),
                "--out",
                str(out_a.relative_to(REPO_ROOT)),
            ],
        )

    # Delta B: A vs RAW
    if a_path and raw_path and reports.get("deltaB"):
        out_b = REPO_ROOT / "novapolis-rp" / reports["deltaB"].replace("/", os.sep)
        run_py(
            "delta_report.py",
            [
                str(a_path.relative_to(REPO_ROOT)),
                str(raw_path.relative_to(REPO_ROOT)),
                "--out",
                str(out_b.relative_to(REPO_ROOT)),
            ],
        )

    # Delta C: B vs RAW
    if b_path and raw_path and reports.get("deltaC"):
        out_c = REPO_ROOT / "novapolis-rp" / reports["deltaC"].replace("/", os.sep)
        run_py(
            "delta_report.py",
            [
                str(b_path.relative_to(REPO_ROOT)),
                str(raw_path.relative_to(REPO_ROOT)),
                "--out",
                str(out_c.relative_to(REPO_ROOT)),
            ],
        )


def main() -> int:
    manifest_path = REPO_ROOT / "novapolis-rp" / "database-curated" / "staging" / "manifest.json"
    if not manifest_path.exists():
        print(f"manifest.json nicht gefunden: {manifest_path}", file=sys.stderr)
        return 2
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        print("manifest.json: Top-Level ist nicht Array", file=sys.stderr)
        return 3
    for entry in data:
        try:
            regen_for_entry(entry)
        except Exception as e:
            print(f"Warnung: Eintrag übersprungen: {e}", file=sys.stderr)
    print("OK: staging reports regeneriert")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
