from __future__ import annotations

import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from novapolis_agent.app.api import sim


@pytest.mark.unit
def test_sim_world_state_reset_and_step(monkeypatch: pytest.MonkeyPatch) -> None:
    sim.reset_state()
    monkeypatch.setattr(sim, "_MAX_EVENTS", 3, raising=False)

    initial = sim.get_world_state()
    assert initial.tick == 0
    assert initial.time == 0.0
    assert initial.events == []
    assert initial.sim_meta["mode"] == "baseline"
    assert initial.sim_meta["seed"] is None

    sim.step_world(sim.StepRequest(dt=0.5))
    sim.step_world(sim.StepRequest(dt=0.25))
    latest = sim.step_world(sim.StepRequest(dt=0.75))
    assert latest.tick == 3
    assert latest.time == 1.5
    assert len(latest.events) == 3

    final = sim.step_world(sim.StepRequest(dt=0.1))
    assert final.tick == 4
    assert pytest.approx(final.time, rel=1e-6) == 1.6
    assert len(final.events) == 3  # capped by patched _MAX_EVENTS
    assert all(event["type"] == "step" for event in final.events)


@pytest.mark.unit
def test_sim_reset_clears_state() -> None:
    sim.step_world(sim.StepRequest(dt=0.3))
    sim.reset_state()
    cleared = sim.get_world_state()
    assert cleared.tick == 0
    assert cleared.time == 0.0
    assert cleared.events == []
    assert cleared.regions == {}
    assert cleared.actors == {}
    assert cleared.sim_meta["mode"] == "baseline"
    assert cleared.sim_meta["seed"] is None


@pytest.mark.unit
def test_sim_event_cap_drops_oldest_entries(monkeypatch: pytest.MonkeyPatch) -> None:
    sim.reset_state()
    monkeypatch.setattr(sim, "_MAX_EVENTS", 5, raising=False)

    for _ in range(8):
        sim.step_world(sim.StepRequest(dt=0.1))

    state = sim.get_world_state()
    assert state.tick == 8
    assert len(state.events) == 5
    assert [event["tick"] for event in state.events] == [4, 5, 6, 7, 8]


@pytest.mark.unit
def test_sim_step_rejects_invalid_dt_and_keeps_state() -> None:
    sim.reset_state()
    before = sim.get_world_state()

    with pytest.raises(ValidationError):
        sim.StepRequest(dt=0.0)
    with pytest.raises(ValidationError):
        sim.StepRequest(dt=-0.5)

    after = sim.get_world_state()
    assert after.tick == before.tick
    assert after.time == before.time
    assert after.events == before.events


@pytest.mark.unit
def test_sim_reset_restores_invariants_after_mutation() -> None:
    sim.reset_state()
    with sim._state_lock:
        sim._world_state.tick = 9
        sim._world_state.time = 12.34
        sim._world_state.regions["alpha"] = {"status": "dirty"}
        sim._world_state.actors["npc_1"] = {"mood": "alert"}
        sim._world_state.events.append({"type": "custom", "tick": 9})
        sim._world_state.sim_meta = {"mode": "custom", "seed": 42}

    sim.reset_state()
    cleared = sim.get_world_state()
    assert cleared.tick == 0
    assert cleared.time == 0.0
    assert cleared.regions == {}
    assert cleared.actors == {}
    assert cleared.events == []
    assert cleared.sim_meta == {"mode": "baseline", "seed": None}


