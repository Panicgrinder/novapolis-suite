#!/usr/bin/env python3
"""
Stream-Ingest für RAW-Exporte (JSONL oder TXT) → kuratierte Szenenblöcke.
- Liest speicherschonend (O(1) RAM)
- Normalisiert leichte Artefakte (Whitespace, Steuerzeichen)
- Schneidet in Blöcke nach max_chars und/oder max_messages
- Schreibt nach database-rp/06-scenes/<YYYYmmdd_HHMM>/scenes_openai_chat.jsonl

WICHTIG: Eingaben müssen aus database-raw/99-exports/ stammen.
Keine Rohdaten direkt in database-rp/ ablegen.

Beispiel:
  python coding/tools/curation/ingest_jsonl.py \
    --in database-raw/99-exports/chat-export-2025-10-23T12-34-56.jsonl \
    --out-dir database-rp/06-scenes --max-chars 12000 --max-messages 80
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
from collections.abc import Iterable
from pathlib import Path
from typing import Any

CTRL_RE = re.compile(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]")
ZW_RE = re.compile(r"[\u200B\u200C\u200D\u2060\uFEFF]")
MULTI_NL_RE = re.compile(r"\n{3,}")
# Kompakt: Tabs/Spaces zusammenfassen - Ziel ist 1 Space (Token-schonend)
MULTI_SPACE_RE = re.compile(r"[ \t]{2,}")


def clean_text(s: str) -> str:
    s = s.replace("\r\n", "\n").replace("\r", "\n")
    s = CTRL_RE.sub("", s)
    s = ZW_RE.sub("", s)
    # Zeilenweise Whitespace-Kompaktion: Tabs→Space, mehrfach Spaces/Tabs → ein Space,
    # anschließend trailing Spaces löschen
    s = MULTI_NL_RE.sub("\n\n", s)
    # Erst grob: Tabs als Space
    s = s.replace("\t", " ")
    # Dann: Runs von 2+ Spaces/Tabs zu einem Space reduzieren
    s = MULTI_SPACE_RE.sub(" ", s)
    # Trailing Spaces pro Zeile entfernen (aber Newlines erhalten)
    s = "\n".join(line.rstrip(" \t") for line in s.split("\n"))
    return s.strip()


def iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            try:
                obj = json.loads(s)
                if isinstance(obj, dict) and "content" in obj:
                    role = str(obj.get("role") or "assistant").lower()
                    content = clean_text(str(obj.get("content") or ""))
                    if content:
                        if role not in ("system", "user", "assistant"):
                            role = "assistant"
                        yield {"role": role, "content": content}
            except Exception:
                # Fallback: behandle Zeile als Plaintext-Nachricht
                content = clean_text(s)
                if content:
                    yield {"role": "assistant", "content": content}


def dedupe_consecutive(msgs: Iterable[dict[str, str]]) -> Iterable[dict[str, str]]:
    last: dict[str, str] | None = None
    for m in msgs:
        if last and last.get("role") == m.get("role") and last.get("content") == m.get("content"):
            continue
        yield m
        last = m


def chunk_messages(
    msgs: Iterable[dict[str, str]], max_chars: int, max_messages: int
) -> Iterable[list[dict[str, str]]]:
    cur: list[dict[str, str]] = []
    cur_chars = 0
    for m in msgs:
        mchars = len(m.get("content", ""))
        if cur and (cur_chars + mchars > max_chars or len(cur) >= max_messages):
            yield cur
            cur = []
            cur_chars = 0
        cur.append(m)
        cur_chars += mchars
    if cur:
        yield cur


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True, help="Pfad zur .jsonl (oder .txt)")
    ap.add_argument(
        "--out-dir", default="database-rp/06-scenes", help="Zielordner für kuratierte Szenen"
    )
    ap.add_argument("--max-chars", type=int, default=12000, help="Max. Zeichen pro Chunk")
    ap.add_argument("--max-messages", type=int, default=80, help="Max. Nachrichten pro Chunk")
    args = ap.parse_args()

    src = Path(args.inp)
    if not src.exists():
        print(f"Input nicht gefunden: {src}", file=sys.stderr)
        return 2

    if "database-raw" not in str(src).replace("\\", "/"):
        print("Sicherheitscheck: Quelle muss unter database-raw/ liegen.", file=sys.stderr)
        return 3

    ts = time.strftime("%Y%m%d_%H%M")
    out_root = Path(args.out_dir) / ts
    out_root.mkdir(parents=True, exist_ok=True)
    out_jsonl = out_root / "scenes_openai_chat.jsonl"

    meta = {
        "_meta": True,
        "source_file": str(src),
        "generated": ts,
        "params": {"max_chars": args.max_chars, "max_messages": args.max_messages},
    }

    # Pipeline: read → clean → dedupe → chunk → write
    stream = iter_jsonl(src)
    stream = dedupe_consecutive(stream)

    written = 0
    with out_jsonl.open("w", encoding="utf-8") as f:
        f.write(json.dumps(meta, ensure_ascii=False) + "\n")
        for i, block in enumerate(
            chunk_messages(stream, args.max_chars, args.max_messages), start=1
        ):
            item = {
                "id": f"scene-{ts}-{i:03d}",
                "messages": block,
                "category": "scene",
                "tags": ["novapolis", "curated"],
                "source_file": str(src),
            }
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
            written += 1

    print(f"OK: {written} Szenen → {out_jsonl}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
