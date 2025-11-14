import argparse
import difflib
import os
import sys


def read_lines(path: str) -> list[str]:
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def jaccard(a: list[str], b: list[str]) -> float:
    sa, sb = set(a), set(b)
    if not sa and not sb:
        return 1.0
    return len(sa & sb) / max(1, len(sa | sb))


def unified_diff_stats(a_path: str, b_path: str) -> tuple[int, int]:
    a = read_lines(a_path)
    b = read_lines(b_path)
    diff = list(difflib.unified_diff(a, b, fromfile=a_path, tofile=b_path, lineterm=""))
    adds = sum(1 for line in diff if line.startswith("+") and not line.startswith("+++"))
    dels = sum(1 for line in diff if line.startswith("-") and not line.startswith("---"))
    return adds, dels


def render_report(a_path: str, b_path: str) -> str:
    a = read_lines(a_path)
    b = read_lines(b_path)
    sim = jaccard(a, b)
    adds, dels = unified_diff_stats(a_path, b_path)
    parts: list[str] = []
    parts.append("# Delta-Report\n")
    parts.append(f"Vergleich: {a_path}  <->  {b_path}\n")
    parts.append(f"- Zeilen A: {len(a)}\n- Zeilen B: {len(b)}")
    parts.append(f"- Jaccard-Ähnlichkeit (Zeilenmenge): {sim:.3f}")
    parts.append(f"- Diff: +{adds}  -{dels}\n")

    # Show a small context diff sample
    parts.append("## Diff (A->B) - Auszug")
    diff = difflib.unified_diff(a, b, fromfile=a_path, tofile=b_path, n=3, lineterm="")
    shown = 0
    for line in diff:
        parts.append(line)
        shown += 1
        if shown > 200:  # keep sample bounded
            parts.append("... (gekürzt) ...")
            break
    return "\n".join(parts).rstrip("\n") + "\n"


def main(argv: list[str] | None = None):
    ap = argparse.ArgumentParser()
    ap.add_argument("fileA")
    ap.add_argument("fileB")
    ap.add_argument(
        "--out", dest="out", help="Optional output .md path; if omitted, prints to stdout"
    )
    args = ap.parse_args(argv)

    a, b = args.fileA, args.fileB
    if not os.path.isfile(a) or not os.path.isfile(b):
        print("Both files must exist.", file=sys.stderr)
        sys.exit(2)

    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass

    content = render_report(a, b)
    if args.out:
        os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
        with open(args.out, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    else:
        print(content, end="")


if __name__ == "__main__":
    main()

