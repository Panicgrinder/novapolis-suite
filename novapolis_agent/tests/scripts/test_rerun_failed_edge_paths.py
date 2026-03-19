from __future__ import annotations

import importlib
import json
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_load_failed_ids_handles_invalid_records(tmp_path: Path) -> None:
    mod = importlib.import_module("scripts.rerun_failed")
    p = tmp_path / "results.jsonl"
    rows = [
        "",  # empty line
        "{not-json}",
        json.dumps({"id": "", "success": False}),
        json.dumps({"id": "eval-11", "success": True, "failed_checks": "bad-type"}),
        json.dumps({"eval_id": "10", "failed_checks": ["x"]}),
        json.dumps({"item_id": "eval-20", "error": "boom"}),
    ]
    p.write_text("\n".join(rows), encoding="utf-8")

    ids = mod._load_failed_ids(str(p))
    assert "eval-11" not in ids
    assert "10" in ids
    assert "eval-20" in ids


@pytest.mark.scripts
@pytest.mark.unit
def test_load_registry_skips_invalid_json_array_entries(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    mod = importlib.import_module("scripts.rerun_failed")
    ds_dir = tmp_path / "eval" / "datasets"
    ds_dir.mkdir(parents=True)

    # Valid JSONL entry
    (ds_dir / "eval-a.jsonl").write_text(
        json.dumps({"id": "eval-1", "messages": []}) + "\n",
        encoding="utf-8",
    )

    # JSON array with mixed invalid entries
    (ds_dir / "eval-b.json").write_text(
        json.dumps([{"id": "eval-2"}, "skip", 3, {"no_id": True}]),
        encoding="utf-8",
    )

    # Broken JSON should be ignored
    (ds_dir / "eval-c.json").write_text("{broken", encoding="utf-8")

    monkeypatch.setattr(mod, "DATASETS_DIR", str(ds_dir), raising=False)

    reg = mod._load_registry()
    assert "eval-1" in reg
    assert "1" in reg
    assert "eval-2" in reg
    assert "2" in reg
