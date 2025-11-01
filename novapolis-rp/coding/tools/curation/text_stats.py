import sys
import os
import math
import argparse
from typing import List, Tuple, Optional

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

def render_stats(paths: List[str]) -> str:
    parts: List[str] = ["# Text Stats\n"]
    for p in paths:
        if not os.path.isfile(p):
            parts.append(f"- {p}: NOT FOUND")
            continue
        lines, words, chars, size, tokens = file_stats(p)
        parts.append(f"## {p}")
        parts.append(f"- Zeilen: {lines}")
        parts.append(f"- Wörter: {words}")
        parts.append(f"- Zeichen: {chars}")
        parts.append(f"- Bytes: {size}")
        parts.append(f"- Rough Tokens (~chars/4): {tokens}\n")
    # Ensure single trailing newline at EOF
    return "\n".join(parts).rstrip("\n") + "\n"


def main(argv: Optional[List[str]] = None):
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs='+', help="Input files to summarize")
    ap.add_argument("--out", dest="out", help="Optional output .md path; if omitted, prints to stdout")
    args = ap.parse_args(argv)

    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # type: ignore[attr-defined]
    except Exception:
        pass

    content = render_stats(args.files)
    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, 'w', encoding='utf-8', newline='\n') as f:
            f.write(content)
    else:
        print(content, end="")

if __name__ == '__main__':
    main()
