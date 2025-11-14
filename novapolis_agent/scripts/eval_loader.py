from __future__ import annotations

import json
import logging
import os
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path
from typing import Any

logger = logging.getLogger("eval_loader")


@dataclass
class FileDiag:
    file: str
    loaded_count: int = 0
    skipped_count: int = 0
    generated_id_count: int = 0
    parse_errors: list[str] = None  # type: ignore[assignment]
    schema_issues: list[str] = None  # type: ignore[assignment]

    def __post_init__(self) -> None:
        if self.parse_errors is None:
            self.parse_errors = []
        if self.schema_issues is None:
            self.schema_issues = []


def _iter_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s:
                continue
            try:
                obj = json.loads(s)
                if isinstance(obj, dict):
                    yield obj
            except Exception as e:
                raise ValueError(f"jsonl parse error: {e}") from e


def _load_json(path: Path) -> list[dict[str, Any]]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return [x for x in data if isinstance(x, dict)]
    if isinstance(data, dict):
        return [data]
    return []


def _normalize_item(
    src: dict[str, Any], *, file_stem: str, next_idx: int
) -> tuple[dict[str, Any] | None, bool, list[str]]:
    """
    Returns: (normalized_item_or_none, id_generated, schema_issues)
    """
    issues: list[str] = []
    item = dict(src)

    # messages normalization
    msgs = item.get("messages")
    if not isinstance(msgs, list):
        # fallback: prompt or conversation
        if isinstance(item.get("prompt"), str):
            msgs = [{"role": "user", "content": str(item["prompt"])}]
        elif isinstance(item.get("conversation"), list):
            msgs = list(item["conversation"])  # type: ignore[list-item]
        else:
            issues.append("missing messages")
            return None, False, issues
    norm_msgs: list[dict[str, str]] = []
    for m in msgs:
        if isinstance(m, dict):
            role = str(m.get("role", "user")).lower().strip()
            content = str(m.get("content", "")).strip()
            if role and content:
                norm_msgs.append({"role": role, "content": content})
    if not norm_msgs:
        issues.append("empty/invalid messages")
        return None, False, issues
    item["messages"] = norm_msgs

    # id normalization
    id_generated = False
    id_val = item.get("id")
    if not isinstance(id_val, str) or not id_val.strip():
        item["id"] = f"{file_stem}-{next_idx:03d}"
        id_generated = True

    return item, id_generated, issues


def load_packages(
    patterns: list[str], combine_out: Path | None = None
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Load and normalize dataset packages from .json/.jsonl files.

    Returns: (items, diagnostics)
    diagnostics per file: file, loaded_count, skipped_count, generated_id_count,
    parse_errors (<=3), schema_issues
    """
    # resolve file list
    files: list[Path] = []
    for pat in patterns:
        for p in Path().glob(pat):
            if p.is_file() and p.suffix.lower() in (".json", ".jsonl"):
                files.append(p)
    # de-dup while keeping order
    seen = set()
    unique_files: list[Path] = []
    for p in files:
        key = str(p.resolve())
        if key not in seen:
            seen.add(key)
            unique_files.append(p)

    items: list[dict[str, Any]] = []
    diags: list[dict[str, Any]] = []

    log_json = os.environ.get("LOG_JSON", "").lower() in ("1", "true", "yes")

    for path in unique_files:
        diag = FileDiag(file=str(path))
        per_file_idx = 1
        try:
            if path.suffix.lower() == ".jsonl":
                raw_iter = list(_iter_jsonl(path))
            else:
                raw_iter = _load_json(path)
        except Exception as e:
            diag.parse_errors.append(str(e))
            diags.append(diag.__dict__)
            if log_json:
                logger.error(
                    json.dumps(
                        {"event": "load_error", "file": str(path), "error": str(e)},
                        ensure_ascii=False,
                    )
                )
            else:
                logger.error(f"{path.name}: Ladefehler: {e}")
            continue

        for obj in raw_iter:
            norm, gen, issues = _normalize_item(obj, file_stem=path.stem, next_idx=per_file_idx)
            if norm is None:
                diag.skipped_count += 1
                if issues:
                    diag.schema_issues.extend(issues)
                continue
            if gen:
                diag.generated_id_count += 1
                per_file_idx += 1
            items.append(norm)
            diag.loaded_count += 1

        # cap parse_errors/schema_issues in diagnostics representation
        if len(diag.parse_errors) > 3:
            diag.parse_errors = diag.parse_errors[:3]
        if len(diag.schema_issues) > 20:
            diag.schema_issues = diag.schema_issues[:20]

        if log_json:
            payload = {"event": "file_loaded", **diag.__dict__}
            logger.info(json.dumps(payload, ensure_ascii=False))
        else:
            short_name = Path(diag.file).name
            msg = (
                short_name
                + ": loaded="
                + str(diag.loaded_count)
                + " gen_id="
                + str(diag.generated_id_count)
                + " skipped="
                + str(diag.skipped_count)
                + " errors="
                + str(len(diag.parse_errors))
            )
            logger.info(msg)
        diags.append(diag.__dict__)

    # optional combined JSONL
    if combine_out is not None:
        try:
            combine_out.parent.mkdir(parents=True, exist_ok=True)

            # sort by numeric suffix in id if present
            def _key(x: dict[str, Any]) -> tuple[str, int]:
                _id = str(x.get("id", ""))
                # find last group of digits
                import re

                m = re.search(r"(\d+)$", _id)
                if m:
                    return (_id[: m.start()], int(m.group(1)))
                return (_id, -1)

            with combine_out.open("w", encoding="utf-8") as f:
                for it in sorted(items, key=_key):
                    f.write(json.dumps(it, ensure_ascii=False) + "\n")
            if log_json:
                payload = {
                    "event": "combined_written",
                    "path": str(combine_out),
                    "count": len(items),
                }
                logger.info(json.dumps(payload, ensure_ascii=False))
            else:
                path_str = str(combine_out)
                count_str = str(len(items))
                msg = "Combined JSONL geschrieben: " + path_str + " (" + count_str + " Einträge)"
                logger.info(msg)
        except Exception as e:
            if log_json:
                payload = {"event": "combined_error", "path": str(combine_out), "error": str(e)}
                logger.error(json.dumps(payload, ensure_ascii=False))
            else:
                logger.error("Fehler beim Schreiben der kombinierten JSONL: " + str(e))

    return items, diags
