import hashlib
import importlib
import json as _json
import logging
import re
import sys
import time
from collections.abc import Mapping
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

import httpx
from fastapi import HTTPException, status

try:
    _ctx_notes_mod = importlib.import_module("utils.context_notes")
except Exception:
    _ctx_notes_mod = importlib.import_module("novapolis_agent.utils.context_notes")

from ..core.content_management import apply_post, apply_pre, modify_prompt_for_freedom, neutralize
from ..core.memory import compose_with_memory, get_memory_store
from ..core.prompts import DEFAULT_SYSTEM_PROMPT, EVAL_SYSTEM_PROMPT, UNRESTRICTED_SYSTEM_PROMPT
from ..utils.session_memory import session_memory
from . import sim as _sim_api
from .chat_helpers import normalize_ollama_options, resolve_ollama_think
from .models import (
    TEXT_RPG_DEFAULT_TURN_WINDOW_MINUTES,
    TEXT_RPG_LOG_CHANNELS,
    TEXT_RPG_SESSION_CONTRACT_VERSION,
    CarryOverItem,
    ChatRequest,
    ChatResponse,
    TurnContext,
)


def _resolve_settings_object() -> Any:
    for module_name in ("app.core.settings", "novapolis_agent.app.core.settings"):
        module = sys.modules.get(module_name)
        if module is not None and hasattr(module, "settings"):
            return module.settings
    for module_name in ("app.core.settings", "novapolis_agent.app.core.settings"):
        try:
            module = importlib.import_module(module_name)
            return module.settings
        except Exception:
            continue
    raise RuntimeError("settings module not available")


class _SettingsProxy:
    def __getattr__(self, name: str) -> Any:
        return getattr(_resolve_settings_object(), name)

    def __setattr__(self, name: str, value: Any) -> None:
        setattr(_resolve_settings_object(), name, value)


load_context_notes = _ctx_notes_mod.load_context_notes
settings = _SettingsProxy()

if TYPE_CHECKING:
    _TfIdfIndex = Any

logger = logging.getLogger(__name__)

_URL_RE = re.compile(r"https?://\S+", re.IGNORECASE)
_EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
_LONG_NUM_RE = re.compile(r"\b\d{4,}\b")
_MULTISPACE_RE = re.compile(r"\s+")
_STRICT_RPG_SECTION_TITLES = ("Szene:", "Konsequenz:", "Optionen:", "State_Patches:")
_SUPPORT_DE_AB_PROFILE = "support_de_ab"
_SUPPORT_DE_AB_DEFAULT_CANDIDATES = ("llama3.1:8b", "qwen3.5:4b")
_SUPPORT_DE_AB_POLITE_MARKERS = (
    "bitte",
    "danke",
    "vielen dank",
    "rueckmeldung",
    "rückmeldung",
    "entschuldigung",
    "freundlichen gruessen",
    "freundlichen grüßen",
)
_SUPPORT_DE_AB_RPG_MARKERS = (
    "szene:",
    "konsequenz:",
    "optionen:",
    "state_patches:",
    "/roll",
    "novapolis",
    "slot-",
    "turn-",
    "gm_only",
    "hidden_context",
)
_SUPPORT_DE_AB_AI_SELF_MARKERS = (
    "als ki",
    "als sprachmodell",
    "ich bin ein computerprogramm",
    "ich bin ein ki-modell",
)
_SUPPORT_DE_AB_STOPWORDS = {
    "aber",
    "alles",
    "beim",
    "bereits",
    "bitte",
    "damit",
    "danke",
    "dass",
    "deine",
    "deiner",
    "deinem",
    "deinen",
    "deutlich",
    "diese",
    "diesem",
    "einen",
    "einer",
    "eines",
    "eurer",
    "fuer",
    "gern",
    "gerne",
    "heute",
    "hier",
    "ihnen",
    "ihre",
    "ihren",
    "ihrer",
    "koennen",
    "können",
    "mehr",
    "noch",
    "oder",
    "sowie",
    "support",
    "unser",
    "unsere",
    "unter",
    "vielen",
    "weiter",
    "werden",
    "wurde",
}


def _bool_from_unknown(value: Any, default: bool = False) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return value != 0
    if isinstance(value, str):
        norm = value.strip().lower()
        if norm in {"1", "true", "yes", "on"}:
            return True
        if norm in {"0", "false", "no", "off"}:
            return False
    return default


def _shadow_mode_enabled(request: ChatRequest, eval_mode: bool) -> bool:
    try:
        if not bool(getattr(settings, "SHADOW_MODE_LOGGING_ENABLED", True)):
            return False
    except Exception:
        return False

    option_flag: Any = None
    try:
        opts_any = getattr(request, "options", None)
        if isinstance(opts_any, Mapping):
            option_flag = cast(Mapping[object, Any], opts_any).get("shadow_mode")
        elif opts_any is not None:
            md = getattr(opts_any, "model_dump", None)
            if callable(md):
                raw = md()
                if isinstance(raw, Mapping):
                    option_flag = cast(Mapping[object, Any], raw).get("shadow_mode")
    except Exception:
        option_flag = None

    if option_flag is None:
        return bool(eval_mode)
    return _bool_from_unknown(option_flag, default=bool(eval_mode))


def _safe_sha256(text: str) -> str:
    try:
        return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()
    except Exception:
        return ""


def _redact_preview(text: str) -> str:
    max_chars = int(getattr(settings, "SHADOW_MODE_PREVIEW_MAX_CHARS", 280) or 280)
    if not bool(getattr(settings, "SHADOW_MODE_REDACT_PREVIEW_ENABLED", True)):
        return (_MULTISPACE_RE.sub(" ", text).strip())[:max_chars]

    out = _URL_RE.sub("<URL>", text)
    out = _EMAIL_RE.sub("<EMAIL>", out)
    out = _LONG_NUM_RE.sub("<NUM>", out)
    out = _MULTISPACE_RE.sub(" ", out).strip()
    return out[:max_chars]


def _options_to_dict(options: Any) -> dict[str, Any]:
    if isinstance(options, Mapping):
        try:
            return {str(key): value for key, value in cast(Mapping[object, Any], options).items()}
        except Exception:
            return {}
    if options is None:
        return {}
    model_dump = getattr(options, "model_dump", None)
    if callable(model_dump):
        try:
            raw = model_dump()
            if isinstance(raw, Mapping):
                return {str(key): value for key, value in cast(Mapping[object, Any], raw).items()}
        except Exception:
            return {}
    return {}


def _coerce_string_list(value: Any) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        stripped = value.strip()
        return [stripped] if stripped else []
    if isinstance(value, list | tuple | set):
        iterable = list(cast(list[Any] | tuple[Any, ...] | set[Any], value))
        items: list[str] = []
        for entry in iterable:
            text = str(entry).strip()
            if text:
                items.append(text)
        return items
    text = str(value).strip()
    return [text] if text else []


def _orchestrator_enabled(options: Mapping[str, Any]) -> bool:
    flag = options.get("orchestrator_enabled")
    enabled = _bool_from_unknown(flag, default=False) if flag is not None else False
    return enabled or any(
        bool(options.get(key))
        for key in (
            "campaign_id",
            "scene_id",
            "slot_id",
            "turn_id",
            "retrieval_query",
            "public_context",
            "hidden_context",
            "scheduler_hints",
            "state_patch_hints",
        )
    )


def _latest_user_text(messages: list[dict[str, str]]) -> str:
    user_texts = [
        message.get("content", "") for message in messages if message.get("role") == "user"
    ]
    return user_texts[-1] if user_texts else ""


def _support_ab_enabled(
    options: Mapping[str, Any],
    *,
    profile_id: str | None,
    eval_mode: bool,
    unrestricted_mode: bool,
) -> bool:
    if eval_mode or unrestricted_mode:
        return False
    if profile_id == _SUPPORT_DE_AB_PROFILE:
        return True
    return _bool_from_unknown(options.get("support_ab_enabled"), default=False)


def _support_ab_force_judge(options: Mapping[str, Any]) -> bool:
    return _bool_from_unknown(options.get("support_force_judge"), default=False)


def _support_ab_candidate_models(options: Mapping[str, Any]) -> list[str]:
    raw_models = _coerce_string_list(options.get("support_candidate_models"))
    candidates = raw_models if len(raw_models) >= 2 else list(_SUPPORT_DE_AB_DEFAULT_CANDIDATES)
    deduped: list[str] = []
    seen: set[str] = set()
    for candidate in candidates:
        normalized = candidate.strip()
        if not normalized:
            continue
        lowered = normalized.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        deduped.append(normalized)
    return deduped[:2] if len(deduped) >= 2 else list(_SUPPORT_DE_AB_DEFAULT_CANDIDATES)


def _support_ab_judge_model(options: Mapping[str, Any]) -> str | None:
    value = str(options.get("support_judge_model", "")).strip()
    return value or None


def _support_ab_query_terms(text: str) -> list[str]:
    tokens = re.findall(r"[a-zA-ZäöüÄÖÜß]{4,}", text.lower())
    deduped: list[str] = []
    seen: set[str] = set()
    for token in tokens:
        if token in _SUPPORT_DE_AB_STOPWORDS:
            continue
        if token in seen:
            continue
        seen.add(token)
        deduped.append(token)
    return deduped[:6]


