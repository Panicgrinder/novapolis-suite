"""Logging von Konversationsdaten als JSONL-Dateien."""

import datetime
import json
import os
from typing import Any, Dict, List, Optional

from utils.time_utils import now_iso


def create_log_record(
    messages: List[Dict[str, str]],
    response: str,
    tool_calls: Optional[List[Dict[str, Any]]] = None,
    summary: Optional[str] = None,
    labels: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    timestamp = now_iso()
    record: Dict[str, Any] = {
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


def log_turn(data: Dict[str, Any]) -> None:
    log_dir = os.path.join("data", "logs")
    os.makedirs(log_dir, exist_ok=True)
    today = datetime.date.today()
    filepath = os.path.join(log_dir, f"{today.isoformat()}.jsonl")
    with open(filepath, "a", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=False) + "\n")
