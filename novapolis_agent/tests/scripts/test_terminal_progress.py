from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_run_command_with_heartbeat_prints_progress_and_captures_output(
    capsys: pytest.CaptureFixture[str],
) -> None:
    from scripts import terminal_progress as mod

    completed = mod.run_command_with_heartbeat(
        [
            sys.executable,
            "-c",
            "import time; time.sleep(0.18); print('fertig', flush=True)",
        ],
        label="pytest smoke",
        heartbeat_seconds=0.05,
    )

    out = capsys.readouterr().out

    assert completed.returncode == 0
    assert "fertig" in completed.stdout
    assert "[progress]" in out
    assert "pytest smoke" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_run_checks_command_uses_heartbeat_helper_for_pytest(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    from scripts import run_checks_and_report as mod

    calls: dict[str, object] = {}

    def fake_progress_runner(command, **kwargs):  # type: ignore[no-redef]
        calls["command"] = list(command)
        calls["label"] = kwargs.get("label")
        return subprocess.CompletedProcess(list(command), 0, "ok\n")

    monkeypatch.setattr(mod, "run_command_with_heartbeat", fake_progress_runner)

    log_path = tmp_path / "pytest.log"
    exit_code, output, duration_ms = mod.run_command(
        [sys.executable, "-m", "pytest", "-q"],
        tmp_path,
        log_path,
        progress_label="pytest",
    )

    assert exit_code == 0
    assert output == "ok\n"
    assert duration_ms >= 0
    assert calls["label"] == "pytest"
    assert log_path.read_text(encoding="utf-8") == "ok\n"
