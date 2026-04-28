#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from collections.abc import Iterable, Mapping
from typing import Any

RP_RUNTIME_PREFIX = "novapolis-rp/database-curated/staging/rp-runtime/"
MUTATING_TOOL_MARKERS = (
    "apply_patch",
    "create_file",
    "edit_notebook_file",
    "rename",
)
PROMPT_KEY_MARKERS = (
    "prompt",
    "message",
    "transcript",
    "conversation",
)
WORKFLOW_TERMS = (
    "turn",
    "zug",
    "szene",
    "admin",
    "rueckmeldung",
    "rückmeldung",
    "auswertung",
    "freigabe",
    "bestaetigung",
    "bestätigung",
    "datenabgleich",
    "fix",
    "nachzug",
)
ADMIN_FIX_TERMS = (
    "admin",
    "rueckmeldung",
    "rückmeldung",
    "auswertung",
    "fix",
    "nachzug",
    "bestaetigung",
    "bestätigung",
    "datenabgleich",
)
FREIGABE_TERMS = (
    "freigabe",
    "freigegeben",
    "spiel den naechsten turn",
    "spiele den naechsten turn",
    "naechster turn",
    "nächster turn",
    "naechsten zug",
    "nächsten zug",
)
OVERRIDE_TERMS = (
    "override rp loop",
    "override rp-loop",
    "mehrturn erlaubt",
    "ignoriere rp loop",
    "ignoriere rp-loop",
)
PATCH_TURN_RE = re.compile(r"(?m)^\+Turn\s+(\d+)\b")
RUNTIME_PATH_RE = re.compile(
    r"novapolis-rp[\\/]database-curated[\\/]staging[\\/]rp-runtime[\\/][^\s\"']+",
    re.IGNORECASE,
)


def normalize_text(value: str) -> str:
    return value.replace("\\", "/").strip().lower()


def flatten_strings(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        yield value
        return
    if isinstance(value, Mapping):
        for item in value.values():
            yield from flatten_strings(item)
        return
    if isinstance(value, list | tuple | set):
        for item in value:
            yield from flatten_strings(item)


def collect_prompt_strings(value: Any, parent_key: str = "") -> list[str]:
    strings: list[str] = []
    if isinstance(value, Mapping):
        for key, item in value.items():
            key_lower = str(key).lower()
            next_parent = f"{parent_key}.{key_lower}" if parent_key else key_lower
            if isinstance(item, str) and any(marker in key_lower for marker in PROMPT_KEY_MARKERS):
                strings.append(item)
            else:
                strings.extend(collect_prompt_strings(item, next_parent))
    elif isinstance(value, list):
        for item in value:
            strings.extend(collect_prompt_strings(item, parent_key))
    return strings


def first_mapping(payload: Mapping[str, Any], *keys: str) -> Mapping[str, Any]:
    for key in keys:
        value = payload.get(key)
        if isinstance(value, Mapping):
            return value
    return {}


def extract_tool_name(payload: Mapping[str, Any]) -> str:
    for key in ("tool_name", "toolName", "tool"):
        value = payload.get(key)
        if isinstance(value, str):
            return value
    nested = first_mapping(payload, "toolInvocation", "toolUse", "input")
    for key in ("tool_name", "toolName", "tool"):
        value = nested.get(key)
        if isinstance(value, str):
            return value
    return ""


def extract_tool_input(payload: Mapping[str, Any]) -> Any:
    for key in ("tool_input", "toolInput", "input"):
        if key in payload:
            return payload[key]
    nested = first_mapping(payload, "toolInvocation", "toolUse")
    for key in ("tool_input", "toolInput", "input"):
        if key in nested:
            return nested[key]
    return {}


def extract_runtime_paths(tool_input: Any) -> list[str]:
    paths: set[str] = set()
    for text in flatten_strings(tool_input):
        normalized = text.replace("\\", "/")
        for match in RUNTIME_PATH_RE.findall(normalized):
            paths.add(normalize_text(match))
    return sorted(paths)


def extract_patch_text(tool_input: Any) -> str:
    if isinstance(tool_input, Mapping):
        for key in ("input", "content", "patch", "newCode"):
            value = tool_input.get(key)
            if isinstance(value, str):
                return value
    if isinstance(tool_input, str):
        return tool_input
    return ""


def added_turns_from_patch(patch_text: str) -> list[int]:
    return [int(match) for match in PATCH_TURN_RE.findall(patch_text)]


def is_mutating_tool(tool_name: str) -> bool:
    tool_name_lower = tool_name.lower()
    return any(marker in tool_name_lower for marker in MUTATING_TOOL_MARKERS)


def contains_any(text: str, terms: tuple[str, ...]) -> bool:
    return any(term in text for term in terms)


def decision_payload(
    decision: str,
    reason: str | None = None,
    system_message: str | None = None,
) -> dict[str, Any]:
    payload: dict[str, Any] = {
        "continue": True,
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": decision,
        },
    }
    if reason:
        payload["hookSpecificOutput"]["permissionDecisionReason"] = reason
    if system_message:
        payload["systemMessage"] = system_message
    return payload