@pytest.mark.unit
def test_sim_session_persistence_writes_expected_artifacts(tmp_path: Path) -> None:
    sim.reset_state()
    original_store_dir = sim._SESSION_STORE_DIR
    sim._SESSION_STORE_DIR = tmp_path / "sim_sessions"
    try:
        record = sim.upsert_session(
            "campaign-alpha",
            sim.SessionUpsertRequest(
                campaign_id="campaign-alpha",
                scene_id="scene-d5",
                slot_id="slot-03",
                slot_index=3,
                turn_id="turn-0003",
                seed=7,
                turn_context=sim.TurnContext(
                    turn_mode="dense",
                    turn_window_minutes=30,
                    tick_minutes=1,
                    budget_class="slightly_over",
                ),
                carry_over=[
                    sim.CarryOverItem(
                        task_id="repair-valve",
                        state="begonnen",
                        resume_hint="Werkzeug liegt bereit",
                        prepared_assets=["Werkzeug", "offener Zugang"],
                    )
                ],
                world_log=[{"event": "world-step"}],
                pc_log=[{"event": "pc-choice", "text": "Investigate D5"}],
                state_patches=[
                    sim.StatePatchRecord(
                        scope="session",
                        op="replace",
                        path="/scene_id",
                        value="scene-d5",
                    )
                ],
            ),
        )

        session_dir = tmp_path / "sim_sessions" / "campaign-alpha"
        assert session_dir.exists()
        assert (session_dir / "savegame.json").exists()
        assert (session_dir / "world_log.jsonl").exists()
        assert (session_dir / "pc_log.jsonl").exists()
        assert (session_dir / "replay_manifest.json").exists()
        assert record.resume_checkpoint_id == "turn-0003"
        assert record.contract_version == "text_rpg_session_v1"
        assert record.session_status == "active"
        assert record.seed == 7
        assert record.log_channels == ["world", "pc", "ally", "sys"]
        assert record.turn_context.turn_mode == "dense"
        assert record.turn_context.tick_minutes == 1
        assert record.carry_over[0].task_id == "repair-valve"
        assert record.world_log[0]["channel"] == "world"
        assert record.pc_log[0]["channel"] == "pc"
        assert record.state_patches[0].session_id == "campaign-alpha"
        assert record.state_patches[0].slot_id == "slot-03"
        assert record.state_patches[0].turn_id == "turn-0003"

        savegame_payload = json.loads((session_dir / "savegame.json").read_text(encoding="utf-8"))
        replay_payload = json.loads(
            (session_dir / "replay_manifest.json").read_text(encoding="utf-8")
        )
        assert savegame_payload["contract_version"] == "text_rpg_session_v1"
        assert savegame_payload["session_status"] == "active"
        assert savegame_payload["campaign_id"] == "campaign-alpha"
        assert savegame_payload["scene_id"] == "scene-d5"
        assert savegame_payload["slot_index"] == 3
        assert savegame_payload["seed"] == 7
        assert savegame_payload["turn_context"] == {
            "turn_mode": "dense",
            "turn_window_minutes": 30,
            "tick_minutes": 1,
            "budget_class": "slightly_over",
        }
        assert savegame_payload["carry_over"] == [
            {
                "task_id": "repair-valve",
                "state": "begonnen",
                "resume_hint": "Werkzeug liegt bereit",
                "prepared_assets": ["Werkzeug", "offener Zugang"],
            }
        ]
        assert savegame_payload["state_patches"] == [
            {
                "patch_id": None,
                "scope": "session",
                "op": "replace",
                "path": "/scene_id",
                "value": "scene-d5",
                "visibility": "pc_visible",
                "evidence_refs": [],
                "replay_epoch_id": None,
                "session_id": "campaign-alpha",
                "campaign_id": "campaign-alpha",
                "scene_id": "scene-d5",
                "slot_id": "slot-03",
                "slot_index": 3,
                "turn_id": "turn-0003",
                "tick": 0,
                "time": 0.0,
                "timestamp": savegame_payload["updated_at"],
            }
        ]
        assert replay_payload["contract_version"] == "text_rpg_session_v1"
        assert replay_payload["session_status"] == "active"
        assert replay_payload["log_channels"] == ["world", "pc", "ally", "sys"]
        assert replay_payload["turn_context"]["turn_mode"] == "dense"
        assert replay_payload["carry_over"][0]["task_id"] == "repair-valve"
    finally:
        sim._SESSION_STORE_DIR = original_store_dir


@pytest.mark.unit
def test_sim_session_reload_merges_existing_logs(tmp_path: Path) -> None:
    sim.reset_state()
    original_store_dir = sim._SESSION_STORE_DIR
    sim._SESSION_STORE_DIR = tmp_path / "sim_sessions"
    try:
        sim.upsert_session(
            "session-beta",
            sim.SessionUpsertRequest(
                slot_index=4,
                world_log=[{"event": "tick-start"}],
            ),
        )
        second = sim.upsert_session(
            "session-beta",
            sim.SessionUpsertRequest(
                turn_id="turn-0002",
                pc_log=[{"event": "player-choice"}],
            ),
        )

        reloaded = sim.get_session("session-beta")
        assert len(reloaded.world_log) == 1
        assert len(reloaded.pc_log) == 1
        assert second.resume_checkpoint_id == "turn-0002"
        assert reloaded.checkpoints[0] == "tick-0000"
        assert reloaded.checkpoints[-1] == "turn-0002"
    finally:
        sim._SESSION_STORE_DIR = original_store_dir


@pytest.mark.unit
def test_sim_session_accepts_handover_slot_index_above_23(tmp_path: Path) -> None:
    sim.reset_state()
    original_store_dir = sim._SESSION_STORE_DIR
    sim._SESSION_STORE_DIR = tmp_path / "sim_sessions"
    try:
        record = sim.upsert_session(
            "session-handover",
            sim.SessionUpsertRequest(
                campaign_id="campaign-handover",
                scene_id="scene-slot40-anchor",
                slot_id="slot-40",
                slot_index=40,
                turn_id="turn-0018",
                carry_over=[
                    sim.CarryOverItem(
                        task_id="follow-anchor",
                        state="offen",
                        resume_hint="folgeanker-halten",
                    )
                ],
                world_log=[{"event": "follow-anchor-fixed"}],
                pc_log=[{"event": "player-choice", "text": "Hold the anchor"}],
            ),
        )

        reloaded = sim.get_session("session-handover")
        assert record.slot_index == 40
        assert record.slot_id == "slot-40"
        assert record.resume_checkpoint_id == "turn-0018"
        assert reloaded.slot_index == 40
        assert reloaded.checkpoints[-1] == "turn-0018"
    finally:
        sim._SESSION_STORE_DIR = original_store_dir
