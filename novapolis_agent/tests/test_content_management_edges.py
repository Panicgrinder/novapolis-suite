from __future__ import annotations

import builtins
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

from app.core import content_management as cm


def test_basic_content_and_prompt_helpers(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cm, "CONTENT_FILTERING_ENABLED", False)
    assert cm.check_content_allowed("explicit") is True

    monkeypatch.setattr(cm, "CONTENT_FILTERING_ENABLED", True)
    assert cm.check_content_allowed("explicit") is True
    assert cm.check_content_allowed("unknown") is False

    assert "Systemprompt" in cm.modify_prompt_for_freedom("basis")
    unrestricted = cm.create_unrestricted_prompt("crisis")
    assert "crisis" in unrestricted
    assert "Szene:" in unrestricted

    assert cm.split_sentences("A. B?") == ["A.", "B?"]
    assert cm.trim_length("abcdef", 3) == "abc"
    assert cm.trim_length("abcdef", 0) == ""
    assert cm.limit_sentences("A. B. C.", 2) == "A. B."
    assert cm.limit_sentences("A. B.", 0) == ""
    assert cm.compact("A   ,   B  .") == "A, B."


def test_split_sentences_fallback_and_text_cleanup(monkeypatch: pytest.MonkeyPatch) -> None:
    class _Boom:
        def split(self, value: str) -> list[str]:
            raise RuntimeError("boom")

    monkeypatch.setattr(cm, "_SENTENCE_SPLIT_RE", _Boom())
    assert cm.split_sentences("raw") == ["raw"]

    cleaned = cm.neutralize("Ich: Gern! [meta] *wink* Du gehst weiter!!!")
    assert "Ich:" not in cleaned
    assert "Du" not in cleaned


def test_resolve_settings_object_import_paths_and_proxy(monkeypatch: pytest.MonkeyPatch) -> None:
    dummy_settings = SimpleNamespace(VALUE=1)
    monkeypatch.setitem(sys.modules, "app.core.settings", SimpleNamespace(settings=dummy_settings))
    assert cm._resolve_settings_object() is dummy_settings

    monkeypatch.delitem(sys.modules, "app.core.settings", raising=False)
    monkeypatch.delitem(sys.modules, "novapolis_agent.app.core.settings", raising=False)

    real_import = builtins.__import__

    def _fake_import(name: str, globals=None, locals=None, fromlist=(), level: int = 0):
        if name == "app.core.settings":
            raise ImportError("missing")
        if name == "novapolis_agent.app.core.settings":
            return SimpleNamespace(settings=dummy_settings)
        return real_import(name, globals, locals, fromlist, level)

    original_import = builtins.__import__
    builtins.__import__ = _fake_import
    try:
        assert cm._resolve_settings_object() is dummy_settings
    finally:
        builtins.__import__ = original_import

    def _raise_import(*args, **kwargs):
        raise ImportError("missing")

    builtins.__import__ = _raise_import
    try:
        assert cm._resolve_settings_object() is None
    finally:
        builtins.__import__ = original_import

    monkeypatch.setattr(cm, "_resolve_settings_object", lambda: None)
    with pytest.raises(AttributeError):
        cm._SettingsProxy().__getattr__("VALUE")
    with pytest.raises(AttributeError):
        cm._SettingsProxy().__setattr__("VALUE", 2)


def test_policy_file_and_merge_helpers(tmp_path: Path) -> None:
    policy_path = tmp_path / "policy.json"
    policy_path.write_text(json.dumps({"forbidden_terms": ["x"]}), encoding="utf-8")

    assert cm._load_policy_file(str(policy_path)) == {"forbidden_terms": ["x"]}
    assert cm._load_policy_file(str(tmp_path / "missing.json")) == {}
    assert cm._merge_terms(["a", "b"], ["b", "c"]) == ["a", "b", "c"]
    assert cm._merge_rewrite_map({"a": 1}, {"b": 2}) == {"a": "1", "b": "2"}

    class _BadStr:
        def __str__(self) -> str:
            raise RuntimeError("boom")

    assert cm._merge_terms(["a"], [_BadStr(), "b"]) == ["a", "b"]


