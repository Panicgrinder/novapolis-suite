from pathlib import Path
import sys
import asyncio


# Ensure repository root on path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from novapolis_agent.scripts import run_eval


def test_get_term_variants_basic():
    v = run_eval.get_term_variants("planung")
    assert isinstance(v, list)
    assert "planung" in v
    # expect simple stem
    assert any(s.startswith("plan") for s in v)


def test_normalize_checks_and_resolve_profile():
    n = run_eval.normalize_checks(["term_inclusion", "rpg_style", "term_inclusion"])
    # expansion should include concrete checks and be deduped
    assert "must_include" in n
    assert "keywords_any" in n
    assert "keywords_at_least" in n
    assert "rpg_style" in n

    t, p, m, eval_mode = run_eval.resolve_profile_overrides("eval", None, None, None)
    assert eval_mode is True
    assert t == 0.2
    assert p == 0.1
    assert m == 128


def test_compute_hint_terms_and_inject():
    item = run_eval.EvaluationItem(
        id="e1",
        messages=[{"role": "user", "content": "Hello"}],
        checks={
            "must_include": ["Alpha", "Beta"],
            "keywords_any": ["Gamma"],
            "keywords_at_least": {"count": 1, "items": ["Delta"]},
        },
    )

    hints = run_eval.compute_hint_terms(item, None, cap=6)
    # terms normalized to lowercase
    assert "alpha" in hints or "beta" in hints

    messages = [{"role": "user", "content": "first"}, {"role": "assistant", "content": "ok"}]
    injected = run_eval.inject_eval_hint(messages, ["a", "b"])
    assert any(m.get("content", "").startswith("Hinweis (Eval):") for m in injected)


def test_check_term_inclusion_with_synonyms(monkeypatch):
    # monkeypatch synonyms loader to return a known mapping
    monkeypatch.setattr(run_eval, "get_synonyms", lambda term: ["synonymx"])
    text = "this text contains synonymx somewhere"
    # with the monkeypatched synonym mapping, searching for 'anything' should match 'synonymx'
    assert run_eval.check_term_inclusion(text, "anything") is True
    assert run_eval.check_term_inclusion(text, "synonymx") is True


def test_rpg_mode_and_score():
    txt = "Novapolis Chronistin erzählt eine Szene."
    assert run_eval.check_rpg_mode(txt) is True
    s = run_eval.rpg_style_score(txt)
    assert s > 0
