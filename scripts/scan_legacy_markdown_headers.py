#!/usr/bin/env python3

"""Scan markdown files for legacy header lines used in S5 migration planning."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

LEGACY_RE = re.compile(r"^(Stand|Letzte Aktualisierung):")
EXCLUDE_PARTS = {
    ".venv",
    "node_modules",
    ".tmp",
    ".tmp-results",
}
EXCLUDE_PREFIXES = ("novapolis-dev/archive/",)

WAVE1_FILES = {
    "README.md",
    "todo.root.md",
    "DONELOG.md",
    "WORKSPACE_STATUS.md",
    "WORKSPACE_INDEX.md",
    "PR_DESCRIPTION.md",
    "single-root-todo.md",
}
WAVE2_PREFIXES = (
    "novapolis-dev/docs/",
    "novapolis_agent/docs/",
)
WAVE3_PREFIXES = ("novapolis-rp/database-rp/",)


@dataclass(frozen=True)
class Hit:
    path: str
    line: int
    text: str


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _excluded(rel: str) -> bool:
    rel_low = rel.lower()
    if any(part.lower() in rel_low.split("/") for part in EXCLUDE_PARTS):
        return True
    return rel_low.startswith(tuple(p.lower() for p in EXCLUDE_PREFIXES))


def _classify_wave(path: str) -> str:
    if path in WAVE1_FILES:
        return "wave1_root_core"
    if path.startswith(WAVE2_PREFIXES):
        return "wave2_dev_agent_docs"
    if path.startswith(WAVE3_PREFIXES):
        return "wave3_rp_database"
    return "wave4_remaining"


def main() -> int:
    root = _repo_root()
    files: list[str] = []
    for p in root.rglob("*.md"):
        rel = p.relative_to(root).as_posix()
        if _excluded(rel):
            continue
        files.append(rel)

    hits: list[Hit] = []
    wave_counts = {
        "wave1_root_core": 0,
        "wave2_dev_agent_docs": 0,
        "wave3_rp_database": 0,
        "wave4_remaining": 0,
    }

    for rel in sorted(files):
        p = root / rel
        matched_in_file = False
        content = p.read_text(encoding="utf-8", errors="ignore")
        for idx, line in enumerate(content.splitlines(), start=1):
            if LEGACY_RE.match(line):
                hits.append(Hit(path=rel, line=idx, text=line.strip()))
                matched_in_file = True
        if matched_in_file:
            wave_counts[_classify_wave(rel)] += 1

    ts_compact = datetime.now().strftime("%Y%m%d_%H%M%S")
    ts_human = datetime.now().strftime("%Y-%m-%d %H:%M")
    out_dir = root / ".tmp" / "results" / "reports"
    out_dir.mkdir(parents=True, exist_ok=True)
    md_path = out_dir / f"legacy_header_scan_{ts_compact}.md"
    json_path = out_dir / f"legacy_header_scan_{ts_compact}.json"

    payload = {
        "timestamp": ts_human,
        "files_scanned": len(files),
        "legacy_hits": len(hits),
        "wave_counts": wave_counts,
        "sample_hits": [hit.__dict__ for hit in hits[:80]],
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines = [
        "---",
        f"stand: {ts_human}",
        "update: Legacy-Header Baseline fuer S5 Etappe-2 Vorbereitung.",
        f"checks: files_scanned={len(files)}; legacy_hits={len(hits)}",
        "---",
        "",
        "Legacy Header Baseline",
        "======================",
        "",
        f"- Files scanned: `{len(files)}`",
        f"- Legacy hits: `{len(hits)}`",
        f"- Wave1 root core: `{wave_counts['wave1_root_core']}`",
        f"- Wave2 dev/agent docs: `{wave_counts['wave2_dev_agent_docs']}`",
        f"- Wave3 rp database: `{wave_counts['wave3_rp_database']}`",
        f"- Wave4 remaining: `{wave_counts['wave4_remaining']}`",
        f"- JSON detail: `{json_path.relative_to(root).as_posix()}`",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"files_scanned={len(files)}")
    print(f"legacy_hits={len(hits)}")
    print(f"wave1_root_core={wave_counts['wave1_root_core']}")
    print(f"wave2_dev_agent_docs={wave_counts['wave2_dev_agent_docs']}")
    print(f"wave3_rp_database={wave_counts['wave3_rp_database']}")
    print(f"wave4_remaining={wave_counts['wave4_remaining']}")
    print(f"report_md={md_path}")
    print(f"report_json={json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
