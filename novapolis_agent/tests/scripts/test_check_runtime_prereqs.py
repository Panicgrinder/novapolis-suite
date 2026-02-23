from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_prereqs_ok(tmp_path: Path) -> None:
    from scripts import check_runtime_prereqs as mod

    (tmp_path / "novapolis_agent" / "app").mkdir(parents=True)
    (tmp_path / "novapolis_agent" / "run_server.py").write_text("", encoding="utf-8")
    (tmp_path / "novapolis_agent" / "app" / "main.py").write_text("", encoding="utf-8")

    data = mod.collect_prereqs(repo_root=tmp_path, strict_venv=False)
    assert data["checks"]["python"]["ok"] is True
    assert data["checks"]["required_files"]["ok"] is True
    assert data["ok"] is True


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_prereqs_missing_files_fails(tmp_path: Path) -> None:
    from scripts import check_runtime_prereqs as mod

    data = mod.collect_prereqs(repo_root=tmp_path, strict_venv=False)
    assert data["checks"]["required_files"]["ok"] is False
    assert data["ok"] is False


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_prereqs_strict_venv_enforced(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    from scripts import check_runtime_prereqs as mod

    (tmp_path / "novapolis_agent" / "app").mkdir(parents=True)
    (tmp_path / "novapolis_agent" / "run_server.py").write_text("", encoding="utf-8")
    (tmp_path / "novapolis_agent" / "app" / "main.py").write_text("", encoding="utf-8")

    monkeypatch.setattr(mod, "_is_venv_active", lambda: False)
    data = mod.collect_prereqs(repo_root=tmp_path, strict_venv=True)
    assert data["checks"]["venv"]["ok"] is False
    assert data["ok"] is False
