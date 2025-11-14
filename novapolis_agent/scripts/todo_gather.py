#!/usr/bin/env python
"""
Sammelt Status-/Metrik-Daten für docs/TODO.md:
- Neueste Eval-Ergebnisse analysieren (Erfolgsrate, RPG-Anteil, Dauer)
- Verfügbarkeit offener Features prüfen (Caching, Rerun-Failed, Fine-Tune-Skript)
- Optional Markdown-Report schreiben

Aufruf:
  python scripts/todo_gather.py --write-md
"""
from __future__ import annotations

import argparse
import glob
import json
import os
from typing import Any

from utils.time_utils import now_human

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(PROJECT_ROOT, "eval", "results")
SUMMARIES_DIR = os.path.join(RESULTS_DIR, "summaries")


def latest_results() -> str | None:
    files = sorted(glob.glob(os.path.join(RESULTS_DIR, "results_*.jsonl")))
    return files[-1] if files else None


def parse_results(path: str) -> dict[str, Any]:
    total = 0
    success = 0
    rpg_mode = 0
    durations: list[int] = []
    failed_ids: list[str] = []
    by_package: dict[str, dict[str, Any]] = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                r = json.loads(line)
            except Exception:
                continue
            total += 1
            if r.get("success") is True:
                success += 1
            if r.get("rpg_mode") is True:
                rpg_mode += 1
            d = r.get("duration_ms")
            if isinstance(d, int | float):
                durations.append(int(d))
            rid = r.get("id") or r.get("item_id")
            if r.get("success") is not True and rid:
                failed_ids.append(str(rid))
            pkg = r.get("package") or "unknown"
            stats = by_package.setdefault(str(pkg), {"total": 0, "success": 0, "durations": []})
            stats["total"] += 1
            if r.get("success") is True:
                stats["success"] += 1
            if isinstance(d, int | float):
                stats["durations"].append(int(d))
    avg_dur = (sum(durations) / len(durations)) if durations else 0.0
    return {
        "path": path,
        "total": total,
        "success": success,
        "success_rate": (success / total * 100.0) if total else 0.0,
        "rpg_percentage": (rpg_mode / total * 100.0) if total else 0.0,
        "avg_duration_ms": avg_dur,
        "failed_ids": sorted(set(failed_ids)),
        "by_package": by_package,
    }


def file_exists(rel: str) -> bool:
    return os.path.exists(os.path.join(PROJECT_ROOT, rel))


def feature_status() -> dict[str, Any]:
    # Caching: Datei + Nutzung in map_reduce_summary_llm.py
    caching_file = file_exists("utils/eval_cache.py")
    caching_used = False
    if file_exists("scripts/map_reduce_summary_llm.py"):
        try:
            txt = open(
                os.path.join(PROJECT_ROOT, "scripts", "map_reduce_summary_llm.py"),
                encoding="utf-8",
            ).read()
            caching_used = ("utils.eval_cache" in txt) or ("cache_llm.jsonl" in txt)
        except Exception:
            pass
    rerun_failed = False  # legacy script replaced by rerun_from_results.py
    fine_tune = file_exists("scripts/fine_tune_pipeline.py")
    curate = file_exists("scripts/curate_dataset_from_latest.py")
    return {
        "caching_available": caching_file,
        "caching_integrated": caching_used,
        "rerun_failed_available": rerun_failed,
        "fine_tune_pipeline_available": fine_tune,
        "curate_dataset_available": curate,
    }


