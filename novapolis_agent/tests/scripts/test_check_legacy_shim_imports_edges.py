from __future__ import annotations

import contextlib
import io
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_module_is_legacy_prefix_and_non_legacy() -> None:
    from scripts import check_legacy_shim_imports as mod

    assert mod._module_is_legacy("app.prompt") is True
    assert mod._module_is_legacy("app.prompt.sub") is True
    assert mod._module_is_legacy("x.app.prompt") is False


@pytest.mark.scripts
@pytest.mark.unit
def test_collect_legacy_imports_importfrom_without_module_is_ignored(tmp_path: Path) -> None:
    from scripts import check_legacy_shim_imports as mod

    f = tmp_path / "a.py"
    f.write_text("from . import x\n", encoding="utf-8")
    hits = mod._collect_legacy_imports(f, tmp_path)
    assert hits == []


@pytest.mark.scripts
@pytest.mark.unit
def test_scan_legacy_imports_deduplicates_files_across_globs(tmp_path: Path) -> None:
    from scripts import check_legacy_shim_imports as mod

    d = tmp_path / "scripts"
    d.mkdir(parents=True, exist_ok=True)
    f = d / "x.py"
    f.write_text("import app.utils.examples\n", encoding="utf-8")

    allowed, disallowed = mod.scan_legacy_imports(
        repo_root=tmp_path,
        include_globs=("scripts/**/*.py", "**/*.py"),
        allowlist=(),
    )
    assert allowed == []
    assert len(disallowed) == 1


@pytest.mark.scripts
@pytest.mark.unit
def test_main_strict_returns_one_with_disallowed(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    from types import SimpleNamespace

    from scripts import check_legacy_shim_imports as mod

    p = tmp_path / "novapolis_agent" / "x.py"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("from app.prompt import y\n", encoding="utf-8")

    monkeypatch.setattr(
        mod,
        "scan_legacy_imports",
        lambda _root: ([], ["novapolis_agent/x.py:1: from app.prompt import ..."]),
    )
    monkeypatch.setattr(
        mod.argparse.ArgumentParser,
        "parse_args",
        lambda self: SimpleNamespace(repo_root=str(tmp_path), strict=True),
    )

    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        rc = mod.main()
    assert rc == 1
    assert "disallowed_hits: 1" in out.getvalue()


@pytest.mark.scripts
@pytest.mark.unit
def test_main_non_strict_returns_zero(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from types import SimpleNamespace

    from scripts import check_legacy_shim_imports as mod

    monkeypatch.setattr(mod, "scan_legacy_imports", lambda _root: (["a"], ["b"]))
    monkeypatch.setattr(
        mod.argparse.ArgumentParser,
        "parse_args",
        lambda self: SimpleNamespace(repo_root=str(tmp_path), strict=False),
    )

    rc = mod.main()
    assert rc == 0
