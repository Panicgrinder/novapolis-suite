"""Minimalistische Simulations-API fuer die Novapolis-Welt."""

from __future__ import annotations

import json
import re
from datetime import UTC, datetime
from pathlib import Path
from threading import Lock
from typing import Any, cast

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from .models import (
    TEXT_RPG_DEFAULT_TURN_WINDOW_MINUTES,
    TEXT_RPG_LOG_CHANNELS,
    TEXT_RPG_SESSION_CONTRACT_VERSION,
    CarryOverItem,
    TurnContext,
)


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


def _default_log_channels() -> list[str]:
    return list(TEXT_RPG_LOG_CHANNELS)


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


class StatePatchRecord(BaseModel):
    patch_id: str | None = None
    scope: str = Field(..., min_length=1)
    op: str = Field(..., min_length=1)
    path: str = Field(..., min_length=1)
    value: Any = None
    visibility: str = "pc_visible"
    evidence_refs: list[str] = Field(default_factory=_empty_strings)
    replay_epoch_id: str | None = None
    session_id: str | None = None
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    slot_index: int | None = None
    turn_id: str | None = None
    tick: int | None = None
    time: float | None = None
    timestamp: str | None = None


def _empty_state_patches() -> list[StatePatchRecord]:
    return []


def _empty_carry_over() -> list[CarryOverItem]:
    return []


def _default_turn_context() -> TurnContext:
    return TurnContext(turn_window_minutes=TEXT_RPG_DEFAULT_TURN_WINDOW_MINUTES)


class SessionUpsertRequest(BaseModel):
    contract_version: str = TEXT_RPG_SESSION_CONTRACT_VERSION
    session_status: str = "active"
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    slot_index: int | None = Field(default=None, ge=0, le=23)
    turn_id: str | None = None
    seed: int | None = None
    turn_context: TurnContext | None = None
    carry_over: list[CarryOverItem] | None = None
    world_state: WorldState | None = None
    state_patches: list[StatePatchRecord] = Field(default_factory=_empty_state_patches)
    world_log: list[dict[str, Any]] = Field(default_factory=_empty_events)
    pc_log: list[dict[str, Any]] = Field(default_factory=_empty_events)


class SessionRecord(BaseModel):
    contract_version: str = TEXT_RPG_SESSION_CONTRACT_VERSION
    session_id: str
    session_status: str = "active"
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
    log_channels: list[str] = Field(default_factory=_default_log_channels)
    artifact_paths: dict[str, str] = Field(default_factory=_empty_dict)
    turn_context: TurnContext = Field(default_factory=_default_turn_context)
    carry_over: list[CarryOverItem] = Field(default_factory=_empty_carry_over)
    world_state: WorldState
    state_patches: list[StatePatchRecord] = Field(default_factory=_empty_state_patches)
    world_log: list[dict[str, Any]] = Field(default_factory=_empty_events)
    pc_log: list[dict[str, Any]] = Field(default_factory=_empty_events)


class ReplayManifest(BaseModel):
    contract_version: str = TEXT_RPG_SESSION_CONTRACT_VERSION
    session_id: str
    session_status: str = "active"
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    slot_index: int | None = None
    turn_id: str | None = None
    seed: int | None = None
    resume_checkpoint_id: str | None = None
    checkpoints: list[str] = Field(default_factory=_empty_strings)
    log_channels: list[str] = Field(default_factory=_default_log_channels)
    artifact_paths: dict[str, str] = Field(default_factory=_empty_dict)
    turn_context: TurnContext = Field(default_factory=_default_turn_context)
    carry_over: list[CarryOverItem] = Field(default_factory=_empty_carry_over)
    world_event_count: int = 0
    pc_event_count: int = 0
    state_patch_count: int = 0
    updated_at: str


class TtsArtifactRecord(BaseModel):
    contract_version: str = TEXT_RPG_SESSION_CONTRACT_VERSION
    session_id: str
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    slot_index: int | None = None
    turn_id: str | None = None
    channel: str = "pc"
    provider: str
    voice: str
    output_format: str
    mime_type: str
    request_hash: str
    cache_key: str | None = None
    cache_hit: bool = False
    artifact_path: str | None = None
    is_placeholder: bool = True
    detail: str = ""
    timestamp: str | None = None


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


def _tts_manifest_path(session_id: str) -> Path:
    return _session_dir(session_id) / "tts_manifest.jsonl"


def _artifact_paths(session_id: str) -> dict[str, str]:
    session_paths = {
        "savegame": _savegame_path(session_id),
        "world_log": _world_log_path(session_id),
        "pc_log": _pc_log_path(session_id),
        "replay_manifest": _replay_manifest_path(session_id),
    }
    tts_manifest_path = _tts_manifest_path(session_id)
    if tts_manifest_path.exists():
        session_paths["tts_manifest"] = tts_manifest_path
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
            parsed_obj = cast(dict[object, Any], parsed)
            entries.append({str(key): value for key, value in parsed_obj.items()})
    return entries


