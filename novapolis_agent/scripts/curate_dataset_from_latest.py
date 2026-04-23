#!/usr/bin/env python
"""
Kuratiert Trainingsdaten aus dem neuesten Eval-Run (results_*.jsonl):
- Wählt die neueste results_*.jsonl unter novapolis_agent/eval/results
- Exportiert in openai_chat-Format (nur erfolgreiche Antworten per Default)
- Erzeugt Train/Val-Pack (dedupliziert, minimaler Output, deterministischer Split)

Nutzung:
    python scripts/curate_dataset_from_latest.py \
        --results-dir novapolis_agent/eval/results \
    --format openai_chat \
    --train-ratio 0.9 \
    --min-output-chars 20 \
        [--include-failures] [--min-rpg-style 0.0] [--exclude-regex "pattern"] [--results-file path]

Ausgabe:
    - Exportierte JSONL unter novapolis_agent/eval/results/finetune
    - Train/Val unter novapolis_agent/eval/results/finetune
  - Kurzer JSON-Report auf stdout
"""

from __future__ import annotations

import argparse
import glob
import json
import os

# Modulpfade vorbereiten
import sys
from typing import Any, cast

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_ROOT = os.path.dirname(PROJECT_ROOT)
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from utils.time_utils import now_compact  # noqa: E402

from scripts import export_finetune as _export  # noqa: E402
from scripts import prepare_finetune_pack as _prepare  # noqa: E402
from scripts import run_eval as _run_eval  # noqa: E402


def _resolve_eval_path(value: str, *, default_base: str = PROJECT_ROOT) -> str:
    if os.path.isabs(value):
        return value
    normalized = value.replace("\\", "/")
    base = (
        REPO_ROOT
        if normalized == "novapolis_agent" or normalized.startswith("novapolis_agent/")
        else default_base
    )
    return os.path.normpath(os.path.join(base, value))


def _latest_results(path: str) -> str | None:
    files = sorted(glob.glob(os.path.join(path, "results_*.jsonl")), reverse=True)
    return files[0] if files else None


def _latest_results_candidates(path: str, pattern: str = "results_*.jsonl") -> list[str]:
    return sorted(glob.glob(os.path.join(path, pattern)), reverse=True)


async def _inspect_candidate_for_export(
    candidate: str,
    *,
    include_failures: bool,
) -> dict[str, Any]:
    inspect_fn = getattr(_export, "inspect_results_for_export", None)
    if callable(inspect_fn):
        return cast(
            dict[str, Any],
            await inspect_fn(candidate, include_failures=include_failures),
        )
    return {
        "ok": True,
        "successful_rows": 0,
        "exportable_count": 0,
        "unmapped_item_ids": [],
    }


