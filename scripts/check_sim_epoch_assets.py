"""Offline validation for Sim epoch logs and optional OGG naming scheme.

This script is designed for tunnel/remote workflows where GUI-driven Godot checks
are impractical. It validates file structure and basic parseability only.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path


EPOCH_DIR_RE = re.compile(r"^epoch\d+$", re.IGNORECASE)
AUDIO_FILE_RE = re.compile(r"^epoch(\d{2})_slot(\d{2})_(pc|world)\.ogg$", re.IGNORECASE)
SLOT_KEYS = ("slot", "time_slot", "slot_index", "slot_id", "hour", "h")


@dataclass(frozen=True)
class CheckMessage:
    level: str
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate offline Sim epoch assets.")
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--epochs-dir",
        default="novapolis-sim/data/epochs",
        help="Path (relative to repo root) containing epoch folders.",
    )
    parser.add_argument(
        "--audio-dir",
        default="novapolis-sim/assets/audio",
        help="Path (relative to repo root) containing OGG files.",
    )
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="Pass when no epoch folders are present (useful for initial setup).",
    )
    parser.add_argument(
        "--check-slot-consistency",
        action="store_true",
        help=(
            "Enable optional slot consistency checks between world_log and pc_log "
            "(expected slot range 0..23)."
        ),
    )
    return parser.parse_args()


def _coerce_slot(value: object) -> int | None:
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    if isinstance(value, str):
        clean = value.strip()
        if clean.isdigit():
            return int(clean)
    return None


def _extract_slot(entry: dict) -> int | None:
    for key in SLOT_KEYS:
        if key in entry:
            slot = _coerce_slot(entry[key])
            if slot is not None:
                return slot

    for nested_key in ("meta", "payload", "data", "context"):
        nested = entry.get(nested_key)
        if isinstance(nested, dict):
            for key in SLOT_KEYS:
                if key in nested:
                    slot = _coerce_slot(nested[key])
                    if slot is not None:
                        return slot
    return None


def _collect_slots(entries: list[dict]) -> tuple[set[int], int]:
    slots: set[int] = set()
    missing = 0
    for entry in entries:
        slot = _extract_slot(entry)
        if slot is None:
            missing += 1
            continue
        slots.add(slot)
    return slots, missing


def _validate_slot_consistency(epoch_name: str, world_entries: list[dict], pc_entries: list[dict]) -> list[CheckMessage]:
    messages: list[CheckMessage] = []

    world_slots, world_missing = _collect_slots(world_entries)
    pc_slots, pc_missing = _collect_slots(pc_entries)

    invalid_world = sorted(slot for slot in world_slots if slot < 0 or slot > 23)
    invalid_pc = sorted(slot for slot in pc_slots if slot < 0 or slot > 23)

    if invalid_world:
        messages.append(
            CheckMessage(
                "FAIL",
                f"{epoch_name}: world_log has invalid slot values outside 0..23: {invalid_world}",
            )
        )
    if invalid_pc:
        messages.append(
            CheckMessage(
                "FAIL",
                f"{epoch_name}: pc_log has invalid slot values outside 0..23: {invalid_pc}",
            )
        )

    if world_entries and not world_slots:
        messages.append(CheckMessage("FAIL", f"{epoch_name}: world_log has entries but no detectable slot values"))
    if pc_entries and not pc_slots:
        messages.append(CheckMessage("FAIL", f"{epoch_name}: pc_log has entries but no detectable slot values"))

    only_world = sorted(world_slots - pc_slots)
    only_pc = sorted(pc_slots - world_slots)
    if only_world or only_pc:
        messages.append(
            CheckMessage(
                "FAIL",
                (
                    f"{epoch_name}: slot mismatch world_vs_pc "
                    f"(only_world={only_world}, only_pc={only_pc})"
                ),
            )
        )
    else:
        messages.append(
            CheckMessage(
                "INFO",
                f"{epoch_name}: slot consistency OK (slots={sorted(world_slots)})",
            )
        )

    if world_missing > 0:
        messages.append(CheckMessage("WARN", f"{epoch_name}: world_log entries without slot key: {world_missing}"))
    if pc_missing > 0:
        messages.append(CheckMessage("WARN", f"{epoch_name}: pc_log entries without slot key: {pc_missing}"))

    return messages


def load_json_lines(path: Path) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(path)

    raw_text = path.read_text(encoding="utf-8")
    stripped = raw_text.strip()

    if stripped == "":
        return []

    if stripped.startswith("["):
        parsed = json.loads(stripped)
        if not isinstance(parsed, list):
            raise ValueError(f"{path} must contain a JSON array or JSONL entries")
        return [item for item in parsed if isinstance(item, dict)]

    entries: list[dict] = []
    for line_number, line in enumerate(raw_text.splitlines(), start=1):
        clean_line = line.strip()
        if clean_line == "":
            continue
        try:
            parsed_line = json.loads(clean_line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number} invalid JSONL: {exc.msg}") from exc
        if isinstance(parsed_line, dict):
            entries.append(parsed_line)
    return entries


def collect_epoch_dirs(epochs_root: Path) -> list[Path]:
    if not epochs_root.exists() or not epochs_root.is_dir():
        return []
    epoch_dirs = [item for item in epochs_root.iterdir() if item.is_dir() and EPOCH_DIR_RE.match(item.name)]
    return sorted(epoch_dirs, key=lambda path: path.name.lower())


def validate_epoch_folder(epoch_dir: Path, *, check_slot_consistency: bool = False) -> list[CheckMessage]:
    messages: list[CheckMessage] = []
    world_log = epoch_dir / "world_log.jsonl"
    pc_log = epoch_dir / "pc_log.jsonl"

    try:
        world_entries = load_json_lines(world_log)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        messages.append(CheckMessage("FAIL", f"{epoch_dir.name}: world_log.jsonl invalid/missing ({exc})"))
        world_entries = []

    try:
        pc_entries = load_json_lines(pc_log)
    except (FileNotFoundError, ValueError, json.JSONDecodeError) as exc:
        messages.append(CheckMessage("FAIL", f"{epoch_dir.name}: pc_log.jsonl invalid/missing ({exc})"))
        pc_entries = []

    if world_entries or pc_entries:
        messages.append(
            CheckMessage(
                "INFO",
                f"{epoch_dir.name}: world={len(world_entries)} entries, pc={len(pc_entries)} entries",
            )
        )

    if check_slot_consistency:
        messages.extend(_validate_slot_consistency(epoch_dir.name, world_entries, pc_entries))

    return messages


def validate_audio_dir(audio_root: Path) -> list[CheckMessage]:
    messages: list[CheckMessage] = []

    if not audio_root.exists():
        messages.append(CheckMessage("WARN", f"audio directory missing: {audio_root.as_posix()}"))
        return messages
    if not audio_root.is_dir():
        messages.append(CheckMessage("FAIL", f"audio path is not a directory: {audio_root.as_posix()}"))
        return messages

    ogg_files = sorted([item for item in audio_root.iterdir() if item.is_file() and item.suffix.lower() == ".ogg"])
    if not ogg_files:
        messages.append(CheckMessage("WARN", "no .ogg files found (naming check skipped)"))
        return messages

    invalid_names = [file_path.name for file_path in ogg_files if not AUDIO_FILE_RE.match(file_path.name)]
    if invalid_names:
        for invalid_name in invalid_names:
            messages.append(
                CheckMessage(
                    "FAIL",
                    f"invalid ogg filename (expected epoch{{dd}}_slot{{hh}}_{{pc|world}}.ogg): {invalid_name}",
                )
            )
    else:
        messages.append(CheckMessage("INFO", f"audio naming valid for {len(ogg_files)} ogg file(s)"))
    return messages


def main() -> int:
    args = parse_args()
    repo_root = Path(args.repo_root).resolve()
    epochs_root = (repo_root / args.epochs_dir).resolve()
    audio_root = (repo_root / args.audio_dir).resolve()

    all_messages: list[CheckMessage] = []

    epoch_dirs = collect_epoch_dirs(epochs_root)
    if not epoch_dirs:
        if args.allow_empty:
            all_messages.append(CheckMessage("WARN", "no epochNN folders found (allow-empty active)"))
        else:
            all_messages.append(
                CheckMessage(
                    "FAIL",
                    f"no epochNN folders found under {epochs_root.as_posix()} (use --allow-empty for bootstrap)",
                )
            )

    for epoch_dir in epoch_dirs:
        all_messages.extend(validate_epoch_folder(epoch_dir, check_slot_consistency=args.check_slot_consistency))

    all_messages.extend(validate_audio_dir(audio_root))

    fail_count = sum(1 for message in all_messages if message.level == "FAIL")
    warn_count = sum(1 for message in all_messages if message.level == "WARN")

    print(f"repo_root={repo_root.as_posix()}")
    print(f"epochs_root={epochs_root.as_posix()}")
    print(f"audio_root={audio_root.as_posix()}")
    print(f"epoch_folders={len(epoch_dirs)}")
    for message in all_messages:
        print(f"{message.level}|{message.text}")
    print(f"summary=fail:{fail_count},warn:{warn_count}")

    return 1 if fail_count > 0 else 0


if __name__ == "__main__":
    raise SystemExit(main())
