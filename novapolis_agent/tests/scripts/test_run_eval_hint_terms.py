from typing import Any

# Importiere die zu testenden Helfer direkt aus dem Runner
from scripts.run_eval import EvaluationItem, compute_hint_terms


def _mk_item(
    must: list[str], any_terms: list[str], atleast_count: int, atleast_items: list[str]
) -> EvaluationItem:
    messages = [{"role": "user", "content": "Sag etwas."}]
    checks: dict[str, Any] = {
        "must_include": must,
        "keywords_any": any_terms,
        "keywords_at_least": {"count": atleast_count, "items": atleast_items},
    }
    return EvaluationItem(id="eval-001", messages=messages, checks=checks)


def test_compute_hint_terms_priority_dedupe_lower_cap():
    item = _mk_item(
        must=["Alpha", "beta", "Alpha"],
        any_terms=["gamma", "BETA", "delta"],
        atleast_count=2,
        atleast_items=["epsilon", "Gamma", "zeta", "eta"],
    )
    # Aktivieren: alle term checks
    enabled = ["must_include", "keywords_at_least", "keywords_any"]

    terms = compute_hint_terms(item, enabled_checks=enabled, cap=6)

    # Erwartung:
    # - Lowercased
    # - Dedupe case-insensitiv
    # - Reihenfolge: must -> at_least.items -> any
    # - Cap = 6
    assert terms == [
        "alpha",  # aus must
        "beta",  # aus must (dedupe zu BETA später)
        "epsilon",  # aus at_least.items
        "gamma",  # aus at_least.items (dedupe zu any 'gamma' später)
        "zeta",  # aus at_least.items
        "eta",  # aus at_least.items (Cap erreicht)
    ]

    # Stelle sicher, dass KEIN weiterer Eintrag vorhanden ist (cap)
    assert len(terms) == 6
