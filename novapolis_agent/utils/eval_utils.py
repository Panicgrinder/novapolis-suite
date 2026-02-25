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


def coerce_eval_records(text: str, source_path: str | None = None) -> list[dict[str, Any]]:
    """Coerced Eval-Datensaetze aus JSON/JSONL/YAML zu einer Liste von Dicts.

    - JSON/JSONL nutzt die bestehende `coerce_json_to_jsonl`-Logik.
    - YAML (`.yaml`/`.yml`) akzeptiert:
      - Liste von Records
      - Multi-Document YAML
      - Dict mit `items: [...]`
    """

    suffix = ""
    if source_path:
        suffix = os.path.splitext(source_path)[1].lower()

    if suffix not in {".yaml", ".yml"}:
        return coerce_json_to_jsonl(text)

    try:
        import yaml  # type: ignore[import-untyped]
    except Exception:
        # Fallback, wenn YAML-Library nicht verfügbar ist.
        return coerce_json_to_jsonl(text)

    try:
        docs = [d for d in yaml.safe_load_all(text) if d is not None]
    except Exception:
        return []

    if not docs:
        return []

    # Single-document YAML
    if len(docs) == 1:
        single = docs[0]
        if isinstance(single, list):
            return [cast(dict[str, Any], r) for r in single if isinstance(r, dict)]
        if isinstance(single, dict):
            items = cast(dict[str, Any], single).get("items")
            if isinstance(items, list):
                return [cast(dict[str, Any], r) for r in items if isinstance(r, dict)]
            return [cast(dict[str, Any], single)]
        return []

    # Multi-document YAML
    out: list[dict[str, Any]] = []
    for doc in docs:
        if isinstance(doc, dict):
            out.append(cast(dict[str, Any], doc))
        elif isinstance(doc, list):
            out.extend([cast(dict[str, Any], r) for r in doc if isinstance(r, dict)])
    return out


def _extract_synonym_values(raw_value: Any) -> list[str]:
    """Extrahiert synonymwertige Strings aus einem Legacy- oder Strukturwert.

    Unterstützte Formate je Key:
    - Legacy: ["syn1", "syn2"]
    - Struktur: {"synonyms": [...], "broader_terms": [...], "narrower_terms": [...]}
    Für die bisherige Matching-Logik werden ausschließlich `synonyms` verwendet.
    """

    if isinstance(raw_value, list):
        return [v for v in raw_value if isinstance(v, str)]

    if isinstance(raw_value, dict):
        synonyms_val = cast(dict[str, Any], raw_value).get("synonyms", [])
        if isinstance(synonyms_val, list):
            return [v for v in synonyms_val if isinstance(v, str)]

    return []


def load_term_relations(
    path: str | list[str] = "eval/config/synonyms.json",
) -> dict[str, dict[str, list[str]]]:
    """Lädt Terminologie-Relationen (synonyms, broader_terms, narrower_terms).

    Rückwärtskompatibel:
    - Legacy-Liste wird als `synonyms` interpretiert.
    - Strukturobjekte werden feldweise übernommen.
    """

    paths = [path] if isinstance(path, str) else list(path)
    merged: dict[str, dict[str, list[str]]] = {}

    def _extract_list_field(obj: dict[str, Any], field: str) -> list[str]:
        val = obj.get(field, [])
        if isinstance(val, list):
            return [v for v in val if isinstance(v, str)]
        return []

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
        for key, value in data.items():
            if not isinstance(key, str):
                continue

            current = merged.setdefault(
                key,
                {
                    "synonyms": [],
                    "broader_terms": [],
                    "narrower_terms": [],
                },
            )

            # Legacy-Liste oder strukturierte Form
            if isinstance(value, list):
                incoming_synonyms = [v for v in value if isinstance(v, str)]
                incoming_broader: list[str] = []
                incoming_narrower: list[str] = []
                structured_override = False
            elif isinstance(value, dict):
                obj = cast(dict[str, Any], value)
                incoming_synonyms = _extract_list_field(obj, "synonyms")
                incoming_broader = _extract_list_field(obj, "broader_terms")
                incoming_narrower = _extract_list_field(obj, "narrower_terms")
                structured_override = True
            else:
                continue

            if structured_override:
                # Strukturwerte sind feldweise autoritativ: sie können
                # bewusst zu breite Basiseinträge überschreiben.
                if "synonyms" in cast(dict[str, Any], value):
                    current["synonyms"] = list(dict.fromkeys(incoming_synonyms))
                if "broader_terms" in cast(dict[str, Any], value):
                    current["broader_terms"] = list(dict.fromkeys(incoming_broader))
                if "narrower_terms" in cast(dict[str, Any], value):
                    current["narrower_terms"] = list(dict.fromkeys(incoming_narrower))
            else:
                for term in incoming_synonyms:
                    if term not in current["synonyms"]:
                        current["synonyms"].append(term)
                for term in incoming_broader:
                    if term not in current["broader_terms"]:
                        current["broader_terms"].append(term)
                for term in incoming_narrower:
                    if term not in current["narrower_terms"]:
                        current["narrower_terms"].append(term)

    return merged


def load_synonyms(path: str | list[str] = "eval/config/synonyms.json") -> dict[str, list[str]]:
    """Lädt eine oder mehrere Synonymdateien und führt deren Inhalte zusammen.

    Hinweis: Bei strukturierter Terminologie werden nur `synonyms` berücksichtigt.
    """

    relations = load_term_relations(path)
    merged: dict[str, list[str]] = {}
    for key, relation in relations.items():
        syns = _extract_synonym_values(relation)
        if syns:
            merged[key] = syns
        else:
            merged[key] = []
    return merged