def _score_support_candidate_response(user_text: str, response_text: str) -> tuple[int, list[str]]:
    text = response_text.strip()
    if not text:
        return (-100, ["empty_response"])

    score = 0
    reasons: list[str] = []
    lowered = text.lower()
    text_len = len(text)

    if 80 <= text_len <= 700:
        score += 2
        reasons.append("good_length")
    elif 40 <= text_len <= 1000:
        score += 1
        reasons.append("acceptable_length")
    elif text_len < 25:
        score -= 3
        reasons.append("too_short")
    elif text_len > 1300:
        score -= 2
        reasons.append("too_long")

    if text[:1].isupper():
        score += 1
        reasons.append("starts_clean")
    if lowered.endswith((".", "!", "?")):
        score += 1
        reasons.append("ends_clean")

    rpg_hits = sum(1 for marker in _SUPPORT_DE_AB_RPG_MARKERS if marker in lowered)
    if rpg_hits > 0:
        score -= 20 + min(10, (rpg_hits - 1) * 3)
        reasons.append("rpg_leak")
    if any(marker in lowered for marker in _SUPPORT_DE_AB_AI_SELF_MARKERS):
        score -= 4
        reasons.append("ai_self_reference")

    polite_hits = sum(1 for marker in _SUPPORT_DE_AB_POLITE_MARKERS if marker in lowered)
    if polite_hits > 0:
        score += min(2, polite_hits)
        reasons.append("polite_markers")

    overlap = sum(1 for term in _support_ab_query_terms(user_text) if term in lowered)
    if overlap > 0:
        score += min(3, overlap)
        reasons.append("query_overlap")

    try:
        neutralized = neutralize(text)
        if len(neutralized) < max(12, text_len // 3):
            score -= 2
            reasons.append("needs_heavy_neutralize")
    except Exception:
        pass

    return score, reasons


def _build_support_judge_messages(
    *,
    user_text: str,
    candidate_a: str,
    candidate_b: str,
) -> list[dict[str, str]]:
    system_prompt = (
        "Du bist ein strenger Qualitaetsrichter fuer deutschsprachige Support-Antworten. "
        "Waehle die bessere versandfaehige Antwort nach diesen Kriterien in Reihenfolge: "
        "Korrektheit, Nutzerbezug, Klarheit, Hoeflichkeit, Knappheit. "
        "Antworte nur mit A oder B."
    )
    user_prompt = (
        "Anfrage:\n"
        f"{user_text}\n\n"
        "Antwort A:\n"
        f"{candidate_a}\n\n"
        "Antwort B:\n"
        f"{candidate_b}\n\n"
        "Welche Antwort ist die bessere versandfaehige Support-Antwort? "
        "Antworte nur mit A oder B."
    )
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]


def _parse_support_judge_choice(text: str) -> str | None:
    match = re.search(r"\b([AB])\b", text.strip().upper())
    if match:
        return match.group(1)
    return None


async def _run_nonstream_ollama_request(
    *,
    messages: list[dict[str, str]],
    raw_options: Mapping[str, Any],
    model_name: str,
    eval_mode: bool,
    client: httpx.AsyncClient | None,
    request_id: str | None,
) -> tuple[str, int | None]:
    norm_opts, base_host = normalize_ollama_options(dict(raw_options), eval_mode=eval_mode)
    think_flag = resolve_ollama_think(dict(raw_options), model_name=model_name)

    ollama_payload: dict[str, Any] = {
        "model": model_name,
        "messages": messages,
        "stream": False,
        "options": norm_opts,
    }
    if think_flag is not None:
        ollama_payload["think"] = think_flag

    ollama_url = f"{base_host}/api/chat"

    async def _post_with(_client: httpx.AsyncClient):
        headers = {"Content-Type": "application/json"}
        if request_id:
            headers[settings.REQUEST_ID_HEADER] = request_id
        if getattr(settings, "LOG_JSON", False):
            logger.info(
                _json.dumps(
                    {
                        "event": "model_request",
                        "url": ollama_url,
                        "model": ollama_payload.get("model"),
                        "options": ollama_payload.get("options", {}),
                        "stream": bool(ollama_payload.get("stream", False)),
                        "request_id": request_id,
                    },
                    ensure_ascii=False,
                )
            )
        else:
            logger.info(
                "Sende Anfrage an Ollama: %s model=%s opts=%s rid=%s",
                ollama_url,
                ollama_payload.get("model"),
                ollama_payload.get("options", {}),
                request_id,
            )
        started = time.time()
        resp = await _client.post(ollama_url, json=ollama_payload, headers=headers)
        return resp, started

    if client is not None:
        response, started = await _post_with(client)
    else:
        async with httpx.AsyncClient(timeout=settings.REQUEST_TIMEOUT) as temp_client:
            response, started = await _post_with(temp_client)

    response.raise_for_status()
    result = response.json()
    generated_content = result.get("message", {}).get("content", "")
    generated_content = _repair_strict_rpg_contract_response(messages, generated_content)

    max_len = max(0, int(getattr(settings, "LOG_TRUNCATE_CHARS", 200)))
    preview = (
        generated_content
        if len(generated_content) <= max_len
        else f"{generated_content[:max_len]}..."
    )
    duration_ms = int((time.time() - started) * 1000)
    if getattr(settings, "LOG_JSON", False):
        logger.info(
            _json.dumps(
                {
                    "event": "model_response",
                    "model": ollama_payload.get("model"),
                    "status": int(response.status_code),
                    "duration_ms": duration_ms,
                    "preview": preview,
                    "request_id": request_id,
                },
                ensure_ascii=False,
            )
        )
    else:
        logger.info(
            "Antwort von Ollama erhalten. %s ms rid=%s Inhalt: %s",
            duration_ms,
            request_id,
            preview,
        )
    return generated_content, duration_ms


def _is_strict_rpg_contract_text(text: str) -> bool:
    return bool(text) and all(title in text for title in _STRICT_RPG_SECTION_TITLES)


def _is_strict_rpg_eval_hint_text(text: str) -> bool:
    normalized = text.strip().lower()
    return normalized.startswith("hinweis:") and "verwende diese begriffe" in normalized


def _strict_rpg_contract_source_text(messages: list[dict[str, str]]) -> str:
    user_texts = [
        message.get("content", "") for message in messages if message.get("role") == "user"
    ]
    for text in reversed(user_texts):
        if _is_strict_rpg_contract_text(text) and not _is_strict_rpg_eval_hint_text(text):
            return text
    return user_texts[-1] if user_texts else ""


def _clip_text(value: str, limit: int = 400) -> str:
    return value if len(value) <= limit else f"{value[:limit]}…"


def _resolve_context_notes() -> str | None:
    try:
        enabled = bool(getattr(settings, "CONTEXT_NOTES_ENABLED", False))
        if not enabled:
            return None
        notes: str | None = None
        try:
            notes = load_context_notes(
                getattr(settings, "CONTEXT_NOTES_PATHS", []),
                getattr(settings, "CONTEXT_NOTES_MAX_CHARS", 4000),
            )
        except Exception:
            notes = None
        if notes:
            return notes
    except Exception:
        return None
    return None


def _resolve_retrieval_query(messages: list[dict[str, str]], options: Mapping[str, Any]) -> str:
    explicit_query = str(options.get("retrieval_query", "")).strip()
    if explicit_query:
        return explicit_query
    return _latest_user_text(messages).strip()


def _sanitize_contract_anchor(value: str) -> str:
    cleaned = re.sub(r"^[\s\"'`]+|[\s\"'`.,;:!?]+$", "", value.strip())
    if not cleaned or cleaned in _STRICT_RPG_SECTION_TITLES:
        return ""
    return cleaned


def _sanitize_contract_list_anchor(value: str) -> str:
    cleaned = _sanitize_contract_anchor(value)
    if not cleaned:
        return ""
    cleaned = re.sub(r"^(?:eine|ein|einen|einem|einer|der|die|das)\s+", "", cleaned, flags=re.I)
    cleaned = re.sub(r"\s+Option$", "", cleaned, flags=re.I)
    return cleaned.strip()


def _extract_visible_contract_anchors(user_text: str) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()

    def _remember(raw_value: str, *, list_item: bool = False) -> None:
        cleaned = (
            _sanitize_contract_list_anchor(raw_value)
            if list_item
            else _sanitize_contract_anchor(raw_value)
        )
        if not cleaned:
            return
        lowered = cleaned.lower()
        if lowered in seen:
            return
        seen.add(lowered)
        anchors.append(cleaned)

    for match in re.findall(r"\b(?:slot_id|turn_id)=([A-Za-z0-9._:-]+)", user_text):
        _remember(match)

    for match in re.findall(r"\b(?:slot-\d+|turn-\d+)\b", user_text, flags=re.IGNORECASE):
        _remember(match)

    progress_match = re.search(
        r"letzte sichtbare Fortschritt war (?:eine|ein|der|die|das)\s+([A-Za-z0-9._-]+)",
        user_text,
        re.IGNORECASE,
    )
    if progress_match:
        _remember(progress_match.group(1))

    visible_only_match = re.search(r"nur ueber\s+(.+?)\s+gespielt", user_text, re.IGNORECASE)
    if visible_only_match:
        for part in re.split(r",|\bund\b", visible_only_match.group(1), flags=re.IGNORECASE):
            _remember(part, list_item=True)

    option_match = re.search(r"Handlungswege stehen:\s+(.+?)\.", user_text, re.IGNORECASE)
    if option_match:
        for part in re.split(r",|\bund\b", option_match.group(1), flags=re.IGNORECASE):
            _remember(part, list_item=True)

    option_roles_match = re.search(
        r"eine\s+([A-Za-z0-9._:-]+),\s+eine\s+([A-Za-z0-9._:-]+)\s+und\s+"
        r"eine\s+([A-Za-z0-9._:-]+)\s+Option",
        user_text,
        re.IGNORECASE,
    )
    if option_roles_match:
        for group_index in (1, 2, 3):
            _remember(option_roles_match.group(group_index))

    return anchors


def _extract_strict_rpg_required_visible_terms(user_text: str) -> list[str]:
    terms: list[str] = []
    seen: set[str] = set()

    visible_only_match = re.search(r"nur ueber\s+(.+?)\s+gespielt", user_text, re.IGNORECASE)
    if not visible_only_match:
        return terms

    for part in re.split(r",|\bund\b", visible_only_match.group(1), flags=re.IGNORECASE):
        cleaned = _sanitize_contract_list_anchor(part)
        if not cleaned:
            continue
        lowered = cleaned.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        terms.append(cleaned)
    return terms


