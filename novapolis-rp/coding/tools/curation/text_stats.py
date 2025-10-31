import sys
import os
import math
from typing import List, Tuple

def rough_token_estimate(text: str) -> int:
    # Very rough heuristic: ~1 token per 4 chars; safer upper bound for mixed langs
    return math.ceil(len(text) / 4)

def file_stats(path: str) -> Tuple[int, int, int, int, int]:
    # returns: (lines, words, chars, bytes, tokens)
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        data = f.read()
    lines = data.count('\n') + (1 if data and not data.endswith('\n') else 0)
    words = len(data.split())
    chars = len(data)
    try:
        size = os.path.getsize(path)
    except OSError:
        size = len(data.encode('utf-8', errors='replace'))
    tokens = rough_token_estimate(data)
    return lines, words, chars, size, tokens

def main(args: List[str]):
    if not args:
        print("Usage: python text_stats.py <file1> [file2 ...]", file=sys.stderr)
        sys.exit(2)
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # type: ignore[attr-defined]
    except Exception:
        pass
    print("# Text Stats\n")
    for p in args:
        if not os.path.isfile(p):
            print(f"- {p}: NOT FOUND")
            continue
        lines, words, chars, size, tokens = file_stats(p)
        print(f"## {p}")
        print(f"- Zeilen: {lines}")
        print(f"- Wörter: {words}")
        print(f"- Zeichen: {chars}")
        print(f"- Bytes: {size}")
        print(f"- Rough Tokens (~chars/4): {tokens}\n")

if __name__ == '__main__':
    main(sys.argv[1:])
