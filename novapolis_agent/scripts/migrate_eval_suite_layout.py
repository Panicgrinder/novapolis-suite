#!/usr/bin/env python
from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


coerce_eval_records = importlib.import_module("utils.eval_utils").coerce_eval_records
ROOT = PROJECT_ROOT
DATASETS = ROOT / "eval" / "datasets"

MAPPING = {
    "neutral": [
        (
            "eval-01-20_prompts_v1.0.json",
            "neutral/neutral_01_20_core.v1.jsonl",
            ["neutral", "core"],
            "neutral-01-20",
        ),
        (
            "eval-81-100_technik_erklaerungen_v1.0.json",
            "neutral/neutral_81_100_tech.v1.jsonl",
            ["neutral", "tech"],
            "neutral-81-100",
        ),
        (
            "gpt_samples.de.jsonl",
            "neutral/neutral_gpt_samples.de.v1.jsonl",
            ["neutral", "chat"],
            "neutral-gpt-sample",
        ),
        (
            "eval-smoke.jsonl",
            "neutral/neutral_smoke.v1.jsonl",
            ["neutral", "smoke"],
            "neutral-smoke",
        ),
        (
            "eval-101-300_generated_v1.0.jsonl",
            "neutral/generated/neutral_101_300_generated.v1.jsonl",
            ["neutral", "generated"],
            "neutral-101-300",
        ),
    ],
    "rpg": [
        (
            "eval-21-40_fantasy_v1.0.json",
            "rpg/rpg_21_40_fantasy.v1.jsonl",
            ["rpg", "fantasy", "szenen"],
            "rpg-21-40",
        ),
        (
            "eval-41-60_dialog_prompts_v1.0.json",
            "rpg/rpg_41_60_dialog.v1.jsonl",
            ["rpg", "dialog"],
            "rpg-41-60",
        ),
        (
            "eval-61-80_szenen_prompts_v1.0.json",
            "rpg/rpg_61_80_szenen.v1.jsonl",
            ["rpg", "szenen"],
            "rpg-61-80",
        ),
    ],
}


def _slugify(text: str) -> str:
    out = []
    for ch in text.lower():
        if ch.isalnum() or ch in {"-", ".", "_"}:
            out.append(ch)
        else:
            out.append("-")
    slug = "".join(out).strip("-")
    while "--" in slug:
        slug = slug.replace("--", "-")
    return slug or "item"


def _norm_tags(existing: Any, defaults: list[str]) -> list[str]:
    tags: list[str] = []
    if isinstance(existing, list):
        tags.extend([str(t).strip().lower() for t in existing if str(t).strip()])
    tags.extend([t.lower() for t in defaults])
    dedup: list[str] = []
    seen: set[str] = set()
    for t in tags:
        if t not in seen:
            seen.add(t)
            dedup.append(t)
    return dedup


def _ensure_id_slug(rec: dict[str, Any], prefix: str, idx: int) -> dict[str, Any]:
    out = dict(rec)
    rec_id = str(out.get("id") or "").strip()
    rec_slug = str(out.get("slug") or "").strip()

    if not rec_slug:
        if rec_id.startswith("eval-"):
            rec_slug = rec_id[5:]
        elif rec_id:
            rec_slug = rec_id
        else:
            rec_slug = f"{prefix}-{idx:03d}"
        rec_slug = _slugify(rec_slug)
        out["slug"] = rec_slug

    if not rec_id:
        out["id"] = f"eval-{rec_slug}"
    elif not rec_id.startswith("eval-"):
        out["id"] = f"eval-{_slugify(rec_id)}"

    return out


def main() -> int:
    generated: list[tuple[str, int]] = []

    for group_items in MAPPING.values():
        for source_name, target_rel, default_tags, prefix in group_items:
            src = DATASETS / source_name
            dst = DATASETS / target_rel
            dst.parent.mkdir(parents=True, exist_ok=True)

            if not src.exists():
                print(f"Skip missing source: {src.relative_to(ROOT)}")
                continue

            text = src.read_text(encoding="utf-8")
            records = coerce_eval_records(text, str(src))

            normalized: list[dict[str, Any]] = []
            for i, rec in enumerate(records, start=1):
                item = _ensure_id_slug(rec, prefix, i)
                item["tags"] = _norm_tags(item.get("tags"), default_tags)
                normalized.append(item)

            with dst.open("w", encoding="utf-8", newline="\n") as f:
                for item in normalized:
                    f.write(json.dumps(item, ensure_ascii=False) + "\n")

            generated.append((str(dst.relative_to(ROOT)), len(normalized)))

    print("Created suite datasets:")
    for path, count in generated:
        print(f"- {path}: {count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
