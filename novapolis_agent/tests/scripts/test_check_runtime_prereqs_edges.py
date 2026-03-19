from __future__ import annotations

import contextlib
import io
from pathlib import Path
from types import SimpleNamespace

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_prereqs_python_too_low(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from scripts import check_runtime_prereqs as mod

    monkeypatch.setattr(mod.sys, "version_info", SimpleNamespace(major=3, minor=10, micro=9))
    monkeypatch.setattr(mod, "_is_venv_active", lambda: True)

    (tmp_path / "novapolis_agent" / "app").mkdir(parents=True, exist_ok=True)
    (tmp_path / "novapolis_agent" / "run_server.py").write_text("", encoding="utf-8")
    (tmp_path / "novapolis_agent" / "app" / "main.py").write_text("", encoding="utf-8")

    data = mod.collect_prereqs(repo_root=tmp_path, strict_venv=False)
    assert data["checks"]["python"]["ok"] is False
    assert data["ok"] is False


@pytest.mark.scripts
@pytest.mark.unit
def test_build_parser_defaults() -> None:
    from scripts import check_runtime_prereqs as mod

    parser = mod.build_parser()
    args = parser.parse_args([])
    assert args.repo_root == "."
    assert args.strict_venv is False
    assert args.json is False


@pytest.mark.scripts
@pytest.mark.unit
def test_main_json_output(monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import check_runtime_prereqs as mod

    monkeypatch.setattr(
        mod.argparse.ArgumentParser,
        "parse_args",
        lambda self: SimpleNamespace(repo_root=".", strict_venv=False, json=True),
    )
    monkeypatch.setattr(
        mod,
        "collect_prereqs",
        lambda repo_root, strict_venv: {
            "ok": True,
            "repo_root": str(repo_root),
            "checks": {"python": {"ok": True}},
        },
    )

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.main()
    assert rc == 0
    assert '"ok": true' in buf.getvalue().lower()


@pytest.mark.scripts
@pytest.mark.unit
def test_main_text_output_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import check_runtime_prereqs as mod

    monkeypatch.setattr(
        mod.argparse.ArgumentParser,
        "parse_args",
        lambda self: SimpleNamespace(repo_root=".", strict_venv=True, json=False),
    )
    monkeypatch.setattr(
        mod,
        "collect_prereqs",
        lambda repo_root, strict_venv: {
            "ok": False,
            "repo_root": str(repo_root),
            "checks": {"python": {"ok": True}, "venv": {"ok": False}},
        },
    )

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = mod.main()
    out = buf.getvalue()
    assert "Runtime prerequisites" in out
    assert "- venv: False" in out
    assert rc == 1
