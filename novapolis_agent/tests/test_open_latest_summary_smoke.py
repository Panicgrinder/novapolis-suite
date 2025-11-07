from __future__ import annotations

import importlib
import io
import os
from contextlib import redirect_stdout
from pathlib import Path

import pytest


def _load_module():
    return importlib.import_module("scripts.open_latest_summary")


@pytest.mark.scripts
@pytest.mark.unit
def test_open_latest_summary_find_and_print(monkeypatch: "pytest.MonkeyPatch", tmp_path: "os.PathLike[str]") -> None:
    # Erzeuge zwei Dummy-Summary-Dateien im tmp-Summaries-Ordner
    sums_dir = Path(tmp_path) / "eval" / "results" / "summaries"
    os.makedirs(sums_dir, exist_ok=True)
    f1 = sums_dir / "summary_ALL_20250101.md"
    f2 = sums_dir / "summary_ALL_20251231.md"
    f1.write_text("A", encoding="utf-8")
    f2.write_text("B", encoding="utf-8")

    mod = _load_module()
    # Patch den Default-SUMMARY_DIR auf unseren tmp-Pfad
    monkeypatch.setattr(mod, "SUMMARY_DIR", sums_dir)
    # Weite den Glob aus, damit er die erzeugten Dateien findet
    monkeypatch.setattr(mod, "SUMMARY_GLOB", "summary_ALL_*.md")

    latest = mod.find_latest_summary(sums_dir)
    assert latest is not None and latest.name == "summary_ALL_20251231.md"

    # Teste main() im print-only Modus
    import sys
    old_argv = sys.argv[:]
    sys.argv = ["open_latest_summary.py", "--print", "--dir", str(sums_dir)]
    try:
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = mod.main()
        out = buf.getvalue()
        assert rc == 0
        assert latest.name in out
    finally:
        sys.argv = old_argv


@pytest.mark.scripts
@pytest.mark.unit
def test_open_latest_summary_handles_missing(tmp_path: "os.PathLike[str]", monkeypatch: "pytest.MonkeyPatch", capsys: "pytest.CaptureFixture[str]") -> None:
    mod = _load_module()

    search_dir = Path(tmp_path) / "empty"
    search_dir.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(mod, "SUMMARY_GLOB", "summary_ALL_*.md")

    import sys

    old_argv = sys.argv[:]
    sys.argv = ["open_latest_summary.py", "--dir", str(search_dir)]
    try:
        exit_code = mod.main()
    finally:
        sys.argv = old_argv

    captured = capsys.readouterr().out
    assert exit_code == 2
    assert "No summaries found" in captured
    assert str(search_dir) in captured


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_prefers_webbrowser(monkeypatch: "pytest.MonkeyPatch", tmp_path: "os.PathLike[str]") -> None:
    mod = _load_module()

    path = Path(tmp_path) / "dummy.md"
    path.write_text("content", encoding="utf-8")

    called = {}

    def fake_open(uri: str) -> bool:
        called["uri"] = uri
        return True

    monkeypatch.setattr(mod.webbrowser, "open", fake_open)

    # Sicherstellen, dass keine Fallback-Kommandos verwendet werden
    monkeypatch.setattr(mod.os, "system", lambda _: (_ for _ in ()).throw(AssertionError("unexpected os.system call")))
    if hasattr(mod.os, "startfile"):
        monkeypatch.setattr(mod.os, "startfile", lambda *_: (_ for _ in ()).throw(AssertionError("unexpected startfile call")))

    mod.open_file(path)

    assert called["uri"] == path.as_uri()


@pytest.mark.scripts
@pytest.mark.unit
def test_open_file_falls_back_to_system(monkeypatch: "pytest.MonkeyPatch", tmp_path: "os.PathLike[str]") -> None:
    mod = _load_module()

    path = Path(tmp_path) / "dummy.md"
    path.write_text("content", encoding="utf-8")

    def fake_open(_: str) -> bool:
        raise RuntimeError("webbrowser unavailable")

    monkeypatch.setattr(mod.webbrowser, "open", fake_open)
    monkeypatch.setattr(mod.platform, "system", lambda: "Linux")

    calls = []

    def fake_system(cmd: str) -> None:
        calls.append(cmd)

    monkeypatch.setattr(mod.os, "system", fake_system)

    mod.open_file(path)

    assert calls == [f"xdg-open '{path}'"]
