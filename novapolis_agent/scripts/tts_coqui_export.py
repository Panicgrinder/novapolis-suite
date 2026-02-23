#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_ALLOWLIST_PATH = Path("novapolis_agent/config/tts_model_allowlist.json")


def load_allowlist(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"allowlist file not found: {path}")
    with path.open("r", encoding="utf-8") as fh:
        data = json.load(fh)
    if not isinstance(data, dict):
        raise ValueError("allowlist must be a JSON object")
    models = data.get("allowlisted_models", [])
    if not isinstance(models, list):
        raise ValueError("allowlisted_models must be a list")
    return data


def validate_model_policy(model_id: str, allowlist: dict[str, Any]) -> tuple[bool, str]:
    default_action = str(allowlist.get("default_action", "deny")).lower()
    require_license_copy = bool(allowlist.get("require_local_license_copy", True))

    for model in allowlist.get("allowlisted_models", []):
        if not isinstance(model, dict):
            continue
        if model.get("id") != model_id:
            continue

        if str(model.get("approval_status", "blocked")).lower() != "approved":
            return False, f"model '{model_id}' is not approved"

        if bool(model.get("tos_required", False)):
            return False, f"model '{model_id}' requires TOS acceptance and is blocked by policy"

        if bool(model.get("non_commercial", False)):
            return False, f"model '{model_id}' is non-commercial and is blocked by policy"

        if bool(model.get("no_derivatives", False)):
            return False, f"model '{model_id}' disallows derivatives and is blocked by policy"

        if require_license_copy:
            license_file = str(model.get("license_file", "")).strip()
            if not license_file:
                return False, f"model '{model_id}' has no local license_file"
            if not Path(license_file).exists():
                return False, f"model '{model_id}' license copy missing: {license_file}"

        return True, f"model '{model_id}' is approved"

    if default_action == "allow":
        return True, f"model '{model_id}' allowed by default_action=allow"
    return False, f"model '{model_id}' is not in allowlist"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Build-time TTS exporter skeleton with strict compliance gating."
    )
    parser.add_argument("--input", required=True, help="Path to jsonl|yaml|txt source input")
    parser.add_argument("--voice-map", required=True, help="Path to YAML voice mapping")
    parser.add_argument("--model-id", required=True, help="Model identifier to be validated against allowlist")
    parser.add_argument(
        "--allowlist",
        default=str(DEFAULT_ALLOWLIST_PATH),
        help="Path to strict model allowlist JSON",
    )
    parser.add_argument("--lang", default="de", help="Language code, default: de")
    parser.add_argument(
        "--output-dir",
        default="novapolis-sim/assets/voiceovers/de/",
        help="Target directory for generated OGG files",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate arguments and planned I/O without running synthesis",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    input_path = Path(args.input)
    voice_map_path = Path(args.voice_map)
    output_dir = Path(args.output_dir)
    allowlist_path = Path(args.allowlist)

    if not input_path.exists():
        print(f"ERROR: input file not found: {input_path}")
        return 1
    if not voice_map_path.exists():
        print(f"ERROR: voice-map file not found: {voice_map_path}")
        return 1

    try:
        allowlist = load_allowlist(allowlist_path)
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: invalid allowlist: {exc}")
        return 1

    is_allowed, reason = validate_model_policy(args.model_id, allowlist)
    if not is_allowed:
        print(f"BLOCKED: {reason}")
        print("Policy is deny-by-default. Add explicit approved entry with local license copy.")
        return 3

    print("TTS exporter skeleton")
    print(f"  input:      {input_path}")
    print(f"  voice-map:  {voice_map_path}")
    print(f"  model-id:   {args.model_id}")
    print(f"  lang:       {args.lang}")
    print(f"  output-dir: {output_dir}")
    print(f"  allowlist:  {allowlist_path}")
    print(f"  policy:     {reason}")

    if args.dry_run:
        print("DRY-RUN: contract and paths are valid; synthesis is intentionally not executed yet.")
        return 0

    print("NOT IMPLEMENTED: synthesis engine integration is pending (see todo.agent-board.md).")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
