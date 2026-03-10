from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_optional_profile_detects_missing_package(tmp_path: Path) -> None:
    from scripts import check_dependency_profiles as mod

    script_file = tmp_path / "openai_tool.py"
    script_file.write_text("from openai import OpenAI\n", encoding="utf-8")

    req_file = tmp_path / "optional-tools.txt"
    req_file.write_text("rich\n", encoding="utf-8")

    result = mod.evaluate_optional_profile(
        repo_root=tmp_path,
        requirement_rel="optional-tools.txt",
        target_rels=("openai_tool.py",),
        module_to_package={"openai": "openai"},
    )

    assert result["missing"] == ["openai"]


@pytest.mark.scripts
@pytest.mark.unit
def test_optional_profile_ok_when_declared(tmp_path: Path) -> None:
    from scripts import check_dependency_profiles as mod

    script_file = tmp_path / "rich_tool.py"
    script_file.write_text("from rich.console import Console\n", encoding="utf-8")

    req_file = tmp_path / "optional-tools.txt"
    req_file.write_text("rich>=13\n", encoding="utf-8")

    result = mod.evaluate_optional_profile(
        repo_root=tmp_path,
        requirement_rel="optional-tools.txt",
        target_rels=("rich_tool.py",),
        module_to_package={"rich": "rich"},
    )

    assert result["missing"] == []
