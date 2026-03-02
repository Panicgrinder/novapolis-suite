"""Minimalistische Simulations-API für die Novapolis-Welt."""

from threading import Lock
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field


def _empty_events() -> list[dict[str, Any]]:
    return []


def _default_sim_meta() -> dict[str, Any]:
    # Prepared metadata block for future scheduler/replay integration.
    return {
        "mode": "baseline",
        "seed": None,
    }


app = FastAPI(
    title="Novapolis Simulation API",
    description="Leichtgewichtige API für Weltzustand und Zeitschrittsteuerung.",
    version="0.1.0",
)


class WorldState(BaseModel):
    tick: int = 0
    time: float = 0.0
    regions: dict[str, Any] = Field(default_factory=dict)
    actors: dict[str, Any] = Field(default_factory=dict)
    events: list[dict[str, Any]] = Field(default_factory=_empty_events)
    sim_meta: dict[str, Any] = Field(default_factory=_default_sim_meta)


class StepRequest(BaseModel):
    dt: float = Field(..., gt=0.0, description="Zeitschritt in Sekunden, muss > 0 sein")


_state_lock = Lock()
_world_state = WorldState()
_MAX_EVENTS = 20


def _snapshot() -> WorldState:
    return WorldState.model_validate(_world_state.model_dump())


@app.get("/world/state", response_model=WorldState)
def get_world_state() -> WorldState:
    with _state_lock:
        return _snapshot()


@app.post("/world/step", response_model=WorldState)
def step_world(request: StepRequest) -> WorldState:
    with _state_lock:
        _world_state.tick += 1
        _world_state.time = round(_world_state.time + request.dt, 6)
        _world_state.events.append(
            {
                "type": "step",
                "dt": request.dt,
                "tick": _world_state.tick,
            }
        )
        if len(_world_state.events) > _MAX_EVENTS:
            del _world_state.events[:-_MAX_EVENTS]
        return _snapshot()


def reset_state() -> None:
    with _state_lock:
        _world_state.tick = 0
        _world_state.time = 0.0
        _world_state.regions.clear()
        _world_state.actors.clear()
        _world_state.events.clear()
        _world_state.sim_meta = _default_sim_meta()


if __name__ == "__main__":  # pragma: no cover
    import os

    import uvicorn

    port = int(os.getenv("AGENT_PORT", "8765"))
    uvicorn.run("app.api.sim:app", host="127.0.0.1", port=port, reload=True)
