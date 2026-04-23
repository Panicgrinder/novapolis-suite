#!/usr/bin/env python
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

DEFAULT_OUTPUT = "novapolis_agent/eval/datasets/curation/session_promotions.v1.jsonl"
ALLOWED_ARTIFACT_NAMES = {
    "savegame.json",
    "replay_manifest.json",
    "pc_log.jsonl",
    "world_log.jsonl",
}


@dataclass(frozen=True)
class SessionPromotionItem:
    item_id: str
    slug: str
    session_id: str
    source_file: str
    prompt: str
    source_kind: str
    promotion_level: str
    license_scope: str
    source_package: str
    artifact_paths: list[str]
    session_status: str
    resume_checkpoint_id: str
    updated_at: str
    pc_event_count: int
    world_event_count: int
    state_patch_count: int
    carry_over_count: int
    last_patch_preview: str
    last_pc_excerpt: str
    last_world_excerpt: str

    def to_record(self) -> dict[str, object]:
        return {
            "id": self.item_id,
            "slug": self.slug,
            "category": "session_promotion_seed",
            "profile": "promotion",
            "tags": [
                "training",
                "promotion",
                "session",
                "runtime",
                "curation-pack",
                "review-required",
                "source-session-replay",
            ],
            "messages": [{"role": "user", "content": self.prompt}],
            "source_file": self.source_file,
            "source_kind": self.source_kind,
            "promotion_level": self.promotion_level,
            "license_scope": self.license_scope,
            "source_package": self.source_package,
            "session_id": self.session_id,
            "meta": {
                "artifact_paths": self.artifact_paths,
                "session_status": self.session_status,
                "resume_checkpoint_id": self.resume_checkpoint_id,
                "updated_at": self.updated_at,
                "pc_event_count": self.pc_event_count,
                "world_event_count": self.world_event_count,
                "state_patch_count": self.state_patch_count,
                "carry_over_count": self.carry_over_count,
                "last_patch_preview": self.last_patch_preview,
                "last_pc_excerpt": self.last_pc_excerpt,
                "last_world_excerpt": self.last_world_excerpt,
                "promotion_target": "rp_ssot_or_curation_pack",
            },
        }


def _slugify(value: str) -> str:
    text = value.lower().strip()
    text = text.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    text = text.replace("ß", "ss")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def _read_json(path: Path) -> dict[str, Any] | None:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return raw if isinstance(raw, dict) else None


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        clean = line.strip()
        if not clean:
            continue
        try:
            raw = json.loads(clean)
        except Exception:
            continue
        if isinstance(raw, dict):
            rows.append(raw)
    return rows


def _truncate(text: str, limit: int = 220) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    if len(clean) <= limit:
        return clean
    return clean[: limit - 3].rstrip() + "..."


def _artifact_paths(repo_root: Path, session_id: str, replay_payload: dict[str, Any]) -> list[str]:
    from_manifest = replay_payload.get("artifact_paths")
    if isinstance(from_manifest, dict):
        values = []
        for value in from_manifest.values():
            if not value:
                continue
            normalized = str(value).replace("\\", "/")
            if Path(normalized).name not in ALLOWED_ARTIFACT_NAMES:
                continue
            values.append(normalized)
        if values:
            return sorted(set(values))

    session_root = repo_root / "novapolis_agent" / "tmp" / "sim_sessions" / session_id
    fallback_paths = [
        session_root / "savegame.json",
        session_root / "world_log.jsonl",
        session_root / "pc_log.jsonl",
        session_root / "replay_manifest.json",
    ]
    resolved: list[str] = []
    for path in fallback_paths:
        if not path.exists():
            continue
        try:
            resolved.append(path.relative_to(repo_root).as_posix())
        except ValueError:
            resolved.append(path.as_posix())
    return sorted(set(resolved))


