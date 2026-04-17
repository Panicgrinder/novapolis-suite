from __future__ import annotations

from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_agent_wrapper_compat_package_mirrors_root_wrappers() -> None:
    repo_root = Path(__file__).resolve().parents[3]
    root_wrapper_dir = repo_root / "scripts" / "agent"
    compat_wrapper_dir = repo_root / "novapolis_agent" / "scripts" / "agent"

    root_public = {
        path.stem
        for path in root_wrapper_dir.glob("*.py")
        if path.name != "__init__.py" and not path.name.startswith("_")
    }
    compat_public = {
        path.stem
        for path in compat_wrapper_dir.glob("*.py")
        if path.name != "__init__.py" and not path.name.startswith("_")
    }

    missing = sorted(root_public - compat_public)
    extra = sorted(compat_public - root_public)
    assert (
        compat_public == root_public
    ), f"compat wrapper drift detected; missing={missing}, extra={extra}"
