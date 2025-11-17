from novapolis_agent.scripts import run_eval as reval


def test_get_term_variants_simple():
    v = reval.get_term_variants("planung")
    # basic expectations: original, no-umlaut variant, and stem
    assert "planung" in v
    assert "plan" in v or "planen" in v


def test_normalize_checks_none():
    assert reval.normalize_checks(None) is None


def test_normalize_checks_expand_and_dedupe():
    out = reval.normalize_checks(["term_inclusion", "foo,bar", "foo"])
    # term_inclusion expands to three checks
    assert "must_include" in out and "keywords_any" in out and "keywords_at_least" in out
    # foo and bar present and no duplicates
    assert any(x == "foo" for x in out)


def test_resolve_profile_overrides_eval():
    t, p, m, eval_mode = reval.resolve_profile_overrides("eval", None, None, None)
    assert eval_mode is True
    assert t == 0.2 and p == 0.1 and m == 128


def test_check_rpg_mode_and_score():
    text = "Novapolis Chronistin\nSzene: Ein kurzer Abschnitt".lower()
    assert reval.check_rpg_mode(text) is True
    score = reval.rpg_style_score(text)
    assert score > 0


def test_normalize_term_for_dedupe_and_compute_hint_terms():
    item = reval.EvaluationItem(
        id="x",
        messages=[],
        checks={
            "must_include": ["Alpha", "beta"],
            "keywords_at_least": {"count": 1, "items": ["gamma"]},
            "keywords_any": ["delta", "alpha"],
        },
    )
    hints = reval.compute_hint_terms(item)
    # must_include terms should come first, normalized lower-case
    assert "alpha" in hints and "beta" in hints
    # dedupe: alpha not duplicated
    assert hints.count("alpha") == 1


def test_inject_eval_hint_idempotent():
    messages = [{"role": "system", "content": "ok"}, {"role": "user", "content": "query"}]
    out = reval.inject_eval_hint(messages, ["a", "b"])
    assert any(m.get("content", "").startswith("Hinweis (Eval):") for m in out)
    # second injection should not duplicate
    out2 = reval.inject_eval_hint(out, ["a", "b"])
    hints = [
        m
        for m in out2
        if m.get("role") == "user" and m.get("content", "").startswith("Hinweis (Eval):")
    ]
    assert len(hints) == 1


def test_check_term_inclusion_uses_variants_and_synonyms(monkeypatch):
    # Stub synonyms to avoid file IO
    monkeypatch.setattr(reval, "get_synonyms", lambda term: [term + "_syn"])
    monkeypatch.setattr(reval, "get_term_variants", lambda t: [t, t + "en", t + "e"])
    text = "Das ist ein test_syn Text mit planen und alpha_syn"
    assert reval.check_term_inclusion(text, "planen") is True
    # synonym match
    assert reval.check_term_inclusion("contains foo_syn", "foo") is True
