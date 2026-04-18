from __future__ import annotations

import json
from pathlib import Path
from types import SimpleNamespace
from typing import Literal

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_build_base_gate_steps_orders_reference_session_before_sim_and_eval(
    tmp_path: Path,
) -> None:
    from scripts import run_text_rpg_product_gate as mod

    python_exec = tmp_path / "python.exe"
    steps = mod.build_base_gate_steps(tmp_path, python_exec, "20260408_140200")

    assert [step.name for step in steps] == [
        "checks_full",
        "pytest_api_streaming",
        "reference_session",
        "sim_epoch_assets",
        "gm_session_eval",
    ]
    assert any("run_text_rpg_reference_session.py" in part for part in steps[2].command)
    assert steps[2].command.count("--spec") == 2
    assert any("text_rpg_reference_session.v1.json" in part for part in steps[2].command)
    assert any(
        "text_rpg_reference_session_handover_slot31_40.v1.json" in part for part in steps[2].command
    )
    assert any("check_sim_epoch_assets.py" in part for part in steps[3].command)
    assert steps[4].command[1:3] == ("-m", "scripts.agent.run_eval")


@pytest.mark.scripts
@pytest.mark.unit
def test_pick_newest_gm_result_prefers_new_file(tmp_path: Path) -> None:
    from scripts import run_text_rpg_product_gate as mod

    old_file = tmp_path / "results_20260408_130000_gm_session.jsonl"
    new_file = tmp_path / "results_20260408_140000_gm_session.jsonl"
    old_file.write_text("{}\n", encoding="utf-8")
    new_file.write_text("{}\n", encoding="utf-8")

    before = {old_file.resolve()}
    after = {old_file.resolve(), new_file.resolve()}
    result = mod.pick_newest_gm_result(before, after)

    assert result == new_file.resolve()


