from __future__ import annotations

import json
import sys
import types
from builtins import __import__ as py_import
from pathlib import Path
from typing import ClassVar

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_load_sources_collects_existing_and_missing_required(tmp_path: Path) -> None:
    from scripts import build_project_context_index as mod

    existing = tmp_path / "docs" / "a.md"
    existing.parent.mkdir(parents=True, exist_ok=True)
    existing.write_text("hello", encoding="utf-8")

    cfg = tmp_path / "sources.json"
    cfg.write_text(
        json.dumps(
            {
                "sources": [
                    {"path": "docs/a.md", "required": True},
                    {"path": "docs/missing.md", "required": True},
                    {"path": "docs/optional-missing.md", "required": False},
                    {"path": "", "required": True},
                    "invalid",
                ]
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    mod._repo_root = lambda: tmp_path  # type: ignore[assignment]
    include, missing_required = mod._load_sources(cfg)

    assert include == [existing.resolve()]
    assert missing_required == [(tmp_path / "docs/missing.md").resolve()]


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_2_when_sources_file_missing(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_project_context_index as mod

    mod._repo_root = lambda: tmp_path  # type: ignore[assignment]
    rc = mod.main(["--sources-file", "missing.json"])

    out = capsys.readouterr().out
    assert rc == 2
    assert "sources file not found" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_3_for_missing_required(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_project_context_index as mod

    cfg = tmp_path / "sources.json"
    cfg.write_text(
        json.dumps({"sources": [{"path": "docs/missing.md", "required": True}]}),
        encoding="utf-8",
    )

    mod._repo_root = lambda: tmp_path  # type: ignore[assignment]
    rc = mod.main(["--sources-file", "sources.json"])

    out = capsys.readouterr().out
    assert rc == 3
    assert "missing required sources" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_4_when_no_existing_sources(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_project_context_index as mod

    cfg = tmp_path / "sources.json"
    cfg.write_text(
        json.dumps({"sources": [{"path": "docs/missing.md", "required": False}]}),
        encoding="utf-8",
    )

    mod._repo_root = lambda: tmp_path  # type: ignore[assignment]
    rc = mod.main(["--sources-file", "sources.json"])

    out = capsys.readouterr().out
    assert rc == 4
    assert "no existing sources" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_5_when_import_fails(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from scripts import build_project_context_index as mod

    src = tmp_path / "docs" / "exists.md"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text("x", encoding="utf-8")

    cfg = tmp_path / "sources.json"
    cfg.write_text(
        json.dumps({"sources": [{"path": "docs/exists.md", "required": True}]}),
        encoding="utf-8",
    )

    mod._repo_root = lambda: tmp_path  # type: ignore[assignment]

    def fake_import(name: str, globals=None, locals=None, fromlist=(), level=0):  # type: ignore[no-untyped-def]
        if name == "utils.rag":
            raise ImportError("forced import failure")
        return py_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr("builtins.__import__", fake_import)
    rc = mod.main(["--sources-file", "sources.json"])

    out = capsys.readouterr().out
    assert rc == 5
    assert "failed to import rag utils" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_main_success_writes_summary_and_index(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from scripts import build_project_context_index as mod

    src = tmp_path / "docs" / "exists.md"
    src.parent.mkdir(parents=True, exist_ok=True)
    src.write_text("source", encoding="utf-8")

    cfg = tmp_path / "sources.json"
    cfg.write_text(
        json.dumps({"sources": [{"path": "docs/exists.md", "required": True}]}),
        encoding="utf-8",
    )

    mod._repo_root = lambda: tmp_path  # type: ignore[assignment]

    class DummyIndex:
        n_docs: ClassVar[int] = 1
        df: ClassVar[dict[str, int]] = {"x": 1, "y": 2}

    rag_mod = types.ModuleType("utils.rag")
    captured: dict[str, object] = {}

    def build_index(paths: list[str]) -> DummyIndex:
        captured["paths"] = paths
        return DummyIndex()

    def save_index(idx: DummyIndex, out_path: str) -> None:
        captured["out"] = out_path
        Path(out_path).write_text("saved", encoding="utf-8")

    rag_mod.build_index = build_index  # type: ignore[attr-defined]
    rag_mod.save_index = save_index  # type: ignore[attr-defined]

    utils_pkg = types.ModuleType("utils")
    saved_modules = dict(sys.modules)
    sys.modules["utils"] = utils_pkg
    sys.modules["utils.rag"] = rag_mod
    try:
        rc = mod.main(["--sources-file", "sources.json", "--out", "out/index.json"])
    finally:
        sys.modules.clear()
        sys.modules.update(saved_modules)

    out = capsys.readouterr().out.strip()
    summary = json.loads(out)

    assert rc == 0
    assert captured["paths"] == [str(src.resolve())]
    assert str(captured["out"]).endswith("out\\index.json")
    assert summary["indexed_sources"] == 1
    assert summary["n_docs"] == 1
    assert summary["vocab"] == 2
    assert str(summary["out"]).replace("\\", "/") == "out/index.json"
