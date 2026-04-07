"""Minimalistische Simulations-API fuer die Novapolis-Welt."""

from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path
from threading import Lock
from typing import Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


def _empty_events() -> list[dict[str, Any]]:
    return []


def _default_sim_meta() -> dict[str, Any]:
    # Prepared metadata block for future scheduler/replay integration.
    return {
        "mode": "baseline",
        "seed": None,
    }


def _empty_dict() -> dict[str, str]:
    return {}


def _empty_strings() -> list[str]:
    return []


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


class SessionUpsertRequest(BaseModel):
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    slot_index: int | None = Field(default=None, ge=0, le=23)
    turn_id: str | None = None
    seed: int | None = None
    world_state: WorldState | None = None
    state_patches: list[dict[str, Any]] = Field(default_factory=_empty_events)
    world_log: list[dict[str, Any]] = Field(default_factory=_empty_events)
    pc_log: list[dict[str, Any]] = Field(default_factory=_empty_events)


class SessionRecord(BaseModel):
    session_id: str
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    slot_index: int | None = None
    turn_id: str | None = None
    seed: int | None = None
    created_at: str
    updated_at: str
    resume_checkpoint_id: str | None = None
    checkpoints: list[str] = Field(default_factory=_empty_strings)
    artifact_paths: dict[str, str] = Field(default_factory=_empty_dict)
    world_state: WorldState
    state_patches: list[dict[str, Any]] = Field(default_factory=_empty_events)
    world_log: list[dict[str, Any]] = Field(default_factory=_empty_events)
    pc_log: list[dict[str, Any]] = Field(default_factory=_empty_events)


class ReplayManifest(BaseModel):
    session_id: str
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    slot_index: int | None = None
    turn_id: str | None = None
    seed: int | None = None
    resume_checkpoint_id: str | None = None
    checkpoints: list[str] = Field(default_factory=_empty_strings)
    artifact_paths: dict[str, str] = Field(default_factory=_empty_dict)
    world_event_count: int = 0
    pc_event_count: int = 0
    state_patch_count: int = 0
    updated_at: str


_state_lock = Lock()
_world_state = WorldState()
_MAX_EVENTS = 20
_MODULE_ROOT = Path(__file__).resolve().parents[2]
_SESSION_STORE_DIR = _MODULE_ROOT / "tmp" / "sim_sessions"
_SESSION_ID_SANITIZER = re.compile(r"[^A-Za-z0-9._-]+")


def _snapshot() -> WorldState:
    return WorldState.model_validate(_world_state.model_dump())


def _now_iso() -> str:
    return datetime.now(UTC).isoformat()


def _sanitize_session_id(session_id: str) -> str:
    clean = _SESSION_ID_SANITIZER.sub("_", session_id.strip())
    clean = clean.strip("._-")
    return clean or "session"


def _session_dir(session_id: str) -> Path:
    return _SESSION_STORE_DIR / _sanitize_session_id(session_id)


def _savegame_path(session_id: str) -> Path:
    return _session_dir(session_id) / "savegame.json"


def _world_log_path(session_id: str) -> Path:
    return _session_dir(session_id) / "world_log.jsonl"


def _pc_log_path(session_id: str) -> Path:
    return _session_dir(session_id) / "pc_log.jsonl"


def _replay_manifest_path(session_id: str) -> Path:
    return _session_dir(session_id) / "replay_manifest.json"


