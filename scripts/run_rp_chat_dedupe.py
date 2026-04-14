#!/usr/bin/env python3
"""Build a consolidated chat-export staging text with dedupe report.

Primary: chat-export-complete.normalized.txt
Secondary: chat-export (1), chat-export, RAW chat exports (02-54, 09-16)

Outputs:
- novapolis-rp/database-curated/staging/chat-export-consolidated.normalized.txt
- novapolis-rp/database-curated/staging/reports/dedupe-chat-export.md
"""

from __future__ import annotations

import hashlib
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STAGING_DIR = REPO_ROOT / "novapolis-rp" / "database-curated" / "staging"
REPORTS_DIR = STAGING_DIR / "reports"

PRIMARY = STAGING_DIR / "chat-export-complete.normalized.txt"
SECONDARY = [
    STAGING_DIR / "chat-export (1).normalized.txt",
    STAGING_DIR / "chat-export.normalized.txt",
    STAGING_DIR / "RAW-chat-export-2025-10-27T09-16-00-188Z.normalized.txt",
    STAGING_DIR / "RAW-chat-export-2025-10-23T02-54-55-897Z.normalized.txt",
]

WINDOW = 5


def normalize_line(s: str) -> str:
    return " ".join(s.strip().split())


def window_hash(lines: list[str], start: int, win: int) -> str:
    chunk = "\n".join(normalize_line(x) for x in lines[start : start + win])
    return hashlib.sha1(chunk.encode("utf-8", errors="replace")).hexdigest()


def build_hashes(lines: list[str], win: int) -> set[str]:
    hashes: set[str] = set()
    for i in range(0, max(0, len(lines) - win + 1)):
        hashes.add(window_hash(lines, i, win))
    return hashes


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8", errors="replace").splitlines()


def iter_unique_segments(
    lines: list[str],
    win: int,
    known: set[str],
) -> list[tuple[int, int]]:
    starts = []
    for i in range(0, max(0, len(lines) - win + 1)):
        h = window_hash(lines, i, win)
        if h not in known:
            starts.append(i)
    if not starts:
        return []
    # group consecutive window starts into segments
    segments: list[tuple[int, int]] = []
    seg_start = starts[0]
    seg_end = starts[0]
    for s in starts[1:]:
        if s == seg_end + 1:
            seg_end = s
        else:
            segments.append((seg_start, seg_end + win - 1))
            seg_start = s
            seg_end = s
    segments.append((seg_start, seg_end + win - 1))
    # clamp end
    segments = [(a, min(b, len(lines) - 1)) for a, b in segments]
    return segments


def add_hashes_for_segment(
    lines: list[str],
    seg: tuple[int, int],
    win: int,
    known: set[str],
) -> None:
    start, end = seg
    for i in range(start, max(start, end - win + 2)):
        if i + win <= len(lines):
            known.add(window_hash(lines, i, win))


def main() -> int:
    if not PRIMARY.exists():
        raise SystemExit(f"Primary missing: {PRIMARY}")

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    primary_lines = read_lines(PRIMARY)
    known = build_hashes(primary_lines, WINDOW)

    consolidated: list[str] = list(primary_lines)
    report_lines = [
        "# Dedupe-Report (Chat-Exports)",
        "",
        f"Primary: {PRIMARY.as_posix()}",
        f"Window size: {WINDOW}",
        "",
    ]

    for src in SECONDARY:
        if not src.exists():
            report_lines.append(f"- {src.name}: NOT FOUND")
            continue
        lines = read_lines(src)
        segments = iter_unique_segments(lines, WINDOW, known)
        report_lines.append(f"- {src.name}: unique segments={len(segments)} (lines={len(lines)})")
        if not segments:
            continue
        consolidated.append("")
        consolidated.append(f"===== SOURCE: {src.name} =====")
        for idx, seg in enumerate(segments, 1):
            start, end = seg
            consolidated.append("")
            consolidated.append(f"----- SEGMENT {idx}: lines {start+1}-{end+1} -----")
            consolidated.extend(lines[start : end + 1])
            add_hashes_for_segment(lines, seg, WINDOW, known)

    out_path = STAGING_DIR / "chat-export-consolidated.normalized.txt"
    out_path.write_text("\n".join(consolidated).rstrip("\n") + "\n", encoding="utf-8")

    report_path = REPORTS_DIR / "dedupe-chat-export.md"
    report_path.write_text("\n".join(report_lines).rstrip("\n") + "\n", encoding="utf-8")

    print(f"Wrote: {out_path}")
    print(f"Wrote: {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