def _last_log_excerpt(entries: list[dict[str, Any]]) -> str:
    if not entries:
        return ""
    for entry in reversed(entries):
        for key in ("content", "text", "event", "summary"):
            value = entry.get(key)
            if isinstance(value, str) and value.strip():
                return _truncate(value)
    return ""


def _last_patch_preview(patches: list[dict[str, Any]]) -> str:
    if not patches:
        return ""
    patch = patches[-1]
    path = str(patch.get("path") or "?")
    op = str(patch.get("op") or "?")
    value = patch.get("value")
    if isinstance(value, str):
        rendered_value = _truncate(value)
    else:
        rendered_value = _truncate(json.dumps(value, ensure_ascii=False))
    return f"{op} {path} => {rendered_value}"


def _build_promotion_prompt(
    *,
    session_id: str,
    session_status: str,
    resume_checkpoint_id: str,
    checkpoints: int,
    carry_over_count: int,
    state_patch_count: int,
    world_event_count: int,
    pc_event_count: int,
    artifact_paths: list[str],
    last_patch_preview: str,
    last_pc_excerpt: str,
    last_world_excerpt: str,
) -> str:
    segments = [
        f"Nutze nur belegte Laufzeit-Artefakte aus Session {session_id}.",
        (
            "Vertragsstand: "
            + f"status={session_status}, "
            + f"resume_checkpoint_id={resume_checkpoint_id or 'n/a'}, "
            + f"checkpoints={checkpoints}, carry_over={carry_over_count}, "
            + f"state_patches={state_patch_count}, world_events={world_event_count}, "
            + f"pc_events={pc_event_count}."
        ),
    ]
    if artifact_paths:
        segments.append("Artefaktkern: " + ", ".join(artifact_paths) + ".")
    if last_patch_preview:
        segments.append(f"Letzter State-Patch: {last_patch_preview}.")
    if last_pc_excerpt:
        segments.append(f"Letzter PC-Log-Kontext: {last_pc_excerpt}.")
    if last_world_excerpt:
        segments.append(f"Letzter World-Log-Kontext: {last_world_excerpt}.")
    segments.append(
        "Formuliere daraus eine knappe Promotionsnotiz fuer RP-SSOT oder ein freigegebenes "
        "Curation-Pack. Erfinde keine neuen Orte, Fraktionen, Mengen, Missionsresultate oder "
        "Beziehungsstaende."
    )
    return " ".join(segments)


