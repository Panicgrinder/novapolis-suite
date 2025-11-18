from __future__ import annotations

import json
import os
import re
from typing import Any, cast


def strip_eval_prefix(s: str) -> str:
    """Entfernt das führende "eval-" Präfix von einer ID, falls vorhanden."""

    try:
        return s[5:] if isinstance(s, str) and s.startswith("eval-") else s
    except Exception:
        return s


def ensure_eval_prefix(s: str) -> str:
    """Stellt sicher, dass eine ID mit "eval-" beginnt."""

    try:
        s_str = str(s)
        return s_str if s_str.startswith("eval-") else f"eval-{s_str}"
    except Exception:
        return str(s)


def truncate(text: str, n: int = 200) -> str:
    """Kürzt einen Text auf Länge *n* und hängt bei Bedarf "..." an."""

    if len(text) <= n:
        return text
    return text[: n - 3] + "..."


def normalize_text(text: str) -> str:
    """Normalisiert einen Text für Vergleiche (Kleinschreibung & Zeichenbereinigung)."""

    text = text.lower()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    text = re.sub(r"[^\w\s-]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def coerce_json_to_jsonl(text: str) -> list[dict[str, Any]]:
    """Konvertiert JSON/JSONL-Inhalte in eine einheitliche Liste von Dictionaries."""

    text = re.sub(r"//.*?$", "", text, flags=re.MULTILINE)
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)

    if text.strip().startswith("[") and text.strip().endswith("]"):
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass

    results: list[dict[str, Any]] = []
    errors = 0
    for line in text.strip().split("\n"):
        if not line.strip():
            continue
        try:
            results.append(json.loads(line))
        except json.JSONDecodeError:
            errors += 1

    if errors == 0 and results:
        return results

    fixed_text = re.sub(r"}\s*{", "},{", text)
    if not fixed_text.strip().startswith("["):
        fixed_text = "[" + fixed_text
    if not fixed_text.strip().endswith("]"):
        fixed_text = fixed_text + "]"

    try:
        return json.loads(fixed_text)
    except json.JSONDecodeError:
        repaired: list[dict[str, Any]] = []
        for raw_line in text.strip().split("\n"):
            line = raw_line.strip()
            if not line:
                continue

            line = line.replace("'", '"')
            try:
                repaired.append(json.loads(line))
                continue
            except json.JSONDecodeError:
                if line.startswith("{") and not line.endswith("}"):
                    line += "}"
                elif not line.startswith("{") and line.endswith("}"):
                    line = "{" + line

                try:
                    repaired.append(json.loads(line))
                except json.JSONDecodeError:
                    continue

        return repaired


def load_synonyms(path: str | list[str] = "eval/config/synonyms.json") -> dict[str, list[str]]:
    """Lädt eine oder mehrere Synonymdateien und führt deren Inhalte zusammen."""

    paths = [path] if isinstance(path, str) else list(path)
    merged: dict[str, list[str]] = {}

    for synonym_path in paths:
        if not os.path.exists(synonym_path):
            continue
        try:
            with open(synonym_path, encoding="utf-8") as handle:
                raw = json.load(handle)
        except Exception as exc:  # pragma: no cover - Logging reicht
            print(f"Fehler beim Laden der Synonymdatei '{synonym_path}': {exc!s}")
            continue

        if not isinstance(raw, dict):
            continue

        data = cast(dict[str, Any], raw)
        for key, values in data.items():
            if not isinstance(key, str) or not isinstance(values, list):
                continue

            acc = merged.setdefault(key, [])
            for value in cast(list[object], values):
                if isinstance(value, str) and value not in acc:
                    acc.append(value)

    return merged
