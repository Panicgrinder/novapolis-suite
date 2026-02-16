#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def criteria_contains(criteria: list[str], token: str) -> bool:
    token_l = token.lower()
    return any(token_l in item.lower() for item in criteria)


def unresolved_is_empty(path: Path) -> bool:
    data = load_json(path)
    if not isinstance(data, dict):
        return False
    keys = ["unresolved_dependencies", "unknown_tokens", "alias_collisions", "alias_suggestions"]
    for key in keys:
        if key not in data:
            continue
        value = data[key]
        if isinstance(value, dict) and value:
            return False
        if isinstance(value, list) and value:
            return False
    return True


def main() -> int:
    root = repo_root()
    manifest_path = root / "novapolis-rp" / "database-curated" / "staging" / "manifest.json"
    if not manifest_path.exists():
        print("[curated-promotion-gate] FAIL: manifest.json fehlt.")
        return 1

    manifest = load_json(manifest_path)
    if not isinstance(manifest, list):
        print("[curated-promotion-gate] FAIL: manifest.json ist kein Array.")
        return 1

    errors: list[str] = []
    checked = 0

    for idx, item in enumerate(manifest):
        if not isinstance(item, dict):
            continue
        promotion = item.get("promotion")
        if not isinstance(promotion, dict):
            continue

        checked += 1
        item_id = str(item.get("id", f"index-{idx}"))
        final_gate = promotion.get("finalGate")
        if not isinstance(final_gate, dict):
            errors.append(f"{item_id}: promotion.finalGate fehlt")
            continue

        criteria = final_gate.get("criteria")
        if not isinstance(criteria, list) or not all(isinstance(c, str) for c in criteria):
            errors.append(f"{item_id}: promotion.finalGate.criteria fehlt/ungültig")
            continue

        if not criteria_contains(criteria, "Entscheidungen"):
            errors.append(f"{item_id}: Criteria ohne Decision-Hinweis")
        if not criteria_contains(criteria, "SSOT"):
            errors.append(f"{item_id}: Criteria ohne SSOT-Hinweis")

        runs = item.get("runs")
        if not isinstance(runs, list):
            errors.append(f"{item_id}: runs fehlt/ungültig")
            continue

        run_types = [r.get("type") for r in runs if isinstance(r, dict)]
        if "review-extract" not in run_types:
            errors.append(f"{item_id}: keine review-extract Evidenz in runs")

        reviewed = item.get("reviewed")
        if not isinstance(reviewed, dict):
            errors.append(f"{item_id}: reviewed-Block fehlt")
            continue

        unresolved = reviewed.get("unresolved")
        if not isinstance(unresolved, dict) or "path" not in unresolved:
            errors.append(f"{item_id}: reviewed.unresolved.path fehlt")
            continue

        unresolved_path = root / "novapolis-rp" / str(unresolved["path"]).replace("database-curated/", "database-curated/")
        if not unresolved_path.exists():
            # fallback: path already repo-relative
            unresolved_path = root / str(unresolved["path"])
        if not unresolved_path.exists():
            errors.append(f"{item_id}: unresolved-Datei fehlt ({unresolved.get('path')})")
            continue
        if not unresolved_is_empty(unresolved_path):
            errors.append(f"{item_id}: unresolved-Datei nicht leer ({unresolved.get('path')})")

    if checked == 0:
        print("[curated-promotion-gate] FAIL: Keine promotion-Einträge im Manifest gefunden.")
        return 1

    if errors:
        print("[curated-promotion-gate] FAIL: Promotion-Regel nicht erfüllt.")
        for err in errors:
            print(f" - {err}")
        return 1

    print(
        "[curated-promotion-gate] PASS: Promotion-Einträge enthalten Decision/SSOT-Kriterien, review-extract Evidenz und leere unresolved-Listen."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
