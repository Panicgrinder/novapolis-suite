from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_scan_legacy_imports_flags_disallowed(tmp_path: Path) -> None:
    from scripts import check_legacy_shim_imports as mod

    target = tmp_path / "novapolis_agent" / "scripts"
    target.mkdir(parents=True, exist_ok=True)
    f = target / "tool.py"
    f.write_text("import app.prompt\n", encoding="utf-8")

    allowed, disallowed = mod.scan_legacy_imports(
        repo_root=tmp_path,
        include_globs=("novapolis_agent/**/*.py",),
        allowlist=(),
    )

    assert allowed == []
    assert len(disallowed) == 1
    assert "import app.prompt" in disallowed[0]


@pytest.mark.scripts
@pytest.mark.unit
def test_scan_legacy_imports_honors_allowlist(tmp_path: Path) -> None:
    from scripts import check_legacy_shim_imports as mod

    target = tmp_path / "novapolis_agent" / "tests"
    target.mkdir(parents=True, exist_ok=True)
    f = target / "test_module_exports.py"
    f.write_text("from app.api.api import router\n", encoding="utf-8")

    allowed, disallowed = mod.scan_legacy_imports(
        repo_root=tmp_path,
        include_globs=("novapolis_agent/**/*.py",),
        allowlist=("novapolis_agent/tests/test_module_exports.py",),
    )

    assert len(allowed) == 1
    assert disallowed == []
