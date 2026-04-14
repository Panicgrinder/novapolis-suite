"""Tests für die Simulations-API."""

from pathlib import Path

import pytest
from app.api import sim
from httpx import ASGITransport, AsyncClient


@pytest.fixture(autouse=True)
def reset_world_state():
    """Setzt den Weltzustand vor und nach jedem Test zurück."""

    sim.reset_state()
    yield
    sim.reset_state()


@pytest.mark.asyncio
async def test_get_world_state_initial_values():
    transport = ASGITransport(app=sim.app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/world/state")

    assert response.status_code == 200
    data = response.json()
    assert data["tick"] == 0
    assert data["time"] == 0.0
    assert data["regions"] == {}
    assert data["actors"] == {}
    assert data["events"] == []
    assert data["sim_meta"]["mode"] == "baseline"
    assert data["sim_meta"]["seed"] is None


@pytest.mark.asyncio
async def test_step_world_advances_state():
    transport = ASGITransport(app=sim.app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        first = await client.post("/world/step", json={"dt": 0.25})
        second = await client.post("/world/step", json={"dt": 0.75})

    assert first.status_code == 200
    first_state = first.json()
    assert first_state["tick"] == 1
    assert pytest.approx(first_state["time"], rel=1e-6) == 0.25

    assert second.status_code == 200
    second_state = second.json()
    assert second_state["tick"] == 2
    assert pytest.approx(second_state["time"], rel=1e-6) == 1.0
    assert second_state["events"][-1]["tick"] == 2
    assert second_state["events"][-1]["dt"] == 0.75
    assert second_state["sim_meta"]["mode"] == "baseline"
    assert second_state["sim_meta"]["seed"] is None


@pytest.mark.asyncio
async def test_step_world_rejects_invalid_dt_and_keeps_state():
    transport = ASGITransport(app=sim.app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        invalid_zero = await client.post("/world/step", json={"dt": 0.0})
        invalid_negative = await client.post("/world/step", json={"dt": -0.1})
        invalid_missing = await client.post("/world/step", json={})
        state = await client.get("/world/state")

    assert invalid_zero.status_code == 422
    assert invalid_negative.status_code == 422
    assert invalid_missing.status_code == 422

    stable = state.json()
    assert stable["tick"] == 0
    assert stable["time"] == 0.0
    assert stable["events"] == []


@pytest.mark.asyncio
async def test_step_world_event_cap_enforced(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr(sim, "_MAX_EVENTS", 4, raising=False)
    transport = ASGITransport(app=sim.app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        for _ in range(7):
            response = await client.post("/world/step", json={"dt": 0.1})
            assert response.status_code == 200
        final_state = (await client.get("/world/state")).json()

    assert final_state["tick"] == 7
    assert len(final_state["events"]) == 4
    assert [event["tick"] for event in final_state["events"]] == [4, 5, 6, 7]


@pytest.mark.asyncio
async def test_session_endpoints_persist_and_expose_replay_manifest(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(sim, "_SESSION_STORE_DIR", tmp_path / "sim_sessions", raising=False)
    transport = ASGITransport(app=sim.app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.put(
            "/session/live-alpha",
            json={
                "contract_version": "text_rpg_session_v1",
                "session_status": "active",
                "campaign_id": "campaign-alpha",
                "scene_id": "scene-d5",
                "slot_id": "slot-05",
                "slot_index": 5,
                "turn_id": "turn-0005",
                "seed": 11,
                "turn_context": {
                    "turn_mode": "standard",
                    "turn_window_minutes": 30,
                    "tick_minutes": None,
                    "budget_class": "within_frame",
                },
                "carry_over": [
                    {
                        "task_id": "nordlinie-check",
                        "state": "offen",
                        "resume_hint": "im naechsten Turn pruefen",
                    }
                ],
                "world_log": [{"event": "world-start"}],
                "pc_log": [{"event": "pc-start", "text": "Look around"}],
                "state_patches": [
                    {
                        "scope": "session",
                        "op": "add",
                        "path": "/flags/0",
                        "value": "started",
                    }
                ],
            },
        )
        current = await client.get("/session/live-alpha")
        replay = await client.get("/session/live-alpha/replay")

    assert response.status_code == 200
    saved = response.json()
    assert saved["contract_version"] == "text_rpg_session_v1"
    assert saved["session_status"] == "active"
    assert saved["campaign_id"] == "campaign-alpha"
    assert saved["world_log"][0]["channel"] == "world"
    assert saved["pc_log"][0]["channel"] == "pc"
    assert saved["state_patches"][0]["slot_id"] == "slot-05"
    assert saved["artifact_paths"]["savegame"].endswith("sim_sessions/live-alpha/savegame.json")

    assert current.status_code == 200
    current_payload = current.json()
    assert current_payload["contract_version"] == "text_rpg_session_v1"
    assert current_payload["resume_checkpoint_id"] == "turn-0005"
    assert current_payload["checkpoints"] == ["turn-0005"]
    assert current_payload["turn_context"]["turn_window_minutes"] == 30
    assert current_payload["carry_over"][0]["task_id"] == "nordlinie-check"

    assert replay.status_code == 200
    replay_payload = replay.json()
    assert replay_payload["contract_version"] == "text_rpg_session_v1"
    assert replay_payload["session_status"] == "active"
    assert replay_payload["world_event_count"] == 1
    assert replay_payload["pc_event_count"] == 1
    assert replay_payload["state_patch_count"] == 1
    assert replay_payload["log_channels"] == ["world", "pc", "ally", "sys"]
    assert replay_payload["turn_context"]["budget_class"] == "within_frame"
    assert replay_payload["artifact_paths"]["world_log"].endswith(
        "sim_sessions/live-alpha/world_log.jsonl"
    )


@pytest.mark.asyncio
async def test_session_endpoints_return_404_for_missing_session(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
):
    monkeypatch.setattr(sim, "_SESSION_STORE_DIR", tmp_path / "sim_sessions", raising=False)
    transport = ASGITransport(app=sim.app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        missing_session = await client.get("/session/missing")
        missing_replay = await client.get("/session/missing/replay")

    assert missing_session.status_code == 404
    assert missing_replay.status_code == 404
