import json
import os
import sys
import tempfile
from typing import Any, cast

# Cache für Module
_run_eval_module = None


def _get_run_eval() -> Any:
    """Cached import with proper path setup."""
    global _run_eval_module
    if _run_eval_module is None:
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        if project_root not in sys.path:
            sys.path.insert(0, project_root)

        from novapolis_agent.scripts import run_eval as _run_eval

        _run_eval_module = _run_eval
    return _run_eval_module


def test_synonyms_overlay_merged_and_deduped():
    run_eval = _get_run_eval()
    old_cfg = run_eval.DEFAULT_CONFIG_DIR
    try:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = os.path.join(tmp, "config")
            os.makedirs(cfg, exist_ok=True)
            base_path = os.path.join(cfg, "synonyms.json")
            overlay_path = os.path.join(cfg, "synonyms.local.json")
            with open(base_path, "w", encoding="utf-8") as f:
                json.dump(
                    {"arzt": ["doktor", "mediziner"], "unternehmen": ["firma"]},
                    f,
                    ensure_ascii=False,
                )
            with open(overlay_path, "w", encoding="utf-8") as f:
                json.dump(
                    {"arzt": ["arzt", "ärztin", "mediziner"], "unternehmen": ["betrieb"]},
                    f,
                    ensure_ascii=False,
                )

            # Patch Config-Dir und Cache leeren
            mod = cast(Any, run_eval)
            mod.DEFAULT_CONFIG_DIR = cfg
            mod._synonyms_cache = None

            syns_arzt = mod.get_synonyms("arzt")
            # Erwartet: Merge + Dedupe (doktor, mediziner, ärztin mindestens)
            for w in ("doktor", "mediziner", "ärztin"):
                assert w in syns_arzt, f"'{w}' fehlt in gemergten Synonymen: {syns_arzt}"

            syns_unternehmen = mod.get_synonyms("unternehmen")
            for w in ("firma", "betrieb"):
                failure_msg = f"'{w}' fehlt in gemergten Synonymen: {syns_unternehmen}"
                assert w in syns_unternehmen, failure_msg
    finally:
        # Restore
        mod2 = cast(Any, run_eval)
        mod2.DEFAULT_CONFIG_DIR = old_cfg
        mod2._synonyms_cache = None


def test_synonyms_overlay_missing_is_silent():
    run_eval = _get_run_eval()
    old_cfg = run_eval.DEFAULT_CONFIG_DIR
    try:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = os.path.join(tmp, "config")
            os.makedirs(cfg, exist_ok=True)
            base_path = os.path.join(cfg, "synonyms.json")
            with open(base_path, "w", encoding="utf-8") as f:
                json.dump({"sicherheit": ["schutz", "sicher"]}, f, ensure_ascii=False)

            # Kein overlay schreiben
            mod = cast(Any, run_eval)
            mod.DEFAULT_CONFIG_DIR = cfg
            mod._synonyms_cache = None

            syns = mod.get_synonyms("sicherheit")
            assert "schutz" in syns and "sicher" in syns
    finally:
        mod2 = cast(Any, run_eval)
        mod2.DEFAULT_CONFIG_DIR = old_cfg
        mod2._synonyms_cache = None


def test_synonyms_structured_relations_only_use_synonyms_for_matching():
    run_eval = _get_run_eval()
    old_cfg = run_eval.DEFAULT_CONFIG_DIR
    try:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = os.path.join(tmp, "config")
            os.makedirs(cfg, exist_ok=True)
            base_path = os.path.join(cfg, "synonyms.json")
            with open(base_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "parmesan": {
                            "synonyms": ["parmigiano", "parmesankäse"],
                            "broader_terms": ["käse"],
                            "narrower_terms": [],
                        }
                    },
                    f,
                    ensure_ascii=False,
                )

            mod = cast(Any, run_eval)
            mod.DEFAULT_CONFIG_DIR = cfg
            mod._synonyms_cache = None

            syns = mod.get_synonyms("parmesan")
            assert "parmigiano" in syns
            assert "parmesankäse" in syns
            # Oberbegriffe dürfen nicht als Synonym in die Matching-Liste rutschen.
            assert "käse" not in syns
    finally:
        mod2 = cast(Any, run_eval)
        mod2.DEFAULT_CONFIG_DIR = old_cfg
        mod2._synonyms_cache = None


def test_synonyms_structured_overlay_overrides_base_synonym_list():
    run_eval = _get_run_eval()
    old_cfg = run_eval.DEFAULT_CONFIG_DIR
    try:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = os.path.join(tmp, "config")
            os.makedirs(cfg, exist_ok=True)
            base_path = os.path.join(cfg, "synonyms.json")
            overlay_path = os.path.join(cfg, "synonyms.local.json")

            with open(base_path, "w", encoding="utf-8") as f:
                json.dump({"parmesan": ["käse", "hartkäse", "bergkäse"]}, f, ensure_ascii=False)
            with open(overlay_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "parmesan": {
                            "synonyms": ["parmigiano", "parmigiano-reggiano"],
                            "broader_terms": ["hartkäse", "käse"],
                            "narrower_terms": [],
                        }
                    },
                    f,
                    ensure_ascii=False,
                )

            mod = cast(Any, run_eval)
            mod.DEFAULT_CONFIG_DIR = cfg
            mod._synonyms_cache = None

            syns = mod.get_synonyms("parmesan")
            assert "parmigiano" in syns
            assert "parmigiano-reggiano" in syns
            # Aus Base-Liste darf nichts "durchbluten", wenn Overlay strukturiert überschreibt.
            assert "käse" not in syns
            assert "hartkäse" not in syns
            assert "bergkäse" not in syns
    finally:
        mod2 = cast(Any, run_eval)
        mod2.DEFAULT_CONFIG_DIR = old_cfg
        mod2._synonyms_cache = None


def test_synonyms_exclude_broader_terms_even_from_external_lookup(
    monkeypatch,
):
    run_eval = _get_run_eval()
    old_cfg = run_eval.DEFAULT_CONFIG_DIR
    try:
        with tempfile.TemporaryDirectory() as tmp:
            cfg = os.path.join(tmp, "config")
            os.makedirs(cfg, exist_ok=True)
            base_path = os.path.join(cfg, "synonyms.json")
            with open(base_path, "w", encoding="utf-8") as f:
                json.dump(
                    {
                        "parmesan": {
                            "synonyms": ["parmigiano"],
                            "broader_terms": ["käse", "hartkäse"],
                            "narrower_terms": [],
                        }
                    },
                    f,
                    ensure_ascii=False,
                )

            mod = cast(Any, run_eval)
            mod.DEFAULT_CONFIG_DIR = cfg
            mod._synonyms_cache = None
            mod._term_relations_cache = None

            monkeypatch.setattr(
                mod,
                "lookup_openthesaurus_synonyms",
                lambda _term, cap=16: ["käse", "hartkase", "bergkäse", "parmigiano"],
                raising=True,
            )

            syns = mod.get_synonyms("parmesan")
            assert "parmigiano" in syns
            assert "käse" not in syns
            assert "hartkase" not in syns
    finally:
        mod2 = cast(Any, run_eval)
        mod2.DEFAULT_CONFIG_DIR = old_cfg
        mod2._synonyms_cache = None
        mod2._term_relations_cache = None
