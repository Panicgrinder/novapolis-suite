import importlib
import os
import types
from pathlib import Path

import pytest

from app.tools import registry


def make_settings(enabled=True, whitelist=None):
    class S:
        TOOLS_ENABLED = enabled

        TOOLS_WHITELIST = whitelist or []

    return S()


def test_registry_calc_add_and_call_tool(monkeypatch):
    # Ensure tools allowed
    monkeypatch.setattr(registry, "settings", make_settings(True, ["calc_add"]))
    # calc_add is pre-registered in module
    res = registry.call_tool("calc_add", {"a": 2, "b": 3})
    assert res.get("ok") is True
    assert isinstance(res.get("data"), dict)
    assert res["data"]["result"] == pytest.approx(5.0)


def test_time_utils_basic():
    tu = importlib.import_module("novapolis_agent.utils.time_utils")
    assert callable(tu.now_human)
    assert isinstance(tu.now_human(), str)
    assert isinstance(tu.now_compact(), str)
    assert isinstance(tu.now_iso(), str)
    assert isinstance(tu.tz_label(), str)
    assert isinstance(tu.now_human_tz(), str)


def test_models_coerce_messages():
    mm = importlib.import_module("novapolis_agent.app.api.models")
    # dict messages
    req = mm.ChatRequest(messages=[{"role": "user", "content": "Hi"}])
    assert isinstance(req.messages, list)
    # object-like message
    class Obj:
        role = "user"

        content = "hello"


    req2 = mm.ChatRequest(messages=[Obj()])
    assert isinstance(req2.messages, list)
    assert req2.messages[0]["content"] == "hello"


def test_open_latest_summary_find_and_open(tmp_path, monkeypatch):
    mod = importlib.import_module("novapolis_agent.scripts.open_latest_summary")
    d = tmp_path / "summaries"
    d.mkdir(parents=True)
    f1 = d / "summary_ALL_20250101_MIXED.md"
    f2 = d / "summary_ALL_20250201_MIXED.md"
    f1.write_text("old")
    f2.write_text("new")
    latest = mod.find_latest_summary(d)
    assert latest is not None and latest.name.endswith("20250201_MIXED.md")

    # open_file should try webbrowser.open first
    called = {}

    def fake_open(uri):
        called["ok"] = True
        return True


    monkeypatch.setattr("webbrowser.open", fake_open)
    mod.open_file(f2)
    assert called.get("ok", False)


def test_open_context_notes_pick_and_ensure(tmp_path, monkeypatch):
    mod = importlib.import_module("novapolis_agent.scripts.open_context_notes")
    # pick_target prefers existing
    p1 = tmp_path / "a.md"
    p1.write_text("x")
    out = mod.pick_target([str(p1), str(tmp_path / "b.md")])
    assert str(p1) == out

    # ensure_file creates file if missing
    target = tmp_path / "cfg" / "context.local.md"
    path = mod.ensure_file(str(target))
    assert os.path.exists(path)


def test_shim_imports():
    # Ensure package shim modules import without executing heavy side-effects
    names = [
        "novapolis_agent",
        "novapolis_agent.app",
        "novapolis_agent.app.main",
        "novapolis_agent.app.api.api",
    ]
    for n in names:
        m = importlib.import_module(n)
        assert isinstance(m, types.ModuleType)
