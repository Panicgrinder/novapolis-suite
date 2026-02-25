from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_openthesaurus_lookup(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    root = tmp_path / "datasets"
    ot = root / "OpenThesaurus-Textversion"
    ot.mkdir(parents=True)
    (ot / "openthesaurus.txt").write_text(
        "Haus;Gebaeude;Wohnhaus\n" "schnell;rasch;fix\n", encoding="utf-8"
    )

    monkeypatch.setenv("EVAL_THIRD_PARTY_DATASETS_ROOT", str(root))

    import importlib

    mod = importlib.import_module("utils.third_party_quality")
    mod.load_openthesaurus_index.cache_clear()

    syns = mod.lookup_openthesaurus_synonyms("haus")
    assert "gebaude" in syns
    assert "wohnhaus" in syns


@pytest.mark.scripts
@pytest.mark.unit
def test_sts_relevance_score(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    root = tmp_path / "datasets"
    deepl = (
        root
        / "german-STSbenchmark-master"
        / "german-STSbenchmark-master"
        / "data"
        / "deepl"
    )
    aws = (
        root
        / "german-STSbenchmark-master"
        / "german-STSbenchmark-master"
        / "data"
        / "aws"
    )
    deepl.mkdir(parents=True)
    aws.mkdir(parents=True)

    sample = "5.0\tEin Haus ist gross\tDas Haus ist sehr gross\n"
    (deepl / "stsb_de_train.csv").write_text(sample, encoding="utf-8")
    (aws / "stsb_de_train.csv").write_text(sample, encoding="utf-8")

    monkeypatch.setenv("EVAL_THIRD_PARTY_DATASETS_ROOT", str(root))

    import importlib

    mod = importlib.import_module("utils.third_party_quality")
    mod.load_sts_idf.cache_clear()

    strong = mod.sts_relevance_score("haus gross", "das haus ist gross")
    weak = mod.sts_relevance_score("haus gross", "computer netzwerk")

    assert strong > weak
    assert strong > 0.5


@pytest.mark.scripts
@pytest.mark.unit
def test_validate_german_terms_with_pos_and_splitter(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    root = tmp_path / "datasets"

    jws = (
        root
        / "jwordsplitter-master"
        / "jwordsplitter-master"
        / "src"
        / "main"
        / "resources"
        / "de"
        / "danielnaber"
        / "jwordsplitter"
    )
    jws.mkdir(parents=True)
    (jws / "languagetool-dict.txt").write_text("haus\nraum\n", encoding="utf-8")
    (jws / "germanPrefixes.txt").write_text("haus\n", encoding="utf-8")
    (jws / "exceptionsGerman.txt").write_text("\n", encoding="utf-8")

    pos = (
        root
        / "german-pos-dict-master"
        / "german-pos-dict-master"
        / "src"
        / "main"
        / "resources"
        / "org"
        / "languagetool"
        / "resource"
        / "de"
    )
    pos.mkdir(parents=True)
    (pos / "sonstige.txt").write_text("haus\thaus\tSUB\n", encoding="utf-8")
    (pos / "EIG.txt").write_text("\n", encoding="utf-8")

    monkeypatch.setenv("EVAL_THIRD_PARTY_DATASETS_ROOT", str(root))

    import importlib

    mod = importlib.import_module("utils.third_party_quality")
    mod.load_compound_resources.cache_clear()
    mod.load_pos_lemma_map.cache_clear()

    report = mod.validate_german_terms(["Haus", "Hausraum", "UnbekanntX"])

    assert report["unknown_count"] == 1
    assert report["unknown_terms"] == ["UnbekanntX"]
