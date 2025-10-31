import sys
import os
import json
import hashlib
from typing import List, Dict


def read_text(path: str) -> str:
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return f.read()


def normalize_text(data: str) -> str:
    # Normalize newlines to \n and trim trailing spaces per line; preserve content otherwise
    data = data.replace('\r\n', '\n').replace('\r', '\n')
    lines = data.split('\n')
    norm_lines = [ln.rstrip() for ln in lines]
    return "\n".join(norm_lines)


def sha1_of(text: str) -> str:
    return hashlib.sha1(text.encode('utf-8', errors='replace')).hexdigest()


def write_text(path: str, content: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)


def chunk_lines(lines: List[str], chunk_size: int) -> List[List[str]]:
    return [lines[i:i+chunk_size] for i in range(0, len(lines), chunk_size)]


def build_index(source: str, normalized_path: str, chunks_dir: str, base_name: str,
                chunk_size: int, lines: List[str], chunks: List[List[str]]) -> Dict:
    idx = {
        'source': source,
        'normalized': normalized_path,
        'chunk_size_lines': chunk_size,
        'total_lines': len(lines),
        'chunks_dir': chunks_dir.replace('\\', '/'),
        'chunks': []
    }
    start = 1
    for i, ch in enumerate(chunks, start=1):
        name = f"{base_name}.part-{i:03d}.txt"
        content = "\n".join(ch)
        entry = {
            'name': name,
            'start_line': start,
            'end_line': start + len(ch) - 1,
            'line_count': len(ch),
            'sha1': sha1_of(content)
        }
        idx['chunks'].append(entry)
        start += len(ch)
    return idx


def main(argv: List[str]):
    if len(argv) < 2:
        print("Usage: python chunk_text.py <input_file> <output_base_dir> [chunk_lines=1000]", file=sys.stderr)
        sys.exit(2)
    src = argv[0]
    out_base = argv[1]
    try:
        chunk_size = int(argv[2]) if len(argv) > 2 else 1000
    except ValueError:
        print("chunk_lines must be an integer", file=sys.stderr)
        sys.exit(2)
    if not os.path.isfile(src):
        print(f"Input not found: {src}", file=sys.stderr)
        sys.exit(2)

    # Prepare paths
    base_name = os.path.splitext(os.path.basename(src))[0]
    normalized_path = os.path.join(out_base, f"{base_name}.normalized.txt")
    chunks_dir = os.path.join(out_base, 'chunks', base_name)
    os.makedirs(chunks_dir, exist_ok=True)

    # Read & normalize
    raw = read_text(src)
    norm = normalize_text(raw)
    write_text(normalized_path, norm)

    # Chunk
    lines = norm.split('\n')
    chunks = chunk_lines(lines, chunk_size)

    # Write chunks
    for i, ch in enumerate(chunks, start=1):
        part_name = f"{base_name}.part-{i:03d}.txt"
        write_text(os.path.join(chunks_dir, part_name), "\n".join(ch))

    # Index
    index = build_index(src.replace('\\', '/'), normalized_path.replace('\\', '/'),
                        chunks_dir, base_name, chunk_size, lines, chunks)
    write_text(os.path.join(chunks_dir, 'index.json'), json.dumps(index, ensure_ascii=False, indent=2))

    # Summary
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')  # type: ignore[attr-defined]
    except Exception:
        pass
    print(f"Wrote normalized: {normalized_path}")
    print(f"Chunks: {len(chunks)} -> {chunks_dir}")


if __name__ == '__main__':
    main(sys.argv[1:])
