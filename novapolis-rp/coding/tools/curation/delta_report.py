import sys
import os
import difflib
from typing import List, Tuple


def read_lines(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return f.read().splitlines()


def jaccard(a: List[str], b: List[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / max(1, len(sa | sb))


def unified_diff_stats(a_path: str, b_path: str) -> Tuple[int, int]:
    a = read_lines(a_path)
    b = read_lines(b_path)
    diff = list(difflib.unified_diff(a, b, fromfile=a_path, tofile=b_path, lineterm=""))
    adds = sum(1 for line in diff if line.startswith('+') and not line.startswith('+++'))
    dels = sum(1 for line in diff if line.startswith('-') and not line.startswith('---'))
    return adds, dels


def report(a_path: str, b_path: str):
    a = read_lines(a_path)
    b = read_lines(b_path)
    sim = jaccard(a, b)
    adds, dels = unified_diff_stats(a_path, b_path)
    print(f"# Delta-Report\n")
    print(f"Vergleich: {a_path}  <->  {b_path}\n")
    print(f"- Zeilen A: {len(a)}\n- Zeilen B: {len(b)}")
    print(f"- Jaccard-Ähnlichkeit (Zeilenmenge): {sim:.3f}")
    print(f"- Diff: +{adds}  -{dels}\n")

    # Show a small context diff sample
    print("## Diff (A->B) – Auszug")
    diff = difflib.unified_diff(a, b, fromfile=a_path, tofile=b_path, n=3, lineterm="")
    shown = 0
    # Ensure UTF-8 friendly output even on Windows consoles
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # type: ignore[attr-defined]
    except Exception:
        pass
    for line in diff:
        print(line)
        shown += 1
        if shown > 200:  # keep sample bounded
            print("... (gekürzt) ...")
            break


def main(argv: List[str]):
    if len(argv) != 2:
        print("Usage: python delta_report.py <fileA> <fileB>", file=sys.stderr)
        sys.exit(2)
    a, b = argv
    if not os.path.isfile(a) or not os.path.isfile(b):
        print("Both files must exist.", file=sys.stderr)
        sys.exit(2)
    report(a, b)

if __name__ == '__main__':
    main(sys.argv[1:])
