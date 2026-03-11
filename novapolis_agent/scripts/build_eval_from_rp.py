#!/usr/bin/env python
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RPEvalItem:
    item_id: str
    slug: str
    source_file: str
    title: str
    prompt: str

    def to_record(self) -> dict[str, object]:
        return {
            "id": self.item_id,
            "slug": self.slug,
            "category": "rp_eval",
            "tags": ["rp", "ssot", "lore", "generated"],
            "source_package": "rp_ssot_builder.v1",
            "messages": [{"role": "user", "content": self.prompt}],
            "checks": {"must_include": [self.title]},
            "meta": {
                "source_file": self.source_file,
                "source_title": self.title,
            },
        }


def _slugify(value: str) -> str:
    text = value.lower().strip()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def _parse_title(md_text: str, fallback: str) -> str:
    lines = md_text.splitlines()
    for line in lines:
        s = line.strip()
        if not s:
            continue
        if s.startswith("---"):
            continue
        if s.startswith("#"):
            return s.lstrip("#").strip()
    return fallback


def _parse_lead(md_text: str) -> str:
    for line in md_text.splitlines():
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if s.startswith("---") or s.startswith("stand:") or s.startswith("checks:"):
            continue
        return s
    return ""


def _build_prompt(title: str, lead: str) -> str:
    if lead:
        return (
            "Erstelle eine kurze, sachliche Inworld-Einordnung auf Basis des RP-SSOT-Eintrags "
            f'"{title}". Beruecksichtige den Kontext: {lead}'
        )
    return (
        "Erstelle eine kurze, sachliche Inworld-Einordnung auf Basis des RP-SSOT-Eintrags "
        f'"{title}".'
    )


def collect_rp_eval_items(
    rp_root: Path,
    limit: int = 120,
    include_glob: str = "**/*.md",
) -> list[RPEvalItem]:
    files = sorted(rp_root.glob(include_glob))
    items: list[RPEvalItem] = []

    for path in files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        title = _parse_title(text, path.stem.replace("-", " "))
        if not title:
            continue
        lead = _parse_lead(text)

        rel = path.relative_to(rp_root).as_posix()
        basis = f"{rel}|{title}"
        short_hash = hashlib.sha1(basis.encode("utf-8")).hexdigest()[:10]
        slug = f"rp-{_slugify(title)[:48]}-{short_hash}"
        item_id = slug

        items.append(
            RPEvalItem(
                item_id=item_id,
                slug=slug,
                source_file=rel,
                title=title,
                prompt=_build_prompt(title, lead),
            )
        )

        if len(items) >= max(0, int(limit)):
            break

    return items


def write_jsonl(path: Path, records: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description="Build eval dataset from RP SSOT markdown")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root path",
    )
    parser.add_argument(
        "--rp-root",
        default="novapolis-rp/database-rp",
        help="Relative RP source root",
    )
    parser.add_argument(
        "--out",
        default="novapolis_agent/eval/datasets/rp/rp_ssot_core.v1.jsonl",
        help="Relative output path",
    )
    parser.add_argument("--limit", type=int, default=120)
    parser.add_argument("--include-glob", default="**/*.md")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    rp_root = (repo_root / args.rp_root).resolve()
    out_path = (repo_root / args.out).resolve()

    if not rp_root.exists():
        print(f"[rp-eval-builder] ERROR rp_root not found: {rp_root}")
        return 2

    items = collect_rp_eval_items(rp_root, limit=args.limit, include_glob=args.include_glob)
    records = [item.to_record() for item in items]
    write_jsonl(out_path, records)

    print("[rp-eval-builder] done")
    print(f"  source_root: {rp_root}")
    print(f"  output: {out_path}")
    print(f"  records: {len(records)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
