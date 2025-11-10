#!/usr/bin/env python
"""
Rerun-Failed für Eval:
- Nimmt die neueste eval/results/results_*.jsonl
- Extrahiert fehlgeschlagene IDs
- Baut ein gefiltertes JSONL-Dataset unter eval/results/tmp/ zum direkten Re-Run

Aufruf:
  python scripts/rerun_failed.py
  python scripts/run_eval.py --patterns "eval/results/tmp/rerun_*.jsonl"
"""
from __future__ import annotations

import datetime as dt
import glob
import json
import os
from typing import Any, cast

from utils.eval_utils import ensure_eval_prefix, strip_eval_prefix

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASETS_DIR = os.path.join(PROJECT_ROOT, "eval", "datasets")
RESULTS_DIR = os.path.join(PROJECT_ROOT, "eval", "results")
TMP_DIR = os.path.join(RESULTS_DIR, "tmp")

def _latest_results() -> str | None:
    files = sorted(glob.glob(os.path.join(RESULTS_DIR, "results_*.jsonl")))
    return files[-1] if files else None

def _load_failed_ids(path: str) -> list[str]:
    failed: list[str] = []
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except Exception:
                continue
            # robust: akzeptiere verschiedene Felder
            rid = str(rec.get("id") or rec.get("item_id") or rec.get("eval_id") or "")
            success = bool(rec.get("success")) if "success" in rec else None
            error = rec.get("error")
            failed_checks = rec.get("failed_checks") or []
            if not isinstance(failed_checks, list):
                failed_checks = []
            if not rid:
                continue
            if success is False or error or failed_checks:
                # Füge beide Schlüsselvarianten hinzu, um robust gegen Präfixe zu sein
                if rid:
                    failed.append(rid)
                    failed.append(strip_eval_prefix(rid))
                    failed.append(ensure_eval_prefix(rid))
    return sorted(set(failed))

def _load_registry() -> dict[str, dict[str, Any]]:
    reg: dict[str, dict[str, Any]] = {}
    # JSONL zuerst
    for p in glob.glob(os.path.join(DATASETS_DIR, "eval-*.jsonl")):
        with open(p, encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except Exception:
                    continue
                if not isinstance(obj, dict):
                    continue
                obj_dict = cast(dict[str, Any], obj)
                rid = obj_dict.get("id")
                if isinstance(rid, str):
                    # Mappe sowohl mit als auch ohne eval- Präfix
                    reg[rid] = obj_dict
                    reg[strip_eval_prefix(rid)] = obj_dict
                    reg[ensure_eval_prefix(rid)] = obj_dict
    # JSON (Array)
    for p in glob.glob(os.path.join(DATASETS_DIR, "eval-*.json")):
        if p.endswith(".jsonl"):
            continue
        try:
            with open(p, encoding="utf-8") as handle:
                arr = json.load(handle)
            if isinstance(arr, list):
                for obj in arr:
                    if not isinstance(obj, dict):
                        continue
                    obj_dict = cast(dict[str, Any], obj)
                    rid = obj_dict.get("id")
                    if isinstance(rid, str):
                        reg[rid] = obj_dict
                        reg[strip_eval_prefix(rid)] = obj_dict
                        reg[ensure_eval_prefix(rid)] = obj_dict
        except Exception:
            continue
    return reg

def main() -> int:
    latest = _latest_results()
    if not latest:
        print("Keine results_*.jsonl gefunden unter eval/results/")
        return 1
    failed = _load_failed_ids(latest)
    if not failed:
        print(f"Keine fehlgeschlagenen IDs in {latest} gefunden.")
        return 0
    reg = _load_registry()
    items = [reg[i] for i in failed if i in reg]
    if not items:
        print("Fehlgeschlagene IDs nicht in eval/datasets gefunden.")
        return 2
    os.makedirs(TMP_DIR, exist_ok=True)
    ts = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
    out_path = os.path.join(TMP_DIR, f"rerun_{ts}_{len(items)}.jsonl")
    with open(out_path, "w", encoding="utf-8") as out:
        for obj in items:
            out.write(json.dumps(obj, ensure_ascii=False) + "\n")
    # Robust gegenüber unterschiedlichen Laufwerken (Windows):
    try:
        rel = os.path.relpath(out_path, PROJECT_ROOT)
    except Exception:
        rel = out_path
    print(f"Re-Run Dataset erstellt: {rel}")
    print("Nächster Schritt:")
    print('  python scripts/run_eval.py --patterns "eval/results/tmp/rerun_*.jsonl"')
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
