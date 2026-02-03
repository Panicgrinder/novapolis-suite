#!/usr/bin/env python3
"""Extract PDF text for RP RAW snapshots into staging/pdfs.

- Uses pypdf to extract text
- Normalizes whitespace (trim lines, collapse internal runs, normalize newlines)
- Writes .txt outputs with UTF-8 + LF
"""
from __future__ import annotations

import re
from pathlib import Path

from pypdf import PdfReader

REPO_ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = REPO_ROOT / "novapolis-rp" / "database-raw" / "99-exports"
OUT_DIR = REPO_ROOT / "novapolis-rp" / "database-curated" / "staging" / "pdfs"

PDFS = [
    "Chronist von Novapolis - Ronjas Novapolis RP.pdf",
    "Chronist von Novapolis - Ronjas Novapolis RP1.pdf",
]


def normalize_text(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = []
    for line in text.split("\n"):
        line = line.strip()
        line = re.sub(r"\s+", " ", line)
        lines.append(line)
    # remove consecutive empty lines
    cleaned = []
    last_empty = False
    for line in lines:
        if line == "":
            if last_empty:
                continue
            last_empty = True
        else:
            last_empty = False
        cleaned.append(line)
    return "\n".join(cleaned).rstrip("\n") + "\n"


def extract_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    parts = []
    for page in reader.pages:
        parts.append(page.extract_text() or "")
    return "\n".join(parts)


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for name in PDFS:
        pdf_path = RAW_DIR / name
        if not pdf_path.exists():
            print(f"WARN: PDF not found: {pdf_path}")
            continue
        out_name = pdf_path.stem + ".extracted.txt"
        out_path = OUT_DIR / out_name
        raw = extract_pdf(pdf_path)
        normalized = normalize_text(raw)
        out_path.write_text(normalized, encoding="utf-8", newline="\n")
        print(f"Wrote: {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