def _extract_strict_rpg_required_option_labels(user_text: str) -> list[str]:
    option_roles_match = re.search(
        r"eine\s+([A-Za-z0-9._:-]+),\s+eine\s+([A-Za-z0-9._:-]+)\s+und\s+"
        r"eine\s+([A-Za-z0-9._:-]+)\s+Option",
        user_text,
        re.IGNORECASE,
    )
    if not option_roles_match:
        return []

    labels: list[str] = []
    seen: set[str] = set()
    for group_index in (1, 2, 3):
        cleaned = _sanitize_contract_list_anchor(option_roles_match.group(group_index))
        if not cleaned:
            continue
        lowered = cleaned.lower()
        if lowered in seen:
            continue
        seen.add(lowered)
        labels.append(cleaned)
    return labels


def _extract_hidden_contract_anchors(user_text: str) -> list[str]:
    anchors: list[str] = []
    seen: set[str] = set()

    def _remember(raw_value: str) -> None:
        cleaned = _sanitize_contract_anchor(raw_value)
        if not cleaned:
            return
        lowered = cleaned.lower()
        if lowered in seen:
            return
        seen.add(lowered)
        anchors.append(cleaned)

    for match in re.findall(
        r"\b((?:verdeckte(?:r|n|s)?|interne(?:r|n|s)?|hidden)\s+"
        r"[A-Za-z0-9._:-]+(?:\s+[A-Za-z0-9._:-]+)?)",
        user_text,
        flags=re.IGNORECASE,
    ):
        _remember(match)

    return anchors


def _build_strict_rpg_contract_hint(messages: list[dict[str, str]]) -> str | None:
    user_text = _strict_rpg_contract_source_text(messages)
    if not _is_strict_rpg_contract_text(user_text):
        return None

    lines = [
        "[Text-RPG-Formatvertrag]",
        (
            "Antworte strikt mit genau diesen Abschnittstiteln: "
            "Szene:, Konsequenz:, Optionen:, State_Patches:."
        ),
        "Unter Optionen muessen genau drei nummerierte Zeilen beginnen mit 1. , 2. , 3. .",
        (
            "Fuege keine weiteren sichtbaren Ueberschriften vor Szene: "
            "oder nach State_Patches: hinzu."
        ),
        (
            "State_Patches muss immer vorhanden sein. "
            "Wenn nichts zu aendern ist, schreibe direkt darunter genau []."
        ),
        "Sichtbare Begriffe und IDs aus dem Userprompt muessen woertlich erhalten bleiben.",
        (
            "Jeder sichtbare Pflichtanker muss mindestens einmal exakt in Szene: "
            "oder Konsequenz: auftauchen. Nicht paraphrasieren, nicht uebersetzen "
            "und keine Schreibweise normalisieren."
        ),
        (
            "Begriffe, die im Userprompt als verdeckt, intern, hidden oder "
            "nicht verratbar markiert sind, duerfen nicht in der sichtbaren Antwort auftauchen."
        ),
    ]
    anchors = _extract_visible_contract_anchors(user_text)
    if anchors:
        lines.append(
            (
                "Sichtbare Pflichtanker aus dem Userprompt, die exakt so in der "
                "Antwort stehen muessen: "
            )
            + ", ".join(anchors)
        )
        lines.append(
            "Wenn ein Pflichtanker ASCII-Umschriften wie ae, oe oder ue nutzt, muss genau "
            "diese ASCII-Schreibweise sichtbar bleiben."
        )
    hidden_anchors = _extract_hidden_contract_anchors(user_text)
    if hidden_anchors:
        lines.append(
            (
                "Diese verdeckten Begriffe aus dem Userprompt duerfen woertlich "
                "nicht in der sichtbaren Antwort auftauchen: "
            )
            + ", ".join(hidden_anchors)
        )
    return "\n".join(lines)


def _inject_strict_rpg_contract_message(messages: list[dict[str, str]]) -> list[dict[str, str]]:
    hint = _build_strict_rpg_contract_hint(messages)
    if hint is None:
        return messages
    if any(
        message.get("role") == "system"
        and message.get("content", "").startswith("[Text-RPG-Formatvertrag]")
        for message in messages
    ):
        return messages
    insert_at = 1 if messages and messages[0].get("role") == "system" else 0
    messages.insert(insert_at, {"role": "system", "content": hint})
    return messages


def _is_strict_rpg_contract_prompt(user_text: str) -> bool:
    return _is_strict_rpg_contract_text(user_text)


def _has_strict_rpg_sections(response_text: str) -> bool:
    return any(title in response_text for title in _STRICT_RPG_SECTION_TITLES)


def _build_strict_rpg_fallback_option_lines(anchors: list[str]) -> list[str]:
    if {"vorsichtige", "riskante", "soziale"}.issubset(set(anchors)):
        return [
            (
                "1. vorsichtige Option: Du sicherst zuerst die Lage und pruefst die "
                "naechsten Hinweise."
            ),
            (
                "2. riskante Option: Du gehst sofort vor und akzeptierst den hoehren "
                "Druck des Moments."
            ),
            "3. soziale Option: Du suchst die Entscheidung gemeinsam mit den Beteiligten.",
        ]

    first_anchor = anchors[0] if anchors else "Lage"
    second_anchor = anchors[1] if len(anchors) > 1 else "Druck"
    third_anchor = anchors[2] if len(anchors) > 2 else "Entscheidung"
    return [
        f"1. {first_anchor} genauer pruefen und die Lage kontrolliert halten.",
        f"2. Unter {second_anchor} sofort vorstossen und das Risiko bewusst tragen.",
        f"3. Die naechste {third_anchor} gemeinsam absichern und danach weitergehen.",
    ]


def _expand_strict_rpg_anchor_aliases(anchor: str) -> list[str]:
    lowered = anchor.strip().lower()
    if not lowered:
        return []
    umlauted = lowered.replace("ae", "ä").replace("oe", "ö").replace("ue", "ü").replace("ss", "ß")
    if umlauted == lowered:
        return []
    return [umlauted]


def _replace_strict_rpg_anchor_aliases(text: str, anchors: list[str]) -> str:
    repaired_text = text
    for anchor in anchors:
        if anchor in repaired_text:
            continue
        for alias in _expand_strict_rpg_anchor_aliases(anchor):
            repaired_text, replacements = re.subn(
                re.escape(alias),
                anchor,
                repaired_text,
                count=1,
                flags=re.IGNORECASE,
            )
            if replacements:
                break
    return repaired_text


