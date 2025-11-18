import json as _json
import logging
import time
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, cast

import httpx
from fastapi import HTTPException, status
from utils.context_notes import load_context_notes

from ..core.content_management import apply_post, apply_pre, modify_prompt_for_freedom
from ..core.memory import compose_with_memory, get_memory_store
from ..core.prompts import DEFAULT_SYSTEM_PROMPT, EVAL_SYSTEM_PROMPT, UNRESTRICTED_SYSTEM_PROMPT
from ..core.settings import settings
from ..utils.session_memory import session_memory
from .chat_helpers import normalize_ollama_options
from .models import ChatRequest, ChatResponse

if TYPE_CHECKING:
    from utils.rag import TfIdfIndex as _TfIdfIndex

logger = logging.getLogger(__name__)


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
            messages.insert(1, {"role": "system", "content": f"[Kontext-Notizen]\n{notes}"})
    except Exception:
        pass

    try:
        if bool(getattr(settings, "RAG_ENABLED", False)):
            from utils.rag import load_index, retrieve

            rag_path = str(getattr(settings, "RAG_INDEX_PATH", "eval/results/rag/index.json"))
            try:
                idx: _TfIdfIndex | None = load_index(rag_path)
                user_texts = [m.get("content", "") for m in messages if m.get("role") == "user"]
                query = user_texts[-1] if user_texts else ""
                if query and idx is not None:
                    top_k = int(getattr(settings, "RAG_TOP_K", 3))
                    _hits_any: object = retrieve(idx, query, top_k=top_k)
                    hits = cast(list[dict[str, Any]], _hits_any)
                    if hits:

                        def _clip(value: str, limit: int = 400) -> str:
                            return value if len(value) <= limit else f"{value[:limit]}…"

                        snippet_text = "\n\n".join(
                            f"- {h.get('source', '?')}: {_clip(str(h.get('text', '')))}"
                            for h in hits
                        )
                        messages.insert(1, {"role": "system", "content": f"[RAG]\n{snippet_text}"})
            except FileNotFoundError:
                pass
            except Exception:
                pass
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
                        policy_post = "allow"
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
                messages.insert(1, {"role": "system", "content": f"[Kontext-Notizen]\n{notes}"})
        except Exception:
            pass

        try:
            if bool(getattr(settings, "RAG_ENABLED", False)):
                from utils.rag import load_index, retrieve

                rag_path = str(getattr(settings, "RAG_INDEX_PATH", "eval/results/rag/index.json"))
                try:
                    idx: _TfIdfIndex | None = load_index(rag_path)
                    user_texts2 = [
                        m.get("content", "") for m in messages if m.get("role") == "user"
                    ]
                    query2 = user_texts2[-1] if user_texts2 else ""
                    if query2 and idx is not None:
                        top_k2 = int(getattr(settings, "RAG_TOP_K", 3))
                        _hits2_any: object = retrieve(idx, query2, top_k=top_k2)
                        hits2 = cast(list[dict[str, Any]], _hits2_any)
                        if hits2:

                            def _clip2(value: str, limit: int = 400) -> str:
                                return value if len(value) <= limit else f"{value[:limit]}…"

                            snippet_text2 = "\n\n".join(
                                f"- {h.get('source', '?')}: {_clip2(str(h.get('text', '')))}"
                                for h in hits2
                            )
                            messages.insert(
                                1, {"role": "system", "content": f"[RAG]\n{snippet_text2}"}
                            )
                except FileNotFoundError:
                    pass
                except Exception:
                    pass
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
            if action == "block":
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="policy_block")
            if action == "rewrite" and getattr(post, "text", None):
                generated_content = str(post.text)
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

        return ChatResponse(content=generated_content, model=settings.MODEL_NAME)
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
        return ChatResponse(content=err_msg, model=settings.MODEL_NAME)
