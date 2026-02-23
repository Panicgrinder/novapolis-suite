from __future__ import annotations

import importlib
import json
from pathlib import Path

import pytest


@pytest.mark.scripts
@pytest.mark.unit
def test_validate_model_policy_blocks_unknown_model() -> None:
    mod = importlib.import_module("scripts.tts_coqui_export")
    ok, reason = mod.validate_model_policy("tts_models/de/example", {"allowlisted_models": []})
    assert ok is False
    assert "not in allowlist" in reason


@pytest.mark.scripts
@pytest.mark.unit
def test_validate_model_policy_requires_local_license_file(tmp_path: Path) -> None:
    mod = importlib.import_module("scripts.tts_coqui_export")
    allowlist = {
        "default_action": "deny",
        "require_local_license_copy": True,
        "allowlisted_models": [
            {
                "id": "tts_models/de/safe",
                "approval_status": "approved",
                "license": "MIT",
                "license_file": str(tmp_path / "missing-license.txt"),
                "tos_required": False,
                "non_commercial": False,
                "no_derivatives": False,
            }
        ],
    }
    ok, reason = mod.validate_model_policy("tts_models/de/safe", allowlist)
    assert ok is False
    assert "license copy missing" in reason


@pytest.mark.scripts
@pytest.mark.unit
def test_main_blocks_with_empty_default_allowlist(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    mod = importlib.import_module("scripts.tts_coqui_export")

    input_file = tmp_path / "in.txt"
    voice_map = tmp_path / "voices.yaml"
    allowlist_file = tmp_path / "allowlist.json"

    input_file.write_text("hello", encoding="utf-8")
    voice_map.write_text("speaker: test", encoding="utf-8")
    allowlist_file.write_text(
        json.dumps(
            {
                "default_action": "deny",
                "require_local_license_copy": True,
                "allowlisted_models": [],
            }
        ),
        encoding="utf-8",
    )

    monkeypatch.setattr(
        mod,
        "build_parser",
        lambda: mod.argparse.ArgumentParser(add_help=False),
    )

    parser = mod.build_parser()
    parser.add_argument("--input")
    parser.add_argument("--voice-map")
    parser.add_argument("--model-id")
    parser.add_argument("--allowlist")
    parser.add_argument("--lang", default="de")
    parser.add_argument("--output-dir", default="out")
    parser.add_argument("--dry-run", action="store_true")

    monkeypatch.setattr(
        parser,
        "parse_args",
        lambda: type(
            "Args",
            (),
            {
                "input": str(input_file),
                "voice_map": str(voice_map),
                "model_id": "tts_models/de/unknown",
                "allowlist": str(allowlist_file),
                "lang": "de",
                "output_dir": str(tmp_path / "out"),
                "dry_run": True,
            },
        )(),
    )

    monkeypatch.setattr(mod, "build_parser", lambda: parser)
    rc = mod.main()
    assert rc == 3
