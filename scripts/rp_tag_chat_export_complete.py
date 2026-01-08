#!/usr/bin/env python3
"""Run YAML-driven tagging for chat-export-complete (staging → reviewed).

This is a thin wrapper around:
  novapolis-rp/coding/tools/curation/tag_chunks_from_yaml.py

It intentionally runs with CWD=novapolis-rp/database-curated/staging so that
`tag_chunks_from_yaml.py` writes its `reports/` logs into staging.
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args(argv)

    repo_root = Path(__file__).resolve().parents[1]
    staging_dir = repo_root / "novapolis-rp" / "database-curated" / "staging"

    python_exe = repo_root / ".venv" / "Scripts" / "python.exe"
    if not python_exe.exists():
        python_exe = Path("python")

    tagger = (
        repo_root
        / "novapolis-rp"
        / "coding"
        / "tools"
        / "curation"
        / "tag_chunks_from_yaml.py"
    )
    yaml_root = repo_root / "novapolis-rp" / "database-rp"
    chunks_root = (
        repo_root
        / "novapolis-rp"
        / "database-curated"
        / "staging"
        / "chunks"
        / "chat-export-complete"
    )
    out_root = (
        repo_root
        / "novapolis-rp"
        / "database-curated"
        / "reviewed"
        / "chat-export-complete"
    )

    cmd: list[str] = [
        str(python_exe),
        str(tagger),
        "--yaml-root",
        str(yaml_root),
        "--chunks-root",
        str(chunks_root),
        "--out-root",
        str(out_root),
        "--range",
        "001-022",
    ]
    if args.dry_run:
        cmd.append("--dry-run")

    proc = subprocess.run(cmd, cwd=str(staging_dir))
    return int(proc.returncode)


if __name__ == "__main__":
    raise SystemExit(main())
