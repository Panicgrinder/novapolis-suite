from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


def _write_session_fixture(session_root: Path, session_id: str) -> None:
    session_dir = session_root / session_id
    session_dir.mkdir(parents=True, exist_ok=True)
    (session_dir / "savegame.json").write_text(
        json.dumps(
            {
                "session_id": session_id,
                "updated_at": "2026-04-21T00:48:00+00:00",
                "carry_over": [{"task_id": "repair-valve"}],
                "state_patches": [
                    {
                        "op": "replace",
                        "path": "/scene_id",
                        "value": "scene-d5",
                    }
                ],
            }
        )
        + "\n",
        encoding="utf-8",
    )
    (session_dir / "replay_manifest.json").write_text(
        json.dumps(
            {
                "session_id": session_id,
                "session_status": "active",
                "resume_checkpoint_id": "turn-0003",
                "checkpoints": ["turn-0003"],
                "artifact_paths": {
                    "savegame": f"tmp/sim_sessions/{session_id}/savegame.json",
                    "world_log": f"tmp/sim_sessions/{session_id}/world_log.jsonl",
                    "pc_log": f"tmp/sim_sessions/{session_id}/pc_log.jsonl",
                    "replay_manifest": f"tmp/sim_sessions/{session_id}/replay_manifest.json",
                },
                "world_event_count": 1,
                "pc_event_count": 2,
                "updated_at": "2026-04-21T00:48:00+00:00",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    (session_dir / "world_log.jsonl").write_text(
        json.dumps({"event": "Dust front reaches D5"}) + "\n",
        encoding="utf-8",
    )
    (session_dir / "pc_log.jsonl").write_text(
        json.dumps({"content": "Szene: Das Ventilhaus steht offen."}) + "\n",
        encoding="utf-8",
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_session_promotion_items_builds_record_shape(tmp_path: Path) -> None:
    from scripts import build_session_promotion_pack as mod

    repo_root = tmp_path
    session_root = repo_root / "novapolis_agent" / "tmp" / "sim_sessions"
    _write_session_fixture(session_root, "campaign-alpha")

    items, skipped = mod.collect_session_promotion_items(repo_root, session_root, limit=5)

    assert skipped == []
    assert len(items) == 1
    record = items[0].to_record()
    assert record["category"] == "session_promotion_seed"
    assert record["source_kind"] == "session_replay"
    assert record["promotion_level"] == "runtime_session_review_required"
    assert record["license_scope"] == "internal"
    assert record["session_id"] == "campaign-alpha"
    assert "Promotionsnotiz" in record["messages"][0]["content"]


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_session_promotion_items_skips_missing_manifest(tmp_path: Path) -> None:
    from scripts import build_session_promotion_pack as mod

    repo_root = tmp_path
    session_root = repo_root / "novapolis_agent" / "tmp" / "sim_sessions"
    session_dir = session_root / "broken"
    session_dir.mkdir(parents=True, exist_ok=True)
    (session_dir / "savegame.json").write_text("{}\n", encoding="utf-8")

    items, skipped = mod.collect_session_promotion_items(repo_root, session_root, limit=5)

    assert items == []
    assert skipped == ["broken: missing replay_manifest.json"]


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_2_when_session_root_missing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_session_promotion_pack as mod

    old_argv = list(sys.argv)
    sys.argv = [
        "build_session_promotion_pack.py",
        "--repo-root",
        str(tmp_path),
        "--session-root",
        "missing",
    ]
    try:
        rc = mod.main()
    finally:
        sys.argv = old_argv

    out = capsys.readouterr().out
    assert rc == 2
    assert "session_root not found" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_main_success_writes_default_output(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_session_promotion_pack as mod

    session_root = tmp_path / "novapolis_agent" / "tmp" / "sim_sessions"
    _write_session_fixture(session_root, "sid-42")

    old_argv = list(sys.argv)
    sys.argv = [
        "build_session_promotion_pack.py",
        "--repo-root",
        str(tmp_path),
        "--limit",
        "5",
    ]
    try:
        rc = mod.main()
    finally:
        sys.argv = old_argv

    out = capsys.readouterr().out
    result = (
        tmp_path
        / "novapolis_agent"
        / "eval"
        / "datasets"
        / "curation"
        / "session_promotions.v1.jsonl"
    )
    assert rc == 0
    assert "[session-promotion-builder] done" in out
    assert result.exists()
    row = json.loads(result.read_text(encoding="utf-8").strip().splitlines()[0])
    assert row["id"].startswith("promote-session-")
    assert row["session_id"] == "sid-42"