def collect_session_promotion_items(
    repo_root: Path,
    session_root: Path,
    *,
    limit: int = 40,
    session_ids: list[str] | None = None,
    promotion_level: str = "runtime_session_review_required",
    license_scope: str = "internal",
    source_package: str = "session_promotion_builder.v1",
) -> tuple[list[SessionPromotionItem], list[str]]:
    allowed_ids = {value.strip() for value in session_ids or [] if value.strip()}
    items: list[SessionPromotionItem] = []
    skipped: list[str] = []

    for savegame_path in sorted(session_root.glob("*/savegame.json")):
        session_dir = savegame_path.parent
        session_id = session_dir.name
        if allowed_ids and session_id not in allowed_ids:
            continue

        replay_manifest_path = session_dir / "replay_manifest.json"
        if not replay_manifest_path.exists():
            skipped.append(f"{session_id}: missing replay_manifest.json")
            continue

        savegame_payload = _read_json(savegame_path)
        replay_payload = _read_json(replay_manifest_path)
        if savegame_payload is None or replay_payload is None:
            skipped.append(f"{session_id}: unreadable savegame/replay manifest")
            continue

        state_patches = list(savegame_payload.get("state_patches") or [])
        carry_over = list(savegame_payload.get("carry_over") or [])
        world_log = _read_jsonl(session_dir / "world_log.jsonl")
        pc_log = _read_jsonl(session_dir / "pc_log.jsonl")
        artifact_paths = _artifact_paths(repo_root, session_id, replay_payload)
        last_patch_preview = _last_patch_preview(state_patches)
        last_pc_excerpt = _last_log_excerpt(pc_log)
        last_world_excerpt = _last_log_excerpt(world_log)
        session_status = str(replay_payload.get("session_status") or "unknown")
        resume_checkpoint_id = str(replay_payload.get("resume_checkpoint_id") or "")
        updated_at = str(
            replay_payload.get("updated_at") or savegame_payload.get("updated_at") or ""
        )
        checkpoints = list(replay_payload.get("checkpoints") or [])
        prompt = _build_promotion_prompt(
            session_id=session_id,
            session_status=session_status,
            resume_checkpoint_id=resume_checkpoint_id,
            checkpoints=len(checkpoints),
            carry_over_count=len(carry_over),
            state_patch_count=len(state_patches),
            world_event_count=int(replay_payload.get("world_event_count") or len(world_log)),
            pc_event_count=int(replay_payload.get("pc_event_count") or len(pc_log)),
            artifact_paths=artifact_paths,
            last_patch_preview=last_patch_preview,
            last_pc_excerpt=last_pc_excerpt,
            last_world_excerpt=last_world_excerpt,
        )
        basis = f"{session_id}|{resume_checkpoint_id}|{updated_at}|{len(state_patches)}"
        short_hash = hashlib.sha1(basis.encode("utf-8")).hexdigest()[:10]
        slug = f"promote-session-{_slugify(session_id)}-{short_hash}"
        replay_artifact = next(
            (path for path in artifact_paths if path.endswith("/replay_manifest.json")),
            "",
        )
        source_file = replay_artifact or replay_manifest_path.relative_to(repo_root).as_posix()
        items.append(
            SessionPromotionItem(
                item_id=slug,
                slug=slug,
                session_id=session_id,
                source_file=source_file,
                prompt=prompt,
                source_kind="session_replay",
                promotion_level=promotion_level,
                license_scope=license_scope,
                source_package=source_package,
                artifact_paths=artifact_paths,
                session_status=session_status,
                resume_checkpoint_id=resume_checkpoint_id,
                updated_at=updated_at,
                pc_event_count=int(replay_payload.get("pc_event_count") or len(pc_log)),
                world_event_count=int(replay_payload.get("world_event_count") or len(world_log)),
                state_patch_count=len(state_patches),
                carry_over_count=len(carry_over),
                last_patch_preview=last_patch_preview,
                last_pc_excerpt=last_pc_excerpt,
                last_world_excerpt=last_world_excerpt,
            )
        )
        if len(items) >= max(0, int(limit)):
            break

    return items, skipped


def write_jsonl(path: Path, records: Iterable[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Build curated session promotion pack")
    parser.add_argument(
        "--repo-root",
        default=str(Path(__file__).resolve().parents[2]),
        help="Repository root path",
    )
    parser.add_argument(
        "--session-root",
        default="novapolis_agent/tmp/sim_sessions",
        help="Relative session artifact root",
    )
    parser.add_argument(
        "--out",
        default=DEFAULT_OUTPUT,
        help="Relative output path for the curation pack",
    )
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument(
        "--session-id", action="append", default=[], help="Repeatable session id filter"
    )
    args = parser.parse_args(argv)

    repo_root = Path(args.repo_root).resolve()
    session_root = (repo_root / args.session_root).resolve()
    out_path = (repo_root / args.out).resolve()

    if not session_root.exists():
        print(f"[session-promotion-builder] ERROR session_root not found: {session_root}")
        return 2

    items, skipped = collect_session_promotion_items(
        repo_root,
        session_root,
        limit=args.limit,
        session_ids=args.session_id or None,
    )
    records = [item.to_record() for item in items]
    write_jsonl(out_path, records)

    print("[session-promotion-builder] done")
    print(f"  session_root: {session_root}")
    print(f"  output: {out_path}")
    print(f"  records: {len(records)}")
    print(f"  skipped: {len(skipped)}")
    if skipped:
        for message in skipped[:5]:
            print(f"  skip: {message}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