def main() -> int:
    # Dynamischer Default-Pfad über Settings
    try:
        from novapolis_agent.app.core.settings import settings

        default_results = _resolve_eval_path(
            getattr(
                settings,
                "EVAL_RESULTS_DIR",
                os.path.join("novapolis_agent", "eval", "results"),
            ),
        )
    except Exception:
        default_results = os.path.join("novapolis_agent", "eval", "results")

    p = argparse.ArgumentParser(
        description="Kuratiert Trainingspakete aus dem neuesten results_*.jsonl"
    )
    p.add_argument(
        "--results-dir",
        default=default_results,
        help=f"Verzeichnis mit results_*.jsonl (Default: {default_results})",
    )
    p.add_argument(
        "--format", choices=["openai_chat", "alpaca"], default="openai_chat", help="Export-Format"
    )
    p.add_argument("--train-ratio", type=float, default=0.9, help="Train-Anteil (0-1)")
    p.add_argument(
        "--min-output-chars",
        type=int,
        default=20,
        help="Mindestlänge der Ausgabe-Zeichen für Filter",
    )
    p.add_argument(
        "--include-failures", action="store_true", help="Auch fehlgeschlagene Antworten exportieren"
    )
    p.add_argument(
        "--min-rpg-style",
        type=float,
        default=0.0,
        help="Mindestschwelle für rpg_style Score (0..1)",
    )
    p.add_argument(
        "--exclude-regex",
        default=None,
        help="Regex zum Ausschließen von Items nach Instruction/Input",
    )
    p.add_argument(
        "--results-file", default=None, help="Konkrete results_*.jsonl statt neuester wählen"
    )
    p.add_argument(
        "--results-glob",
        default="results_*.jsonl",
        help=(
            "Glob relativ zu --results-dir fuer Kandidaten-Auswahl " "(Default: results_*.jsonl)"
        ),
    )
    # Zusätzliche Filter/Metriken (Defaults: aus)
    p.add_argument(
        "--min-assistant-words",
        type=int,
        default=0,
        help="Mindestanzahl Wörter im Assistant-Output",
    )
    p.add_argument(
        "--min-instr-cover",
        type=float,
        default=0.0,
        help="Mindestanteil Instruktions-Token in Antwort (0..1)",
    )
    p.add_argument(
        "--require-list-min",
        type=int,
        default=0,
        help="Minimale Anzahl Listenpunkte im Output (-/*/1./1))",
    )
    args = p.parse_args()

    results_dir = args.results_dir
    candidates = (
        [args.results_file]
        if args.results_file
        else _latest_results_candidates(results_dir, args.results_glob)
    )
    if not candidates:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": (
                        f"Keine Results-Dateien fuer Glob {args.results_glob} in {results_dir}"
                    ),
                }
            )
        )
        return 2

    selection_failures: list[dict[str, Any]] = []
    chosen: str | None = None

    import asyncio

    for candidate in candidates:
        inspection = asyncio.run(
            _inspect_candidate_for_export(
                candidate,
                include_failures=args.include_failures,
            )
        )
        if inspection.get("ok"):
            chosen = candidate
            break

        selection_failures.append(
            {
                "results": candidate,
                "error": inspection.get("error"),
                "successful_rows": inspection.get("successful_rows", 0),
                "exportable_count": inspection.get("exportable_count", 0),
                "unmapped_item_ids": inspection.get("unmapped_item_ids", []),
            }
        )

    if not chosen:
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": "Keine kuratierbare results_*.jsonl gefunden",
                    "results_dir": results_dir,
                    "results_glob": args.results_glob,
                    "checked_candidates": selection_failures[:5],
                },
                ensure_ascii=False,
            )
        )
        return 2

    finetune_dir = os.path.join(results_dir, "finetune")
    os.makedirs(finetune_dir, exist_ok=True)

    # 1) Export
    exp = asyncio.run(
        _export.export_from_results(
            chosen,
            out_dir=finetune_dir,
            format=args.format,
            include_failures=args.include_failures,
        )
    )
    if not exp.get("ok"):
        print(
            json.dumps(
                {
                    "ok": False,
                    "error": exp.get("error"),
                    "results": chosen,
                    "patterns_used": exp.get("patterns_used", []),
                    "successful_rows": exp.get("successful_rows", 0),
                    "exportable_count": exp.get("exportable_count", 0),
                    "unmapped_item_ids": exp.get("unmapped_item_ids", []),
                },
                ensure_ascii=False,
            )
        )
        return 3

    exported_path = str(exp.get("out"))

    # Optional: Qualitätsfilter anwenden, wenn mind. ein Filter aktiv ist
    do_filter = (
        args.min_rpg_style > 0.0
        or bool(args.exclude_regex)
        or args.min_assistant_words > 0
        or args.min_instr_cover > 0.0
        or args.require_list_min > 0
    )
    if do_filter:
        # Laden und filtern
        import re

        def _iter_jsonl(path: str):
            with open(path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    yield json.loads(line)

        records: list[dict[str, Any]] = list(_iter_jsonl(exported_path))
        filtered: list[dict[str, Any]] = []
        pattern = re.compile(args.exclude_regex) if args.exclude_regex else None
        word_re = re.compile(r"[a-z0-9]+", re.IGNORECASE)

        def _assistant_text(rec: dict[str, Any]) -> str:
            if args.format == "openai_chat":
                msgs = cast(list[dict[str, str]], rec.get("messages") or [])
                return (
                    "\n".join(
                        [
                            str(m.get("content", ""))
                            for m in msgs
                            if str(m.get("role")) == "assistant"
                        ]
                    )
                    or ""
                )
            else:
                return str(rec.get("output", ""))

        def _instruction_text(rec: dict[str, Any]) -> str:
            if args.format == "openai_chat":
                msgs2 = cast(list[dict[str, str]], rec.get("messages") or [])
                return next(
                    (str(m.get("content", "")) for m in msgs2 if str(m.get("role")) == "user"), ""
                )
            else:
                return str(rec.get("instruction", ""))

        def _tokenize(text: str) -> list[str]:
            return word_re.findall(text.lower())

        def _list_points(text: str) -> int:
            cnt = 0
            for line in text.splitlines():
                s = line.strip()
                if s.startswith("- ") or s.startswith("* "):
                    cnt += 1
                elif re.match(r"^\d+[\.)]\s+", s):
                    cnt += 1
            return cnt

        for rec in records:
            text = _assistant_text(rec)
            instr = _instruction_text(rec)
            score = float(_run_eval.rpg_style_score(text))
            if score < args.min_rpg_style:
                continue
            if pattern is not None:
                # Instruction/Input heranziehen
                if args.format == "openai_chat":
                    msgs2 = cast(list[dict[str, str]], rec.get("messages") or [])
                    other = (
                        "\n".join(
                            [
                                str(m.get("content", ""))
                                for m in msgs2
                                if str(m.get("role")) != "user"
                            ]
                        )
                        or ""
                    )
                    hay = f"{instr}\n{other}"
                else:
                    inp = str(rec.get("input", ""))
                    hay = f"{instr}\n{inp}"
                if pattern.search(hay):
                    continue

            # Mindestanzahl Wörter im Assistant-Output
            if args.min_assistant_words > 0:
                if len(_tokenize(text)) < int(args.min_assistant_words):
                    continue

            # Instruction-Coverage
            if args.min_instr_cover > 0.0:
                instr_toks = set(_tokenize(instr))
                if instr_toks:
                    resp_toks = set(_tokenize(text))
                    cover = len(instr_toks & resp_toks) / max(1, len(instr_toks))
                    if cover < float(args.min_instr_cover):
                        continue

            # Listenformat mindestens N Punkte
            if args.require_list_min > 0:
                if _list_points(text) < int(args.require_list_min):
                    continue
            filtered.append(rec)

        # Falls alles herausgefiltert wurde, abbrechen mit Info
        if not filtered:
            print(
                json.dumps(
                    {
                        "ok": False,
                        "error": "Alle Einträge wurden durch Filter ausgeschlossen",
                        "results": chosen,
                        "export": exported_path,
                        "filters": {
                            "min_rpg_style": args.min_rpg_style,
                            "exclude_regex": args.exclude_regex,
                        },
                    },
                    ensure_ascii=False,
                )
            )
            return 5

        # Überschreiben exportierter Datei mit gefilterten Einträgen
        with open(exported_path, "w", encoding="utf-8") as f:
            for r in filtered:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")

    # 2) Train/Val Pack
    pack = _prepare.prepare_pack(
        src_path=exported_path,
        out_dir=finetune_dir,
        format=args.format,
        train_ratio=args.train_ratio,
        seed=42,
        min_output_chars=args.min_output_chars,
        dedupe_by_instruction=True,
    )
    if not pack.get("ok"):
        print(json.dumps({"ok": False, "error": pack.get("error")}))
        return 4

    report: dict[str, Any] = {
        "ok": True,
        "timestamp": now_compact(),
        "results": chosen,
        "export": exported_path,
        "train": pack.get("train"),
        "val": pack.get("val"),
        "counts": pack.get("counts"),
    }
    if selection_failures:
        report["skipped_results"] = selection_failures[:5]
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