def evaluate(payload: Mapping[str, Any]) -> dict[str, Any]:
    tool_name = extract_tool_name(payload)
    tool_input = extract_tool_input(payload)
    if not is_mutating_tool(tool_name):
        return decision_payload("allow")

    runtime_paths = extract_runtime_paths(tool_input)
    if not runtime_paths:
        return decision_payload("allow")

    prompt_text = normalize_text("\n".join(collect_prompt_strings(payload)))
    if contains_any(prompt_text, OVERRIDE_TERMS):
        return decision_payload("allow")

    patch_text = extract_patch_text(tool_input)
    added_turns = added_turns_from_patch(patch_text)
    has_workflow_marker = contains_any(prompt_text, WORKFLOW_TERMS)
    looks_like_admin_fix = contains_any(prompt_text, ADMIN_FIX_TERMS)
    has_freigabe = contains_any(prompt_text, FREIGABE_TERMS)

    if len(added_turns) > 1:
        return decision_payload(
            "deny",
            "RP-Runtime-Guard: Mehrere neue Turns in einer Mutation erkannt.",
            (
                "RP-Runtime-Guard blockiert diese Mutation: Im RP-Testbetrieb ist "
                "pro Antwort nur ein begrenzter Schritt zulaessig."
            ),
        )

    if added_turns and looks_like_admin_fix and not has_freigabe:
        turn_label = added_turns[0]
        return decision_payload(
            "deny",
            (
                "RP-Runtime-Guard: Neuer Turn "
                f"{turn_label} nach Admin-Fix ohne ausdrueckliche Freigabe erkannt."
            ),
            (
                "RP-Runtime-Guard blockiert diese Mutation: Nach "
                "Admin-Rueckmeldung zuerst Bestaetigung und Datenabgleich, "
                "neuer Turn erst nach Freigabe."
            ),
        )

    if added_turns and not has_freigabe:
        turn_label = added_turns[0]
        return decision_payload(
            "ask",
            (
                "RP-Runtime-Guard: Neuer Turn "
                f"{turn_label} im RP-Runtime-Slice ohne klaren Freigabeanker."
            ),
            (
                "RP-Runtime-Guard: Bitte kurz pruefen, ob der neue Turn im "
                "aktuellen Admin-/Freigabestand wirklich freigegeben ist."
            ),
        )

    if not has_workflow_marker:
        return decision_payload(
            "ask",
            (
                "RP-Runtime-Guard: Mutation im RP-Runtime-Bereich ohne klaren "
                "Turn-/Admin-/Freigabeanker."
            ),
            (
                "RP-Runtime-Guard: Bitte den RP-Mindestablauf explizit machen: "
                "Turn, Admin-Nachzug oder Freigabe."
            ),
        )

    return decision_payload("allow")


def main() -> int:
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, Mapping):
            raise ValueError("Hook payload must be a JSON object.")
    except Exception as exc:
        json.dump(
            decision_payload(
                "ask",
                f"RP-Runtime-Guard: Hook-Payload konnte nicht sicher gelesen werden ({exc}).",
                (
                    "RP-Runtime-Guard: Unklarer Hook-Kontext, bitte Mutation im "
                    "RP-Runtime-Slice kurz manuell bestaetigen."
                ),
            ),
            sys.stdout,
        )
        sys.stdout.write("\n")
        return 0

    json.dump(evaluate(payload), sys.stdout)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
