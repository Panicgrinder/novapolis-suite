#!/usr/bin/env python
"""
Einfache Evaluierungs-UI (Konsolenmenü) für den CVN Agent.

Funktionen:
- Läufe starten (Pakete wählen, Limit setzen) - ASGI & Eval-Modus
- Frühere Ergebnisse ansehen (results_*.jsonl)
- Fehlgeschlagene Elemente aus einem Ergebnislauf erneut ausführen

Später erweiterbar um weitere Punkte (z. B. Feintuning).
"""

from __future__ import annotations

import asyncio
import glob
import json
import logging
import os
import sys
import warnings
from dataclasses import asdict
from typing import Any, cast


def _load_run_eval_module():
    """Lädt scripts/run_eval.py als Modul, um dessen Funktionen wiederzuverwenden."""
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)
    import importlib.util

    run_eval_path = os.path.join(project_root, "scripts", "run_eval.py")
    spec = importlib.util.spec_from_file_location("run_eval", run_eval_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Konnte run_eval.py nicht laden")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


run_eval = _load_run_eval_module()

# Lockere Typaliases für bessere Lint-Kompatibilität
EvalResult = Any
EvalItem = Any


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def list_eval_packages() -> list[str]:
    """Listet verfügbare Eval-Pakete (Dateien) auf).

    Bevorzugt den datasets-Ordner; fällt auf eval/ zurück. Kombiniert beide ohne Duplikate.
    """
    dataset_dir: str = getattr(run_eval, "DEFAULT_DATASET_DIR", os.path.join("eval", "datasets"))
    eval_dir: str = getattr(run_eval, "DEFAULT_EVAL_DIR", "eval")
    pattern: str = run_eval.DEFAULT_FILE_PATTERN
    files: list[str] = []
    seen: set[str] = set()
    for base in [dataset_dir, eval_dir]:
        try:
            for path in sorted(glob.glob(os.path.join(base, pattern))):
                norm = os.path.normpath(path)
                if norm not in seen:
                    seen.add(norm)
                    files.append(norm)
        except Exception:
            continue
    return files


def prompt_multi_select(options: list[str], title: str) -> list[str]:
    """Mehrfachauswahl via Indizes mit robustem Parser.

    Unterstützt:
    - Trennzeichen: Komma, Semikolon, Leerzeichen (z. B. "1,3 5;7")
    - Bereiche: "2-4" expandiert zu 2,3,4
    - Schlüsselwörter: "all" / "*" für alle
    - Leere Eingabe: alle
    """
    if not options:
        return []
    print(title)
    for i, opt in enumerate(options, start=1):
        print(f"  {i}. {os.path.basename(opt)}")
    raw = input("Auswahl (z. B. 1,3 5-7; leer = alle): ").strip()
    if not raw:
        return options
    low = raw.lower()
    if low in ("*", "all", "alles"):
        return options
    # Tokenisieren nach , ; oder Whitespace
    import re as _re

    tokens = [t for t in _re.split(r"[\s,;]+", raw) if t]
    idxs: list[int] = []
    for tok in tokens:
        if "-" in tok and tok.count("-") == 1:
            a, b = tok.split("-", 1)
            if a.isdigit() and b.isdigit():
                start = int(a)
                end = int(b)
                if start <= end:
                    idxs.extend(list(range(start, end + 1)))
                else:
                    idxs.extend(list(range(end, start + 1)))
                continue
        if tok.isdigit():
            idxs.append(int(tok))
    # Dedupe und validieren
    chosen: list[str] = []
    seen: set[int] = set()
    for i in idxs:
        if 1 <= i <= len(options) and i not in seen:
            seen.add(i)
            chosen.append(options[i - 1])
    return chosen or options


def prompt_int(prompt: str, default: int) -> int:
    raw = input(f"{prompt} (Default {default}): ").strip()
    if not raw:
        return default
    try:
        return max(0, int(raw))
    except ValueError:
        return default


def list_result_files() -> list[str]:
    results_dir: str = getattr(
        run_eval, "DEFAULT_RESULTS_DIR", getattr(run_eval, "DEFAULT_EVAL_DIR", "eval/results")
    )
    files = sorted(glob.glob(os.path.join(results_dir, "results_*.jsonl")), reverse=True)
    return files


def choose_from_list(options: list[str], title: str) -> str | None:
    if not options:
        print("Keine Einträge vorhanden.")
        return None
    print(title)
    for i, path in enumerate(options, start=1):
        print(f"  {i}. {os.path.basename(path)}")
    raw = input("Auswahl (Zahl, leer = Abbrechen): ").strip()
    if not raw:
        return None
    if raw.isdigit():
        idx = int(raw)
        if 1 <= idx <= len(options):
            return options[idx - 1]
    return None


def ensure_eval_files_exist() -> None:
    eval_dir: str = getattr(
        run_eval, "DEFAULT_EVAL_DIR", getattr(run_eval, "DEFAULT_DATASET_DIR", "eval/datasets")
    )
    os.makedirs(eval_dir, exist_ok=True)
    pattern: str = run_eval.DEFAULT_FILE_PATTERN
    if not any(glob.glob(os.path.join(eval_dir, pattern))):
        example_file = os.path.join(eval_dir, "eval-21-40_fantasy_v1.0.jsonl")
        print("Keine Eval-Dateien gefunden - erstelle Demo-Paket …")
        run_eval.create_example_eval_file(example_file, 21, 20)


def profiles_path() -> str:
    cfg_dir: str = getattr(
        run_eval, "DEFAULT_CONFIG_DIR", getattr(run_eval, "DEFAULT_EVAL_DIR", "eval/config")
    )
    return os.path.join(cfg_dir, "profiles.json")


def load_profiles() -> dict[str, dict[str, Any]]:
    path = profiles_path()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    # Defaults, falls keine Datei existiert
    return {
        "default": {
            "model": None,
            "host": None,
            "temperature": None,
            "top_p": None,
            "num_predict": None,
            "checks": None,
            # Laufparameter
            "quiet": True,  # reduzierte Logs standardmäßig
            "asgi": True,  # In-Process-Client
            "eval_mode": True,  # RPG deaktiviert für Evals
        }
    }


def save_profiles(data: dict[str, dict[str, Any]]) -> None:
    os.makedirs(getattr(run_eval, "DEFAULT_CONFIG_DIR", run_eval.DEFAULT_EVAL_DIR), exist_ok=True)
    with open(profiles_path(), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def choose_profile(profiles: dict[str, dict[str, Any]]) -> str:
    keys = list(profiles.keys())
    print("Profile:")
    for i, k in enumerate(keys, start=1):
        print(f"  {i}. {k}")
    raw = input("Auswahl (leer = default): ").strip()
    if raw.isdigit():
        idx = int(raw)
        if 1 <= idx <= len(keys):
            return keys[idx - 1]
    return "default"


def action_edit_profiles() -> None:
    clear_screen()
    data = load_profiles()
    print("Profile bearbeiten/anlegen\n")
    name = input("Profilname (leer = default): ").strip() or "default"
    prof = data.get(
        name,
        {
            "model": None,
            "host": None,
            "temperature": None,
            "top_p": None,
            "num_predict": None,
            "checks": None,
            "quiet": True,
            "asgi": True,
            "eval_mode": True,
        },
    )
    prof["model"] = input(f"Model [{prof.get('model') or '-'}]: ").strip() or prof.get("model")
    prof["host"] = input(f"Host [{prof.get('host') or '-'}]: ").strip() or prof.get("host")
    t = input(
        f"Temperature [{prof.get('temperature') if prof.get('temperature') is not None else '-'}]: "
    ).strip()
    if t:
        try:
            prof["temperature"] = float(t)
        except ValueError:
            pass
    tp = input(f"top_p [{prof.get('top_p') if prof.get('top_p') is not None else '-'}]: ").strip()
    if tp:
        try:
            prof["top_p"] = float(tp)
        except ValueError:
            pass
    default_np = prof.get("num_predict") if prof.get("num_predict") is not None else "-"
    np = input(f"num_predict/max_tokens [{default_np}]: ").strip()
    if np:
        try:
            prof["num_predict"] = int(np)
        except ValueError:
            pass
    checks = input("Checks (Kommagetrennt, leer = alle / unverändert): ").strip()
    if checks:
        prof["checks"] = [p.strip() for p in checks.split(",") if p.strip()]
    q = input(f"Quiet-Mode (y/n, leer = unverändert [{prof.get('quiet')}]): ").strip().lower()
    if q in ("y", "yes"):
        prof["quiet"] = True
    elif q in ("n", "no"):
        prof["quiet"] = False
    # Laufparameter toggles
    a = (
        input(f"ASGI (In-Process) verwenden? (y/n, leer = unverändert [{prof.get('asgi')}]): ")
        .strip()
        .lower()
    )
    if a in ("y", "yes"):
        prof["asgi"] = True
    elif a in ("n", "no"):
        prof["asgi"] = False
    e_default = prof.get("eval_mode")
    e = (
        input(f"Eval-Modus aktivieren (RPG aus)? (y/n, leer = unverändert [{e_default}]): ")
        .strip()
        .lower()
    )
    if e in ("y", "yes"):
        prof["eval_mode"] = True
    elif e in ("n", "no"):
        prof["eval_mode"] = False
    data[name] = prof
    save_profiles(data)
    print("Gespeichert.")
    input("Weiter mit Enter …")


def action_start_run() -> None:
    clear_screen()
    ensure_eval_files_exist()
    packages: list[str] = list_eval_packages()
    if not packages:
        print("Keine Eval-Pakete gefunden.")
        input("Weiter mit Enter …")
        return
    chosen: list[str] = prompt_multi_select(packages, "Verfügbare Pakete:")
    # Default-Limit: Anzahl der Prompts pro ausgewählter Datei grob als 20 pro Datei
    default_limit = max(1, 20 * len(chosen))
    limit = prompt_int("Limit (0 = alle aus Auswahl)", default_limit)
    patterns: list[str] = chosen

    # Profil wählen (optional)
    prof_data = load_profiles()
    use_profile = input("Profil verwenden? (y/N): ").strip().lower() == "y"
    profile_name = "default"
    profile = prof_data.get("default", {})
    if use_profile:
        profile_name = choose_profile(prof_data)
        profile = prof_data.get(profile_name, {})

    # Optionale Check-Auswahl
    check_types = [
        "must_include",
        "keywords_any",
        "keywords_at_least",
        "not_include",
        "regex",
        "rpg_style",
    ]
    print("\nWelche Checks sollen aktiv sein? (leer = alle)")
    for i, c in enumerate(check_types, start=1):
        print(f"  {i}. {c}")
    default_checks = ",".join(profile.get("checks") or []) if profile.get("checks") else ""
    raw_checks = (
        input(f"Auswahl (z. B. 1,3) oder Namen, Kommagetrennt [{default_checks}]: ").strip()
        or default_checks
    )
    enabled_checks: list[str] | None = None
    if raw_checks:
        parts = [p.strip() for p in raw_checks.split(",") if p.strip()]
        chosen_checks: list[str] = []
        for p in parts:
            if p.isdigit():
                idx = int(p)
                if 1 <= idx <= len(check_types):
                    chosen_checks.append(check_types[idx - 1])
            elif p in check_types:
                chosen_checks.append(p)
        enabled_checks = list(dict.fromkeys(chosen_checks)) or None

    # Overrides aus Profil
    model_override = profile.get("model")
    host_override = profile.get("host")
    temperature_override = profile.get("temperature")
    top_p_override = profile.get("top_p")
    num_predict_override = profile.get("num_predict")

    # Debug/Quiet-Optionen
    dbg = input("Debug-Modus aktivieren? (y/N): ").strip().lower() == "y"
    prof_quiet = profile.get("quiet")
    quiet_mode = (True if prof_quiet is None else bool(prof_quiet)) and (not dbg)
    # Profillaufparameter
    prof_asgi = bool(profile.get("asgi", True))
    prof_eval = bool(profile.get("eval_mode", True))

    # Mehrere kürzere Zeilen, damit Line-Length-Regel (E501) eingehalten wird
    print("\nStarte Evaluierung:")
    print(f"  Profil: {profile_name}, Debug: {dbg}, Quiet: {quiet_mode}")
    print(f"  ASGI: {prof_asgi}, Eval: {prof_eval}\n")
    if temperature_override is not None:
        print(f"  • temperature: {temperature_override}")
    if top_p_override is not None:
        print(f"  • top_p: {top_p_override}")
    if num_predict_override is not None:
        print(f"  • num_predict: {num_predict_override}")

    # Optional: temporär Logger-Level für Debug erhöhen
    prev_levels: dict[str, int] = {}
    noisy_loggers = ["app", "app.api.chat", "httpx", "uvicorn", "asyncio"]
    try:
        if dbg:
            for name in noisy_loggers:
                lg = logging.getLogger(name)
                prev_levels[name] = lg.level
                # asyncio im Debug nicht drosseln, alles andere auf DEBUG
                lg.setLevel(logging.DEBUG)

        results: list[EvalResult] = asyncio.run(
            run_eval.run_evaluation(
                patterns=patterns,
                api_url=run_eval.DEFAULT_API_URL,
                limit=(None if limit == 0 else limit),
                eval_mode=prof_eval,
                asgi=prof_asgi,
                enabled_checks=enabled_checks,
                model_override=model_override,
                temperature_override=temperature_override,
                host_override=host_override,
                top_p_override=top_p_override,
                num_predict_override=num_predict_override,
                quiet=quiet_mode,
            )
        )
    finally:
        if dbg:
            for name, lvl in prev_levels.items():
                logging.getLogger(name).setLevel(lvl)
    if results:
        run_eval.print_results(results)
    else:
        print("Keine Ergebnisse - möglicherweise abgebrochen oder keine Einträge gefunden.")
    input("Weiter mit Enter …")


def load_results_from_file(path: str) -> list[EvalResult]:  # lockerer Typ
    """Lädt JSONL-Ergebnisse in EvaluationResult-Objekte."""
    results: list[EvalResult] = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            raw = json.loads(line)
            if not isinstance(raw, dict):
                continue
            data: dict[str, Any] = cast(dict[str, Any], raw)
            # Meta-Header-Zeilen überspringen
            if data.get("_meta") is True:
                continue
            # Felder an Dataclass übergeben (fehlende Felder mit Defaults)
            res: EvalResult = run_eval.EvaluationResult(
                item_id=data.get("item_id", ""),
                response=data.get("response", ""),
                checks_passed=data.get("checks_passed", {}),
                success=bool(data.get("success", False)),
                failed_checks=list(data.get("failed_checks", [])),
                error=data.get("error"),
                source_file=data.get("source_file"),
                source_package=data.get("source_package"),
                duration_ms=int(data.get("duration_ms", 0)),
            )
            results.append(res)
    return results


def load_run_meta(path: str) -> dict[str, Any] | None:
    """Lädt die Meta-Header-Zeile einer results_*.jsonl-Datei (falls vorhanden)."""
    try:
        with open(path, encoding="utf-8") as f:
            first = f.readline().strip()
            if not first:
                return None
            raw = json.loads(first)
            if not isinstance(raw, dict):
                return None
            data: dict[str, Any] = cast(dict[str, Any], raw)
            if data.get("_meta") is True:
                return data
    except Exception:
        return None
    return None


def action_trends() -> None:
    clear_screen()
    files = list_result_files()
    if not files:
        print("Keine Ergebnisdateien gefunden.")
        input("Weiter mit Enter …")
        return
    print("Analysiere Läufe …\n")
    summaries: list[dict[str, Any]] = []
    sweep_summaries: dict[str, list[dict[str, Any]]] = {}
    for path in files:
        meta = load_run_meta(path) or {}
        results = load_results_from_file(path)
        if not results:
            continue
        total = len(results)
        success = sum(1 for r in results if r.success)
        rate = (success / total) * 100.0
        avg_ms = int(sum(r.duration_ms for r in results) / total)
        rpg = sum(1 for r in results if run_eval.check_rpg_mode(r.response))
        top_p_val = None
        try:
            meta_dict = cast(dict[str, Any], meta)
            ov = cast(dict[str, Any], (meta_dict.get("overrides") or {}))
            top_p_val = ov.get("top_p")
        except Exception:
            top_p_val = None
        row: dict[str, Any] = {
            "file": os.path.basename(path),
            "timestamp": meta.get("timestamp") or "-",
            "model": (meta.get("overrides", {}).get("model") or meta.get("model") or "-"),
            "host": (meta.get("overrides", {}).get("host") or meta.get("host") or "-"),
            "temp": (
                meta.get("overrides", {}).get("temperature") or meta.get("temperature") or "-"
            ),
            "top_p": top_p_val if top_p_val is not None else "-",
            "checks": ",".join(meta.get("enabled_checks") or []),
            "total": total,
            "success": success,
            "rate": rate,
            "avg_ms": avg_ms,
            "rpg": rpg,
        }
        summaries.append(row)
        # Sweep-Gruppierung, falls Tag- bzw. Suffix-Pattern erkannt
        # Erwartete Namen: results_YYYYmmdd_HHMM[_tag]_tX[_pY][_nZ].jsonl
        base: str = str(row.get("file", ""))
        import re as _re

        match = _re.match(r"results_\d{8}_\d{4}(?:_[^_]+)?(?:_.+)?\.jsonl$", base)
        if match:
            sweep_summaries.setdefault("all", []).append(row)

    if not summaries:
        print("Keine auswertbaren Läufe gefunden.")
        input("Weiter mit Enter …")
        return

    # Übersichts-Tabelle (letzte 10)
    print("Letzte Läufe:\n")
    header = f"{'Zeit':<13}  {'Model':<18}  {'OK':>6}/{ 'Tot':<4}"
    header += f"  {'Rate':>6}  {'Øms':>6}  {'RPG':>4}  Datei"
    print(header)
    print("-" * len(header))
    for s in summaries[:10]:
        zeit = (
            s["timestamp"][-5:]
            if isinstance(s["timestamp"], str) and len(s["timestamp"]) >= 13
            else s["timestamp"]
        )
        model = str(s["model"])[:18]
        line = f"{zeit:<13}  {model:<18}  {s['success']:>6}/{s['total']:<4}"
        line += f"  {s['rate']:>5.1f}%  {s['avg_ms']:>6}  {s['rpg']:>4}  {s['file']}"
        print(line)

    # Gesamtübersicht
    grand_total = sum(s["total"] for s in summaries)
    grand_success = sum(s["success"] for s in summaries)
    grand_rate = (grand_success / grand_total) * 100.0 if grand_total else 0.0
    print(f"\nGesamt: {grand_success}/{grand_total} ({grand_rate:.1f}%)\n")

    # Optional: Sweep-Aggregation anzeigen (letzte 12 Einträge mit temp/top_p/Øms/Rate)
    if sweep_summaries:
        print("\nSweep-Aggregation (letzte 12):\n")
        left = f"{'Datei':<28}  {'temp':>6}  {'top_p':>6}  {'OK':>6}/{ 'Tot':<4}"
        right = f"  {'Rate':>6}  {'Øms':>6}"
        print(left + right)
        for s in sweep_summaries.get("all", [])[:12]:
            part1 = f"{s['file']:<28}  {s['temp']!s:>6}  {s['top_p']!s:>6}"
            part2 = f"  {s['success']:>6}/{s['total']:<4}"
            line2 = part1 + part2
            line2 += f"  {s['rate']:>5.1f}%"
            line2 += f"  {s['avg_ms']:>6}"
            print(line2)

    # CSV-Export
    if input("Runs als CSV exportieren? (y/N): ").strip().lower() == "y":
        out_csv = os.path.join(
            getattr(run_eval, "DEFAULT_RESULTS_DIR", run_eval.DEFAULT_EVAL_DIR), "runs_summary.csv"
        )
        import csv

        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(
                [
                    "file",
                    "timestamp",
                    "model",
                    "host",
                    "temperature",
                    "top_p",
                    "checks",
                    "total",
                    "success",
                    "rate",
                    "avg_ms",
                    "rpg",
                ]
            )
            for s in summaries:
                w.writerow(
                    [
                        s["file"],
                        s["timestamp"],
                        s["model"],
                        s["host"],
                        s["temp"],
                        s["top_p"],
                        s["checks"],
                        s["total"],
                        s["success"],
                        f"{s['rate']:.1f}",
                        s["avg_ms"],
                        s["rpg"],
                    ]
                )
        print(f"CSV exportiert: {out_csv}")

    # Detail: Paket-Statistik für einen Lauf
    if input("Paket-Statistik eines Laufs ansehen? (y/N): ").strip().lower() == "y":
        fname = choose_from_list([s["file"] for s in summaries], "Wähle Lauf:")
        if fname:
            path = os.path.join(
                getattr(run_eval, "DEFAULT_RESULTS_DIR", run_eval.DEFAULT_EVAL_DIR), fname
            )
            results = load_results_from_file(path)
            if not results:
                print("Keine Ergebnisse in dieser Datei.")
            else:
                stats: dict[str, dict[str, int]] = {}
                for r in results:
                    pkg = r.source_package or "unbekannt"
                    d = stats.setdefault(pkg, {"tot": 0, "ok": 0, "dur": 0})
                    d["tot"] += 1
                    d["dur"] += r.duration_ms
                    if r.success:
                        d["ok"] += 1
                print("\nPaket-Statistik:\n")
                ph = f"{'Paket':<30}  {'OK':>6}/{ 'Tot':<4}  {'Rate':>6}  {'Øms':>6}"
                print(ph)
                print("-" * len(ph))
                for pkg, d in sorted(stats.items()):
                    rate = (d["ok"] / d["tot"]) * 100.0 if d["tot"] else 0.0
                    avg = int(d["dur"] / d["tot"]) if d["tot"] else 0
                    print(f"{pkg:<30}  {d['ok']:>6}/{d['tot']:<4}  {rate:>5.1f}%  {avg:>6}")
    input("Weiter mit Enter …")


def action_view_results() -> None:
    clear_screen()
    files = list_result_files()
    chosen = choose_from_list(files, "Vorhandene Ergebnisdateien:")
    if not chosen:
        return
    raw_results = load_results_from_file(chosen)
    # Filter Meta-Header-Zeilen
    results: list[EvalResult] = [r for r in raw_results if not getattr(r, "_meta", False)]
    # Optionaler Filter
    print("Filter: 1) alle  2) nur Fails  3) nur Success")
    fsel = input("Auswahl (leer=alle): ").strip()
    if fsel == "2":
        results = [r for r in results if not r.success]
    elif fsel == "3":
        results = [r for r in results if r.success]
    # Export-Option
    export = input("Als CSV exportieren? (y/N): ").strip().lower() == "y"
    if export:
        out_csv = os.path.splitext(chosen)[0] + "_export.csv"
        import csv

        with open(out_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "success", "package", "duration_ms", "failed_checks"])
            for r in results:
                writer.writerow(
                    [
                        r.item_id,
                        r.success,
                        r.source_package or "-",
                        r.duration_ms,
                        "; ".join(r.failed_checks),
                    ]
                )
        print(f"CSV exportiert: {out_csv}")
    # Markdown-Export
    md = input("Als Markdown-Report exportieren? (y/N): ").strip().lower() == "y"
    if md:
        out_md = os.path.splitext(chosen)[0] + "_report.md"
        successful = sum(1 for r in results if r.success)
        total = len(results)
        with open(out_md, "w", encoding="utf-8") as f:
            f.write("# Evaluierungsreport\n\n")
            f.write(f"Quelle: {os.path.basename(chosen)}\n\n")
            f.write(
                f"Erfolg: {successful}/{total} ({(successful/total*100 if total else 0):.1f}%)\n\n"
            )
            f.write("## Fehlgeschlagene Tests\n\n")
            for r in results:
                if not r.success:
                    f.write(f"- {r.item_id}: {', '.join(r.failed_checks)}\n")
        print(f"Markdown exportiert: {out_md}")
    if results:
        run_eval.print_results(results)
    else:
        print("Datei enthält keine Ergebnisse.")
    input("Weiter mit Enter …")


async def _evaluate_specific_items(items: list[EvalItem]) -> list[EvalResult]:
    """Evaluiert die übergebenen Items (ASGI, Eval-Modus).

    Schreibt eine neue results_*.jsonl-Datei mit den Ergebnissen.
    """
    # Ergebnis-Dateiname (results-Verzeichnis)
    results_dir: str = getattr(run_eval, "DEFAULT_RESULTS_DIR", run_eval.DEFAULT_EVAL_DIR)
    from utils.time_utils import now_compact

    timestamp = now_compact()
    os.makedirs(results_dir, exist_ok=True)
    out_path = os.path.join(results_dir, f"results_{timestamp}.jsonl")

    # ASGI-Client vorbereiten
    import httpx
    from app.main import app as fastapi_app

    transport = httpx.ASGITransport(app=fastapi_app)
    client = httpx.AsyncClient(transport=transport, base_url="http://asgi")
    api_url = "/chat"

    results: list[EvalResult] = []
    try:
        from rich.progress import Progress

        with Progress() as progress:
            task = progress.add_task("[cyan]Evaluiere (Retry)…", total=len(items))
            for item in items:
                res: EvalResult = await run_eval.evaluate_item(
                    item, api_url=api_url, eval_mode=True, client=client
                )
                results.append(res)
                # sofort persistieren
                with open(out_path, "a", encoding="utf-8") as f:
                    d = asdict(res)
                    d["response"] = run_eval.truncate(d.get("response", ""), 500)
                    f.write(json.dumps(d, ensure_ascii=False) + "\n")
                progress.update(task, advance=1)
    finally:
        await client.aclose()

    logging.info(f"Ergebnisse wurden in {out_path} gespeichert.")
    return results


def action_rerun_failed() -> None:
    clear_screen()
    files = list_result_files()
    chosen = choose_from_list(
        files, "Ergebnisdatei für erneute Ausführung fehlgeschlagener Items wählen:"
    )
    if not chosen:
        return

    # Lade Ergebnisse und extrahiere fehlgeschlagene IDs
    prev_results: list[EvalResult] = load_results_from_file(chosen)
    failed_ids: list[str] = [r.item_id for r in prev_results if not r.success]
    if not failed_ids:
        print("Keine fehlgeschlagenen Items in der gewählten Datei.")
        input("Weiter mit Enter …")
        return

    print(f"Gefundene fehlgeschlagene Items: {len(failed_ids)}")

    # Lade alle Items aus den Standardpaketen und filtere nach IDs
    patterns: list[str] = [os.path.join(run_eval.DEFAULT_EVAL_DIR, run_eval.DEFAULT_FILE_PATTERN)]
    from utils.eval_utils import ensure_eval_prefix, strip_eval_prefix

    all_items: list[EvalItem] = asyncio.run(run_eval.load_evaluation_items(patterns))
    # Erzeuge eine normalisierte ID-Menge (Original, mit eval-, ohne eval-)
    id_set: set[str] = set()
    for rid in failed_ids:
        id_set.add(rid)
        id_set.add(ensure_eval_prefix(rid))
        id_set.add(strip_eval_prefix(rid))
    items_to_rerun: list[EvalItem] = [it for it in all_items if it.id in id_set]

    if not items_to_rerun:
        print("Keine passenden Items in den Eval-Paketen gefunden.")
        input("Weiter mit Enter …")
        return

    print(f"Starte erneute Ausführung von {len(items_to_rerun)} Items …\n")
    results: list[EvalResult] = asyncio.run(_evaluate_specific_items(items_to_rerun))
    if results:
        run_eval.print_results(results)
    input("Weiter mit Enter …")


def action_export_finetune() -> None:
    clear_screen()
    files = list_result_files()
    chosen = choose_from_list(files, "Ergebnisdatei für Finetuning-Export wählen:")
    if not chosen:
        return
    fmt = input("Format wählen: 1) alpaca  2) openai_chat [1]: ").strip()
    fmt = "openai_chat" if fmt == "2" else "alpaca"
    inc = input("Auch Fehlschläge exportieren? (y/N): ").strip().lower() == "y"
    # Export ausführen
    try:
        import importlib

        exporter = importlib.import_module("scripts.export_finetune")
        export_fn = exporter.export_from_results
    except Exception as e:
        print("Exporter nicht verfügbar:", e)
        input("Weiter mit Enter …")
        return
    out: dict[str, Any] = asyncio.run(export_fn(chosen, format=fmt, include_failures=inc))
    if out.get("ok"):
        print(f"Export erfolgreich: {out['out']} ({out['count']} Einträge)")
        if input("Train/Val-Paket aus Export erstellen? (y/N): ").strip().lower() == "y":
            try:
                import importlib

                packer = importlib.import_module("scripts.prepare_finetune_pack")
                pack_res: dict[str, Any] = packer.prepare_pack(out["out"], format=fmt)
                if pack_res.get("ok"):
                    print(
                        "Train:",
                        pack_res["train"],
                        "Val:",
                        pack_res["val"],
                        "Counts:",
                        pack_res["counts"],
                    )
                else:
                    print("Pack-Fehler:", pack_res.get("error"))
            except Exception as e:
                print("Pack-Tool nicht verfügbar:", e)
    else:
        print("Fehler:", out.get("error"))
    input("Weiter mit Enter …")


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    # Generelle Reduktion von asyncio-Noise außerhalb von DEBUG
    if not logging.getLogger().isEnabledFor(logging.DEBUG):
        logging.getLogger("asyncio").setLevel(logging.WARNING)
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", category=ResourceWarning)
    while True:
        clear_screen()
        print("CVN Agent - Evaluierungsmenü")
        print("============================\n")
        print("1) Lauf starten (Pakete & Limit)")
        print("2) Ergebnisse ansehen")
        print("3) Fehlgeschlagene erneut ausführen")
        print("4) Trends / Aggregation")
        print("5) Finetuning-Export aus Ergebnissen")
        print("6) Profile verwalten")
        print("7) Beenden")
        choice = input("\nAuswahl: ").strip()
        if choice == "1":
            action_start_run()
        elif choice == "2":
            action_view_results()
        elif choice == "3":
            action_rerun_failed()
        elif choice == "4":
            action_trends()
        elif choice == "5":
            action_export_finetune()
        elif choice == "6":
            action_edit_profiles()
        elif choice == "7":
            break


if __name__ == "__main__":
    main()
