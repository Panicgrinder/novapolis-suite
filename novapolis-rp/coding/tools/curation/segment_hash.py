import sys
import os
import hashlib
from collections import defaultdict
from typing import List, Dict, Tuple


def normalize_line(s: str) -> str:
    # Trim, collapse internal whitespace
    return " ".join(s.strip().split())


def window_hash(lines: List[str], start: int, win: int) -> str:
    chunk = "\n".join(lines[start:start+win])
    return hashlib.sha1(chunk.encode('utf-8', errors='replace')).hexdigest()


def index_file(path: str, win: int) -> Dict[str, List[int]]:
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        raw_lines = f.read().splitlines()
    lines = [normalize_line(x) for x in raw_lines if normalize_line(x) != ""]
    idx: Dict[str, List[int]] = defaultdict(list)
    for i in range(0, max(0, len(lines) - win + 1)):
        h = window_hash(lines, i, win)
        idx[h].append(i)
    return idx


def cross_duplicates(files: List[str], win: int) -> Dict[str, Dict[str, List[int]]]:
    # returns hash -> file -> positions
    per_file = {p: index_file(p, win) for p in files}
    all_hashes = set().union(*[set(m.keys()) for m in per_file.values()])
    result: Dict[str, Dict[str, List[int]]] = {}
    for h in all_hashes:
        present = {p: per_file[p][h] for p in files if h in per_file[p]}
        if len(present) > 1:
            result[h] = present
    return result


def print_summary(files: List[str], win: int):
    print(f"# Segment-Hash Dedupe (window={win})\n")
    per_file_dupes: List[Tuple[str, int]] = []
    for p in files:
        idx = index_file(p, win)
        internal_dup = sum(1 for positions in idx.values() if len(positions) > 1)
        per_file_dupes.append((p, internal_dup))
    for p, d in per_file_dupes:
        print(f"- {p}: interne Dupe-Hashes (>=2 Vorkommen): {d}")
    cross = cross_duplicates(files, win)
    print(f"\nGemeinsame Segmente über Dateien: {len(cross)}")
    # Print a few examples
    shown = 0
    for h, mapping in cross.items():
        if shown >= 10:
            break
        print(f"\n## Hash {h[:12]}…")
        for fp, pos in mapping.items():
            print(f"- {fp}: Positionen {pos[:5]}{'…' if len(pos)>5 else ''}")
        shown += 1


def main(argv: List[str]):
    if len(argv) < 2:
        print("Usage: python segment_hash.py <window_lines:int> <file1> [file2 ...]", file=sys.stderr)
        sys.exit(2)
    try:
        win = int(argv[0])
    except ValueError:
        print("First argument must be integer window size.", file=sys.stderr)
        sys.exit(2)
    files = argv[1:]
    files = [f for f in files if os.path.isfile(f)]
    if not files:
        print("No valid files given.", file=sys.stderr)
        sys.exit(2)
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # type: ignore[attr-defined]
    except Exception:
        pass
    print_summary(files, win)

if __name__ == '__main__':
    main(sys.argv[1:])
