from __future__ import annotations

import pytest
from app.api import sim
from pydantic import ValidationError


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
