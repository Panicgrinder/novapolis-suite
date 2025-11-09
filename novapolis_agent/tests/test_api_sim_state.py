from __future__ import annotations

import pytest

from app.api import sim


@pytest.mark.unit
def test_sim_world_state_reset_and_step(monkeypatch: pytest.MonkeyPatch) -> None:
    sim.reset_state()
    monkeypatch.setattr(sim, "_MAX_EVENTS", 3, raising=False)

    initial = sim.get_world_state()
    assert initial.tick == 0
    assert initial.time == 0.0
    assert initial.events == []

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
