from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_slot_consistency_ok_when_sets_match(tmp_path: Path) -> None:
    from scripts import check_sim_epoch_assets as mod

    epoch = tmp_path / "epoch01"
    epoch.mkdir(parents=True)

    (epoch / "world_log.jsonl").write_text(
        '{"slot": 0}\n{"slot": 1}\n{"slot": 2}\n',
        encoding="utf-8",
    )
    (epoch / "pc_log.jsonl").write_text(
        '{"slot": 0}\n{"slot": 1}\n{"slot": 2}\n',
        encoding="utf-8",
    )

    messages = mod.validate_epoch_folder(epoch, check_slot_consistency=True)
    fail_texts = [m.text for m in messages if m.level == "FAIL"]
    assert fail_texts == []
    assert any("slot consistency OK" in m.text for m in messages)


@pytest.mark.scripts
@pytest.mark.unit
def test_slot_consistency_fails_on_mismatch(tmp_path: Path) -> None:
    from scripts import check_sim_epoch_assets as mod

    epoch = tmp_path / "epoch02"
    epoch.mkdir(parents=True)

    (epoch / "world_log.jsonl").write_text(
        '{"slot": 0}\n{"slot": 1}\n',
        encoding="utf-8",
    )
    (epoch / "pc_log.jsonl").write_text(
        '{"slot": 1}\n{"slot": 3}\n',
        encoding="utf-8",
    )

    messages = mod.validate_epoch_folder(epoch, check_slot_consistency=True)
    assert any(m.level == "FAIL" and "slot mismatch world_vs_pc" in m.text for m in messages)


@pytest.mark.scripts
@pytest.mark.unit
def test_slot_consistency_fails_without_detectable_slots(tmp_path: Path) -> None:
    from scripts import check_sim_epoch_assets as mod

    epoch = tmp_path / "epoch03"
    epoch.mkdir(parents=True)

    (epoch / "world_log.jsonl").write_text(
        '{"tick": 1}\n{"tick": 2}\n',
        encoding="utf-8",
    )
    (epoch / "pc_log.jsonl").write_text(
        '{"tick": 1}\n',
        encoding="utf-8",
    )

    messages = mod.validate_epoch_folder(epoch, check_slot_consistency=True)
    assert any(m.level == "FAIL" and "no detectable slot values" in m.text for m in messages)


@pytest.mark.scripts
@pytest.mark.unit
def test_slot_consistency_fails_for_out_of_range_slot(tmp_path: Path) -> None:
    from scripts import check_sim_epoch_assets as mod

    epoch = tmp_path / "epoch04"
    epoch.mkdir(parents=True)

    (epoch / "world_log.jsonl").write_text(
        '{"slot": 0}\n{"slot": 25}\n',
        encoding="utf-8",
    )
    (epoch / "pc_log.jsonl").write_text(
        '{"slot": 0}\n{"slot": 25}\n',
        encoding="utf-8",
    )

    messages = mod.validate_epoch_folder(epoch, check_slot_consistency=True)
    assert any(m.level == "FAIL" and "outside 0..23" in m.text for m in messages)
