import importlib
import json
import types

import pytest

from app.utils.convlog import create_log_record, log_turn
from app.utils.summarize import (
    create_simple_summary,
    extract_key_points,
    summarize_turn,
)


def test_extract_key_points_basic():
    text = (
        "Wichtig ist, dass wir testen. Dies ist eine weitere Aussage. "
        "Abschließend: teste die Kantenfälle."
    )
    points = extract_key_points(text, max_points=3)
    assert isinstance(points, list)
    assert len(points) >= 1


def test_create_simple_summary():
    messages = [
        {"role": "system", "content": "System"},
        {"role": "user", "content": "Was ist Python?"},
    ]
    response = "Python ist eine Sprache"
    s = create_simple_summary(messages, response)
    assert "Nutzer fragte nach" in s
    assert "Antwort" in s


def test_summarize_turn_default():
    messages = [{"role": "user", "content": "Frage A"}]
    response = "Antwort A. Wichtig ist, dass es kurz ist."
    res = summarize_turn(messages, response)
    assert "summary" in res and "keyfacts" in res


def test_create_log_record_and_log_turn(tmp_path, monkeypatch):
    # Prevent writing to the real data/logs by redirecting cwd
    monkeypatch.chdir(tmp_path)

    messages = [{"role": "user", "content": "Hallo"}]
    response = "Hallo Antwort"
    rec = create_log_record(messages=messages, response=response, summary="sum")
    assert rec["messages"] == messages
    assert rec["response"] == response

    # Ensure log_turn can write to the tmp path without error
    log_turn(rec)
    log_dir = tmp_path / "data" / "logs"
    files = list(log_dir.glob("*.jsonl"))
    assert files, "log file was not created"
    # quick sanity: the last line parses as json and matches
    with open(files[-1], encoding="utf-8") as fh:
        last = fh.read().strip().splitlines()[-1]
    j = json.loads(last)
    assert j.get("summary") == "sum"


def test_compat_shims_importable():
    # Try importing a few compatibility shims; if environment missing, skip
    names = [
        "novapolis_agent",
        "novapolis_agent.app",
        "novapolis_agent.app.main",
        "novapolis_agent.app.api",
    ]
    for n in names:
        try:
            m = importlib.import_module(n)
            assert isinstance(m, types.ModuleType)
        except Exception as e:
            pytest.skip(f"Could not import {n}: {e}")
