from __future__ import annotations

from types import SimpleNamespace

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_default_cpu_limit_prefers_small_slice() -> None:
    from scripts import run_with_cpu_limit as mod

    assert mod.default_cpu_limit(12) == 4
    assert mod.default_cpu_limit(8) == 4
    assert mod.default_cpu_limit(4) == 2
    assert mod.default_cpu_limit(2) == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_build_limited_env_sets_thread_caps() -> None:
    from scripts import run_with_cpu_limit as mod

    env = mod.build_limited_env({"OMP_NUM_THREADS": "9"}, 4)

    assert env["OMP_NUM_THREADS"] == "9"
    assert env["OPENBLAS_NUM_THREADS"] == "4"
    assert env["MKL_NUM_THREADS"] == "4"
    assert env["TOKENIZERS_PARALLELISM"] == "false"
    assert env["NVP_CPU_LIMIT_ACTIVE"] == "4"


@pytest.mark.scripts
@pytest.mark.unit
def test_main_runs_child_with_resolved_cpu_limit(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import run_with_cpu_limit as mod

    calls: dict[str, object] = {}

    monkeypatch.setattr(mod, "detect_logical_cpus", lambda: 12)
    monkeypatch.setattr(mod, "set_current_process_limits", lambda mask, priority: True)
    monkeypatch.setattr(mod, "apply_limits_to_pid", lambda pid, mask, priority: True)

    class DummyPopen:
        def __init__(self, command, env=None):
            calls["command"] = command
            calls["env"] = env
            self.pid = 4242

        def wait(self) -> int:
            return 0

    monkeypatch.setattr(mod.subprocess, "Popen", DummyPopen)

    rc = mod.main(["--", "python", "-m", "pytest", "-q"])
    out = capsys.readouterr().out

    assert rc == 0
    assert "active=4" in out
    assert calls["command"] == ["python", "-m", "pytest", "-q"]
    env = calls["env"]
    assert isinstance(env, dict)
    assert env["NVP_CPU_LIMIT"] == "4"


@pytest.mark.scripts
@pytest.mark.unit
def test_main_without_command_returns_usage_error(
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import run_with_cpu_limit as mod

    rc = mod.main([])
    err = capsys.readouterr().err

    assert rc == 2
    assert "No command provided" in err