def _extract_strict_rpg_sections(response_text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    for match in re.finditer(
        r"(Szene:|Konsequenz:|Optionen:|State_Patches:)\s*(.*?)(?=(?:Szene:|Konsequenz:|Optionen:|State_Patches:)|\Z)",
        response_text,
        flags=re.DOTALL,
    ):
        title = match.group(1)
        if title in sections:
            continue
        sections[title] = match.group(2).strip()
    return sections


def _normalize_strict_rpg_narration(text: str, fallback: str) -> str:
    cleaned = _MULTISPACE_RE.sub(" ", text).strip()
    return cleaned or fallback


def _split_strict_rpg_option_bodies(option_text: str) -> list[str]:
    numbered_options: dict[int, str] = {}
    for match in re.finditer(
        r"(?:^|\s)([123])\.\s*(.*?)(?=(?:\s+[123]\.\s)|\Z)",
        option_text.strip(),
        flags=re.DOTALL,
    ):
        option_index = int(match.group(1))
        if option_index in numbered_options:
            continue
        numbered_options[option_index] = match.group(2).strip()
    return [numbered_options[index] for index in (1, 2, 3) if index in numbered_options]


def _strip_strict_rpg_option_lead(text: str) -> str:
    cleaned = text.strip()
    cleaned = re.sub(r"^[123]\.\s*", "", cleaned)
    cleaned = re.sub(r"^(vorsichtige|riskante|soziale)\s+Option:\s*", "", cleaned, flags=re.I)
    cleaned = re.sub(r"^(vorsichtige|riskante|soziale)\s*:\s*", "", cleaned, flags=re.I)
    cleaned = re.sub(
        r"^(vorsichtig(?:e)?|riskant(?:e)?|sozial(?:e)?)\s*:?\s*",
        "",
        cleaned,
        flags=re.I,
    )
    cleaned = _MULTISPACE_RE.sub(" ", cleaned).strip(" -")
    return cleaned


def _unique_contract_terms(*groups: list[str]) -> list[str]:
    unique_terms: list[str] = []
    seen: set[str] = set()
    for group in groups:
        for value in group:
            cleaned = _sanitize_contract_anchor(value)
            if not cleaned:
                continue
            lowered = cleaned.lower()
            if lowered in seen:
                continue
            seen.add(lowered)
            unique_terms.append(cleaned)
    return unique_terms


def _normalize_strict_rpg_option_lines(
    option_text: str,
    anchors: list[str],
    required_labels: list[str],
) -> list[str]:
    fallback_seed = required_labels if required_labels else anchors
    fallback_lines = _build_strict_rpg_fallback_option_lines(fallback_seed)
    fallback_bodies = [_strip_strict_rpg_option_lead(line) for line in fallback_lines]
    option_bodies = _split_strict_rpg_option_bodies(option_text) if option_text else []

    normalized_lines: list[str] = []
    for option_index in range(3):
        raw_body = option_bodies[option_index] if option_index < len(option_bodies) else ""
        body = _strip_strict_rpg_option_lead(raw_body)
        if not body:
            body = fallback_bodies[option_index]
        if required_labels:
            normalized_lines.append(
                f"{option_index + 1}. {required_labels[option_index]} Option: {body}"
            )
        else:
            normalized_lines.append(f"{option_index + 1}. {body}")
    return normalized_lines


def _normalize_strict_rpg_state_patches(state_patches_text: str) -> str:
    cleaned = state_patches_text.strip()
    return cleaned or "[]"


def _ensure_strict_rpg_visible_anchors(
    scene_text: str,
    consequence_text: str,
    anchors: list[str],
) -> tuple[str, str]:
    if not anchors:
        return scene_text, consequence_text

    scene_text = _replace_strict_rpg_anchor_aliases(scene_text, anchors)
    consequence_text = _replace_strict_rpg_anchor_aliases(consequence_text, anchors)

    combined_text = "\n".join(part for part in (scene_text, consequence_text) if part)
    missing_anchors = [anchor for anchor in anchors if anchor not in combined_text]
    if not missing_anchors:
        return scene_text, consequence_text

    if {"Geraeusch", "Druck", "Entscheidung"}.intersection(set(missing_anchors)):
        preferred_terms = [
            term for term in ("Geraeusch", "Druck", "Entscheidung") if term in anchors
        ]
        anchor_clause = f"{', '.join(preferred_terms)} bleiben die einzigen sichtbaren Leitplanken."
    else:
        anchor_clause = f"Sichtbare Leitplanken: {', '.join(missing_anchors)}."
    if consequence_text:
        separator = " " if consequence_text.rstrip().endswith((".", "!", "?")) else ". "
        consequence_text = consequence_text.rstrip() + separator + anchor_clause
    else:
        consequence_text = anchor_clause
    return scene_text, consequence_text


def _compose_strict_rpg_contract_response(
    scene_text: str,
    consequence_text: str,
    option_lines: list[str],
    state_patches_text: str,
) -> str:
    return "\n".join(
        [
            f"Szene: {scene_text}",
            "",
            f"Konsequenz: {consequence_text}",
            "",
            "Optionen:",
            *option_lines,
            "",
            "State_Patches:",
            state_patches_text,
        ]
    ).strip()


def _repair_strict_rpg_contract_response(messages: list[dict[str, str]], response_text: str) -> str:
    user_text = _strict_rpg_contract_source_text(messages)
    if not _is_strict_rpg_contract_prompt(user_text) or not response_text.strip():
        return response_text

    sections = _extract_strict_rpg_sections(response_text)
    visible_anchors = _extract_visible_contract_anchors(user_text)
    required_visible_terms = _extract_strict_rpg_required_visible_terms(user_text)
    required_option_labels = _extract_strict_rpg_required_option_labels(user_text)
    anchors = _unique_contract_terms(required_visible_terms, visible_anchors)
    scene_source = sections.get("Szene:", "")
    consequence_source = sections.get("Konsequenz:", "")
    if not sections:
        scene_source = response_text.strip()

    scene_text = _normalize_strict_rpg_narration(scene_source, "Die Lage bleibt angespannt.")
    default_consequence = "Der naechste Schritt bleibt offen."
    if any(anchor in {"Geraeusch", "Druck", "Entscheidung"} for anchor in anchors):
        default_consequence = "Der Druck der naechsten Entscheidung bleibt unmittelbar spuerbar."
    consequence_text = _normalize_strict_rpg_narration(consequence_source, default_consequence)
    scene_text, consequence_text = _ensure_strict_rpg_visible_anchors(
        scene_text,
        consequence_text,
        anchors,
    )

    option_lines = _normalize_strict_rpg_option_lines(
        sections.get("Optionen:", ""),
        anchors,
        required_option_labels,
    )
    state_patches_text = _normalize_strict_rpg_state_patches(sections.get("State_Patches:", ""))
    return _compose_strict_rpg_contract_response(
        scene_text,
        consequence_text,
        option_lines,
        state_patches_text,
    )


def _resolve_rag_hits(query: str) -> list[dict[str, Any]]:
    if not query:
        return []
    if not bool(getattr(settings, "RAG_ENABLED", False)):
        return []
    from utils.rag import load_index, retrieve

    rag_path = str(
        getattr(settings, "RAG_INDEX_PATH", "novapolis_agent/eval/results/rag/index.json")
    )
    try:
        idx: _TfIdfIndex | None = load_index(rag_path)
        if idx is None:
            return []
        top_k = int(getattr(settings, "RAG_TOP_K", 3))
        hits_any: object = retrieve(idx, query, top_k=top_k)
        hits = cast(list[dict[str, Any]], hits_any)
        return hits or []
    except FileNotFoundError:
        return []
    except Exception:
        return []


def _build_rag_snippet_text(hits: list[dict[str, Any]]) -> str:
    return "\n\n".join(
        f"- {hit.get('source', '?')}: {_clip_text(str(hit.get('text', '')))}" for hit in hits
    )


def _session_snapshot_text(session_id: str | None) -> str | None:
    if not session_id:
        return None
    record = _sim_api.load_session_record(session_id)
    if record is None:
        return None
    snapshot: dict[str, Any] = {
        "session_id": record.session_id,
        "session_status": record.session_status,
        "campaign_id": record.campaign_id,
        "scene_id": record.scene_id,
        "slot_id": record.slot_id,
        "slot_index": record.slot_index,
        "turn_id": record.turn_id,
        "resume_checkpoint_id": record.resume_checkpoint_id,
        "turn_context": record.turn_context.model_dump(),
        "carry_over": [item.model_dump() for item in record.carry_over[-3:]],
        "checkpoints": record.checkpoints[-3:],
        "world_tick": record.world_state.tick,
        "world_time": record.world_state.time,
        "recent_pc_log": record.pc_log[-2:],
        "recent_state_patches": [patch.model_dump() for patch in record.state_patches[-3:]],
    }
    return _json.dumps(snapshot, ensure_ascii=False, indent=2)


def _parse_state_patches(content: str) -> list[_sim_api.StatePatchRecord]:
    match = re.search(
        r"(?is)state_patches\s*:\s*(.*?)(?:\n\s*\n|\Z)",
        content,
    )
    if not match:
        return []
    raw_block = match.group(1).strip()
    if not raw_block:
        return []
    normalized = raw_block.lower().strip(" .")
    if normalized in {"none", "keine", "keine aenderungen", "keine änderungen"}:
        return []

    patches: list[_sim_api.StatePatchRecord] = []
    raw_lines = [line.strip() for line in raw_block.splitlines() if line.strip()]
    if not raw_lines:
        raw_lines = [raw_block]

    for index, line in enumerate(raw_lines, start=1):
        cleaned = line.lstrip("-* ").strip()
        if not cleaned:
            continue
        if cleaned.startswith("{") and cleaned.endswith("}"):
            try:
                payload = _json.loads(cleaned)
                if isinstance(payload, dict):
                    patches.append(_sim_api.StatePatchRecord.model_validate(payload))
                    continue
            except Exception:
                pass

        path_match = re.match(r"(?P<path>[A-Za-z0-9_.-]+)\s*=\s*(?P<value>.+)", cleaned)
        if path_match:
            patches.append(
                _sim_api.StatePatchRecord(
                    patch_id=f"llm-{index}",
                    scope="session",
                    op="set",
                    path=path_match.group("path"),
                    value=path_match.group("value").strip(),
                )
            )
            continue

        patches.append(
            _sim_api.StatePatchRecord(
                patch_id=f"llm-{index}",
                scope="narrative",
                op="note",
                path=f"state_patches/{index}",
                value=cleaned,
            )
        )
    return patches


def _persist_orchestrator_turn(request: ChatRequest, content: str) -> None:
    options = _options_to_dict(getattr(request, "options", None))
    session_id_raw = getattr(request, "session_id", None) or options.get("session_id")
    session_id = str(session_id_raw).strip() if isinstance(session_id_raw, str) else ""
    if not session_id:
        return

    campaign_id = str(options.get("campaign_id", "")).strip() or None
    scene_id = str(options.get("scene_id", "")).strip() or None
    slot_id = str(options.get("slot_id", "")).strip() or None
    turn_id = str(options.get("turn_id", "")).strip() or None
    turn_mode = str(options.get("turn_mode", "")).strip() or "standard"
    raw_turn_window = options.get("turn_window_minutes")
    raw_tick_minutes = options.get("tick_minutes")
    budget_class = str(options.get("budget_class", "")).strip() or None
    turn_window_minutes = (
        int(raw_turn_window)
        if isinstance(raw_turn_window, int) and raw_turn_window > 0
        else TEXT_RPG_DEFAULT_TURN_WINDOW_MINUTES
    )
    tick_minutes = (
        int(raw_tick_minutes)
        if isinstance(raw_tick_minutes, int) and raw_tick_minutes > 0
        else None
    )
    carry_over_raw = options.get("carry_over")
    carry_over: list[CarryOverItem] | None = None
    if isinstance(carry_over_raw, list):
        carry_over_entries = cast(list[Any], carry_over_raw)
        carry_over = [CarryOverItem.model_validate(item) for item in carry_over_entries]
    state_patches = _parse_state_patches(content)
    _sim_api.upsert_session(
        session_id,
        _sim_api.SessionUpsertRequest(
            contract_version=TEXT_RPG_SESSION_CONTRACT_VERSION,
            session_status="active",
            campaign_id=campaign_id,
            scene_id=scene_id,
            slot_id=slot_id,
            turn_id=turn_id,
            turn_context=TurnContext(
                turn_mode=turn_mode,
                turn_window_minutes=turn_window_minutes,
                tick_minutes=tick_minutes,
                budget_class=budget_class,
            ),
            carry_over=carry_over,
            pc_log=[{"role": "assistant", "channel": "pc", "content": content}],
            state_patches=state_patches,
        ),
    )


def _build_orchestrator_messages(
    request: ChatRequest,
    *,
    context_notes: str | None = None,
    rag_hits: list[dict[str, Any]] | None = None,
    retrieval_query: str | None = None,
) -> list[dict[str, str]]:
    options = _options_to_dict(getattr(request, "options", None))
    enabled = _orchestrator_enabled(options)
    if not enabled:
        return []

    session_id = getattr(request, "session_id", None) or options.get("session_id")
    frame_fields = {
        "profile_id": getattr(request, "profile_id", None),
        "campaign_id": options.get("campaign_id"),
        "session_id": session_id,
        "scene_id": options.get("scene_id"),
        "slot_id": options.get("slot_id"),
        "turn_id": options.get("turn_id"),
    }
    lines = [
        "[Text-RPG-Orchestrator]",
        "Arbeite als kontrollierte Spielleitung auf dem kanonischen Novapolis-Produktpfad.",
        (
            "Nutze Projektkontext, RP-SSOT und Scheduler-Hinweise nur regelkonform "
            "und ohne freie Kanonerweiterung."
        ),
        "Antworte weiter im Format Szene/Konsequenz/Optionen/State_Patches.",
        (
            "Inhalte aus dem Hidden-Context bleiben intern und duerfen nicht direkt "
            "an die PC-Sicht auslaufen."
        ),
    ]

    frame_lines = [
        f"- {key}: {value}"
        for key, value in frame_fields.items()
        if isinstance(value, str) and value.strip()
    ]
    if frame_lines:
        lines.extend(["[Sitzungsrahmen]", *frame_lines])

    session_snapshot = _session_snapshot_text(session_id)
    if session_snapshot:
        lines.extend(["[Session-Stand intern]", session_snapshot])

    public_context = str(options.get("public_context", "")).strip()
    if public_context:
        lines.extend(["[PC-Sicht]", public_context])

    context_notes_text = str(context_notes or "").strip()
    if context_notes_text:
        lines.extend(["[Projektkontext-Notizen intern]", context_notes_text])

    retrieval_query_text = str(retrieval_query or "").strip()
    if retrieval_query_text:
        lines.extend(["[Retrieval-Query]", retrieval_query_text])

    if rag_hits:
        lines.extend(["[RP-/Projektkontext-Retrieval intern]", _build_rag_snippet_text(rag_hits)])

    hidden_context = str(options.get("hidden_context", "")).strip()
    if hidden_context:
        lines.extend(["[Hidden-Context intern]", hidden_context])

    scheduler_hints = _coerce_string_list(options.get("scheduler_hints"))
    if scheduler_hints:
        lines.extend(["[Scheduler-Hinweise]", *[f"- {hint}" for hint in scheduler_hints]])

    state_patch_hints = _coerce_string_list(options.get("state_patch_hints"))
    if state_patch_hints:
        lines.extend(["[State-Patch-Ziele]", *[f"- {hint}" for hint in state_patch_hints]])

    return [{"role": "system", "content": "\n".join(lines)}]


def _inject_orchestrator_messages(
    messages: list[dict[str, str]],
    request: ChatRequest,
    *,
    context_notes: str | None = None,
    rag_hits: list[dict[str, Any]] | None = None,
    retrieval_query: str | None = None,
) -> list[dict[str, str]]:
    additions = _build_orchestrator_messages(
        request,
        context_notes=context_notes,
        rag_hits=rag_hits,
        retrieval_query=retrieval_query,
    )
    if not additions:
        return messages
    insert_at = 1 if messages and messages[0].get("role") == "system" else 0
    for message in reversed(additions):
        messages.insert(insert_at, message)
    return messages


def _build_contract_chat_response(
    request: ChatRequest,
    *,
    content: str,
    model: str | None,
) -> ChatResponse:
    options = _options_to_dict(getattr(request, "options", None))
    session_id_raw = getattr(request, "session_id", None) or options.get("session_id")
    session_id = str(session_id_raw).strip() if isinstance(session_id_raw, str) else None
    campaign_id = str(options.get("campaign_id", "")).strip() or None
    scene_id = str(options.get("scene_id", "")).strip() or None
    slot_id = str(options.get("slot_id", "")).strip() or None
    turn_id = str(options.get("turn_id", "")).strip() or None
    turn_context: TurnContext | None = None
    carry_over: list[CarryOverItem] | None = None
    checkpoint_id: str | None = None

    contract_active = _orchestrator_enabled(options) or any(
        value for value in (session_id, campaign_id, scene_id, slot_id, turn_id)
    )

    if contract_active and session_id:
        record = _sim_api.load_session_record(session_id)
        if record is not None:
            campaign_id = record.campaign_id or campaign_id
            scene_id = record.scene_id or scene_id
            slot_id = record.slot_id or slot_id
            turn_id = record.turn_id or turn_id
            checkpoint_id = record.resume_checkpoint_id
            turn_context = record.turn_context
            carry_over = list(record.carry_over)

    if contract_active and turn_context is None:
        raw_turn_window = options.get("turn_window_minutes")
        raw_tick_minutes = options.get("tick_minutes")
        turn_context = TurnContext(
            turn_mode=str(options.get("turn_mode", "")).strip() or "standard",
            turn_window_minutes=(
                int(raw_turn_window)
                if isinstance(raw_turn_window, int) and raw_turn_window > 0
                else TEXT_RPG_DEFAULT_TURN_WINDOW_MINUTES
            ),
            tick_minutes=(
                int(raw_tick_minutes)
                if isinstance(raw_tick_minutes, int) and raw_tick_minutes > 0
                else None
            ),
            budget_class=str(options.get("budget_class", "")).strip() or None,
        )

    if contract_active and checkpoint_id is None:
        checkpoint_id = turn_id

    return ChatResponse(
        content=content,
        model=model,
        contract_version=TEXT_RPG_SESSION_CONTRACT_VERSION if contract_active else None,
        session_id=session_id,
        campaign_id=campaign_id,
        scene_id=scene_id,
        slot_id=slot_id,
        turn_id=turn_id,
        session_status="active" if contract_active else None,
        resume_checkpoint_id=checkpoint_id,
        replay_checkpoint_id=checkpoint_id,
        log_channels=list(TEXT_RPG_LOG_CHANNELS) if contract_active else None,
        turn_context=turn_context,
        carry_over=carry_over if contract_active else None,
    )


def _append_shadow_mode_event(
    *,
    request: ChatRequest,
    eval_mode: bool,
    unrestricted_mode: bool,
    request_id: str | None,
    stream: bool,
    messages: list[dict[str, str]],
    response_text: str,
    policy_post: str,
) -> None:
    if not _shadow_mode_enabled(request, eval_mode):
        return
    if unrestricted_mode:
        return

    try:
        user_texts = [m.get("content", "") for m in messages if m.get("role") == "user"]
        last_user = user_texts[-1] if user_texts else ""
        event: dict[str, Any] = {
            "ts": int(time.time()),
            "request_id": request_id,
            "stream": stream,
            "mode": "eval" if eval_mode else "default",
            "policy_post": policy_post,
            "rag_enabled": bool(getattr(settings, "RAG_ENABLED", False)),
            "rag_index_path": str(getattr(settings, "RAG_INDEX_PATH", "")),
            "user_chars": len(last_user),
            "response_chars": len(response_text),
            "user_hash": _safe_sha256(last_user),
            "response_hash": _safe_sha256(response_text),
            # Redacted previews enable later AI/human review without storing raw PII.
            "user_preview_redacted": _redact_preview(last_user),
            "response_preview_redacted": _redact_preview(response_text),
        }
        out_path = Path(
            str(getattr(settings, "SHADOW_MODE_LOG_PATH", ".tmp/results/logs/shadow_mode.jsonl"))
        )
        out_path.parent.mkdir(parents=True, exist_ok=True)
        with out_path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(_json.dumps(event, ensure_ascii=False) + "\n")
    except Exception as shadow_err:
        logger.warning("Schattenmodus-Logging fehlgeschlagen rid=%s: %s", request_id, shadow_err)


async def stream_chat_request(
    request: ChatRequest,
    eval_mode: bool = False,
    unrestricted_mode: bool = False,
    client: httpx.AsyncClient | None = None,
    request_id: str | None = None,
):
    messages: list[dict[str, str]] = []
    for m in request.messages:
        if isinstance(m, dict):
            role = m.get("role", "user")
            content = m.get("content", "")
        else:
            role = getattr(m, "role", "user")
            content = getattr(m, "content", "")
        messages.append({"role": role, "content": content})

    if eval_mode:
        logger.info("Eval-Modus aktiv (stream): Ersetze Systemprompt rid=%s", request_id)
        messages = [msg for msg in messages if msg.get("role") != "system"]
        sys_prompt = EVAL_SYSTEM_PROMPT
        if getattr(settings, "CONTENT_POLICY_ENABLED", False):
            try:
                sys_prompt = modify_prompt_for_freedom(sys_prompt)
            except Exception:
                pass
        messages.insert(0, {"role": "system", "content": sys_prompt})
    elif unrestricted_mode:
        logger.info(
            "Uneingeschränkter Modus aktiv (stream): Ersetze Systemprompt rid=%s", request_id
        )
        messages = [msg for msg in messages if msg.get("role") != "system"]
        sys_prompt = UNRESTRICTED_SYSTEM_PROMPT
        if getattr(settings, "CONTENT_POLICY_ENABLED", False):
            try:
                sys_prompt = modify_prompt_for_freedom(sys_prompt)
            except Exception:
                pass
        messages.insert(0, {"role": "system", "content": sys_prompt})
    else:
        if not any(msg.get("role") == "system" for msg in messages):
            sys_prompt = DEFAULT_SYSTEM_PROMPT
            if getattr(settings, "CONTENT_POLICY_ENABLED", False):
                try:
                    sys_prompt = modify_prompt_for_freedom(sys_prompt)
                except Exception:
                    pass
            messages.insert(0, {"role": "system", "content": sys_prompt})

    messages = _inject_strict_rpg_contract_message(messages)

    # Optionaler Canvas-Zähler aus Request-Optionen
    try:
        cc_val: int | None = None
        opts_any = getattr(request, "options", None)
        if isinstance(opts_any, Mapping):
            try:
                v = cast(Mapping[object, Any], opts_any).get("canvas_count")
            except Exception:
                v = None
        elif opts_any is not None:
            md = getattr(opts_any, "model_dump", None)
            v = None
            if callable(md):
                try:
                    raw = md()
                    if isinstance(raw, Mapping):
                        v = cast(Mapping[object, Any], raw).get("canvas_count")
                except Exception:
                    v = None
        else:
            v = None
        if isinstance(v, int):
            cc_val = v
        elif isinstance(v, str) and v.isdigit():
            try:
                cc_val = int(v)
            except Exception:
                cc_val = None
        if cc_val is not None and cc_val >= 0:
            messages.insert(1, {"role": "system", "content": f"Canvas geladen: {cc_val}"})
    except Exception:
        pass

    options = _options_to_dict(getattr(request, "options", None))
    orchestrator_enabled = _orchestrator_enabled(options)
    notes: str | None = None
    rag_hits: list[dict[str, Any]] = []
    retrieval_query = ""

    try:
        notes = _resolve_context_notes()
        if notes and not orchestrator_enabled:
            messages.insert(1, {"role": "system", "content": f"[Kontext-Notizen]\n{notes}"})
    except Exception:
        notes = None

    try:
        retrieval_query = _resolve_retrieval_query(messages, options)
        rag_hits = _resolve_rag_hits(retrieval_query)
        if rag_hits and not orchestrator_enabled:
            messages.insert(
                1,
                {"role": "system", "content": f"[RAG]\n{_build_rag_snippet_text(rag_hits)}"},
            )
    except Exception:
        rag_hits = []

    try:
        messages = _inject_orchestrator_messages(
            messages,
            request,
            context_notes=notes if orchestrator_enabled else None,
            rag_hits=rag_hits if orchestrator_enabled else None,
            retrieval_query=retrieval_query if orchestrator_enabled else None,
        )
    except Exception:
        pass

    session_id: str | None = None
    try:
        sid_top = getattr(request, "session_id", None)
        opts_any0 = getattr(request, "options", None)
        opts0: dict[str, Any] = {}
        if isinstance(opts_any0, Mapping):
            try:
                opts_map0 = cast(Mapping[object, Any], opts_any0)
                opts0 = {str(k): v for k, v in opts_map0.items()}
            except Exception:
                opts0 = {}
        elif opts_any0 is not None:
            md = getattr(opts_any0, "model_dump", None)
            if callable(md):
                try:
                    raw0 = md()
                    if isinstance(raw0, Mapping):
                        opts0 = {str(k): v for k, v in cast(Mapping[object, Any], raw0).items()}
                    else:
                        opts0 = {}
                except Exception:
                    opts0 = {}
            else:
                opts0 = {}
        sid_opt = opts0.get("session_id")
        sid_val = sid_top or sid_opt
        session_id = str(sid_val) if isinstance(sid_val, str) and sid_val else None
    except Exception:
        session_id = None

    try:
        messages = await compose_with_memory(cast(list[Mapping[str, str]], messages), session_id)
    except Exception:
        pass

    try:
        mode = "unrestricted" if unrestricted_mode else ("eval" if eval_mode else "default")
        profile_id = getattr(request, "profile_id", None)
        pre = apply_pre(cast(list[Mapping[str, Any]], messages), mode=mode, profile_id=profile_id)
        if pre and getattr(pre, "action", "allow") == "block":

            async def _blocked_gen():
                if getattr(settings, "LOG_JSON", False):
                    logger.info(
                        _json.dumps(
                            {
                                "event": "policy_pre",
                                "action": "block",
                                "mode": mode,
                                "request_id": request_id,
                            },
                            ensure_ascii=False,
                        )
                    )
                else:
                    logger.info("Policy-Pre blockierte die Anfrage. rid=%s", request_id)
                yield "event: error\ndata: policy_block\n\n"
                yield "event: done\ndata: {}\n\n"

            return _blocked_gen()
        if pre and getattr(pre, "action", "allow") == "rewrite" and getattr(pre, "messages", None):
            pre_msgs = getattr(pre, "messages", None)
            if pre_msgs:
                messages = [
                    {
                        "role": str((cast(Mapping[str, Any], message)).get("role", "user")),
                        "content": str((cast(Mapping[str, Any], message)).get("content", "")),
                    }
                    for message in pre_msgs
                    if isinstance(message, Mapping)
                ]
            if getattr(settings, "LOG_JSON", False):
                logger.info(
                    _json.dumps(
                        {
                            "event": "policy_pre",
                            "action": "rewrite",
                            "mode": mode,
                            "request_id": request_id,
                        },
                        ensure_ascii=False,
                    )
                )
            else:
                logger.info("Policy-Pre hat Nachrichten umgeschrieben. rid=%s", request_id)
    except Exception:
        pass

    req_model = getattr(request, "model", None)
    raw_any = getattr(request, "options", None)
    raw_opts: dict[str, Any] = {}
    if isinstance(raw_any, Mapping):
        try:
            raw_map = cast(Mapping[object, Any], raw_any)
            raw_opts = {str(k): v for k, v in raw_map.items()}
        except Exception:
            raw_opts = {}
    elif raw_any is not None:
        md = getattr(raw_any, "model_dump", None)
        if callable(md):
            try:
                raw0 = md()
                if isinstance(raw0, Mapping):
                    raw_opts = {str(k): v for k, v in cast(Mapping[object, Any], raw0).items()}
                else:
                    raw_opts = {}
            except Exception:
                raw_opts = {}
        else:
            raw_opts = {}
    else:
        raw_opts = {}
    resolved_model = req_model or settings.MODEL_NAME
    norm_opts, base_host = normalize_ollama_options(raw_opts, eval_mode=eval_mode)
    think_flag = resolve_ollama_think(raw_opts, model_name=resolved_model)

    try:
        if getattr(settings, "SESSION_MEMORY_ENABLED", False):
            opts_mem = getattr(request, "options", None)
            sess_id: str | None = None
            if isinstance(opts_mem, dict):
                opts_mapping = cast(Mapping[str, Any], opts_mem)
                val_any = opts_mapping.get("session_id")
                sess_id = val_any if isinstance(val_any, str) and val_any else None
            if isinstance(sess_id, str) and sess_id:
                prior = session_memory.get(sess_id)
                if prior:
                    sys_msgs = [m for m in messages if m.get("role") == "system"]
                    non_sys = [m for m in messages if m.get("role") != "system"]
                    prior_cast = [
                        {"role": str(m.get("role", "user")), "content": str(m.get("content", ""))}
                        for m in prior
                    ]
                    messages = sys_msgs + prior_cast + non_sys
    except Exception:
        pass

    ollama_payload: dict[str, Any] = {
        "model": resolved_model,
        "messages": messages,
        "stream": True,
        "options": norm_opts,
    }
    if think_flag is not None:
        ollama_payload["think"] = think_flag

    ollama_url = f"{base_host}/api/chat"

    headers = {"Content-Type": "application/json"}
    if request_id:
        headers[settings.REQUEST_ID_HEADER] = request_id
    if getattr(settings, "LOG_JSON", False):
        logger.info(
            _json.dumps(
                {
                    "event": "model_request",
                    "url": ollama_url,
                    "model": ollama_payload.get("model"),
                    "options": ollama_payload.get("options", {}),
                    "stream": True,
                    "request_id": request_id,
                },
                ensure_ascii=False,
            )
        )
    else:
        logger.info(
            "Sende Streaming-Anfrage an Ollama: %s model=%s opts=%s rid=%s",
            ollama_url,
            ollama_payload.get("model"),
            ollama_payload.get("options", {}),
            request_id,
        )

    async def _gen():
        started = time.time()
        try:
            try:
                mode0 = (
                    "unrestricted" if unrestricted_mode else ("eval" if eval_mode else "default")
                )
                params: dict[str, Any] = {
                    "mode": mode0,
                    "request_id": request_id,
                    "model": ollama_payload.get("model"),
                    "options": ollama_payload.get("options", {}),
                }
                payload_json = _json.dumps({"params": params}, ensure_ascii=False)
                yield "event: meta\ndata: " + payload_json + "\n\n"
            except Exception:
                pass

            async def _do_stream(_client: httpx.AsyncClient):
                final_text_parts: list[str] = []
                async with _client.stream(
                    "POST", ollama_url, json=ollama_payload, headers=headers
                ) as resp:
                    resp.raise_for_status()
                    async for line in resp.aiter_lines():
                        if not line:
                            continue
                        try:
                            data = _json.loads(line)
                            content = data.get("message", {}).get("content")
                            if content:
                                yield f"data: {content}\n\n"
                                final_text_parts.append(content)
                            if data.get("done"):
                                break
                        except Exception:
                            yield f"data: {line}\n\n"
                try:
                    final_text = "".join(final_text_parts)
                    mode = (
                        "unrestricted"
                        if unrestricted_mode
                        else ("eval" if eval_mode else "default")
                    )
                    profile_id = getattr(request, "profile_id", None)
                    final_text = _repair_strict_rpg_contract_response(messages, final_text)
                    action = "allow"
                    effective_text = final_text
                    policy_post = "allow"
                    try:
                        post = apply_post(final_text, mode=mode, profile_id=profile_id)
                        action = getattr(post, "action", "allow")
                        if action == "rewrite" and getattr(post, "text", None):
                            effective_text = str(post.text)
                        elif action == "block":
                            effective_text = final_text
                    except NameError:
                        try:
                            fn = apply_post
                            text_key = "text"
                            if (
                                callable(fn)
                                and hasattr(fn, "__globals__")
                                and isinstance(fn.__globals__, dict)
                            ):
                                globals_dict = fn.__globals__
                                had_key = text_key in globals_dict
                                prev_val = globals_dict.get(text_key)
                                globals_dict[text_key] = final_text
                                try:
                                    post = fn(final_text, mode=mode, profile_id=profile_id)
                                    action = getattr(post, "action", "allow")
                                    if action == "rewrite" and getattr(post, "text", None):
                                        effective_text = str(post.text)
                                    elif action == "block":
                                        effective_text = final_text
                                finally:
                                    if had_key:
                                        globals_dict[text_key] = prev_val
                                    else:
                                        globals_dict.pop(text_key, None)
                            else:
                                action = "allow"
                                effective_text = final_text
                        except Exception:
                            action = "allow"
                            effective_text = final_text
                    except Exception:
                        action = "allow"
                        effective_text = final_text

                    effective_text = _repair_strict_rpg_contract_response(messages, effective_text)

                    try:
                        if action == "block":
                            policy_post = "blocked"
                        elif effective_text != final_text and effective_text:
                            policy_post = "rewritten"
                        meta: dict[str, Any] = {
                            "policy_post": policy_post,
                            "request_id": request_id,
                        }
                        if policy_post == "rewritten":
                            delta_len = max(0, len(effective_text) - len(final_text))
                            meta["delta_len"] = delta_len
                        meta_json = _json.dumps(meta, ensure_ascii=False)
                        yield "event: meta\ndata: " + meta_json + "\n\n"
                    except Exception:
                        pass

                    try:
                        _append_shadow_mode_event(
                            request=request,
                            eval_mode=eval_mode,
                            unrestricted_mode=unrestricted_mode,
                            request_id=request_id,
                            stream=True,
                            messages=messages,
                            response_text=effective_text,
                            policy_post=policy_post,
                        )
                    except Exception:
                        pass

                    if effective_text != final_text and effective_text:
                        try:
                            delta = {"text": effective_text}
                            delta_json = _json.dumps(delta, ensure_ascii=False)
                            yield "event: delta\ndata: " + delta_json + "\n\n"
                        except Exception:
                            pass

                    try:
                        if session_id and getattr(settings, "MEMORY_ENABLED", True):
                            store = get_memory_store()
                            user_inputs = [m for m in messages if m.get("role") == "user"]
                            last_user = user_inputs[-1]["content"] if user_inputs else ""
                            await store.append(session_id, "user", last_user)
                            await store.append(session_id, "assistant", effective_text)
                    except Exception as mem_err:
                        logger.warning("Memory-Append fehlgeschlagen (stream): %s", mem_err)
                except Exception:
                    pass

            if client is not None:
                async for chunk in _do_stream(client):
                    yield chunk
            else:
                async with httpx.AsyncClient(timeout=settings.REQUEST_TIMEOUT) as temp_client:
                    async for chunk in _do_stream(temp_client):
                        yield chunk

        except Exception as exc:
            if getattr(settings, "LOG_JSON", False):
                logger.exception(
                    _json.dumps(
                        {"event": "model_error", "error": str(exc), "request_id": request_id},
                        ensure_ascii=False,
                    )
                )
            else:
                logger.exception("Streaming-Fehler: %s", exc)
            yield f"event: error\ndata: {exc!s}\n\n"
            try:
                if session_id and getattr(settings, "MEMORY_ENABLED", True):
                    store = get_memory_store()
                    user_inputs = [m for m in messages if m.get("role") == "user"]
                    last_user = user_inputs[-1]["content"] if user_inputs else ""
                    await store.append(session_id, "user", f"{last_user}\n<!-- aborted=true -->")
            except Exception as mem_err2:
                logger.warning("Memory-Append (aborted) fehlgeschlagen: %s", mem_err2)
        finally:
            duration_ms = int((time.time() - started) * 1000)
            if getattr(settings, "LOG_JSON", False):
                logger.info(
                    _json.dumps(
                        {
                            "event": "model_stream_done",
                            "duration_ms": duration_ms,
                            "request_id": request_id,
                        },
                        ensure_ascii=False,
                    )
                )
            else:
                logger.info("Streaming abgeschlossen in %s ms rid=%s", duration_ms, request_id)
            yield "event: done\ndata: {}\n\n"

    return _gen()


async def process_chat_request(
    request: ChatRequest,
    eval_mode: bool = False,
    unrestricted_mode: bool = False,
    client: httpx.AsyncClient | None = None,
    request_id: str | None = None,
) -> ChatResponse:
    try:
        messages: list[dict[str, str]] = []
        for m in request.messages:
            if isinstance(m, dict):
                role = m.get("role", "user")
                content = m.get("content", "")
            else:
                role = getattr(m, "role", "user")
                content = getattr(m, "content", "")
            messages.append({"role": role, "content": content})

        if eval_mode:
            logger.info("Eval-Modus aktiv: Ersetze Systemprompt rid=%s", request_id)
            messages = [msg for msg in messages if msg.get("role") != "system"]
            sys_prompt = EVAL_SYSTEM_PROMPT
            if getattr(settings, "CONTENT_POLICY_ENABLED", False):
                try:
                    sys_prompt = modify_prompt_for_freedom(sys_prompt)
                except Exception:
                    pass
            messages.insert(0, {"role": "system", "content": sys_prompt})
        elif unrestricted_mode:
            logger.info("Uneingeschränkter Modus aktiv: Ersetze Systemprompt rid=%s", request_id)
            messages = [msg for msg in messages if msg.get("role") != "system"]
            sys_prompt = UNRESTRICTED_SYSTEM_PROMPT
            if getattr(settings, "CONTENT_POLICY_ENABLED", False):
                try:
                    sys_prompt = modify_prompt_for_freedom(sys_prompt)
                except Exception:
                    pass
            messages.insert(0, {"role": "system", "content": sys_prompt})
        else:
            if not any(msg.get("role") == "system" for msg in messages):
                sys_prompt = DEFAULT_SYSTEM_PROMPT
                if getattr(settings, "CONTENT_POLICY_ENABLED", False):
                    try:
                        sys_prompt = modify_prompt_for_freedom(sys_prompt)
                    except Exception:
                        pass
                messages.insert(0, {"role": "system", "content": sys_prompt})

        messages = _inject_strict_rpg_contract_message(messages)

        # Optionaler Canvas-Zähler aus Request-Optionen
        try:
            cc_val2: int | None = None
            opts_any2 = getattr(request, "options", None)
            if isinstance(opts_any2, Mapping):
                try:
                    v2 = cast(Mapping[object, Any], opts_any2).get("canvas_count")
                except Exception:
                    v2 = None
            elif opts_any2 is not None:
                md2 = getattr(opts_any2, "model_dump", None)
                v2 = None
                if callable(md2):
                    try:
                        raw2 = md2()
                        if isinstance(raw2, Mapping):
                            v2 = cast(Mapping[object, Any], raw2).get("canvas_count")
                    except Exception:
                        v2 = None
            else:
                v2 = None
            if isinstance(v2, int):
                cc_val2 = v2
            elif isinstance(v2, str) and v2.isdigit():
                try:
                    cc_val2 = int(v2)
                except Exception:
                    cc_val2 = None
            if cc_val2 is not None and cc_val2 >= 0:
                messages.insert(1, {"role": "system", "content": f"Canvas geladen: {cc_val2}"})
        except Exception:
            pass

        options = _options_to_dict(getattr(request, "options", None))
        orchestrator_enabled = _orchestrator_enabled(options)
        notes: str | None = None
        rag_hits: list[dict[str, Any]] = []
        retrieval_query = ""

        try:
            notes = _resolve_context_notes()
            if notes and not orchestrator_enabled:
                messages.insert(1, {"role": "system", "content": f"[Kontext-Notizen]\n{notes}"})
        except Exception:
            notes = None

        try:
            retrieval_query = _resolve_retrieval_query(messages, options)
            rag_hits = _resolve_rag_hits(retrieval_query)
            if rag_hits and not orchestrator_enabled:
                messages.insert(
                    1,
                    {"role": "system", "content": f"[RAG]\n{_build_rag_snippet_text(rag_hits)}"},
                )
        except Exception:
            rag_hits = []

        try:
            messages = _inject_orchestrator_messages(
                messages,
                request,
                context_notes=notes if orchestrator_enabled else None,
                rag_hits=rag_hits if orchestrator_enabled else None,
                retrieval_query=retrieval_query if orchestrator_enabled else None,
            )
        except Exception:
            pass

        session_id: str | None = None
        try:
            sid_top = getattr(request, "session_id", None)
            opts_any = getattr(request, "options", None)
            opts0: dict[str, Any] = {}
            if isinstance(opts_any, Mapping):
                try:
                    opts_map = cast(Mapping[object, Any], opts_any)
                    opts0 = {str(k): v for k, v in opts_map.items()}
                except Exception:
                    opts0 = {}
            elif opts_any is not None:
                md = getattr(opts_any, "model_dump", None)
                if callable(md):
                    try:
                        raw = md()
                        if isinstance(raw, Mapping):
                            opts0 = {str(k): v for k, v in cast(Mapping[object, Any], raw).items()}
                        else:
                            opts0 = {}
                    except Exception:
                        opts0 = {}
                else:
                    opts0 = {}
            sid_opt = opts0.get("session_id")
            sid_val = sid_top or sid_opt
            session_id = str(sid_val) if isinstance(sid_val, str) and sid_val else None
        except Exception:
            session_id = None

        try:
            messages = await compose_with_memory(
                cast(list[Mapping[str, str]], messages), session_id
            )
        except Exception:
            pass

        try:
            mode = "unrestricted" if unrestricted_mode else ("eval" if eval_mode else "default")
            profile_id = getattr(request, "profile_id", None)
            pre = apply_pre(
                cast(list[Mapping[str, Any]], messages), mode=mode, profile_id=profile_id
            )
            if pre and getattr(pre, "action", "allow") == "block":
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="policy_block")
            if (
                pre
                and getattr(pre, "action", "allow") == "rewrite"
                and getattr(pre, "messages", None)
            ):
                pre_msgs = getattr(pre, "messages", None)
                if pre_msgs:
                    messages = [
                        {
                            "role": str((cast(Mapping[str, Any], message)).get("role", "user")),
                            "content": str((cast(Mapping[str, Any], message)).get("content", "")),
                        }
                        for message in pre_msgs
                        if isinstance(message, Mapping)
                    ]
                if getattr(settings, "LOG_JSON", False):
                    logger.info(
                        _json.dumps(
                            {
                                "event": "policy_pre",
                                "action": "rewrite",
                                "mode": mode,
                                "request_id": request_id,
                            },
                            ensure_ascii=False,
                        )
                    )
                else:
                    logger.info("Policy-Pre hat Nachrichten umgeschrieben. rid=%s", request_id)
        except Exception:
            pass

        req_model = getattr(request, "model", None)
        profile_id = getattr(request, "profile_id", None)
        raw_any2 = getattr(request, "options", None)
        raw_opts2: dict[str, Any] = {}
        if isinstance(raw_any2, Mapping):
            try:
                raw_map2 = cast(Mapping[object, Any], raw_any2)
                raw_opts2 = {str(k): v for k, v in raw_map2.items()}
            except Exception:
                raw_opts2 = {}
        elif raw_any2 is not None:
            md = getattr(raw_any2, "model_dump", None)
            if callable(md):
                try:
                    raw2 = md()
                    if isinstance(raw2, Mapping):
                        raw_opts2 = {str(k): v for k, v in cast(Mapping[object, Any], raw2).items()}
                    else:
                        raw_opts2 = {}
                except Exception:
                    raw_opts2 = {}
            else:
                raw_opts2 = {}
        else:
            raw_opts2 = {}
        resolved_model = req_model or settings.MODEL_NAME

        try:
            if getattr(settings, "SESSION_MEMORY_ENABLED", False):
                opts2 = getattr(request, "options", None)
                sess_id2: str | None = None
                if isinstance(opts2, dict):
                    opts_mapping2 = cast(Mapping[str, Any], opts2)
                    val_any2 = opts_mapping2.get("session_id")
                    sess_id2 = val_any2 if isinstance(val_any2, str) and val_any2 else None
                if isinstance(sess_id2, str) and sess_id2:
                    prior2 = session_memory.get(sess_id2)
                    if prior2:
                        sys_msgs2 = [m for m in messages if m.get("role") == "system"]
                        non_sys2 = [m for m in messages if m.get("role") != "system"]
                        prior2_cast = [
                            {
                                "role": str(m.get("role", "user")),
                                "content": str(m.get("content", "")),
                            }
                            for m in prior2
                        ]
                        messages = sys_msgs2 + prior2_cast + non_sys2
        except Exception:
            pass

        selected_model = resolved_model
        if _support_ab_enabled(
            raw_opts2,
            profile_id=profile_id,
            eval_mode=eval_mode,
            unrestricted_mode=unrestricted_mode,
        ):
            candidate_models = _support_ab_candidate_models(raw_opts2)
            candidate_results: list[dict[str, Any]] = []
            last_user_text = _latest_user_text(messages)
            for candidate_model in candidate_models:
                candidate_text, candidate_duration = await _run_nonstream_ollama_request(
                    messages=messages,
                    raw_options=raw_opts2,
                    model_name=candidate_model,
                    eval_mode=eval_mode,
                    client=client,
                    request_id=request_id,
                )
                candidate_score, candidate_reasons = _score_support_candidate_response(
                    last_user_text, candidate_text
                )
                candidate_results.append(
                    {
                        "model": candidate_model,
                        "text": candidate_text,
                        "duration_ms": candidate_duration,
                        "score": candidate_score,
                        "reasons": candidate_reasons,
                    }
                )

            ranked_candidates = sorted(
                candidate_results,
                key=lambda item: (
                    int(cast(int, item.get("score", -100))),
                    -int(cast(int | None, item.get("duration_ms", 0)) or 0),
                ),
                reverse=True,
            )
            winner = ranked_candidates[0]
            runner_up = ranked_candidates[1] if len(ranked_candidates) > 1 else None
            judge_model = _support_ab_judge_model(raw_opts2)
            use_judge = _support_ab_force_judge(raw_opts2)
            if judge_model and len(candidate_results) >= 2 and (use_judge or runner_up is not None):
                score_gap = (
                    abs(
                        int(cast(int, winner.get("score", -100)))
                        - int(cast(int, runner_up.get("score", -100)))
                    )
                    if runner_up is not None
                    else 0
                )
                if use_judge or score_gap <= 1:
                    judge_messages = _build_support_judge_messages(
                        user_text=last_user_text,
                        candidate_a=str(candidate_results[0].get("text", "")),
                        candidate_b=str(candidate_results[1].get("text", "")),
                    )
                    judge_text, _judge_duration = await _run_nonstream_ollama_request(
                        messages=judge_messages,
                        raw_options={
                            **raw_opts2,
                            "temperature": 0.0,
                            "top_p": 0.1,
                            "num_predict": 32,
                        },
                        model_name=judge_model,
                        eval_mode=False,
                        client=client,
                        request_id=request_id,
                    )
                    judge_choice = _parse_support_judge_choice(judge_text)
                    if judge_choice == "A":
                        winner = candidate_results[0]
                    elif judge_choice == "B":
                        winner = candidate_results[1]
                    if getattr(settings, "LOG_JSON", False):
                        logger.info(
                            _json.dumps(
                                {
                                    "event": "support_ab_judge",
                                    "judge_model": judge_model,
                                    "choice": judge_choice,
                                    "request_id": request_id,
                                },
                                ensure_ascii=False,
                            )
                        )
                    else:
                        logger.info(
                            "support_de_ab judge=%s choice=%s rid=%s",
                            judge_model,
                            judge_choice,
                            request_id,
                        )

            generated_content = str(winner.get("text", ""))
            selected_model = str(winner.get("model", resolved_model))
            logger.info(
                "support_de_ab gewaehlt: model=%s score=%s reasons=%s rid=%s",
                selected_model,
                winner.get("score"),
                ",".join(cast(list[str], winner.get("reasons", []))),
                request_id,
            )
        else:
            generated_content, _duration_ms = await _run_nonstream_ollama_request(
                messages=messages,
                raw_options=raw_opts2,
                model_name=resolved_model,
                eval_mode=eval_mode,
                client=client,
                request_id=request_id,
            )

        try:
            mode = "unrestricted" if unrestricted_mode else ("eval" if eval_mode else "default")
            post = apply_post(generated_content, mode=mode, profile_id=profile_id)
            action = getattr(post, "action", "allow")
            policy_post = "allow"
            if action == "block":
                policy_post = "blocked"
                _append_shadow_mode_event(
                    request=request,
                    eval_mode=eval_mode,
                    unrestricted_mode=unrestricted_mode,
                    request_id=request_id,
                    stream=False,
                    messages=messages,
                    response_text=generated_content,
                    policy_post=policy_post,
                )
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="policy_block")
            if action == "rewrite" and getattr(post, "text", None):
                generated_content = str(post.text)
                policy_post = "rewritten"
                if getattr(settings, "LOG_JSON", False):
                    logger.info(
                        _json.dumps(
                            {
                                "event": "policy_post",
                                "action": "rewrite",
                                "mode": mode,
                                "request_id": request_id,
                            },
                            ensure_ascii=False,
                        )
                    )
                else:
                    logger.info("Policy-Post hat Antwort umgeschrieben. rid=%s", request_id)
            generated_content = _repair_strict_rpg_contract_response(messages, generated_content)
            _append_shadow_mode_event(
                request=request,
                eval_mode=eval_mode,
                unrestricted_mode=unrestricted_mode,
                request_id=request_id,
                stream=False,
                messages=messages,
                response_text=generated_content,
                policy_post=policy_post,
            )
        except HTTPException:
            raise
        except Exception:
            pass

        try:
            if session_id and getattr(settings, "MEMORY_ENABLED", True):
                store = get_memory_store()
                user_inputs = [m for m in messages if m.get("role") == "user"]
                last_user = user_inputs[-1]["content"] if user_inputs else ""
                await store.append(session_id, "user", last_user)
                await store.append(session_id, "assistant", generated_content)
        except Exception as mem_err3:
            logger.warning("Memory-Append fehlgeschlagen: %s", mem_err3)

        try:
            _persist_orchestrator_turn(request, generated_content)
        except Exception as persist_err:
            logger.warning("Session-Writeback fehlgeschlagen: %s", persist_err)

        return _build_contract_chat_response(
            request,
            content=generated_content,
            model=selected_model,
        )
    except HTTPException:
        raise
    except Exception as exc:
        try:
            sid_top = getattr(request, "session_id", None)
            opts_any = getattr(request, "options", None)
            opts_err: dict[str, Any] = {}
            if isinstance(opts_any, Mapping):
                try:
                    opts_err = dict(cast(Mapping[str, Any], opts_any))
                except Exception:
                    opts_err = {}
            sid_opt = opts_err.get("session_id")
            sid_val = sid_top or sid_opt
            session_id = str(sid_val) if isinstance(sid_val, str) and sid_val else None
            if session_id and getattr(settings, "MEMORY_ENABLED", True):
                store = get_memory_store()
                raw_msgs: list[dict[str, str]] = []
                for m in request.messages:
                    if isinstance(m, dict):
                        role = m.get("role", "user")
                        content = m.get("content", "")
                    else:
                        role = getattr(m, "role", "user")
                        content = getattr(m, "content", "")
                    raw_msgs.append({"role": role, "content": content})
                user_inputs = [m for m in raw_msgs if m.get("role") == "user"]
                last_user = user_inputs[-1]["content"] if user_inputs else ""
                await store.append(session_id, "user", f"{last_user}\n<!-- aborted=true -->")
        except Exception as mem_err4:
            logger.warning("Memory-Append (error path) fehlgeschlagen: %s", mem_err4)
        if getattr(settings, "LOG_JSON", False):
            logger.exception(
                _json.dumps(
                    {"event": "model_error", "error": str(exc), "request_id": request_id},
                    ensure_ascii=False,
                )
            )
        else:
            logger.exception("Fehler bei der Verarbeitung der Chat-Anfrage: %s", exc)
        err_msg = (
            "Entschuldigung, bei der Verarbeitung Ihrer Anfrage ist ein Fehler aufgetreten: "
            + str(exc)
        )
        return _build_contract_chat_response(
            request,
            content=err_msg,
            model=settings.MODEL_NAME,
        )
