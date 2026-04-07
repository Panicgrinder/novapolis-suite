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

from ..core.content_management import apply_post, apply_pre, modify_prompt_for_freedom
from ..core.memory import compose_with_memory, get_memory_store
from ..core.prompts import DEFAULT_SYSTEM_PROMPT, EVAL_SYSTEM_PROMPT, UNRESTRICTED_SYSTEM_PROMPT
from ..utils.session_memory import session_memory
from .chat_helpers import normalize_ollama_options
from .models import (
    ChatRequest,
    ChatResponse,
    TEXT_RPG_LOG_CHANNELS,
    TEXT_RPG_SESSION_CONTRACT_VERSION,
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
        items: list[str] = []
        for entry in value:
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


def _clip_text(value: str, limit: int = 400) -> str:
    return value if len(value) <= limit else f"{value[:limit]}…"


def _resolve_context_notes() -> str | None:
    try:
        enabled = bool(getattr(settings, "CONTEXT_NOTES_ENABLED", False))
        notes: str | None = None
        try:
            notes = load_context_notes(
                getattr(settings, "CONTEXT_NOTES_PATHS", []),
                getattr(settings, "CONTEXT_NOTES_MAX_CHARS", 4000),
            )
        except Exception:
            notes = None
        if (enabled or notes) and notes:
            return notes
    except Exception:
        return None
    return None


def _resolve_retrieval_query(messages: list[dict[str, str]], options: Mapping[str, Any]) -> str:
    explicit_query = str(options.get("retrieval_query", "")).strip()
    if explicit_query:
        return explicit_query
    return _latest_user_text(messages).strip()


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

    contract_active = _orchestrator_enabled(options) or any(
        value for value in (session_id, campaign_id, scene_id, slot_id, turn_id)
    )

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
        replay_checkpoint_id=turn_id,
        log_channels=list(TEXT_RPG_LOG_CHANNELS) if contract_active else None,
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
    norm_opts, base_host = normalize_ollama_options(raw_opts, eval_mode=eval_mode)

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
        "model": req_model or settings.MODEL_NAME,
        "messages": messages,
        "stream": True,
        "options": norm_opts,
    }

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
        norm_opts2, base_host = normalize_ollama_options(raw_opts2, eval_mode=eval_mode)

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

        ollama_payload: dict[str, Any] = {
            "model": req_model or settings.MODEL_NAME,
            "messages": messages,
            "stream": False,
            "options": norm_opts2,
        }

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
            # mypy: Response may not have custom attribute _started; use Any cast to set it
            from typing import Any as _Any

            resp_any = cast(_Any, resp)
            resp_any._started = started
            return resp

        if client is not None:
            response = await _post_with(client)
        else:
            async with httpx.AsyncClient(timeout=settings.REQUEST_TIMEOUT) as temp_client:
                response = await _post_with(temp_client)

        response.raise_for_status()
        result = response.json()
        generated_content = result.get("message", {}).get("content", "")

        max_len = max(0, int(getattr(settings, "LOG_TRUNCATE_CHARS", 200)))
        preview = (
            generated_content
            if len(generated_content) <= max_len
            else f"{generated_content[:max_len]}..."
        )
        started = getattr(response, "_started", None)
        duration_ms = int((time.time() - started) * 1000) if isinstance(started, float) else None
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
            if duration_ms is not None:
                logger.info(
                    "Antwort von Ollama erhalten. %s ms rid=%s Inhalt: %s",
                    duration_ms,
                    request_id,
                    preview,
                )
            else:
                logger.info("Antwort von Ollama erhalten. rid=%s Inhalt: %s", request_id, preview)

        try:
            mode = "unrestricted" if unrestricted_mode else ("eval" if eval_mode else "default")
            profile_id = getattr(request, "profile_id", None)
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

        return _build_contract_chat_response(
            request,
            content=generated_content,
            model=settings.MODEL_NAME,
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
