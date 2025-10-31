#!/usr/bin/env python3
"""
Scan RAW export directory for sidecar flag files (e.g., *.flags.txt) and print a concise report.
Convention:
- For each RAW file X.txt, an optional sidecar X.flags.txt may exist
- Recognized flags: 'vorsichtig_behandeln' (handle with caution)
Exit code 0: ran successfully; prints summary lines
"""
from __future__ import annotations
import sys
import pathlib

RAW_DIR = pathlib.Path(__file__).resolve().parents[3] / 'database-raw' / '99-exports'

def main() -> int:
    if not RAW_DIR.exists():
        print(f"WARN: RAW dir not found: {RAW_DIR}")
        return 0
    flagged = []
    for p in RAW_DIR.glob('*.flags.txt'):
        base = p.name[:-10]  # strip '.flags.txt'
        raw = p.with_name(base + '.txt')
        flag_content = p.read_text(encoding='utf-8', errors='ignore')
        flags = []
        for line in flag_content.splitlines():
            if line.startswith('FLAG:'):
                flags.append(line.split(':', 1)[1].strip())
        flagged.append((raw.name if raw.exists() else base + '.txt', p.name, flags))

    if not flagged:
        print('No sidecar flags found.')
        return 0

    print('Sidecar flag report:')
    for raw_name, sidecar_name, flags in sorted(flagged):
        flags_str = ', '.join(flags) if flags else '(none)'
        print(f"- RAW: {raw_name} | Sidecar: {sidecar_name} | Flags: {flags_str}")
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
