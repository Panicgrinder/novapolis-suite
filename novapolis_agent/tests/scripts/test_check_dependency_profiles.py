from __future__ import annotations

import sys
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_parse_requirement_names_handles_versions_and_comments(tmp_path: Path) -> None:
    from scripts import check_dependency_profiles as mod

    req = tmp_path / "optional-tools.txt"
    req.write_text(
        "\n".join(
            [
                "# comment",
                "openai>=1.0",
                "rich==13.7.0 ; python_version >= '3.11'",
                "pypdf[extra]",
                "",
            ]
        ),
        encoding="utf-8",
    )

    names = mod.parse_requirement_names(req)
    assert names == {"openai", "rich", "pypdf"}


@pytest.mark.scripts
@pytest.mark.unit
def test_parse_requirement_names_missing_file_returns_empty(tmp_path: Path) -> None:
    from scripts import check_dependency_profiles as mod

    assert mod.parse_requirement_names(tmp_path / "missing.txt") == set()


@pytest.mark.scripts
@pytest.mark.unit
def test_imported_top_modules_collects_imports(tmp_path: Path) -> None:
    from scripts import check_dependency_profiles as mod

    py = tmp_path / "x.py"
    py.write_text(
        "import openai\nfrom rich.console import Console\nfrom pypdf import PdfReader\n",
        encoding="utf-8",
    )

    mods = mod.imported_top_modules(py)
    assert {"openai", "rich", "pypdf"}.issubset(mods)


@pytest.mark.scripts
@pytest.mark.unit
def test_evaluate_optional_profile_reports_missing_and_extra(tmp_path: Path) -> None:
    from scripts import check_dependency_profiles as mod

    req = tmp_path / "req.txt"
    req.write_text("openai\nunknown_pkg\n", encoding="utf-8")

    target = tmp_path / "script.py"
    target.write_text("from rich.console import Console\n", encoding="utf-8")

    result = mod.evaluate_optional_profile(
        tmp_path,
        "req.txt",
        ("script.py",),
        {"openai": "openai", "rich": "rich", "pypdf": "pypdf"},
    )

    assert result["missing"] == ["rich"]
    assert result["extra"] == ["unknown_pkg"]
    assert result["used"] == ["rich"]


@pytest.mark.scripts
@pytest.mark.unit
def test_evaluate_optional_profile_ok_when_declared(tmp_path: Path) -> None:
    from scripts import check_dependency_profiles as mod

    req = tmp_path / "req.txt"
    req.write_text("rich>=13\n", encoding="utf-8")
    target = tmp_path / "script.py"
    target.write_text("from rich.console import Console\n", encoding="utf-8")

    result = mod.evaluate_optional_profile(
        repo_root=tmp_path,
        requirement_rel="req.txt",
        target_rels=("script.py",),
        module_to_package={"rich": "rich"},
    )

    assert result["missing"] == []


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_0_without_strict_on_warnings(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from scripts import check_dependency_profiles as mod

    req = tmp_path / "req.txt"
    req.write_text("openai\n", encoding="utf-8")
    target = tmp_path / "script.py"
    target.write_text("from rich.console import Console\n", encoding="utf-8")

    monkeypatch.setattr(mod, "DEFAULT_TARGETS", ("script.py",))
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "check_dependency_profiles.py",
            "--repo-root",
            str(tmp_path),
            "--requirements-file",
            "req.txt",
        ],
    )

    assert mod.main() == 0


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_1_with_strict_on_warnings(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from scripts import check_dependency_profiles as mod

    req = tmp_path / "req.txt"
    req.write_text("openai\n", encoding="utf-8")
    target = tmp_path / "script.py"
    target.write_text("from rich.console import Console\n", encoding="utf-8")

    monkeypatch.setattr(mod, "DEFAULT_TARGETS", ("script.py",))
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "check_dependency_profiles.py",
            "--repo-root",
            str(tmp_path),
            "--requirements-file",
            "req.txt",
            "--strict",
        ],
    )

    assert mod.main() == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_main_returns_0_when_profile_consistent(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from scripts import check_dependency_profiles as mod

    req = tmp_path / "req.txt"
    req.write_text("openai\nrich\n", encoding="utf-8")
    target = tmp_path / "script.py"
    target.write_text("import openai\nfrom rich.console import Console\n", encoding="utf-8")

    monkeypatch.setattr(mod, "DEFAULT_TARGETS", ("script.py",))
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "check_dependency_profiles.py",
            "--repo-root",
            str(tmp_path),
            "--requirements-file",
            "req.txt",
        ],
    )

    assert mod.main() == 0