@pytest.mark.scripts
@pytest.mark.unit
def test_run_gm_runtime_preflight_reports_listener_and_model(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from scripts import run_text_rpg_product_gate as mod

    monkeypatch.setattr(
        mod,
        "load_runtime_target",
        lambda: ("http://localhost:11434", "qwen2.5:7b"),
    )

    class _DummySocket:
        def __enter__(self) -> object:
            return object()

        def __exit__(self, exc_type, exc, tb) -> Literal[False]:
            return False

    monkeypatch.setattr(mod.socket, "create_connection", lambda *args, **kwargs: _DummySocket())

    class _DummyResponse:
        status = 200

        def __enter__(self) -> _DummyResponse:
            return self

        def __exit__(self, exc_type, exc, tb) -> Literal[False]:
            return False

        def read(self) -> bytes:
            return json.dumps(
                {"models": [{"name": "qwen2.5:7b"}, {"name": "llama3.1:8b"}]},
                ensure_ascii=False,
            ).encode("utf-8")

    monkeypatch.setattr(mod.urllib.request, "urlopen", lambda *args, **kwargs: _DummyResponse())

    result = mod.run_gm_runtime_preflight(tmp_path, "20260408_2230")

    assert result.status == "PASS"
    assert result.metadata["host"] == "http://localhost:11434"
    assert result.metadata["model"] == "qwen2.5:7b"
    assert "qwen2.5:7b" in result.metadata["available_models"]


@pytest.mark.scripts
@pytest.mark.unit
def test_build_gm_diagnosis_distinguishes_preflight_and_eval_failures() -> None:
    from scripts import run_text_rpg_product_gate as mod

    preflight_fail = mod.StepResult(
        name="gm_runtime_preflight",
        status="FAIL",
        exit_code=1,
        duration_ms=5,
        command=[],
        cwd=".",
        log_path="preflight.log",
        metadata={
            "error_kind": "runtime_unreachable",
            "error_detail": "connection refused",
            "host": "http://localhost:11434",
            "model": "qwen3.5:4b",
        },
    )
    diagnosis = mod.build_gm_diagnosis([preflight_fail])
    assert diagnosis["phase"] == "preflight"
    assert diagnosis["classification"] == "runtime_unreachable"
    assert "gm runtime preflight" in diagnosis["hint"]

    preflight_ok = mod.StepResult(
        name="gm_runtime_preflight",
        status="PASS",
        exit_code=0,
        duration_ms=5,
        command=[],
        cwd=".",
        log_path="preflight.log",
        metadata={"host": "http://localhost:11434", "model": "qwen3.5:4b"},
    )
    eval_fail = mod.StepResult(
        name="gm_session_eval",
        status="PASS",
        exit_code=0,
        duration_ms=20,
        command=[],
        cwd=".",
        log_path="gm_eval.log",
        metadata={
            "failure_summary": "gm_timeout_504=1, runtime_unreachable=1",
            "failure_examples": "gm_timeout_504:gm.session.continuity.v1",
        },
    )
    diagnosis = mod.build_gm_diagnosis([preflight_ok, eval_fail])
    assert diagnosis["phase"] == "eval"
    assert diagnosis["classification"] == "eval_runtime_or_execution_failures"
    assert diagnosis["detail"] == "gm_timeout_504=1, runtime_unreachable=1"


@pytest.mark.scripts
@pytest.mark.unit
def test_run_gm_preflight_only_returns_diagnostic_fail(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from scripts import run_text_rpg_product_gate as mod

    monkeypatch.setattr(
        mod,
        "run_gm_runtime_preflight",
        lambda *_args, **_kwargs: mod.StepResult(
            name="gm_runtime_preflight",
            status="FAIL",
            exit_code=1,
            duration_ms=1,
            command=[],
            cwd=".",
            log_path="preflight.log",
            metadata={
                "error_kind": "model_missing",
                "error_detail": "qwen3.5:4b",
                "host": "http://localhost:11434",
                "model": "qwen3.5:4b",
            },
        ),
    )

    report = mod.run_gm_preflight_only(tmp_path, "20260418_0500")

    assert report["status"] == "FAIL"
    assert report["errors"] == ["gm_runtime_preflight classified: model_missing"]
    assert report["gm_diagnosis"]["classification"] == "model_missing"


@pytest.mark.scripts
@pytest.mark.unit
def test_load_runtime_target_prefers_app_settings_module(monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import run_text_rpg_product_gate as mod

    fake_settings_module = SimpleNamespace(
        get_settings=lambda: SimpleNamespace(
            OLLAMA_HOST="http://localhost:11434",
            MODEL_NAME="qwen2.5:7b",
        )
    )

    monkeypatch.setattr(
        mod.importlib,
        "import_module",
        lambda name: fake_settings_module if name == "app.core.settings" else None,
    )
    monkeypatch.setattr(mod.sys, "modules", {}, raising=False)

    host, model = mod.load_runtime_target()

    assert host == "http://localhost:11434"
    assert model == "qwen2.5:7b"


@pytest.mark.scripts
@pytest.mark.unit
def test_run_step_sets_utf8_env(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from scripts import run_text_rpg_product_gate as mod

    captured: dict[str, object] = {}

    def _fake_run(*args, **kwargs):
        captured["env"] = kwargs.get("env")
        return SimpleNamespace(returncode=0, stdout="ok")

    monkeypatch.setattr(mod.subprocess, "run", _fake_run)

    result = mod.run_step(
        mod.GateStep(
            name="demo",
            command=("python", "demo.py"),
            cwd=tmp_path,
            log_path=tmp_path / "demo.log",
        ),
        tmp_path,
    )

    env = captured["env"]
    assert isinstance(env, dict)
    assert env["PYTHONIOENCODING"] == "utf-8"
    assert env["PYTHONUTF8"] == "1"
    assert result.status == "PASS"


@pytest.mark.scripts
@pytest.mark.unit
def test_load_summary_severity_reads_blocker(tmp_path: Path) -> None:
    from scripts import run_text_rpg_product_gate as mod

    report_json = tmp_path / "gm_summary.json"
    report_json.write_text(
        json.dumps({"summary": {"severity": "blocker"}}, ensure_ascii=False),
        encoding="utf-8",
    )

    assert mod.load_summary_severity(report_json) == "blocker"


@pytest.mark.scripts
@pytest.mark.unit
def test_classify_gm_eval_failures_separates_runtime_500_and_timeout(tmp_path: Path) -> None:
    from scripts import run_text_rpg_product_gate as mod

    result_file = tmp_path / "results_20260408_2150_gm_session.jsonl"
    result_file.write_text(
        "\n".join(
            [
                '{"_meta": true, "host": "http://localhost:11434"}',
                (
                    '{"slug": "gm.session.continuity.v1", '
                    '"response": "Server error \'500 Internal Server Error\' for url '
                    "'http://localhost:11434/api/chat'\"}"
                ),
                (
                    '{"slug": "gm.session.reveal-discipline.v1", '
                    '"error": "Server error \'504 Gateway Timeout\' for url '
                    "'http://asgi/chat'\"}"
                ),
                (
                    '{"slug": "gm.session.option-quality.v1", '
                    '"response": "All connection attempts failed"}'
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    errors, metadata = mod.classify_gm_eval_failures(result_file)

    assert "gm_session_eval classified: gm_timeout_504 (1)" in errors
    assert "gm_session_eval classified: ollama_http_500 (1)" in errors
    assert "gm_session_eval classified: runtime_unreachable (1)" in errors
    assert metadata["failure_summary"] == (
        "gm_timeout_504=1, ollama_http_500=1, runtime_unreachable=1"
    )


@pytest.mark.scripts
@pytest.mark.unit
def test_run_product_gate_fails_on_blocker_summary(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from scripts import run_text_rpg_product_gate as mod

    reports_dir = tmp_path / ".tmp" / "results" / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    results_dir = tmp_path / "novapolis_agent" / "eval" / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    result_file = results_dir / "results_20260409_0000_gm_session.jsonl"
    result_file.write_text('{"_meta": true}\n', encoding="utf-8")

    summary_json_rel = ".tmp/results/reports/gm_session_kpi_summary_20260409_0000.json"
    summary_json_abs = tmp_path / summary_json_rel
    summary_json_abs.parent.mkdir(parents=True, exist_ok=True)
    summary_json_abs.write_text(
        json.dumps({"summary": {"severity": "blocker"}}, ensure_ascii=False),
        encoding="utf-8",
    )

    base_steps = [
        mod.GateStep(
            name="gm_session_eval",
            command=("python", "eval.py"),
            cwd=tmp_path,
            log_path=reports_dir / "gm_eval.log",
        )
    ]
    summary_step = mod.GateStep(
        name="gm_session_summary",
        command=("python", "summary.py"),
        cwd=tmp_path,
        log_path=reports_dir / "gm_summary.log",
        metadata={"report_json": summary_json_rel, "report_md": ".tmp/results/reports/gm.md"},
    )

    monkeypatch.setattr(mod, "build_base_gate_steps", lambda *args, **kwargs: base_steps)
    monkeypatch.setattr(
        mod,
        "run_gm_runtime_preflight",
        lambda *args, **kwargs: mod.StepResult(
            name="gm_runtime_preflight",
            status="PASS",
            exit_code=0,
            duration_ms=1,
            command=[],
            cwd=".",
            log_path="preflight.log",
            metadata={"host": "http://localhost:11434"},
        ),
    )
    monkeypatch.setattr(
        mod,
        "build_gm_summary_step",
        lambda *args, **kwargs: summary_step,
    )
    monkeypatch.setattr(mod, "list_gm_result_files", lambda *_: {result_file.resolve()})
    monkeypatch.setattr(mod, "pick_newest_gm_result", lambda *_: result_file.resolve())
    monkeypatch.setattr(
        mod,
        "classify_gm_eval_failures",
        lambda *_: ([], {"failure_summary": "none"}),
    )

    def _fake_run_step(step, _repo_root):
        return mod.StepResult(
            name=step.name,
            status="PASS",
            exit_code=0,
            duration_ms=1,
            command=list(step.command),
            cwd=".",
            log_path=step.log_path.as_posix(),
            metadata=dict(step.metadata),
        )

    monkeypatch.setattr(mod, "run_step", _fake_run_step)

    report = mod.run_product_gate(tmp_path, tmp_path / "python.exe", "20260409_0000", False)

    assert report["status"] == "FAIL"
    assert "gm_session summary classified: blocker" in report["errors"]
    assert report["gm_diagnosis"]["phase"] == "summary"
    assert report["gm_diagnosis"]["classification"] == "summary_blocker"
