from __future__ import annotations

import importlib
import subprocess
from pathlib import Path

import pytest


def _load_module():
    return importlib.import_module("scripts.append_done")


@pytest.mark.scripts
@pytest.mark.unit
def test_get_author_prefers_git(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()
    monkeypatch.setattr(
        subprocess,
        "check_output",
        lambda *args, **kwargs: "Git User\n",
    )
    assert mod.get_author() == "Git User"


@pytest.mark.scripts
@pytest.mark.unit
def test_get_author_fallback_to_env(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()

    def _raise(*args, **kwargs):
        raise subprocess.CalledProcessError(1, "git")

    monkeypatch.setattr(subprocess, "check_output", _raise)
    monkeypatch.delenv("USER", raising=False)
    monkeypatch.setenv("USERNAME", "Local User")
    assert mod.get_author() == "Local User"


@pytest.mark.scripts
@pytest.mark.unit
def test_append_done_adds_timezone_header(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()
    log_path = tmp_path / "docs" / "DONELOG.txt"
    log_path.parent.mkdir(parents=True)
    log_path.write_text("# DONELOG\n", encoding="utf-8")

    monkeypatch.setattr(mod, "PROJECT_ROOT", str(tmp_path), raising=False)
    monkeypatch.setattr(mod, "LOG_PATH", str(log_path), raising=False)
    monkeypatch.setattr(mod, "get_author", lambda: "Tester", raising=False)
    monkeypatch.setenv("CVN_TZ", "Europe/Berlin")
    monkeypatch.setenv("USERNAME", "IgnoredUser")
    monkeypatch.setattr("utils.time_utils.now_human_tz", lambda: "2025-11-09 04:05 CET")
    monkeypatch.setattr("utils.time_utils.tz_label", lambda: "CET")

    rc = mod.main(["Neue Änderung"])
    assert rc == 0

    lines = log_path.read_text(encoding="utf-8").splitlines()
    assert "Zeitzone: Europe/Berlin (CET)" in lines
    assert any(line.endswith("| Tester | Neue Änderung") for line in lines)


@pytest.mark.scripts
@pytest.mark.unit
def test_append_done_fallback_without_time_utils(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()
    log_path = tmp_path / "docs" / "DONELOG.txt"
    log_path.parent.mkdir(parents=True)

    monkeypatch.setattr(mod, "PROJECT_ROOT", str(tmp_path), raising=False)
    monkeypatch.setattr(mod, "LOG_PATH", str(log_path), raising=False)
    monkeypatch.setattr(mod, "get_author", lambda: "FallbackTester", raising=False)

    def _boom():
        raise RuntimeError("boom")

    monkeypatch.setattr("utils.time_utils.now_human_tz", _boom)
    monkeypatch.setattr("utils.time_utils.tz_label", _boom)

    rc = mod.main(["Fallback Pfad"])
    assert rc == 0

    content = log_path.read_text(encoding="utf-8").splitlines()
    assert any(line.endswith("| FallbackTester | Fallback Pfad") for line in content)
