"""Heuristische Zusammenfassungs-Utilities."""

import re
from collections.abc import Callable
from typing import Any


def extract_key_points(text: str, max_points: int = 5) -> list[str]:
    important_markers = [
        r"wichtig ist,? dass",
        r"beachte,? dass",
        r"zu?sammenfassend",
        r"zusammen?gefasst",
        r"im ergebnis",
        r"schlussfolgernd",
        r"daher",
        r"deshalb",
        r"folglich",
        r"abschließend",
    ]
    sentences = re.split(r"(?<=[.!?])\s+", text)
    key_sentences: list[str] = []
    for sentence in sentences:
        stripped = sentence.strip()
        if not stripped:
            continue
        for marker in important_markers:
            if re.search(marker, stripped.lower()):
                key_sentences.append(stripped)
                break
    if len(key_sentences) < max_points:
        remaining = [s for s in sentences if s and s.strip() and s not in key_sentences]
        remaining.sort(key=len, reverse=True)
        key_sentences.extend(remaining[: max_points - len(key_sentences)])
    key_points: list[str] = []
    for sentence in key_sentences[:max_points]:
        key_points.append(sentence if len(sentence) <= 100 else f"{sentence[:97]}...")
    return key_points


def create_simple_summary(messages: list[dict[str, str]], response: str) -> str:
    user_inputs = [msg["content"] for msg in messages if msg.get("role") == "user"]
    last_user_input = user_inputs[-1] if user_inputs else ""
    user_summary = last_user_input if len(last_user_input) <= 50 else f"{last_user_input[:47]}..."
    response_summary = response if len(response) <= 100 else f"{response[:97]}..."
    return f"Nutzer fragte nach '{user_summary}'. Antwort: '{response_summary}'"


def summarize_turn(
    messages: list[dict[str, str]],
    response: str,
    use_llm: bool = False,
    llm_function: Callable[[list[dict[str, str]], str], dict[str, Any]] | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {}
    if use_llm and llm_function:
        llm_result = llm_function(messages, response)
        result["summary"] = llm_result.get("summary", "")
        result["keyfacts"] = llm_result.get("keyfacts", [])
    else:
        result["summary"] = create_simple_summary(messages, response)
        result["keyfacts"] = extract_key_points(response)
    return result


def llm_summarize(messages: list[dict[str, str]], response: str) -> dict[str, Any]:
    summary = create_simple_summary(messages, response)
    keyfacts = extract_key_points(response)
    return {"summary": summary, "keyfacts": keyfacts}
