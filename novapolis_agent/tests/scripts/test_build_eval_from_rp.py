from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_slugify_and_parsers() -> None:
    from scripts import build_eval_from_rp as mod

    assert mod._slugify(" AeOeUe ss Test ") == "aeoeue-ss-test"
    assert mod._parse_title("---\nstand: x\n---\n# Titel\nText", "fallback") == "Titel"
    assert mod._parse_title("\n\n", "fallback") == "fallback"
    assert mod._parse_lead("# Head\n\nstand: 1\nchecks: ok\nErster Satz\nWeiter") == "Erster Satz"
    assert mod._parse_lead("# Nur Head\n---\nchecks: a\n") == ""


@pytest.mark.scripts
@pytest.mark.unit
def test_build_prompt_variants() -> None:
    from scripts import build_eval_from_rp as mod

    with_lead = mod._build_prompt("Titel", "Kontext")
    without_lead = mod._build_prompt("Titel", "")
    assert "Kontext" in with_lead
    assert "Titel" in with_lead
    assert "Kontext" not in without_lead


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_items_respects_limit_and_record_shape(tmp_path: Path) -> None:
    from scripts import build_eval_from_rp as mod

    (tmp_path / "a.md").write_text("# Alpha\nLead eins", encoding="utf-8")
    (tmp_path / "b.md").write_text("# Beta\nLead zwei", encoding="utf-8")

    items = mod.collect_rp_eval_items(tmp_path, limit=1)
    assert len(items) == 1

    rec = items[0].to_record()
    assert rec["category"] == "rp_eval"
    assert rec["source_package"] == "rp_ssot_builder.v1"
    assert isinstance(rec["messages"], list)
    assert items[0].slug.startswith("rp-")


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_items_stable_slug_for_realistic_paths(tmp_path: Path) -> None:
    from scripts import build_eval_from_rp as mod

    rp = tmp_path / "novapolis-rp" / "database-rp"
    a = rp / "01-factions" / "novapolis" / "02-characters" / "Mara-Quinn.md"
    b = rp / "00-admin" / "Current-State.md"
    a.parent.mkdir(parents=True, exist_ok=True)
    b.parent.mkdir(parents=True, exist_ok=True)

    a.write_text("# Mara Quinn\n\nWichtige Person in Novapolis.\n", encoding="utf-8")
    b.write_text("# Current State\n\nLagebild und Prioritaeten.\n", encoding="utf-8")

    items = mod.collect_rp_eval_items(rp_root=rp, limit=1)
    assert len(items) == 1
    assert items[0].slug.startswith("rp-")
    assert items[0].item_id == items[0].slug


@pytest.mark.scripts
@pytest.mark.unit
def test_write_jsonl_creates_parent_and_outputs_records(tmp_path: Path) -> None:
    from scripts import build_eval_from_rp as mod

    out = tmp_path / "x" / "y" / "out.jsonl"
    rec = {
        "id": "rp-test-1",
        "slug": "rp-test-1",
        "messages": [{"role": "user", "content": "Hallo"}],
        "tags": ["rp"],
    }
    mod.write_jsonl(out, [{"id": "a"}, rec])

    assert out.exists()
    lines = out.read_text(encoding="utf-8").strip().splitlines()
    assert len(lines) == 2
    assert json.loads(lines[0])["id"] == "a"
    assert json.loads(lines[1])["id"] == "rp-test-1"


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_2_when_rp_root_missing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_eval_from_rp as mod

    old_argv = list(sys.argv)
    sys.argv = [
        "build_eval_from_rp.py",
        "--repo-root",
        str(tmp_path),
        "--rp-root",
        "missing",
        "--out",
        "out/data.jsonl",
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
def test_main_success_writes_output(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    from scripts import build_eval_from_rp as mod

    rp_root = tmp_path / "rp"
    rp_root.mkdir(parents=True, exist_ok=True)
    (rp_root / "entry.md").write_text("# Titel\nLead", encoding="utf-8")

    old_argv = list(sys.argv)
    sys.argv = [
        "build_eval_from_rp.py",
        "--repo-root",
        str(tmp_path),
        "--rp-root",
        "rp",
        "--out",
        "out/rp.jsonl",
        "--limit",
        "5",
        "--include-glob",
        "**/*.md",
    ]
    try:
        rc = mod.main()
    finally:
        sys.argv = old_argv

    out = capsys.readouterr().out
    result = tmp_path / "out" / "rp.jsonl"
    assert rc == 0
    assert "[rp-eval-builder] done" in out
    assert result.exists()
    rows = result.read_text(encoding="utf-8").strip().splitlines()
    assert len(rows) == 1
    row = json.loads(rows[0])
    assert row["id"].startswith("rp-")
    assert row["checks"]["must_include"] == ["Titel"]
