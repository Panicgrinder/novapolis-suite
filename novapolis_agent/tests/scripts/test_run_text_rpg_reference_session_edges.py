from __future__ import annotations

import asyncio
import json
import runpy
from pathlib import Path
from types import SimpleNamespace

import pytest


class _DummyResponse:
    def __init__(self, status_code: int, payload: dict[str, object] | None = None, text: str = ""):
        self.status_code = status_code
        self._payload = payload or {}
        self.text = text

    def json(self) -> dict[str, object]:
        return dict(self._payload)


def _write_spec(path: Path) -> None:
    path.write_text(
        json.dumps(
            {
                "session_id": "ref-session",
                "steps": [{"scene_id": "scene-a", "slot_id": "slot-01", "turn_id": "turn-0001"}],
                "expected": {},
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_read_jsonl_missing_and_filters_non_dict_lines(tmp_path: Path) -> None:
    from scripts import run_text_rpg_reference_session as mod

    assert mod._read_jsonl(tmp_path / "missing.jsonl") == []

    data_path = tmp_path / "data.jsonl"
    data_path.write_text('{"a": 1}\n[]\n\n{"b": 2}\n', encoding="utf-8")

    assert mod._read_jsonl(data_path) == [{"a": 1}, {"b": 2}]


@pytest.mark.scripts
@pytest.mark.unit
@pytest.mark.parametrize(
    ("payload", "expected_message"),
    [
        ([], "must contain a JSON object"),
        ({}, "requires non-empty session_id"),
        ({"session_id": "x", "steps": []}, "requires non-empty steps list"),
        ({"session_id": "x", "steps": [1]}, "step 1 must be an object"),
        ({"session_id": "x", "steps": [{}], "expected": []}, "field 'expected' must be an object"),
    ],
)
def test_load_reference_spec_rejects_invalid_shapes(
    tmp_path: Path, payload: object, expected_message: str
) -> None:
    from scripts import run_text_rpg_reference_session as mod

    spec_path = tmp_path / "invalid.json"
    spec_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    with pytest.raises(ValueError, match=expected_message):
        mod.load_reference_spec(spec_path)


@pytest.mark.scripts
@pytest.mark.unit
def test_validate_expected_reports_mismatches_and_missing_artifacts(tmp_path: Path) -> None:
    from scripts import run_text_rpg_reference_session as mod

    actual = {
        "contract_version": "v1",
        "session_status": "active",
        "scene_id": "scene-a",
        "slot_id": "slot-01",
        "slot_index": 1,
        "turn_id": "turn-0001",
        "resume_checkpoint_id": "turn-0001",
        "turn_context": {"turn_mode": "standard", "turn_window_minutes": 30},
        "carry_over_count": 0,
        "checkpoints": ["turn-0001"],
        "world_log_count": 1,
        "pc_log_count": 1,
        "state_patch_count": 1,
        "world_event_count": 1,
        "pc_event_count": 1,
        "artifacts": {
            "savegame": {"exists": False},
            "world_log": {"exists": False},
            "pc_log": {"exists": True},
            "replay_manifest": {"exists": False},
        },
    }
    expected = {
        "scene_id": "scene-b",
        "slot_id": "slot-02",
        "carry_over_count": 2,
        "world_log_count": 2,
    }

    errors = mod._validate_expected(actual, expected)

    assert "expected scene_id='scene-b' but got 'scene-a'" in errors
    assert "expected slot_id='slot-02' but got 'slot-01'" in errors
    assert "expected carry_over_count=2 but got 0" in errors
    assert "expected world_log_count=2 but got 1" in errors
    assert "missing artifact: savegame" in errors
    assert "missing artifact: world_log" in errors
    assert "missing artifact: replay_manifest" in errors


@pytest.mark.scripts
@pytest.mark.unit
def test_build_markdown_renders_artifact_entries_and_error_block() -> None:
    from scripts import run_text_rpg_reference_session as mod

    report = {
        "status": "FAIL",
        "session_id": "demo",
        "spec_path": "spec.json",
        "session_store_dir": "store",
        "steps": [{"step": 1}],
        "actual": {
            "contract_version": "v1",
            "session_status": "active",
            "scene_id": "scene-a",
            "slot_id": "slot-01",
            "slot_index": 1,
            "turn_id": "turn-0001",
            "resume_checkpoint_id": "turn-0001",
            "turn_context": {"turn_mode": "standard", "turn_window_minutes": 30},
            "carry_over_count": 0,
            "world_log_count": 1,
            "pc_log_count": 1,
            "state_patch_count": 1,
            "artifacts": {
                "world_log": {"exists": True, "path": "world.jsonl", "entries": 2},
                "savegame": {"exists": True, "path": "savegame.json"},
            },
        },
        "errors": ["boom"],
    }

    markdown = mod._build_markdown(report)

    assert "entries=2" in markdown
    assert "boom" in markdown


@pytest.mark.scripts
@pytest.mark.unit
def test_run_reference_session_reports_step_failure_and_restores_store(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from novapolis_agent.app import api as api_pkg
    from scripts import run_text_rpg_reference_session as mod

    spec_path = tmp_path / "spec.json"
    _write_spec(spec_path)

    resets: list[str] = []
    original_store = tmp_path / "original-store"
    fake_sim = SimpleNamespace(
        _SESSION_STORE_DIR=original_store,
        _sanitize_session_id=lambda value: f"san-{value}",
        reset_state=lambda: resets.append("reset"),
        app=object(),
    )
    monkeypatch.setattr(api_pkg, "sim", fake_sim, raising=False)
    monkeypatch.setattr(mod.httpx, "ASGITransport", lambda app: ("transport", app))

    class _DummyAsyncClient:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self) -> _DummyAsyncClient:
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def put(self, url: str, json: dict[str, object]) -> _DummyResponse:
            return _DummyResponse(500, text="boom")

        async def get(self, url: str) -> _DummyResponse:
            raise AssertionError("get must not be called after step failure")

    monkeypatch.setattr(mod.httpx, "AsyncClient", _DummyAsyncClient)

    report = asyncio.run(mod.run_reference_session(spec_path, tmp_path / "sessions"))

    assert report["status"] == "FAIL"
    assert report["steps"] == []
    assert any("step 1 failed with status 500: boom" in entry for entry in report["errors"])
    assert fake_sim._SESSION_STORE_DIR == original_store
    assert resets == ["reset", "reset"]


@pytest.mark.scripts
@pytest.mark.unit
def test_run_reference_session_reports_session_and_replay_fetch_failures(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from novapolis_agent.app import api as api_pkg
    from scripts import run_text_rpg_reference_session as mod

    spec_path = tmp_path / "spec.json"
    _write_spec(spec_path)

    fake_sim = SimpleNamespace(
        _SESSION_STORE_DIR=tmp_path / "original-store",
        _sanitize_session_id=lambda value: value,
        reset_state=lambda: None,
        app=object(),
    )
    monkeypatch.setattr(api_pkg, "sim", fake_sim, raising=False)
    monkeypatch.setattr(mod.httpx, "ASGITransport", lambda app: app)

    class _DummyAsyncClient:
        def __init__(self, *args, **kwargs) -> None:
            pass

        async def __aenter__(self) -> _DummyAsyncClient:
            return self

        async def __aexit__(self, exc_type, exc, tb) -> bool:
            return False

        async def put(self, url: str, json: dict[str, object]) -> _DummyResponse:
            return _DummyResponse(
                200,
                payload={
                    "scene_id": "scene-a",
                    "slot_id": "slot-01",
                    "turn_id": "turn-0001",
                    "resume_checkpoint_id": "turn-0001",
                    "world_log": [],
                    "pc_log": [],
                    "state_patches": [],
                },
            )

        async def get(self, url: str) -> _DummyResponse:
            if url.endswith("/replay"):
                return _DummyResponse(502, text="replay-down")
            return _DummyResponse(503, text="session-down")

    monkeypatch.setattr(mod.httpx, "AsyncClient", _DummyAsyncClient)

    report = asyncio.run(mod.run_reference_session(spec_path, tmp_path / "sessions"))

    assert report["status"] == "FAIL"
    assert len(report["steps"]) == 1
    assert any(
        "session fetch failed with status 503: session-down" in entry for entry in report["errors"]
    )
    assert any(
        "replay fetch failed with status 502: replay-down" in entry for entry in report["errors"]
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_main_writes_reports_for_success_and_failure(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import run_text_rpg_reference_session as mod

    async def _fake_success(spec_path: Path, session_store_dir: Path) -> dict[str, object]:
        return {
            "status": "PASS",
            "session_id": "ok-session",
            "spec_path": spec_path.as_posix(),
            "session_store_dir": session_store_dir.as_posix(),
            "steps": [],
            "actual": {"artifacts": {}},
            "errors": [],
        }

    monkeypatch.setattr(mod, "run_reference_session", _fake_success)
    monkeypatch.setattr(
        "sys.argv",
        [
            "run_text_rpg_reference_session.py",
            "--repo-root",
            str(tmp_path),
            "--report-json",
            "reports/out.json",
            "--report-md",
            "reports/out.md",
        ],
    )

    assert mod.main() == 0
    assert (tmp_path / "reports" / "out.json").exists()
    assert (tmp_path / "reports" / "out.md").exists()
    success_output = capsys.readouterr().out
    assert "[reference-session] status=PASS" in success_output

    async def _fake_failure(spec_path: Path, session_store_dir: Path) -> dict[str, object]:
        return {
            "status": "FAIL",
            "session_id": "bad-session",
            "spec_path": spec_path.as_posix(),
            "session_store_dir": session_store_dir.as_posix(),
            "steps": [],
            "actual": {"artifacts": {}},
            "errors": ["broken"],
        }

    monkeypatch.setattr(mod, "run_reference_session", _fake_failure)
    monkeypatch.setattr(
        "sys.argv",
        [
            "run_text_rpg_reference_session.py",
            "--repo-root",
            str(tmp_path),
        ],
    )

    assert mod.main() == 1
    failure_output = capsys.readouterr().out
    assert "[reference-session] status=FAIL" in failure_output
    assert "[reference-session] error=broken" in failure_output


@pytest.mark.scripts
@pytest.mark.unit
def test_module_main_executes_via_runpy(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    script_path = (
        Path(__file__).resolve().parents[2] / "scripts" / "run_text_rpg_reference_session.py"
    )
    spec_path = tmp_path / "reference-session.json"
    spec_path.write_text(
        json.dumps(
            {
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
                            {"scope": "session", "op": "add", "path": "/flags/a", "value": True}
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
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "run_text_rpg_reference_session.py",
            "--repo-root",
            str(tmp_path),
            "--spec",
            "reference-session.json",
            "--session-store-dir",
            "sessions",
            "--report-json",
            "reports/out.json",
            "--report-md",
            "reports/out.md",
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        runpy.run_path(str(script_path), run_name="__main__")

    assert exc_info.value.code == 0
    assert (tmp_path / "reports" / "out.json").exists()
