from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_rp_eval_items_stable_slug_and_limit(tmp_path: Path) -> None:
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
def test_write_jsonl_outputs_records(tmp_path: Path) -> None:
    from scripts import build_eval_from_rp as mod

    out = tmp_path / "novapolis_agent" / "eval" / "datasets" / "rp" / "rp_ssot_core.v1.jsonl"
    rec = {
        "id": "rp-test-1",
        "slug": "rp-test-1",
        "messages": [{"role": "user", "content": "Hallo"}],
        "tags": ["rp"],
    }

    mod.write_jsonl(out, [rec])

    text = out.read_text(encoding="utf-8")
    assert "rp-test-1" in text
    assert text.endswith("\n")