def _artifact_paths(session_id: str) -> dict[str, str]:
    session_paths = {
        "savegame": _savegame_path(session_id),
        "world_log": _world_log_path(session_id),
        "pc_log": _pc_log_path(session_id),
        "replay_manifest": _replay_manifest_path(session_id),
    }
    artifact_paths: dict[str, str] = {}
    for key, path in session_paths.items():
        try:
            artifact_paths[key] = path.relative_to(_MODULE_ROOT).as_posix()
        except ValueError:
            artifact_paths[key] = path.as_posix()
    return artifact_paths


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def _write_jsonl(path: Path, entries: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not entries:
        path.write_text("", encoding="utf-8")
        return
    lines = [json.dumps(entry) for entry in entries]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    entries: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        clean_line = line.strip()
        if not clean_line:
            continue
        parsed = json.loads(clean_line)
        if isinstance(parsed, dict):
            entries.append(parsed)
    return entries


def _default_session_record(session_id: str) -> SessionRecord:
    now = _now_iso()
    return SessionRecord(
        session_id=session_id,
        created_at=now,
        updated_at=now,
        artifact_paths=_artifact_paths(session_id),
        world_state=_snapshot(),
    )


def _checkpoint_id(world_state: WorldState, turn_id: str | None) -> str:
    if turn_id:
        return turn_id
    return f"tick-{world_state.tick:04d}"


def _normalize_log_entries(
    entries: list[dict[str, Any]],
    *,
    channel: str,
    session_id: str,
    campaign_id: str | None,
    scene_id: str | None,
    slot_id: str | None,
    slot_index: int | None,
    turn_id: str | None,
    world_state: WorldState,
    timestamp: str,
) -> list[dict[str, Any]]:
    normalized_entries: list[dict[str, Any]] = []
    for raw_entry in entries:
        entry = dict(raw_entry)
        entry.setdefault("channel", channel)
        entry.setdefault("session_id", session_id)
        if campaign_id:
            entry.setdefault("campaign_id", campaign_id)
        if scene_id:
            entry.setdefault("scene_id", scene_id)
        if slot_id:
            entry.setdefault("slot_id", slot_id)
        if slot_index is not None:
            entry.setdefault("slot_index", slot_index)
        if turn_id:
            entry.setdefault("turn_id", turn_id)
        entry.setdefault("tick", world_state.tick)
        entry.setdefault("time", world_state.time)
        entry.setdefault("timestamp", timestamp)
        normalized_entries.append(entry)
    return normalized_entries


def _session_payload(record: SessionRecord) -> dict[str, Any]:
    payload = record.model_dump()
    payload.pop("world_log", None)
    payload.pop("pc_log", None)
    payload.pop("artifact_paths", None)
    return payload


def _build_replay_manifest(record: SessionRecord) -> ReplayManifest:
    return ReplayManifest(
        session_id=record.session_id,
        campaign_id=record.campaign_id,
        scene_id=record.scene_id,
        slot_id=record.slot_id,
        slot_index=record.slot_index,
        turn_id=record.turn_id,
        seed=record.seed,
        resume_checkpoint_id=record.resume_checkpoint_id,
        checkpoints=list(record.checkpoints),
        artifact_paths=dict(record.artifact_paths),
        world_event_count=len(record.world_log),
        pc_event_count=len(record.pc_log),
        state_patch_count=len(record.state_patches),
        updated_at=record.updated_at,
    )


def _persist_session(record: SessionRecord) -> None:
    _write_json(_savegame_path(record.session_id), _session_payload(record))
    _write_jsonl(_world_log_path(record.session_id), record.world_log)
    _write_jsonl(_pc_log_path(record.session_id), record.pc_log)
    replay_manifest = _build_replay_manifest(record)
    _write_json(_replay_manifest_path(record.session_id), replay_manifest.model_dump())


def _load_session(session_id: str) -> SessionRecord | None:
    savegame_path = _savegame_path(session_id)
    if not savegame_path.exists():
        return None

    payload = json.loads(savegame_path.read_text(encoding="utf-8"))
    payload["artifact_paths"] = _artifact_paths(session_id)
    payload["world_log"] = _load_jsonl(_world_log_path(session_id))
    payload["pc_log"] = _load_jsonl(_pc_log_path(session_id))
    return SessionRecord.model_validate(payload)


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


@app.put("/session/{session_id}", response_model=SessionRecord)
def upsert_session(session_id: str, request: SessionUpsertRequest) -> SessionRecord:
    with _state_lock:
        record = _load_session(session_id) or _default_session_record(session_id)

        if request.campaign_id is not None:
            record.campaign_id = request.campaign_id
        if request.scene_id is not None:
            record.scene_id = request.scene_id
        if request.slot_id is not None:
            record.slot_id = request.slot_id
        if request.slot_index is not None:
            record.slot_index = request.slot_index
        if request.turn_id is not None:
            record.turn_id = request.turn_id
        if request.seed is not None:
            record.seed = request.seed

        if request.world_state is not None:
            record.world_state = request.world_state

        if request.seed is not None:
            record.world_state.sim_meta = {
                **record.world_state.sim_meta,
                "seed": request.seed,
            }

        record.updated_at = _now_iso()
        record.resume_checkpoint_id = _checkpoint_id(record.world_state, record.turn_id)
        if record.resume_checkpoint_id not in record.checkpoints:
            record.checkpoints.append(record.resume_checkpoint_id)

        record.world_log.extend(
            _normalize_log_entries(
                request.world_log,
                channel="world",
                session_id=record.session_id,
                campaign_id=record.campaign_id,
                scene_id=record.scene_id,
                slot_id=record.slot_id,
                slot_index=record.slot_index,
                turn_id=record.turn_id,
                world_state=record.world_state,
                timestamp=record.updated_at,
            )
        )
        record.pc_log.extend(
            _normalize_log_entries(
                request.pc_log,
                channel="pc",
                session_id=record.session_id,
                campaign_id=record.campaign_id,
                scene_id=record.scene_id,
                slot_id=record.slot_id,
                slot_index=record.slot_index,
                turn_id=record.turn_id,
                world_state=record.world_state,
                timestamp=record.updated_at,
            )
        )
        record.state_patches.extend(request.state_patches)
        record.artifact_paths = _artifact_paths(session_id)

        _persist_session(record)
        return record


@app.get("/session/{session_id}", response_model=SessionRecord)
def get_session(session_id: str) -> SessionRecord:
    with _state_lock:
        record = _load_session(session_id)
        if record is None:
            raise HTTPException(status_code=404, detail="session not found")
        return record


@app.get("/session/{session_id}/replay", response_model=ReplayManifest)
def get_session_replay(session_id: str) -> ReplayManifest:
    with _state_lock:
        record = _load_session(session_id)
        if record is None:
            raise HTTPException(status_code=404, detail="session not found")
        replay_manifest_path = _replay_manifest_path(session_id)
        if replay_manifest_path.exists():
            payload = json.loads(replay_manifest_path.read_text(encoding="utf-8"))
            return ReplayManifest.model_validate(payload)
        return _build_replay_manifest(record)


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
