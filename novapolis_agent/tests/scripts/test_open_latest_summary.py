from __future__ import annotations

import importlib
from pathlib import Path
from types import SimpleNamespace

import pytest


def _load_module():
    return importlib.import_module("scripts.open_latest_summary")


def _set_args(monkeypatch: pytest.MonkeyPatch, module, **kwargs) -> None:
    def _parse_args(self):
        return SimpleNamespace(**kwargs)

    monkeypatch.setattr(module.argparse.ArgumentParser, "parse_args", _parse_args)


@pytest.mark.scripts
@pytest.mark.unit
def test_find_latest_summary_selects_newest(tmp_path: Path) -> None:
    module = _load_module()
    dir_path = tmp_path / "summaries"
    dir_path.mkdir()
    (dir_path / "summary_ALL_20240101_MIXED.md").write_text("one", encoding="utf-8")
    (dir_path / "summary_ALL_20240201_MIXED.md").write_text("two", encoding="utf-8")

    latest = module.find_latest_summary(dir_path)
    assert latest and latest.name.endswith("20240201_MIXED.md")


@pytest.mark.scripts
@pytest.mark.unit
def test_find_latest_summary_handles_missing_dir(tmp_path: Path) -> None:
    module = _load_module()
    assert module.find_latest_summary(tmp_path / "missing") is None


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_uses_webbrowser(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    module = _load_module()
    file_path = tmp_path / "summary_ALL_20240101_MIXED.md"
    file_path.write_text("data", encoding="utf-8")

    calls: list[str] = []
    monkeypatch.setattr(module.webbrowser, "open", lambda uri: calls.append(uri) or True)
    module.open_file(file_path)
    assert calls and calls[0].endswith("20240101_MIXED.md")


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_windows_fallback(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    module = _load_module()
    file_path = tmp_path / "summary_ALL_20240101_MIXED.md"
    file_path.write_text("data", encoding="utf-8")

    monkeypatch.setattr(module.webbrowser, "open", lambda _: False)
    monkeypatch.setattr(module.platform, "system", lambda: "Windows")
    calls: list[str] = []
    monkeypatch.setattr(module.os, "startfile", lambda path: calls.append(path), raising=False)
    monkeypatch.setattr(
        module.os, "system", lambda cmd: (_ for _ in ()).throw(RuntimeError("should not run"))
    )

    module.open_file(file_path)
    assert calls == [str(file_path)]


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_linux_fallback(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    module = _load_module()
    file_path = tmp_path / "summary_ALL_20240101_MIXED.md"
    file_path.write_text("data", encoding="utf-8")

    monkeypatch.setattr(module.webbrowser, "open", lambda _: False)
    monkeypatch.setattr(module.platform, "system", lambda: "Linux")
    monkeypatch.delattr(module.os, "startfile", raising=False)
    cmds: list[str] = []
    monkeypatch.setattr(module.os, "system", lambda cmd: cmds.append(cmd))

    module.open_file(file_path)
    assert cmds and "xdg-open" in cmds[0]


@pytest.mark.scripts
@pytest.mark.unit
def test_main_prints_path_when_requested(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    module = _load_module()
    file_path = tmp_path / "summary_ALL_20240101_MIXED.md"
    file_path.write_text("data", encoding="utf-8")

    _set_args(monkeypatch, module, do_print=True, dir=str(tmp_path))
    monkeypatch.setattr(module, "open_file", lambda path: None)

    rc = module.main()
    assert rc == 0
    out = capsys.readouterr().out.strip()
    assert out.endswith("20240101_MIXED.md")


@pytest.mark.scripts
@pytest.mark.unit
def test_main_opens_file_when_available(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    module = _load_module()
    file_path = tmp_path / "summary_ALL_20240101_MIXED.md"
    file_path.write_text("data", encoding="utf-8")

    called = []
    _set_args(monkeypatch, module, do_print=False, dir=str(tmp_path))

    def _fake_open(path: Path) -> None:
        called.append(path)

    monkeypatch.setattr(module, "open_file", _fake_open)

    rc = module.main()
    assert rc == 0
    assert called and called[0].name.endswith("20240101_MIXED.md")


@pytest.mark.scripts
@pytest.mark.unit
def test_main_reports_missing_directory(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    module = _load_module()
    empty_dir = tmp_path / "empty"
    empty_dir.mkdir()

    _set_args(monkeypatch, module, do_print=False, dir=str(empty_dir))

    rc = module.main()
    assert rc == 2
    assert f"No summaries found in {empty_dir}" in capsys.readouterr().out
