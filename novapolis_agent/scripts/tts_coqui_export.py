#!/usr/bin/env python
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

DEFAULT_ALLOWLIST_PATH = Path("novapolis_agent/config/tts_model_allowlist.json")
PLACEHOLDER_OGG_BYTES = (
    b"OggS\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x1a\xc4\x8f\x91\x00\x00\x00\x00\x00\x00\x00\x00"
    b"\x01\x13OpusHead\x01\x01\x38\x01\x80\xbb\x00\x00\x00\x00"
)


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


def _load_yaml(path: Path) -> Any:
    try:
        import yaml  # type: ignore[import-untyped]
    except Exception as exc:  # pragma: no cover
        raise ValueError("yaml parsing not available (install pyyaml)") from exc
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def _slugify(value: str, fallback: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip()).strip("-").lower()
    return cleaned[:64] if cleaned else fallback


def load_voice_map(path: Path) -> tuple[dict[str, str], str]:
    raw = _load_yaml(path)
    if not isinstance(raw, dict):
        raise ValueError("voice-map must be a YAML object")

    voices_section = raw.get("voices") if isinstance(raw.get("voices"), dict) else raw
    if not isinstance(voices_section, dict):
        raise ValueError("voice-map requires a mapping (top-level or under 'voices')")

    voice_map: dict[str, str] = {}
    for key, value in voices_section.items():
        map_key = str(key).strip()
        map_value = str(value).strip()
        if map_key and map_value:
            voice_map[map_key] = map_value

    default_voice = str(raw.get("default_voice", "default")).strip() or "default"
    return voice_map, default_voice


def _coerce_record(item: Any, index: int) -> dict[str, str] | None:
    if isinstance(item, str):
        text = item.strip()
        if not text:
            return None
        return {"id": f"line-{index:04d}", "text": text, "voice": "default"}
    if not isinstance(item, dict):
        return None

    text = str(item.get("text") or item.get("prompt") or item.get("content") or "").strip()
    if not text:
        return None
    record_id = str(item.get("id") or item.get("slug") or f"item-{index:04d}").strip()
    voice = str(item.get("voice") or item.get("voice_id") or "default").strip()
    return {"id": record_id or f"item-{index:04d}", "text": text, "voice": voice or "default"}


def load_input_records(path: Path) -> list[dict[str, str]]:
    suffix = path.suffix.lower()
    records: list[dict[str, str]] = []

    if suffix in {".txt", ".md"}:
        lines = path.read_text(encoding="utf-8").splitlines()
        for index, line in enumerate(lines, start=1):
            rec = _coerce_record(line, index)
            if rec:
                records.append(rec)
        return records

    if suffix == ".jsonl":
        for index, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if not line.strip():
                continue
            raw = json.loads(line)
            rec = _coerce_record(raw, index)
            if rec:
                records.append(rec)
        return records

    if suffix in {".json", ".yaml", ".yml"}:
        if suffix == ".json":
            raw = json.loads(path.read_text(encoding="utf-8"))
        else:
            raw = _load_yaml(path)
        if isinstance(raw, list):
            for index, item in enumerate(raw, start=1):
                rec = _coerce_record(item, index)
                if rec:
                    records.append(rec)
            return records
        rec = _coerce_record(raw, 1)
        return [rec] if rec else []

    raise ValueError(f"unsupported input format: {suffix}")


def build_cache_key(*, text: str, voice: str, lang: str, model_id: str) -> str:
    payload = {
        "text": text,
        "voice": voice,
        "lang": lang,
        "model_id": model_id,
        "format": "ogg",
        "pipeline": "build-time-mvp",
    }
    data = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def ensure_cached_ogg(cache_file: Path) -> bool:
    if cache_file.exists():
        return True
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_bytes(PLACEHOLDER_OGG_BYTES)
    return False


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
    parser.add_argument(
        "--input",
        required=True,
        help="Path to jsonl|yaml|txt source input",
    )
    parser.add_argument(
        "--voice-map",
        required=True,
        help="Path to YAML voice mapping",
    )
    parser.add_argument(
        "--model-id", required=True, help="Model identifier to be validated against allowlist"
    )
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
    parser.add_argument(
        "--manifest",
        default="tts_export_manifest.json",
        help="Manifest filename written to output directory",
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

    try:
        voice_map, default_voice_key = load_voice_map(voice_map_path)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid voice-map: {exc}")
        return 1

    try:
        records = load_input_records(input_path)
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: invalid input payload: {exc}")
        return 1
    if not records:
        print("ERROR: no valid input records found")
        return 1

    is_allowed, reason = validate_model_policy(args.model_id, allowlist)
    if not is_allowed:
        print(f"BLOCKED: {reason}")
        print("Policy is deny-by-default. Add explicit approved entry with local license copy.")
        return 3

    print("TTS exporter build-time MVP")
    print(f"  input:      {input_path}")
    print(f"  voice-map:  {voice_map_path}")
    print(f"  model-id:   {args.model_id}")
    print(f"  lang:       {args.lang}")
    print(f"  output-dir: {output_dir}")
    print(f"  allowlist:  {allowlist_path}")
    print(f"  policy:     {reason}")
    print(f"  records:    {len(records)}")

    if args.dry_run:
        print("DRY-RUN: contract and paths are valid; files are not written.")
        return 0

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        cache_root = output_dir / "_cache"
        manifest_path = output_dir / str(args.manifest)

        exported = 0
        cache_hits = 0
        manifest_rows: list[dict[str, Any]] = []
        for index, rec in enumerate(records, start=1):
            requested_voice = rec.get("voice", "default").strip() or "default"
            resolved_voice = voice_map.get(requested_voice) or voice_map.get(default_voice_key)
            resolved_voice = resolved_voice or requested_voice

            cache_key = build_cache_key(
                text=rec["text"],
                voice=resolved_voice,
                lang=args.lang,
                model_id=args.model_id,
            )
            cache_path = cache_root / cache_key[:2] / f"{cache_key}.ogg"
            cache_hit = ensure_cached_ogg(cache_path)
            if cache_hit:
                cache_hits += 1

            rec_slug = _slugify(rec.get("id", f"item-{index:04d}"), f"item-{index:04d}")
            voice_slug = _slugify(resolved_voice, "voice")
            out_name = f"{args.lang}-{voice_slug}-{rec_slug}-{cache_key[:12]}.ogg"
            out_path = output_dir / out_name
            shutil.copyfile(cache_path, out_path)

            manifest_rows.append(
                {
                    "id": rec.get("id"),
                    "voice_requested": requested_voice,
                    "voice_resolved": resolved_voice,
                    "cache_key": cache_key,
                    "cache_path": str(cache_path),
                    "output_path": str(out_path),
                    "cache_hit": cache_hit,
                    "bytes": out_path.stat().st_size,
                }
            )
            exported += 1

        manifest = {
            "ok": True,
            "model_id": args.model_id,
            "lang": args.lang,
            "input": str(input_path),
            "voice_map": str(voice_map_path),
            "output_dir": str(output_dir),
            "cache_root": str(cache_root),
            "records_total": len(records),
            "exported": exported,
            "cache_hits": cache_hits,
            "cache_misses": exported - cache_hits,
            "items": manifest_rows,
        }
        manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"EXPORT OK: exported={exported}, cache_hits={cache_hits}, manifest={manifest_path}")
        return 0
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: export failed: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
