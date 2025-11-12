from __future__ import annotations

import json
import logging
import os
from pathlib import Path

logger = logging.getLogger("syn_loader")

ALLOWED_CHARS = set("abcdefghijklmnopqrstuvwxyz0123456789 äöüß./-_")


def _merge_dicts(base: dict[str, list[str]], overlay: dict[str, list[str]]) -> dict[str, list[str]]:
    out = dict(base)
    for k, v in overlay.items():
        out[k] = list(v)
    return out


def _sanitize_dict(d: dict[str, list[str]]) -> tuple[dict[str, list[str]], int]:
    dropped = 0
    out: dict[str, list[str]] = {}
    for k, vals in d.items():
        if not isinstance(k, str):
            dropped += 1
            continue
        key = "".join(ch for ch in k.lower() if ch in ALLOWED_CHARS).strip()
        if not key:
            dropped += 1
            continue
        norm_vals: list[str] = []
        for val in vals:
            if not isinstance(val, str):
                dropped += 1
                continue
            nv = "".join(ch for ch in val.lower() if ch in ALLOWED_CHARS).strip()
            if nv:
                norm_vals.append(nv)
            else:
                dropped += 1
        # dedupe + sort
        norm_vals = sorted(list({*norm_vals}))
        out[key] = norm_vals
    return out, dropped


def load_synonyms() -> tuple[dict[str, list[str]], int]:
    """Load and merge synonyms from eval/config/, with additional and local overlays.
    Returns (merged_dict, count_total).
    """
    base = Path("eval/config/synonyms.json")
    add = Path("eval/config/synonyms.additional.json")
    local = Path("eval/config/synonyms.local.json")

    def _read(p: Path) -> dict[str, list[str]]:
        try:
            if p.exists():
                with p.open("r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    return {str(k): list(v) for k, v in data.items() if isinstance(v, list)}
        except Exception as e:
            logger.warning(f"Fehler beim Laden von {p}: {e}")
        return {}

    b = _read(base)
    a = _read(add)
    l = _read(local)

    merged = _merge_dicts(b, a)
    merged = _merge_dicts(merged, l)

    sanitized, dropped = _sanitize_dict(merged)

    # logging
    log_mode = "JSON" if os.environ.get("LOG_JSON", "").lower() in ("1", "true", "yes") else "TEXT"
    logger.info("Ladevorgang Synonyme gestartet (log_mode=%s)", log_mode)
    logger.info(f"Anzahl der Synonym-Einträge (merged): {len(sanitized)}; dropped={dropped}")

    return sanitized, len(sanitized)
