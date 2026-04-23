from __future__ import annotations

from pathlib import Path

import pytest

from scripts import check_sim_hub_prefs_contract as mod


@pytest.mark.scripts
@pytest.mark.unit
def test_hub_prefs_contract_passes_repo_fixtures() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    assert mod.main(["--repo-root", str(repo_root)]) == 0


@pytest.mark.scripts
@pytest.mark.unit
def test_hub_prefs_contract_detects_key_drift(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    fixture_dir = repo_root / "fixtures"
    scripts_dir = repo_root / "novapolis-sim" / "scripts"
    scripts_dir.mkdir(parents=True)
    fixture_dir.mkdir(parents=True)
    (scripts_dir / "Main.gd").write_text(
        'func _load_hub_preferences() -> void:\n\tvar values = {"session_id": "x"}\n\nfunc _save_hub_preferences(silent: bool = false) -> void:\n\tvar values = {"scene_id": "y"}\n',
        encoding="utf-8",
    )
    for name in ("empty.cfg", "partial.cfg", "legacy.cfg"):
        (fixture_dir / name).write_text("[hub]\n", encoding="utf-8")

    assert mod.main(["--repo-root", str(repo_root), "--fixture-dir", str(fixture_dir)]) == 1