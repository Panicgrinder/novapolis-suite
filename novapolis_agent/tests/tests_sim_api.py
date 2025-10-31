"""Tests für die Simulations-API."""

import pytest
from httpx import ASGITransport, AsyncClient

from app.api import sim


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
