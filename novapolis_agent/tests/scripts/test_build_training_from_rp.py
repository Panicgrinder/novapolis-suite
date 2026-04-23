from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_derive_source_kind_and_prompt_variants() -> None:
    from scripts import build_training_from_rp as mod

    assert mod._derive_source_kind("00-admin/Canvas-T0-Timeline.md") == "admin"
    assert mod._derive_source_kind("01-factions/x/02-characters/Mara.md") == "character"
    assert mod._derive_source_kind("01-factions/x/03-locations/Tunnel.md") == "location"
    assert mod._derive_source_kind("01-factions/x/04-inventory/Depot.md") == "inventory"
    assert mod._derive_source_kind("01-factions/x/01-overview.md") == "faction"

    lore_prompt = mod._build_training_prompt("Titel", "Kontext", "character", "lore")
    ops_prompt = mod._build_training_prompt("Titel", "Kontext", "inventory", "ops")
    assert "Chronistin-Vorlage" in lore_prompt
    assert "operative Lage-" in ops_prompt
    assert "Kontext" in lore_prompt
    assert "Erfinde keine neuen Orte" in ops_prompt


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_training_items_record_shape(tmp_path: Path) -> None:
    from scripts import build_training_from_rp as mod

    rp_root = tmp_path / "rp"
    entry = rp_root / "00-admin" / "lage.md"
    entry.parent.mkdir(parents=True, exist_ok=True)
    entry.write_text("# Lagebild\nKnappes Signal", encoding="utf-8")

    items = mod.collect_rp_training_items(rp_root, profile="ops", limit=5)
    assert len(items) == 1
    record = items[0].to_record()
    assert record["category"] == "rp_training_seed"
    assert record["profile"] == "ops"
    assert record["source_kind"] == "admin"
    assert record["promotion_level"] == "rp_ssot_reviewed"
    assert record["license_scope"] == "internal"
    assert isinstance(record["messages"], list)


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_training_items_respects_globs_and_limit(tmp_path: Path) -> None:
    from scripts import build_training_from_rp as mod

    rp_root = tmp_path / "rp"
    admin = rp_root / "00-admin" / "a.md"
    inv = rp_root / "01-factions" / "novapolis" / "04-inventory" / "b.md"
    admin.parent.mkdir(parents=True, exist_ok=True)
    inv.parent.mkdir(parents=True, exist_ok=True)
    admin.write_text("# Alpha\nLead", encoding="utf-8")
    inv.write_text("# Beta\nLead", encoding="utf-8")

    items = mod.collect_rp_training_items(
        rp_root,
        profile="ops",
        limit=1,
        include_globs=["00-admin/**/*.md", "01-factions/**/04-inventory/**/*.md"],
    )
    assert len(items) == 1
    assert items[0].source_file.startswith("00-admin/")


@pytest.mark.scripts
@pytest.mark.unit
def test_write_jsonl_creates_parent_and_outputs_records(tmp_path: Path) -> None:
    from scripts import build_training_from_rp as mod

    out = tmp_path / "x" / "y" / "out.jsonl"
    mod.write_jsonl(out, [{"id": "a"}, {"id": "b", "messages": []}])

    assert out.exists()
    rows = out.read_text(encoding="utf-8").strip().splitlines()
    assert json.loads(rows[0])["id"] == "a"
    assert json.loads(rows[1])["id"] == "b"


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_2_when_rp_root_missing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_training_from_rp as mod

    old_argv = list(sys.argv)
    sys.argv = [
        "build_training_from_rp.py",
        "--repo-root",
        str(tmp_path),
        "--rp-root",
        "missing",
    ]
    try:
        rc = mod.main()
    finally:
        sys.argv = old_argv

    out = capsys.readouterr().out
    assert rc == 2
    assert "rp_root not found" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_main_success_writes_profile_default_output(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_training_from_rp as mod

    rp_root = tmp_path / "rp"
    rp_root.mkdir(parents=True, exist_ok=True)
    (rp_root / "entry.md").write_text("# Titel\nLead", encoding="utf-8")

    old_argv = list(sys.argv)
    sys.argv = [
        "build_training_from_rp.py",
        "--repo-root",
        str(tmp_path),
        "--rp-root",
        "rp",
        "--profile",
        "lore",
        "--limit",
        "5",
    ]
    try:
        rc = mod.main()
    finally:
        sys.argv = old_argv

    out = capsys.readouterr().out
    result = (
        tmp_path / "novapolis_agent" / "eval" / "datasets" / "training" / "rp_lore_train.v1.jsonl"
    )
    assert rc == 0
    assert "[rp-train-builder] done" in out
    assert result.exists()
    row = json.loads(result.read_text(encoding="utf-8").strip().splitlines()[0])
    assert row["id"].startswith("train-rp-lore-")
    assert row["profile"] == "lore"
