from __future__ import annotations

import asyncio
import importlib
import json
import os
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import pytest


def _load_module():
    return importlib.import_module("scripts.export_finetune")


def _write_results(path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps({"_meta": True}) + "\n")
        f.write(
            json.dumps(
                {
                    "item_id": "item-1",
                    "response": "Antwort",
                    "checks_passed": {"must_include": True},
                    "success": True,
                    "failed_checks": [],
                    "source_file": "eval-01.jsonl",
                    "source_package": "general",
                },
                ensure_ascii=False,
            )
            + "\n"
        )


@pytest.mark.scripts
@pytest.mark.unit
def test_export_finetune_openai_chat_with_patterns(tmp_path: os.PathLike[str]) -> None:
    # Mini Dataset
    dataset = os.path.join(tmp_path, "eval-01.jsonl")
    with open(dataset, "w", encoding="utf-8") as f:
        f.write(
            json.dumps(
                {
                    "id": "item-1",
                    "messages": [{"role": "user", "content": "Sag hallo"}],
                    "source_package": "general",
                },
                ensure_ascii=False,
            )
            + "\n"
        )

    results = os.path.join(tmp_path, "results_20250101_1200.jsonl")
    _write_results(results)

    # Export mit Patterns (nur unser temp dataset) und Format openai_chat
    exporter = _load_module()
    ds_pattern = dataset.replace("\\", "/")
    out = asyncio.run(
        exporter.export_from_results(
            results_path=results,
            out_dir=str(tmp_path),
            format="openai_chat",
            include_failures=False,
            patterns=[ds_pattern],
        )
    )
    assert out.get("ok")
    out_path = str(out.get("out"))
    assert os.path.exists(out_path)
    with open(out_path, encoding="utf-8") as f:
        lines = [json.loads(line) for line in f if line.strip()]
    assert len(lines) == 1
    rec = lines[0]
    assert isinstance(rec.get("messages"), list)
    assert rec.get("meta", {}).get("id") == "item-1"


@pytest.mark.scripts
@pytest.mark.unit
def test_export_finetune_alpaca_includes_failures(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    exporter = _load_module()

    results = tmp_path / "results.jsonl"
    rows = [
        {"item_id": "item-1", "response": "Antwort A", "success": True, "failed_checks": []},
        {"item_id": "item-1", "response": "Antwort B", "success": False, "failed_checks": ["fail"]},
    ]
    results.write_text("\n".join(json.dumps(r) for r in rows), encoding="utf-8")

    async def fake_map(patterns: Any) -> dict[str, Any]:
        item = SimpleNamespace(
            id="item-1",
            messages=[
                {"role": "system", "content": "System Hinweis"},
                {"role": "user", "content": "Instruktion"},
                {"role": "user", "content": "Zusatz"},
            ],
            source_package="pkg-1",
        )
        return {"item-1": item}

    monkeypatch.setattr(exporter, "_load_items_map", fake_map)
    monkeypatch.setattr(exporter, "now_compact", lambda: "20251107_1300")

    out = asyncio.run(
        exporter.export_from_results(
            results_path=str(results),
            out_dir=str(tmp_path),
            format="alpaca",
            include_failures=True,
            patterns=None,
        )
    )

    assert out["ok"] is True
    assert out["count"] == 2
    produced = Path(out["out"])
    payload = [
        json.loads(line)
        for line in produced.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert len(payload) == 2
    record = payload[0]
    assert record["instruction"] == "Instruktion"
    assert "System Hinweis" in record["input"] and "Zusatz" in record["input"]
    assert record["meta"]["package"] == "pkg-1"
    assert payload[1]["meta"]["failed_checks"] == ["fail"]


@pytest.mark.scripts
@pytest.mark.unit
def test_export_finetune_handles_empty_results(tmp_path: Path) -> None:
    exporter = _load_module()

    empty_results = tmp_path / "empty.jsonl"
    empty_results.write_text("\n", encoding="utf-8")

    out = asyncio.run(
        exporter.export_from_results(results_path=str(empty_results), out_dir=str(tmp_path))
    )

    assert out["ok"] is False
    assert out["error"] == "Keine Ergebnisse in Datei"


def test_first_user_message_helper() -> None:
    exporter = _load_module()

    instr, other = exporter._first_user_message(
        [
            {"role": "system", "content": "Init"},
            {"role": "user", "content": "Frage"},
            {"role": "assistant", "content": "Antwort"},
            {"role": "user", "content": "Noch was"},
        ]
    )

    assert instr == "Frage"
    assert "Init" in other and "Antwort" in other and "Noch was" in other
