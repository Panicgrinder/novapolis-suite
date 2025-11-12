"""Logging von Konversationsdaten als JSONL-Dateien."""

import datetime
import json
import os
from typing import Any

from utils.time_utils import now_iso


def create_log_record(
    messages: list[dict[str, str]],
    response: str,
    tool_calls: list[dict[str, Any]] | None = None,
    summary: str | None = None,
    labels: dict[str, Any] | None = None,
) -> dict[str, Any]:
    timestamp = now_iso()
    record: dict[str, Any] = {
        "timestamp": timestamp,
        "messages": messages,
        "response": response,
    }
    if tool_calls:
        record["tool_calls"] = tool_calls
    if summary:
        record["summary"] = summary
    if labels:
        record["labels"] = labels
    return record


def log_turn(data: dict[str, Any]) -> None:
    log_dir = os.path.join("data", "logs")
    os.makedirs(log_dir, exist_ok=True)
    today = datetime.date.today()
    filepath = os.path.join(log_dir, f"{today.isoformat()}.jsonl")
    with open(filepath, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=False) + "\n")
