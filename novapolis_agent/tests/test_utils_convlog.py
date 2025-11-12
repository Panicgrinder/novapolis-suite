from __future__ import annotations

import datetime as dt
import json

import pytest
from app.utils import convlog


@pytest.mark.unit
def test_create_log_record_includes_optional_fields(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(convlog, "now_iso", lambda: "2025-11-09T04:05:00")
    record = convlog.create_log_record(
        messages=[{"role": "user", "content": "Hallo"}],
        response="Antwort",
        tool_calls=[{"name": "tool", "arguments": {"x": 1}}],
        summary="Kurz",
        labels={"topic": "demo"},
    )
    assert record["timestamp"] == "2025-11-09T04:05:00"
    assert "tool_calls" in record and record["tool_calls"][0]["name"] == "tool"
    assert record["summary"] == "Kurz"
    assert record["labels"] == {"topic": "demo"}


@pytest.mark.unit
def test_log_turn_writes_jsonl(tmp_path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    payload = {"foo": "bar"}

    convlog.log_turn(payload)

    expected_file = tmp_path / "data" / "logs" / f"{dt.date.today().isoformat()}.jsonl"
    assert expected_file.exists()
    content = expected_file.read_text(encoding="utf-8").strip()
    assert json.loads(content) == payload
