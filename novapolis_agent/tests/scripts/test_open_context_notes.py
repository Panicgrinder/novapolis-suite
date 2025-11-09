from __future__ import annotations

import builtins
import importlib
import json
import os
from pathlib import Path

import pytest


def _load_module():
    return importlib.import_module("scripts.open_context_notes")


@pytest.mark.scripts
@pytest.mark.unit
def test_ensure_file_uses_sample_if_present(tmp_path: Path) -> None:
    mod = _load_module()
    target_dir = tmp_path / "cfg"
    sample_path = target_dir / "context.local.sample.md"
    sample_path.parent.mkdir(parents=True)
    sample_path.write_text("# sample\n", encoding="utf-8")

    target = str(target_dir / "context.local.md")
    result_path = mod.ensure_file(target)

    assert result_path == target
    assert (target_dir / "context.local.md").read_text(encoding="utf-8") == "# sample\n"


@pytest.mark.scripts
@pytest.mark.unit
def test_ensure_file_creates_default_when_missing(tmp_path: Path) -> None:
    mod = _load_module()
    target = tmp_path / "cfg" / "context.local.md"
    created = mod.ensure_file(str(target))

    assert created.endswith("context.local.md")
    assert target.exists()
    assert target.read_text(encoding="utf-8").startswith("# Kontext-Notizen")


@pytest.mark.scripts
@pytest.mark.unit
def test_pick_target_prefers_existing(tmp_path: Path) -> None:
    mod = _load_module()
    existing = tmp_path / "existing.md"
    existing.write_text("", encoding="utf-8")
    other = tmp_path / "other.md"

    result = mod.pick_target([str(existing), str(other)])
    assert result == str(existing)


@pytest.mark.scripts
@pytest.mark.unit
def test_pick_target_returns_default_for_empty_list() -> None:
    mod = _load_module()
    result = mod.pick_target([])
    assert result.endswith(os.path.join("eval", "config", "context.local.md"))


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_uses_webbrowser(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()
    calls: list[str] = []
    monkeypatch.setattr(mod.webbrowser, "open", lambda path: calls.append(path) or True)
    mod.open_file("/tmp/context.md")
    assert calls == ["/tmp/context.md"]


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_windows_startfile(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()
    monkeypatch.setattr(mod.webbrowser, "open", lambda path: False)
    monkeypatch.setattr(mod.platform, "system", lambda: "Windows")
    calls: list[str] = []
    monkeypatch.setattr(mod.os, "startfile", lambda path: calls.append(path), raising=False)
    monkeypatch.setattr(mod.os, "system", lambda cmd: (_ for _ in ()).throw(RuntimeError("should not call")))

    mod.open_file("C:/context.md")
    assert calls == ["C:/context.md"]


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_linux_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()
    monkeypatch.setattr(mod.webbrowser, "open", lambda path: False)
    monkeypatch.setattr(mod.platform, "system", lambda: "Linux")
    monkeypatch.delattr(mod.os, "startfile", raising=False)
    cmds: list[str] = []
    monkeypatch.setattr(mod.os, "system", lambda cmd: cmds.append(cmd))

    mod.open_file("/tmp/context.md")
    assert cmds and "xdg-open" in cmds[0]


@pytest.mark.scripts
@pytest.mark.unit
def test_ensure_file_recovers_when_sample_read_fails(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    mod = _load_module()
    target = tmp_path / "cfg" / "context.local.md"
    sample = target.parent / "context.local.sample.md"
    sample.parent.mkdir(parents=True)
    sample.write_text("# fallback\n", encoding="utf-8")

    real_open = builtins.open

    def _mock_open(path: str, mode: str = "r", encoding: str | None = None):
        if path.endswith("context.local.sample.md") and "r" in mode:
            raise OSError("cannot read sample")
        return real_open(path, mode, encoding=encoding)

    monkeypatch.setattr("builtins.open", _mock_open)
    result = mod.ensure_file(str(target))

    assert result.endswith("context.local.md")
    assert target.exists()
    assert target.read_text(encoding="utf-8").startswith("# Kontext-Notizen")


@pytest.mark.scripts
@pytest.mark.unit
def test_main_success(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    mod = _load_module()
    target = tmp_path / "context.md"
    monkeypatch.setattr(mod.settings, "CONTEXT_NOTES_PATHS", [str(target)], raising=False)
    monkeypatch.setattr(mod.webbrowser, "open", lambda path: True)

    rc = mod.main()
    assert rc == 0
    out = capsys.readouterr().out.strip().splitlines()
    assert out
    payload = json.loads(out[0])
    assert payload["opening"].endswith("context.md")


@pytest.mark.scripts
@pytest.mark.unit
def test_main_reports_error(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    mod = _load_module()
    target = tmp_path / "context.md"
    monkeypatch.setattr(mod.settings, "CONTEXT_NOTES_PATHS", [str(target)], raising=False)
    monkeypatch.setattr(mod, "open_file", lambda _: (_ for _ in ()).throw(RuntimeError("boom")))

    rc = mod.main()
    assert rc == 1
    lines = capsys.readouterr().out.strip().splitlines()
    assert json.loads(lines[0])["opening"].endswith("context.md")
    assert json.loads(lines[-1])["error"] == "boom"
