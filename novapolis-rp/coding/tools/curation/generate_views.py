import os
import sys


def read_lines(path: str) -> list[str]:
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read().splitlines()


def write_lines(path: str, lines: list[str]):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


def recent_views(normalized_path: str, out_dir: str, sizes=(500, 1000)) -> list[str]:
    lines = read_lines(normalized_path)
    written = []
    for n in sizes:
        tail = lines[-n:] if n <= len(lines) else lines[:]
        rev = list(reversed(tail))
        out_path = os.path.join(out_dir, f"recent-{n}.txt")
        write_lines(out_path, rev)
        written.append(out_path)
    return written


def reverse_chunks(chunks_dir: str, out_subdir: str = "reverse") -> str:
    rev_dir = os.path.join(chunks_dir, out_subdir)
    os.makedirs(rev_dir, exist_ok=True)
    for name in sorted(os.listdir(chunks_dir)):
        if not name.endswith(".txt"):
            continue
        if not name.endswith(".part-{:03d}.txt".format(int(name.split("part-")[-1].split(".")[0]))):
            # skip non-part files like index.json
            pass
        in_path = os.path.join(chunks_dir, name)
        if not os.path.isfile(in_path):
            continue
        lines = read_lines(in_path)
        out_path = os.path.join(rev_dir, name.replace(".txt", ".rev.txt"))
        write_lines(out_path, list(reversed(lines)))
    return rev_dir


def main(argv: list[str]):
    if len(argv) < 2:
        print("Usage: python generate_views.py <normalized_path> <chunks_dir>", file=sys.stderr)
        sys.exit(2)
    normalized_path = argv[0]
    chunks_dir = argv[1]
    out_dir = os.path.dirname(normalized_path)
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")  # type: ignore[attr-defined]
    except Exception:
        pass
    recents = recent_views(normalized_path, out_dir, sizes=(500, 1000))
    rev_dir = reverse_chunks(chunks_dir, out_subdir="reverse")
    print("Recent views:")
    for p in recents:
        print("- ", p)
    print("Reverse chunk dir:", rev_dir)


if __name__ == "__main__":
    main(sys.argv[1:])
