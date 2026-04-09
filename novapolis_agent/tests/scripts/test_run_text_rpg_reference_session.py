from __future__ import annotations

import asyncio
import json
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_run_reference_session_writes_expected_artifacts(tmp_path: Path) -> None:
    from scripts import run_text_rpg_reference_session as mod

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
    assert report["actual"]["artifacts"]["savegame"]["exists"] is True
    assert report["actual"]["artifacts"]["replay_manifest"]["exists"] is True
    assert (tmp_path / "sessions" / "reference-session" / "world_log.jsonl").exists()
