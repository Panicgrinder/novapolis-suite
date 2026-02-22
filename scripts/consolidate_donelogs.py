#!/usr/bin/env python3

"""Consolidate workspace done logs into 5 central module/root logs.

Output files are written to novapolis-dev/archive/docs/donelogs:
- donelog_root.md
- donelog_agent.md
- donelog_dev.md
- donelog_rp.md
- donelog_sim.md

Entries are deduplicated and sorted newest-first.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

ENTRY_RE = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}) \| ([^|]+) \| (.+)$")
STAND_RE = re.compile(r"^stand:\s*(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\s*$", re.IGNORECASE)


@dataclass(frozen=True)
class Entry:
    ts: datetime
    ts_text: str
    author: str
    summary: str
    source: str
    scope: str


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    candidates = [
        root / "DONELOG.md",
        root / "novapolis_agent" / "docs" / "DONELOG.txt",
        root / "novapolis-dev" / "docs" / "donelog.md",
        root / ".tmp-results" / "sorted_DONELOG.txt",
    ]
    for p in candidates:
        if p.exists():
            files.append(p)

    done_logs_dir = root / "novapolis-dev" / "archive" / "docs" / "donelogs"
    if done_logs_dir.exists():
        for p in sorted(done_logs_dir.glob("*.md")):
            if p.name in {
                "donelog_root.md",
                "donelog_agent.md",
                "donelog_dev.md",
                "donelog_rp.md",
                "donelog_sim.md",
            }:
                continue
            files.append(p)
    return files


def _extract_entries(path: Path, root: Path) -> list[Entry]:
    rel = path.relative_to(root).as_posix()
    text = path.read_text(encoding="utf-8", errors="ignore")
    entries: list[Entry] = []

    # Explicit timestamped entries.
    for line in text.splitlines():
        m = ENTRY_RE.match(line.strip())
        if not m:
            continue
        ts_text, author, summary = m.group(1), m.group(2).strip(), m.group(3).strip()
        ts = datetime.strptime(ts_text, "%Y-%m-%d %H:%M")
        scope = _classify_scope(rel, summary)
        entries.append(Entry(ts, ts_text, author, summary, rel, scope))

    # Synthetic receipt entry from frontmatter stand for postflight files.
    if path.name.startswith(("postflight_", "scan_links_postflight_", "dedupe_")):
        stand: str | None = None
        for line in text.splitlines()[:40]:
            sm = STAND_RE.match(line.strip())
            if sm:
                stand = sm.group(1)
                break
        if stand is not None:
            ts = datetime.strptime(stand, "%Y-%m-%d %H:%M")
            summary = f"Archived receipt: {path.name}"
            entries.append(Entry(ts, stand, "system", summary, rel, "root"))

    return entries


def _classify_scope(source_rel: str, summary: str) -> str:
    s = summary.lower()
    src = source_rel.lower()

    if "novapolis-sim" in src or "godot" in s or "sim " in s or " simulation" in s:
        return "sim"
    if (
        "novapolis-rp" in src
        or " database-rp" in s
        or "canvas" in s
        or "rp " in s
        or "curated" in s
        or "tagging" in s
    ):
        return "rp"
    if (
        "novapolis_agent" in src
        or "fastapi" in s
        or "ollama" in s
        or "pytest" in s
        or "mypy" in s
        or "pyright" in s
        or "app/" in s
        or "agent" in s
    ):
        return "agent"
    if "novapolis-dev" in src or "workspace_index" in s or "readme" in s:
        return "dev"
    return "root"


def _dedupe(entries: list[Entry]) -> list[Entry]:
    seen: set[tuple[str, str, str]] = set()
    out: list[Entry] = []
    for e in sorted(entries, key=lambda x: (x.ts, x.author, x.summary), reverse=True):
        key = (e.ts_text, e.author, e.summary)
        if key in seen:
            continue
        seen.add(key)
        out.append(e)
    return out


def _write_scope_file(out_dir: Path, scope: str, entries: list[Entry]) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    file_path = out_dir / f"donelog_{scope}.md"
    title = f"DONELOG {scope.upper()}"

    lines = [
        "---",
        f"stand: {now}",
        "update: Konsolidierter Ziellog aus Workspace-Quellen (neuester Eintrag oben).",
        "checks: generated_by_scripts_consolidate_donelogs_py",
        "---",
        "",
        title,
        "=" * len(title),
        "",
        "Format: `YYYY-MM-DD HH:mm | author | summary | source=<relative-path>`",
        "",
    ]
    for e in sorted(entries, key=lambda x: x.ts, reverse=True):
        lines.append(f"{e.ts_text} | {e.author} | {e.summary} | source={e.source}")
    lines.append("")
    file_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    root = _repo_root()
    out_dir = root / "novapolis-dev" / "archive" / "docs" / "donelogs"
    out_dir.mkdir(parents=True, exist_ok=True)

    sources = _source_files(root)
    all_entries: list[Entry] = []
    for src in sources:
        all_entries.extend(_extract_entries(src, root))

    entries = _dedupe(all_entries)
    scopes = {"root": [], "agent": [], "dev": [], "rp": [], "sim": []}
    for e in entries:
        scopes[e.scope].append(e)

    for scope in ("root", "agent", "dev", "rp", "sim"):
        _write_scope_file(out_dir, scope, scopes[scope])

    print(f"sources={len(sources)}")
    print(f"entries_total={len(all_entries)}")
    print(f"entries_unique={len(entries)}")
    for scope in ("root", "agent", "dev", "rp", "sim"):
        print(f"{scope}={len(scopes[scope])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
