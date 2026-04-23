from __future__ import annotations

import argparse
import configparser
import json
import re
from pathlib import Path
from typing import Any


DEFAULT_FIXTURE_DIR = "novapolis-sim/tests/fixtures/hub_prefs"
EXPECTED_KEYS = {
    "show_sim_card",
    "show_api_card",
    "show_eval_card",
    "default_panel",
    "refresh_profile",
    "session_id",
    "scene_id",
    "resume_checkpoint_id",
    "selected_replay_checkpoint_id",
}


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Static contract check for novapolis-sim hub_prefs")
    parser.add_argument("--repo-root", default=Path(__file__).resolve().parents[1])
    parser.add_argument("--fixture-dir", default=DEFAULT_FIXTURE_DIR)
    return parser.parse_args(argv)


def _extract_function_block(source_text: str, func_name: str) -> str:
    marker = f"func {func_name}"
    start = source_text.find(marker)
    if start == -1:
        raise ValueError(f"missing function {func_name}")
    tail = source_text[start:]
    next_func = tail.find("\nfunc ", len(marker))
    return tail if next_func == -1 else tail[:next_func]


def _extract_pref_keys(source_text: str, func_name: str, call_name: str) -> set[str]:
    block = _extract_function_block(source_text, func_name)
    call_pos = block.find(call_name)
    call_block = block[call_pos:] if call_pos != -1 else block
    next_paren = call_block.find("\n\t)")
    relevant = call_block if next_paren == -1 else call_block[:next_paren]
    return set(re.findall(r'"([a-z_]+)"\s*:', relevant))


def _coerce_like_default(raw: str, default: Any) -> Any:
    if isinstance(default, bool):
        return raw.strip().lower() in {"1", "true", "yes"}
    return raw.strip().strip('"')


def _load_fixture(path: Path, defaults: dict[str, Any]) -> dict[str, Any]:
    values = dict(defaults)
    parser = configparser.ConfigParser()
    parser.read(path, encoding="utf-8")
    if not parser.has_section("hub"):
        return values
    for key, default in defaults.items():
        if parser.has_option("hub", key):
            values[key] = _coerce_like_default(parser.get("hub", key), default)
    return values


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)
    repo_root = Path(args.repo_root).resolve()
    main_gd = repo_root / "novapolis-sim" / "scripts" / "Main.gd"
    fixture_dir = (repo_root / args.fixture_dir).resolve()

    source_text = main_gd.read_text(encoding="utf-8")
    load_keys = _extract_pref_keys(source_text, "_load_hub_preferences", "load_preferences(")
    save_keys = _extract_pref_keys(source_text, "_save_hub_preferences", "save_preferences(")
    errors: list[str] = []

    if load_keys != save_keys:
        errors.append(f"load/save key drift: load={sorted(load_keys)}, save={sorted(save_keys)}")
    if load_keys != EXPECTED_KEYS:
        errors.append(f"unexpected hub prefs key set: {sorted(load_keys)}")

    defaults = {
        "show_sim_card": True,
        "show_api_card": True,
        "show_eval_card": True,
        "default_panel": "live",
        "refresh_profile": "normal",
        "session_id": "sim-hub-default",
        "scene_id": "scene-default",
        "resume_checkpoint_id": "resume-default",
        "selected_replay_checkpoint_id": "resume-default",
    }

    empty_values = _load_fixture(fixture_dir / "empty.cfg", defaults)
    if empty_values != defaults:
        errors.append("empty fixture does not fall back to defaults")

    partial_values = _load_fixture(fixture_dir / "partial.cfg", defaults)
    if partial_values["session_id"] != "sim-hub-existing" or partial_values["default_panel"] != "chat":
        errors.append("partial fixture does not preserve stored session/default_panel values")
    if partial_values["resume_checkpoint_id"] != defaults["resume_checkpoint_id"]:
        errors.append("partial fixture should keep default resume checkpoint")

    legacy_values = _load_fixture(fixture_dir / "legacy.cfg", defaults)
    if legacy_values["refresh_profile"] != "slow" or legacy_values["selected_replay_checkpoint_id"] != "slot-03":
        errors.append("legacy fixture does not preserve refresh_profile or replay checkpoint")
    if legacy_values["session_id"] != defaults["session_id"]:
        errors.append("legacy fixture should fall back to default session_id")

    if errors:
        print(json.dumps({"ok": False, "errors": errors}, ensure_ascii=False))
        return 1

    print(
        json.dumps(
            {
                "ok": True,
                "keys": sorted(load_keys),
                "fixtures": ["empty.cfg", "partial.cfg", "legacy.cfg"],
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())