from __future__ import annotations

import contextlib
import importlib
import io
import os
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_customize_unrestricted_prompt_missing_block(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    mod = importlib.import_module("scripts.customize_prompts")
    prompts_file = tmp_path / "prompts.py"
    prompts_file.write_text('DEFAULT_SYSTEM_PROMPT = "x"\n', encoding="utf-8")
    monkeypatch.setattr(mod, "PROMPTS_FILE", os.fspath(prompts_file), raising=False)

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod.customize_unrestricted_prompt()
    assert "nicht finden" in buf.getvalue()


@pytest.mark.scripts
@pytest.mark.unit
def test_customize_unrestricted_prompt_empty_input_no_changes(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    mod = importlib.import_module("scripts.customize_prompts")
    prompts_file = tmp_path / "prompts.py"
    prompts_file.write_text('UNRESTRICTED_SYSTEM_PROMPT = """ALT"""\n', encoding="utf-8")
    monkeypatch.setattr(mod, "PROMPTS_FILE", os.fspath(prompts_file), raising=False)

    # immediate EOF -> empty input
    monkeypatch.setattr("builtins.input", lambda prompt="": (_ for _ in ()).throw(EOFError()))

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod.customize_unrestricted_prompt()
    assert "Keine Änderungen vorgenommen" in buf.getvalue()
    assert "ALT" in prompts_file.read_text(encoding="utf-8")


@pytest.mark.scripts
@pytest.mark.unit
def test_create_content_rules_invalid_load_and_inputs(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    mod = importlib.import_module("scripts.customize_prompts")
    project_root = tmp_path
    app_core = project_root / "app" / "core"
    app_core.mkdir(parents=True, exist_ok=True)
    rules_file = app_core / "content_rules.json"
    rules_file.write_text("{broken", encoding="utf-8")

    monkeypatch.setattr(mod, "project_root", os.fspath(project_root), raising=False)

    inputs = iter(
        [
            "ohne-doppelpunkt",
            "Kategorie: vielleicht",
            "Kategorie: erlaubt",
            "fertig",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda prompt="": next(inputs))

    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        mod.create_content_rules()
    out = buf.getvalue()
    assert "Fehler beim Laden" in out
    assert "Ungültiges Format" in out
    assert "Ungültiger Wert" in out


@pytest.mark.scripts
@pytest.mark.unit
def test_customize_prompts_main_flag_dispatch(monkeypatch: pytest.MonkeyPatch) -> None:
    mod = importlib.import_module("scripts.customize_prompts")
    calls: list[str] = []

    monkeypatch.setattr(mod, "customize_unrestricted_prompt", lambda: calls.append("u"))
    monkeypatch.setattr(mod, "create_content_rules", lambda: calls.append("r"))

    argv_backup = mod.sys.argv[:]
    try:
        mod.sys.argv = ["customize_prompts.py", "--customize-unrestricted"]
        mod.main()
        mod.sys.argv = ["customize_prompts.py", "--create-rules"]
        mod.main()
    finally:
        mod.sys.argv = argv_backup

    assert calls == ["u", "r"]
