from __future__ import annotations

import asyncio
import importlib
import json
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_run_reference_session_writes_expected_artifacts(tmp_path: Path) -> None:
    mod = importlib.import_module("scripts.run_text_rpg_reference_session")

    spec = {
        "session_id": "reference-session",
        "steps": [
            {
                "contract_version": "text_rpg_session_v1",
                "session_status": "active",
                "campaign_id": "campaign-alpha",
                "scene_id": "scene-a",
                "slot_id": "slot-01",
                "slot_index": 1,
                "turn_id": "turn-0001",
                "turn_context": {
                    "turn_mode": "standard",
                    "turn_window_minutes": 30,
                    "tick_minutes": None,
                    "budget_class": "within_frame",
                },
                "world_log": [{"event": "world-a"}],
                "pc_log": [{"event": "pc-a"}],
                "state_patches": [
                    {
                        "scope": "session",
                        "op": "add",
                        "path": "/flags/a",
                        "value": True,
                    }
                ],
            },
            {
                "contract_version": "text_rpg_session_v1",
                "session_status": "active",
                "campaign_id": "campaign-alpha",
                "scene_id": "scene-b",
                "slot_id": "slot-02",
                "slot_index": 2,
                "turn_id": "turn-0002",
                "carry_over": [
                    {
                        "task_id": "follow-up",
                        "state": "offen",
                        "resume_hint": "naechsten Turn starten",
                    }
                ],
                "world_log": [{"event": "world-b"}],
                "pc_log": [{"event": "pc-b"}],
                "state_patches": [
                    {
                        "scope": "session",
                        "op": "replace",
                        "path": "/scene_id",
                        "value": "scene-b",
                    }
                ],
            },
        ],
        "expected": {
            "contract_version": "text_rpg_session_v1",
            "session_status": "active",
            "scene_id": "scene-b",
            "slot_id": "slot-02",
            "slot_index": 2,
            "turn_id": "turn-0002",
            "resume_checkpoint_id": "turn-0002",
            "turn_context": {
                "turn_mode": "standard",
                "turn_window_minutes": 30,
                "tick_minutes": None,
                "budget_class": "within_frame",
            },
            "carry_over_count": 1,
            "checkpoints": ["turn-0001", "turn-0002"],
            "world_log_count": 2,
            "pc_log_count": 2,
            "state_patch_count": 2,
            "world_event_count": 2,
            "pc_event_count": 2,
        },
    }
    spec_path = tmp_path / "reference-session.json"
    spec_path.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")

    report = asyncio.run(mod.run_reference_session(spec_path, tmp_path / "sessions"))

    assert report["status"] == "PASS"
    assert report["actual"]["scene_id"] == "scene-b"
    assert report["actual"]["world_log_count"] == 2
    assert report["actual"]["pc_log_count"] == 2
    assert report["actual"]["state_patch_count"] == 2
    assert report["actual"]["turn_context"]["turn_window_minutes"] == 30
    assert report["actual"]["carry_over_count"] == 1
    assert report["actual"]["artifacts"]["savegame"]["exists"] is True
    assert report["actual"]["artifacts"]["replay_manifest"]["exists"] is True
    assert (tmp_path / "sessions" / "reference-session" / "world_log.jsonl").exists()


@pytest.mark.scripts
@pytest.mark.unit
def test_run_reference_sessions_aggregates_multiple_specs(tmp_path: Path) -> None:
    mod = importlib.import_module("scripts.run_text_rpg_reference_session")

    first_spec = {
        "session_id": "reference-base",
        "steps": [
            {
                "contract_version": "text_rpg_session_v1",
                "session_status": "active",
                "campaign_id": "campaign-alpha",
                "scene_id": "scene-a",
                "slot_id": "slot-01",
                "slot_index": 1,
                "turn_id": "turn-0001",
                "world_state": {
                    "tick": 1,
                    "time": 1.0,
                    "regions": {},
                    "actors": {},
                    "events": [],
                },
                "world_log": [{"event": "world-a"}],
                "pc_log": [{"event": "pc-a"}],
                "state_patches": [
                    {
                        "scope": "session",
                        "op": "add",
                        "path": "/flags/a",
                        "value": True,
                    }
                ],
            }
        ],
        "expected": {
            "contract_version": "text_rpg_session_v1",
            "session_status": "active",
            "scene_id": "scene-a",
            "slot_id": "slot-01",
            "slot_index": 1,
            "turn_id": "turn-0001",
            "resume_checkpoint_id": "turn-0001",
            "checkpoints": ["turn-0001"],
            "world_log_count": 1,
            "pc_log_count": 1,
            "state_patch_count": 1,
            "world_event_count": 1,
            "pc_event_count": 1,
        },
    }
    second_spec = {
        "session_id": "reference-handover",
        "steps": [
            {
                "contract_version": "text_rpg_session_v1",
                "session_status": "active",
                "campaign_id": "campaign-beta",
                "scene_id": "scene-handover",
                "slot_id": "slot-31",
                "slot_index": 31,
                "turn_id": "turn-0011",
                "turn_context": {
                    "turn_mode": "standard",
                    "turn_window_minutes": 30,
                    "tick_minutes": 1,
                    "budget_class": "within_frame",
                },
                "world_state": {
                    "tick": 31,
                    "time": 31.0,
                    "regions": {},
                    "actors": {},
                    "events": [],
                },
                "carry_over": [
                    {
                        "task_id": "handover",
                        "state": "offen",
                        "resume_hint": "handover-weiterziehen",
                    }
                ],
                "world_log": [{"event": "world-handover"}],
                "pc_log": [{"event": "pc-handover"}],
                "state_patches": [
                    {
                        "scope": "session",
                        "op": "add",
                        "path": "/flags/handover",
                        "value": True,
                    }
                ],
            }
        ],
        "expected": {
            "contract_version": "text_rpg_session_v1",
            "session_status": "active",
            "scene_id": "scene-handover",
            "slot_id": "slot-31",
            "slot_index": 31,
            "turn_id": "turn-0011",
            "resume_checkpoint_id": "turn-0011",
            "turn_context": {
                "turn_mode": "standard",
                "turn_window_minutes": 30,
                "tick_minutes": 1,
                "budget_class": "within_frame",
            },
            "carry_over_count": 1,
            "checkpoints": ["turn-0011"],
            "world_log_count": 1,
            "pc_log_count": 1,
            "state_patch_count": 1,
            "world_event_count": 1,
            "pc_event_count": 1,
        },
    }
    first_path = tmp_path / "reference-base.json"
    second_path = tmp_path / "reference-handover.json"
    first_path.write_text(json.dumps(first_spec, ensure_ascii=False, indent=2), encoding="utf-8")
    second_path.write_text(
        json.dumps(second_spec, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    report = asyncio.run(
        mod.run_reference_sessions([first_path, second_path], tmp_path / "sessions")
    )

    assert report["status"] == "PASS"
    assert report["case_count"] == 2
    assert report["passed_cases"] == 2
    assert [case["session_id"] for case in report["cases"]] == [
        "reference-base",
        "reference-handover",
    ]