def _default_session_record(session_id: str) -> SessionRecord:
    now = _now_iso()
    return SessionRecord(
        session_id=session_id,
        created_at=now,
        updated_at=now,
        log_channels=_default_log_channels(),
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


def _normalize_state_patches(
    entries: list[StatePatchRecord],
    *,
    session_id: str,
    campaign_id: str | None,
    scene_id: str | None,
    slot_id: str | None,
    slot_index: int | None,
    turn_id: str | None,
    world_state: WorldState,
    timestamp: str,
) -> list[StatePatchRecord]:
    normalized_entries: list[StatePatchRecord] = []
    for raw_patch in entries:
        patch = raw_patch.model_dump()
        if not patch.get("session_id"):
            patch["session_id"] = session_id
        if campaign_id:
            if not patch.get("campaign_id"):
                patch["campaign_id"] = campaign_id
        if scene_id:
            if not patch.get("scene_id"):
                patch["scene_id"] = scene_id
        if slot_id:
            if not patch.get("slot_id"):
                patch["slot_id"] = slot_id
        if slot_index is not None:
            if patch.get("slot_index") is None:
                patch["slot_index"] = slot_index
        if turn_id:
            if not patch.get("turn_id"):
                patch["turn_id"] = turn_id
        if patch.get("tick") is None:
            patch["tick"] = world_state.tick
        if patch.get("time") is None:
            patch["time"] = world_state.time
        if not patch.get("timestamp"):
            patch["timestamp"] = timestamp
        normalized_entries.append(StatePatchRecord.model_validate(patch))
    return normalized_entries


def _validate_contract_version(contract_version: str) -> None:
    if contract_version != TEXT_RPG_SESSION_CONTRACT_VERSION:
        raise HTTPException(status_code=400, detail="unsupported contract_version")


def _validate_session_status(session_status: str) -> None:
    if session_status not in {"created", "active", "paused", "completed", "aborted"}:
        raise HTTPException(status_code=400, detail="unsupported session_status")


def _validate_log_channel(channel: str) -> None:
    if channel not in TEXT_RPG_LOG_CHANNELS:
        raise HTTPException(status_code=400, detail="unsupported log channel")


def _session_payload(record: SessionRecord) -> dict[str, Any]:
    payload = record.model_dump()
    payload.pop("world_log", None)
    payload.pop("pc_log", None)
    payload.pop("artifact_paths", None)
    return payload


def _build_replay_manifest(record: SessionRecord) -> ReplayManifest:
    return ReplayManifest(
        contract_version=record.contract_version,
        session_id=record.session_id,
        session_status=record.session_status,
        campaign_id=record.campaign_id,
        scene_id=record.scene_id,
        slot_id=record.slot_id,
        slot_index=record.slot_index,
        turn_id=record.turn_id,
        seed=record.seed,
        resume_checkpoint_id=record.resume_checkpoint_id,
        checkpoints=list(record.checkpoints),
        log_channels=list(record.log_channels),
        artifact_paths=dict(record.artifact_paths),
        turn_context=record.turn_context,
        carry_over=list(record.carry_over),
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


def load_session_record(session_id: str) -> SessionRecord | None:
    with _state_lock:
        return _load_session(session_id)


def record_tts_artifact(session_id: str, request: TtsArtifactRecord) -> TtsArtifactRecord:
    with _state_lock:
        record = _load_session(session_id) or _default_session_record(session_id)
        _validate_contract_version(request.contract_version)
        _validate_log_channel(request.channel)

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

        timestamp = _now_iso()
        record.updated_at = timestamp
        record.resume_checkpoint_id = _checkpoint_id(record.world_state, record.turn_id)
        if record.resume_checkpoint_id not in record.checkpoints:
            record.checkpoints.append(record.resume_checkpoint_id)

        payload = request.model_dump()
        payload["session_id"] = record.session_id
        payload["campaign_id"] = payload.get("campaign_id") or record.campaign_id
        payload["scene_id"] = payload.get("scene_id") or record.scene_id
        payload["slot_id"] = payload.get("slot_id") or record.slot_id
        if payload.get("slot_index") is None:
            payload["slot_index"] = record.slot_index
        payload["turn_id"] = payload.get("turn_id") or record.turn_id
        payload["timestamp"] = payload.get("timestamp") or timestamp
        entry = TtsArtifactRecord.model_validate(payload)

        manifest_path = _tts_manifest_path(session_id)
        entries = _load_jsonl(manifest_path)
        entries.append(entry.model_dump())
        _write_jsonl(manifest_path, entries)

        record.artifact_paths = _artifact_paths(session_id)
        _persist_session(record)
        return entry


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

        _validate_contract_version(request.contract_version)
        _validate_session_status(request.session_status)

        record.contract_version = request.contract_version
        record.session_status = request.session_status

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
        if request.turn_context is not None:
            record.turn_context = request.turn_context
        if request.carry_over is not None:
            record.carry_over = list(request.carry_over)

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
        record.state_patches.extend(
            _normalize_state_patches(
                request.state_patches,
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
