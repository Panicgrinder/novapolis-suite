"""Minimalistische Simulations-API für die Novapolis-Welt."""

from threading import Lock
from typing import Any, Dict, List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="Novapolis Simulation API",
    description="Leichtgewichtige API für Weltzustand und Zeitschrittsteuerung.",
    version="0.1.0",
)


class WorldState(BaseModel):
    """Gemeinsamer Zustand der Simulationswelt."""

    tick: int = 0
    time: float = 0.0
    regions: Dict[str, Any] = Field(default_factory=dict)
    actors: Dict[str, Any] = Field(default_factory=dict)
    events: List[Dict[str, Any]] = Field(default_factory=list)


class StepRequest(BaseModel):
    """Eingabe für einen Zeitschritt."""

    dt: float = Field(..., gt=0.0, description="Zeitschritt in Sekunden, muss > 0 sein")


_state_lock = Lock()
_world_state = WorldState()
_MAX_EVENTS = 20


def _snapshot() -> WorldState:
    """Gibt eine kopierte Repräsentation des Weltzustands zurück."""

    return WorldState.model_validate(_world_state.model_dump())


@app.get("/world/state", response_model=WorldState)
def get_world_state() -> WorldState:
    """Liefert den aktuellen Weltzustand."""

    with _state_lock:
        return _snapshot()


@app.post("/world/step", response_model=WorldState)
def step_world(request: StepRequest) -> WorldState:
    """Inkrementiert Tick und Zeit anhand des übergebenen Zeitschritts."""

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
    """Setzt den Weltzustand zurück (primär für Tests)."""

    with _state_lock:
        _world_state.tick = 0
        _world_state.time = 0.0
        _world_state.regions.clear()
        _world_state.actors.clear()
        _world_state.events.clear()


if __name__ == "__main__":  # pragma: no cover - Helfer für manuelle Starts
    import os

    port = int(os.getenv("AGENT_PORT", "8765"))
    uvicorn.run("app.api.sim:app", host="127.0.0.1", port=port, reload=True)
