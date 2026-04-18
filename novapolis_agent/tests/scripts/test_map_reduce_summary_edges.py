from __future__ import annotations

import contextlib
import importlib
import io
import runpy
from pathlib import Path

import pytest


def _load_module():
    return importlib.import_module("scripts.map_reduce_summary")


@pytest.mark.scripts
@pytest.mark.unit
def test_safe_read_and_summarize_python_fallbacks(tmp_path: Path) -> None:
    mod = _load_module()

    sample = tmp_path / "sample.txt"
    sample.write_text("abcdef", encoding="utf-8")

    assert mod.safe_read(str(sample)) == "abcdef"
    assert mod.safe_read(str(sample), max_bytes=3) == "abc"
    assert mod.safe_read(str(tmp_path / "missing.txt")) == ""

    broken_python = "def broken(\n"
    summary = mod.summarize_python(str(tmp_path / "broken.py"), broken_python, max_chars=6)
    assert summary == "def br"


@pytest.mark.scripts
@pytest.mark.unit
def test_summarize_markdown_and_json_edge_cases(tmp_path: Path) -> None:
    mod = _load_module()

    markdown = mod.summarize_markdown(str(tmp_path / "plain.md"), "Nur Text\nOhne Marker", 120)
    assert "Nur Text" in markdown

    json_fail = mod.summarize_json(
        str(tmp_path / "broken.jsonl"),
        "not-json\n\nnot-json\nnot-json\nnot-json\nnot-json\n{\"late\": true}\n",
        160,
    )
    assert "Konnte JSON nicht parsen" in json_fail
    assert "not-json" in json_fail

    json_scalar = mod.summarize_json(str(tmp_path / "scalar.json"), "42", 200)
    assert "JSON-Inhalt erkannt" in json_scalar


@pytest.mark.scripts
@pytest.mark.unit
def test_walk_scope_skips_non_text_files_and_summary_errors(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    mod = _load_module()

    root = tmp_path / "scope"
    root.mkdir()
    (root / "skip.bin").write_bytes(b"\x00\x01")
    bad_text = root / "bad.txt"
    bad_text.write_text("content", encoding="utf-8")

    def _boom(path: str, max_chars: int = 1200) -> str:
        raise RuntimeError(f"boom: {path}:{max_chars}")

    monkeypatch.setattr(mod, "summarize_file", _boom)

    assert mod.walk_scope(str(root)) == []


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_1_for_invalid_and_empty_scopes(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    mod = _load_module()

    empty_scope = tmp_path / "empty"
    empty_scope.mkdir()

    monkeypatch.setitem(mod.SCOPES, "MISSING_SCOPE", str(tmp_path / "does-not-exist"))
    monkeypatch.setitem(mod.SCOPES, "EMPTY_SCOPE", str(empty_scope))

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.main(["--scopes", "MISSING_SCOPE,EMPTY_SCOPE", "--out-dir", str(tmp_path)])

    assert rc == 1
    assert "Keine Scopes gefunden oder keine Dateien" in buf.getvalue()


@pytest.mark.scripts
@pytest.mark.unit
def test_module_main_executes_via_runpy_on_error(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str], tmp_path: Path
) -> None:
    script_path = Path(__file__).resolve().parents[2] / "scripts" / "map_reduce_summary.py"

    monkeypatch.setattr(
        "sys.argv",
        [
            "map_reduce_summary.py",
            "--scopes",
            "UNKNOWN_SCOPE",
            "--out-dir",
            str(tmp_path),
        ],
    )

    with pytest.raises(SystemExit) as exc_info:
        runpy.run_path(str(script_path), run_name="__main__")

    assert exc_info.value.code == 1
    assert "Keine Scopes gefunden oder keine Dateien" in capsys.readouterr().out