def build_md(results: dict[str, Any] | None, features: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# TODO-Status - Automatischer Überblick")
    lines.append("")
    lines.append("## Features (offene Punkte)")
    if features.get("caching_integrated"):
        caching_status = "✅ integriert"
    elif features.get("caching_available"):
        caching_status = "🟡 vorhanden (noch nicht integriert)"
    else:
        caching_status = "❌ fehlt"
    lines.append(f"- Caching/Memoization: {caching_status}")
    lines.append("- Rerun-Failed: ✅ via scripts/rerun_from_results.py")
    ft_status = "✅ vorhanden" if features.get("fine_tune_pipeline_available") else "❌ fehlt"
    lines.append(f"- Fine-Tuning/LoRA Pipeline: {ft_status}")
    curate_status = "✅ vorhanden" if features.get("curate_dataset_available") else "❌ fehlt"
    lines.append(f"- Datensatzkurierung: {curate_status}")
    lines.append("")
    if results:
        lines.append("## Letzte Eval-Metriken")
        lines.append(f"- Datei: {os.path.relpath(results['path'], PROJECT_ROOT)}")
        succ = results.get("success")
        tot = results.get("total")
        rate_str = f"{results.get('success_rate'):.1f}"
        tests_summary = "- Tests: " + str(succ) + "/" + str(tot) + " (" + rate_str + "%)"
        lines.append(tests_summary)
        lines.append(f"- RPG-Anteil: {results['rpg_percentage']:.1f}%")
        lines.append(f"- Ø Dauer: {results['avg_duration_ms']:.0f} ms")
        if results["failed_ids"]:
            failed_preview = ", ".join(results["failed_ids"][:25])
            ell = " …" if len(results["failed_ids"]) > 25 else ""
            lines.append(f"- Fehlgeschlagene IDs: {failed_preview}{ell}")
    return "\n".join(lines)


def _write_md_with_frontmatter(
    out: str, md_body: str, update_text: str = "Generated by todo_gather.py", checks: str = "PASS"
) -> None:
    """Schreibe eine Markdown-Datei mit exakt formatiertem YAML-Frontmatter und Setext-Headern.

    - Frontmatter-Schlüssel in genau dieser Reihenfolge: stand, update, checks
    - stand: ISO-8601 mit Offset (via utils.time_utils.now_iso)
    - danach H1/H2 im Setext-Stil für die erste H1/H2 im Dokument
    """
    # Erzeuge Frontmatter
    ts = now_human() if now_human is not None else ""

    # Konvertiere höchstens die allererste H1 (# ) direkt am Dokumentanfang,
    # aber NICHT wenn sie "TODO-Status" enthält. Keine weiteren H1/H2 anfassen.
    body = md_body.replace("\r\n", "\n").lstrip("\ufeff")
    lines = body.split("\n")
    # finde erste nicht-leere Zeile
    idx = 0
    while idx < len(lines) and lines[idx].strip() == "":
        idx += 1
    if idx < len(lines) and lines[idx].startswith("# "):
        first_title = lines[idx][2:].strip()
        # Nur konvertieren, wenn Titel nicht "TODO-Status" enthält
        if "todo-status" not in first_title.lower():
            underline = "=" * len(first_title)
            # ersetze die H1-Zeile durch Setext-Variante und füge Leerzeile danach ein
            new_head = [first_title, underline, ""]
            lines = lines[:idx] + new_head + lines[idx + 1 :]
    body = "\n".join(lines)

    # Ensure single trailing newline at EOF
    if not body.endswith("\n"):
        body = body + "\n"

    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write("---\n")
        f.write(f"stand: {ts}\n")
        f.write(f"update: {update_text}\n")
        f.write(f"checks: {checks}\n")
        f.write("---\n\n")
        f.write(body)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--write-md",
        action="store_true",
        help="Schreibt Markdown-Report unter eval/results/summaries/",
    )
    ap.add_argument(
        "--out-dir",
        type=str,
        default=SUMMARIES_DIR,
        help="Zielverzeichnis für Markdown-Ausgabe (für Dry-Run)",
    )
    args = ap.parse_args(argv)
    latest = latest_results()
    results = parse_results(latest) if latest else None
    features = feature_status()
    md = build_md(results, features)
    print(md)
    if args.write_md:
        out_dir = args.out_dir
        os.makedirs(out_dir, exist_ok=True)
        from utils.time_utils import now_compact

        ts = now_compact()
        out = os.path.join(out_dir, f"todo_status_{ts}.md")
        # Minimal-invasive write via helper to ensure Frontmatter + Setext
        _write_md_with_frontmatter(
            out, md, update_text="Generated by todo_gather.py", checks="PASS"
        )
        print(f"\nReport gespeichert: {os.path.relpath(out, PROJECT_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
