from __future__ import annotations

import json
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_get_term_variants_basic() -> None:
    import importlib

    run_eval = importlib.import_module("scripts.run_eval")
    variants: list[str] = run_eval.get_term_variants("Planung")
    vset = {v.lower() for v in variants}
    # Erwartet: Grundform, Stamm, -en Form, Pluralvarianten
    # Die Implementierung liefert die ursprüngliche Schreibweise, nicht zwingend lowercased
    assert "planung" in vset
    assert "plan" in vset  # "Planung" -> "plan"
    assert "planen" in vset  # "Planung" -> "planen"
    assert ("planung" + "en") in vset  # generische Pluralableitung


@pytest.mark.scripts
@pytest.mark.unit
def test_check_term_inclusion_with_variants_and_synonyms(monkeypatch: pytest.MonkeyPatch) -> None:
    import importlib

    run_eval = importlib.import_module("scripts.run_eval")

    # Synonyme deterministisch machen
    def _fake_synonyms(term: str) -> list[str]:
        # Für "sicherheit" und "risiko" künstliche Synonyme liefern
        if term in ("sicherheit", "sicher"):
            return ["schutz", "absicherung"]
        if term in ("risiko",):
            return ["gefahr"]
        return []

    monkeypatch.setattr(run_eval, "get_synonyms", _fake_synonyms, raising=True)

    text = (
        "Wir planen Maßnahmen zur Absicherung. "
        "Die Gefahr wird minimiert und ein sicherer Betrieb gewährleistet."
    ).lower()

    # Direkte Enthaltenheit
    assert run_eval.check_term_inclusion(text, "gefahr") is True
    # Über Synonyme (risiko -> gefahr)
    assert run_eval.check_term_inclusion(text, "risiko") is True
    # Varianten (Sicherheit -> sicher)
    assert run_eval.check_term_inclusion(text, "Sicherheit") is True
    # Zusammengesetzter Begriff: beide Wörter (oder Synonyme) im Text
    assert run_eval.check_term_inclusion(text, "sichere gefahr") is True


@pytest.mark.scripts
@pytest.mark.unit
def test_get_synonyms_uses_additional_overlay(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    import importlib

    run_eval = importlib.import_module("scripts.run_eval")

    cfg = tmp_path / "eval" / "config"
    cfg.mkdir(parents=True, exist_ok=True)
    (cfg / "synonyms.json").write_text(
        json.dumps({"signal": ["zeichen"]}, ensure_ascii=False), encoding="utf-8"
    )
    (cfg / "synonyms.additional.json").write_text(
        json.dumps({"signal": ["indikator"]}, ensure_ascii=False), encoding="utf-8"
    )
    (cfg / "synonyms.local.json").write_text(
        json.dumps({"signal": ["hinweis"]}, ensure_ascii=False), encoding="utf-8"
    )

    monkeypatch.setattr(run_eval, "DEFAULT_CONFIG_DIR", str(cfg), raising=True)
    monkeypatch.setattr(run_eval, "_synonyms_cache", None, raising=True)
    monkeypatch.setattr(run_eval, "_term_relations_cache", None, raising=True)
    monkeypatch.setattr(
        run_eval,
        "lookup_openthesaurus_synonyms",
        lambda _term, cap=16: [],
        raising=True,
    )

    syns = run_eval.get_synonyms("signal")
    sset = set(syns)
    assert "hinweis" in sset
    assert "indikator" in sset
