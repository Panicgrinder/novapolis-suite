#!/usr/bin/env python
"""
Exportiert Finetuning-Datensätze (SFT/OpenAI-Chat) aus einer results_*.jsonl-Datei.

Formate:
- alpaca: { instruction, input, output, meta }
- openai_chat: { messages: [{role, content}, ...], meta }

Standard: Nur erfolgreiche Antworten exportieren.
"""

from __future__ import annotations

import glob
import json
import os
import sys
from typing import Any, cast

from utils.time_utils import now_compact


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(PROJECT_ROOT)


def _load_run_eval_module():
    if PROJECT_ROOT not in sys.path:
        sys.path.insert(0, PROJECT_ROOT)
    import importlib.util

    run_eval_path = os.path.join(PROJECT_ROOT, "scripts", "run_eval.py")
    spec = importlib.util.spec_from_file_location("run_eval", run_eval_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Konnte run_eval.py nicht laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # type: ignore
    return module


run_eval = _load_run_eval_module()


def _load_results(path: str) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
    meta: dict[str, Any] | None = None
    rows: list[dict[str, Any]] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                raw = json.loads(line)
            except Exception:
                # Überspringe nicht-JSON-Zeilen robust
                continue
            if not isinstance(raw, dict):
                continue
            data: dict[str, Any] = cast(dict[str, Any], raw)
            if data.get("_meta") is True:
                if meta is None:
                    meta = data
                continue
            rows.append(data)
    return meta, rows


def _dataset_dir() -> str:
    return str(getattr(run_eval, "DEFAULT_DATASET_DIR", os.path.join(PROJECT_ROOT, "eval", "datasets")))


def _dedupe_preserve_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for value in values:
        if not value:
            continue
        key = os.path.normcase(os.path.normpath(value))
        if key in seen:
            continue
        seen.add(key)
        ordered.append(value)
    return ordered


def _resolve_existing_inputs(raw_inputs: list[str], dataset_dir: str) -> list[str]:
    resolved: list[str] = []

    for raw_input in raw_inputs:
        if not raw_input:
            continue

        basename = os.path.basename(raw_input.replace("\\", "/"))
        candidate_inputs: list[str] = []

        if os.path.isabs(raw_input):
            candidate_inputs.append(raw_input)
        else:
            candidate_inputs.extend(
                [
                    raw_input,
                    os.path.join(REPO_ROOT, raw_input),
                    os.path.join(PROJECT_ROOT, raw_input),
                    os.path.join(dataset_dir, raw_input),
                ]
            )
            if basename:
                candidate_inputs.append(os.path.join(dataset_dir, "**", basename))

        for candidate in _dedupe_preserve_order(candidate_inputs):
            matches = sorted(glob.glob(candidate, recursive=True))
            if matches:
                resolved.extend([match for match in matches if os.path.isfile(match)])
                continue
            if os.path.isfile(candidate):
                resolved.append(candidate)

    return _dedupe_preserve_order(resolved)


def _derive_patterns_from_results(
    rows: list[dict[str, Any]],
    meta: dict[str, Any] | None,
    patterns: list[str] | None = None,
) -> list[str]:
    dataset_dir = _dataset_dir()

    if patterns is not None:
        return _resolve_existing_inputs(list(patterns), dataset_dir)

    meta_patterns = [
        str(value)
        for value in cast(list[Any], (meta or {}).get("patterns") or [])
        if isinstance(value, str) and value.strip()
    ]
    source_files = [
        str(row.get("source_file"))
        for row in rows
        if isinstance(row.get("source_file"), str) and str(row.get("source_file")).strip()
    ]

    resolved = _resolve_existing_inputs(meta_patterns, dataset_dir)
    resolved.extend(_resolve_existing_inputs(source_files, dataset_dir))
    return _dedupe_preserve_order(resolved)


def _item_lookup_keys(item: Any) -> list[str]:
    item_id = str(getattr(item, "id", "") or "").strip()
    slug = str(getattr(item, "slug", "") or "").strip()
    keys: list[str] = []

    for raw_value in [item_id, slug]:
        if not raw_value:
            continue
        keys.append(raw_value)
        if raw_value.startswith("eval-"):
            keys.append(raw_value[5:])
        else:
            keys.append(f"eval-{raw_value}")

    return _dedupe_preserve_order(keys)


def _result_lookup_keys(row: dict[str, Any]) -> list[str]:
    keys: list[str] = []
    for field in ("item_id", "slug", "id", "eval_id"):
        raw_value = row.get(field)
        if raw_value is None:
            continue
        value = str(raw_value).strip()
        if not value:
            continue
        keys.append(value)
        if value.startswith("eval-"):
            keys.append(value[5:])
        else:
            keys.append(f"eval-{value}")
    return _dedupe_preserve_order(keys)


def _match_item_for_row(row: dict[str, Any], id_map: dict[str, Any]) -> Any | None:
    for key in _result_lookup_keys(row):
        item = id_map.get(key)
        if item is not None:
            return item
    return None


def _collect_export_pairs(
    rows: list[dict[str, Any]],
    id_map: dict[str, Any],
) -> tuple[list[tuple[dict[str, Any], Any]], list[str]]:
    pairs: list[tuple[dict[str, Any], Any]] = []
    unmapped_ids: list[str] = []

    for row in rows:
        item = _match_item_for_row(row, id_map)
        if item is None:
            unmapped_ids.append(str(row.get("item_id") or row.get("id") or "unbekannt"))
            continue
        pairs.append((row, item))

    return pairs, unmapped_ids


async def _load_items_map(patterns: list[str] | None = None) -> dict[str, Any]:
    items = await run_eval.load_evaluation_items(patterns)
    id_map: dict[str, Any] = {}
    for it in items:
        for key in _item_lookup_keys(it):
            id_map[key] = it
    return id_map


def _first_user_message(messages: list[dict[str, str]]) -> tuple[str, str]:
    """Liefert (instruction, input)."""
    if not messages:
        return ("", "")
    # Nimm die erste user-Nachricht als Instruction,
    # alles andere (weitere user/assistant/system) wird als Input zusammengefasst
    instruction = ""
    others: list[str] = []
    for m in messages:
        role = m.get("role")
        content = m.get("content", "")
        if instruction == "" and role == "user":
            instruction = content
        else:
            if content:
                others.append(content)
    return (instruction, "\n\n".join(others))


async def export_from_results(
    results_path: str,
    out_dir: str | None = None,
    format: str = "alpaca",
    include_failures: bool = False,
    patterns: list[str] | None = None,
) -> dict[str, Any]:
    if out_dir is None:
        # Nutze Settings statt hardcoded fallback
        try:
            try:
                from app.core.settings import settings
            except Exception:
                from novapolis_agent.app.core.settings import settings

            out_dir_str = os.path.join(
                os.path.dirname(os.path.dirname(__file__)),
                getattr(settings, "EVAL_RESULTS_DIR", os.path.join("novapolis_agent", "eval", "results")),
            )
        except Exception:
            out_dir_str = str(getattr(run_eval, "DEFAULT_RESULTS_DIR", run_eval.DEFAULT_EVAL_DIR))
    else:
        out_dir_str = str(out_dir)
    os.makedirs(out_dir_str, exist_ok=True)

    analysis = await inspect_results_for_export(
        results_path,
        include_failures=include_failures,
        patterns=patterns,
    )
    if not analysis.get("ok"):
        return {
            "ok": False,
            "error": analysis.get("error"),
            "results": results_path,
            "patterns_used": analysis.get("patterns_used", []),
            "meta_patterns": analysis.get("meta_patterns", []),
            "successful_rows": analysis.get("successful_rows", 0),
            "exportable_count": analysis.get("exportable_count", 0),
            "unmapped_item_ids": analysis.get("unmapped_item_ids", []),
            "used_broad_fallback": analysis.get("used_broad_fallback", False),
        }

    export_pairs = cast(list[tuple[dict[str, Any], Any]], analysis["export_pairs"])

    rows = [row for row, _item in export_pairs]

    timestamp = now_compact()
    base = os.path.splitext(os.path.basename(results_path))[0]
    out_path: str = os.path.join(out_dir_str, f"finetune_{format}_{base}_{timestamp}.jsonl")

    count = 0
    with open(out_path, "w", encoding="utf-8") as out:
        for r, item in export_pairs:
            item_id = str(r.get("item_id") or r.get("id") or getattr(item, "id", ""))
            messages = cast(list[dict[str, str]], item.messages or [])
            response = r.get("response", "")

            if format == "alpaca":
                instr, inp = _first_user_message(messages)
                rec: dict[str, Any] = {
                    "instruction": instr,
                    "input": inp,
                    "output": response,
                    "meta": {
                        "id": item_id,
                        "package": item.source_package,
                        "success": bool(r.get("success")),
                        "failed_checks": r.get("failed_checks", []),
                    },
                }
            elif format == "openai_chat":
                # Bewahre alle bisherigen Nachrichten, hänge Assistant-Output an
                msgs: list[dict[str, str]] = list(messages)
                msgs.append({"role": "assistant", "content": response})
                rec: dict[str, Any] = {
                    "messages": msgs,
                    "meta": {
                        "id": item_id,
                        "package": item.source_package,
                        "success": bool(r.get("success")),
                        "failed_checks": r.get("failed_checks", []),
                    },
                }
            else:
                raise ValueError("Unbekanntes Format: " + format)

            out.write(json.dumps(rec, ensure_ascii=False) + "\n")
            count += 1

    return {
        "ok": True,
        "out": out_path,
        "count": count,
        "results": results_path,
        "patterns_used": analysis.get("patterns_used", []),
        "used_broad_fallback": analysis.get("used_broad_fallback", False),
        "unmapped_item_ids": analysis.get("unmapped_item_ids", []),
    }


async def inspect_results_for_export(
    results_path: str,
    include_failures: bool = False,
    patterns: list[str] | None = None,
) -> dict[str, Any]:
    meta, rows = _load_results(results_path)
    if not rows:
        return {"ok": False, "error": "Keine Ergebnisse in Datei"}

    candidate_rows = rows if include_failures else [row for row in rows if row.get("success")]
    if not candidate_rows:
        return {"ok": False, "error": "Keine erfolgreichen Ergebnisse für Export"}

    resolved_patterns = _derive_patterns_from_results(candidate_rows, meta, patterns)
    id_map = await _load_items_map(resolved_patterns or None)
    export_pairs, unmapped_ids = _collect_export_pairs(candidate_rows, id_map)
    used_broad_fallback = False

    if not export_pairs and patterns is None:
        broad_patterns = [os.path.join(_dataset_dir(), "**", "*.json*")]
        broad_map = await _load_items_map(broad_patterns)
        broad_pairs, broad_unmapped = _collect_export_pairs(candidate_rows, broad_map)
        if broad_pairs:
            resolved_patterns = broad_patterns
            id_map = broad_map
            export_pairs = broad_pairs
            unmapped_ids = broad_unmapped
            used_broad_fallback = True

    if not export_pairs:
        return {
            "ok": False,
            "error": "Kein exportierbares Item gefunden; Results verweisen wahrscheinlich auf veraltete oder nicht mehr auflösbare Dataset-Pfade.",
            "meta_patterns": [
                str(value)
                for value in cast(list[Any], (meta or {}).get("patterns") or [])
                if isinstance(value, str) and value.strip()
            ],
            "patterns_used": resolved_patterns,
            "successful_rows": len(candidate_rows),
            "exportable_count": 0,
            "unmapped_item_ids": unmapped_ids[:20],
            "used_broad_fallback": used_broad_fallback,
        }

    return {
        "ok": True,
        "meta_patterns": [
            str(value)
            for value in cast(list[Any], (meta or {}).get("patterns") or [])
            if isinstance(value, str) and value.strip()
        ],
        "patterns_used": resolved_patterns,
        "successful_rows": len(candidate_rows),
        "exportable_count": len(export_pairs),
        "unmapped_item_ids": unmapped_ids[:20],
        "used_broad_fallback": used_broad_fallback,
        "export_pairs": export_pairs,
    }


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Exportiert Fine-Tuning-Datensatz aus results_*.jsonl"
    )
    parser.add_argument("results", help="Pfad zur results_*.jsonl Datei")
    parser.add_argument("--format", choices=["alpaca", "openai_chat"], default="alpaca")
    parser.add_argument(
        "--include-failures", action="store_true", help="Auch fehlgeschlagene Antworten exportieren"
    )
    args = parser.parse_args()

    res = __import__(__name__)
    import asyncio

    out = asyncio.run(
        export_from_results(
            args.results, format=args.format, include_failures=args.include_failures
        )
    )
    if out.get("ok"):
        print(f"Export: {out['out']} ({out['count']} Einträge)")
    else:
        print("Fehler:", out.get("error"))