def test_get_policies_and_bypass_variants(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    policy_path = tmp_path / "profiles.json"
    policy_path.write_text(
        json.dumps(
            {
                "default": {"forbidden_terms": ["bad"], "rewrite_map": {"tea": "coffee"}},
                "profiles": {"eval": {"forbidden_terms": ["evalban"], "rewrite_map": {"foo": "bar"}}},
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(POLICIES_ENABLED=True, POLICY_FILE=str(policy_path), POLICY_STRICT_UNRESTRICTED_BYPASS=True),
    )
    assert cm._get_policies(mode="eval") == {
        "forbidden_terms": ["bad", "evalban"],
        "rewrite_map": {"tea": "coffee", "foo": "bar"},
    }
    assert cm._should_bypass_policies(True) is True

    simple_policy = tmp_path / "simple.json"
    simple_policy.write_text(json.dumps({"rewrite_map": {"x": "y"}}), encoding="utf-8")
    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(POLICIES_ENABLED=True, POLICY_FILE=str(simple_policy), POLICY_STRICT_UNRESTRICTED_BYPASS=True),
    )
    assert cm._get_policies(mode="default") == {"rewrite_map": {"x": "y"}}

    list_policy = tmp_path / "list.json"
    list_policy.write_text("[]", encoding="utf-8")
    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(POLICIES_ENABLED=True, POLICY_FILE=str(list_policy), POLICY_STRICT_UNRESTRICTED_BYPASS=True),
    )
    assert cm._get_policies(mode="default") == {}

    monkeypatch.setattr(cm, "settings", None)
    assert cm._get_policies(mode="default") == {}
    assert cm._should_bypass_policies(False) is False

    monkeypatch.setattr(cm, "settings", SimpleNamespace())
    assert cm._get_policies(mode="default") == {}

    monkeypatch.setattr(cm, "settings", cm._SettingsProxy())

    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(POLICIES_ENABLED=True, POLICY_FILE="", POLICY_STRICT_UNRESTRICTED_BYPASS=True),
    )
    assert cm._get_policies(mode="default") == {}

    weird_policy = tmp_path / "weird.json"
    weird_policy.write_text(json.dumps({"default": [], "profiles": [], "other": 1}), encoding="utf-8")
    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(POLICIES_ENABLED=True, POLICY_FILE=str(weird_policy), POLICY_STRICT_UNRESTRICTED_BYPASS=True),
    )
    assert cm._get_policies(mode="default") == {"forbidden_terms": [], "rewrite_map": {}}

    non_dict_profile = tmp_path / "non_dict_profile.json"
    non_dict_profile.write_text(
        json.dumps({"default": {"forbidden_terms": ["base"]}, "profiles": {"eval": "skip-me"}}),
        encoding="utf-8",
    )
    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(POLICIES_ENABLED=True, POLICY_FILE=str(non_dict_profile), POLICY_STRICT_UNRESTRICTED_BYPASS=True),
    )
    assert cm._get_policies(mode="eval") == {"forbidden_terms": ["base"], "rewrite_map": {}}

    monkeypatch.setattr(cm, "_merge_rewrite_map", lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError("boom")))
    assert cm._get_policies(mode="eval") == {}

    class _BrokenSettings:
        POLICIES_ENABLED = True

        def __getattr__(self, name: str) -> object:
            raise RuntimeError("broken")

    broken_settings = _BrokenSettings()
    monkeypatch.setattr(cm, "settings", broken_settings)
    assert cm._should_bypass_policies(True) is False


def test_apply_pre_and_post_cover_rewrite_block_and_exceptions(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    policy_path = tmp_path / "policy.json"
    policy_path.write_text(
        json.dumps(
            {
                "forbidden_terms": ["bad"],
                "rewrite_map": {"foo": "bar"},
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(
            POLICIES_ENABLED=True,
            POLICY_FILE=str(policy_path),
            POLICY_STRICT_UNRESTRICTED_BYPASS=True,
            EVAL_POST_REWRITE_ENABLED=True,
            EVAL_POST_MAX_SENTENCES="bad-int",
            EVAL_POST_MAX_CHARS="bad-int",
        ),
    )

    assert cm.apply_pre([{"role": "user", "content": "this is bad"}], mode="unrestricted").action == "allow"

    pre_rewrite = cm.apply_pre(
        [{"role": "system", "content": "keep"}, {"role": "user", "content": "foo here"}],
        mode="default",
    )
    assert pre_rewrite.action == "rewrite"
    assert pre_rewrite.messages == [
        {"role": "system", "content": "keep"},
        {"role": "user", "content": "bar here"},
    ]

    pre_block = cm.apply_pre([{"role": "user", "content": "bad idea"}], mode="default")
    assert pre_block.action == "block"

    eval_post = cm.apply_post("Ich: Gern! foo bleibt.", mode="eval")
    assert eval_post.action == "rewrite"
    assert eval_post.reason == "eval_post"

    normal_post = cm.apply_post("foo remains", mode="default")
    assert normal_post.action == "rewrite"
    assert normal_post.text == "bar remains"

    blocked_post = cm.apply_post("this is bad", mode="default")
    assert blocked_post.action == "block"

    monkeypatch.setattr(cm, "_get_policies", lambda **kwargs: (_ for _ in ()).throw(RuntimeError("boom")))
    assert cm.apply_pre([{"role": "user", "content": "x"}], mode="default").action == "allow"
    assert cm.apply_post("x", mode="default").action == "allow"


def test_apply_pre_and_post_cover_disabled_and_eval_passthrough(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(cm, "settings", None)
    assert cm.apply_pre([{"role": "user", "content": "x"}], mode="default").action == "allow"
    assert cm.apply_post("x", mode="default").action == "allow"

    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(
            POLICIES_ENABLED=True,
            POLICY_FILE="",
            POLICY_STRICT_UNRESTRICTED_BYPASS=True,
            EVAL_POST_REWRITE_ENABLED=True,
            EVAL_POST_MAX_SENTENCES=2,
            EVAL_POST_MAX_CHARS=240,
        ),
    )
    monkeypatch.setattr(cm, "_get_policies", lambda **kwargs: {"forbidden_terms": [], "rewrite_map": {}})

    unchanged = cm.apply_post("Sachlich bleiben.", mode="eval")
    assert unchanged.action == "allow"


def test_apply_post_eval_identity_path_continues_into_rules(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        cm,
        "_resolve_settings_object",
        lambda: SimpleNamespace(
            POLICIES_ENABLED=True,
            POLICY_FILE="",
            POLICY_STRICT_UNRESTRICTED_BYPASS=True,
            EVAL_POST_REWRITE_ENABLED=True,
            EVAL_POST_MAX_SENTENCES=2,
            EVAL_POST_MAX_CHARS=240,
        ),
    )
    monkeypatch.setattr(cm, "neutralize", lambda text: text)
    monkeypatch.setattr(cm, "limit_sentences", lambda text, max_sentences: text)
    monkeypatch.setattr(cm, "trim_length", lambda text, max_chars: text)
    monkeypatch.setattr(cm, "compact", lambda text: text)
    monkeypatch.setattr(cm, "_get_policies", lambda **kwargs: {"forbidden_terms": [], "rewrite_map": {}})

    result = cm.apply_post("Unveraendert.", mode="eval")
    assert result.action == "allow"