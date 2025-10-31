"""Content-Management und Policy-Hooks für den CVN Agent."""

from __future__ import annotations

import json
import re
from typing import Any, Dict, Iterable, List, Mapping, Optional, cast

CONTENT_FILTERING_ENABLED = False

CONTENT_TYPES = {
    "explicit": True,
    "mature": True,
    "violent": True,
    "controversial": True,
    "political": True,
    "offensive": True,
}


def check_content_allowed(content_type: str) -> bool:
    if not CONTENT_FILTERING_ENABLED:
        return True
    return CONTENT_TYPES.get(content_type, False)


def modify_prompt_for_freedom(system_prompt: str) -> str:
    prompt_parts = [
        "# Systemprompt für CVN Agent",
        "# HIER KÖNNEN SIE IHRE EIGENEN ANWEISUNGEN EINFÜGEN",
        "# OHNE EXTERNE EINSCHRÄNKUNGEN",
        system_prompt,
    ]
    return "\n".join(prompt_parts)


def create_unrestricted_prompt(scenario_type: str) -> str:
    return f"""
    # CVN Agent Szenario: {scenario_type}

    Welt: Novapolis (postapokalyptisches Setting)

    Anweisungen:
    - Erstelle realistische Szenarien und Konsequenzen
    - Berücksichtige die harte Realität der postapokalyptischen Welt
    - [IHRE EIGENEN ANWEISUNGEN HIER]

    Format:
    Szene: [Beschreibung]
    Konsequenz: [Ergebnis]
    Optionen: [Mögliche Handlungen]
    """


try:
    from .settings import settings
except Exception:  # pragma: no cover - fail-open für Importzyklen
    settings = None  # type: ignore[assignment]


class PreResult:
    def __init__(self, action: str = "allow", messages: Optional[List[Dict[str, str]]] = None, reason: Optional[str] = None) -> None:
        self.action = action
        self.messages = messages
        self.reason = reason


class PostResult:
    def __init__(self, action: str = "allow", text: Optional[str] = None, reason: Optional[str] = None) -> None:
        self.action = action
        self.text = text
        self.reason = reason


_SENTENCE_SPLIT_RE = re.compile(r"(?<=[\.\?\!])\s+")


def split_sentences(text: str) -> List[str]:
    try:
        return [part.strip() for part in _SENTENCE_SPLIT_RE.split(text) if part and part.strip()]
    except Exception:
        return [text]


def trim_length(text: str, max_chars: int) -> str:
    if max_chars <= 0:
        return ""
    if len(text) <= max_chars:
        return text
    return text[:max_chars].rstrip()


def limit_sentences(text: str, max_sentences: int) -> str:
    if max_sentences <= 0:
        return ""
    return " ".join(split_sentences(text)[:max_sentences])


_ROLEPLAY_MARKERS = ("ich:", "du:", "wir:", "narrator:", "erzähler:", "spieler:", "gm:", "*", "[", "]")
_FILLERS = ("gern", "gerne", "natürlich", "klar", "sicher", "also", "übrigens", "ähm")


def _strip_roleplay_markers(value: str) -> str:
    value = re.sub(r"\*[^*]*\*", " ", value)
    value = re.sub(r"\[[^\]]*\]", " ", value)
    value = re.sub(r"^(ich|du|wir|narrator|erzähler|spieler|gm)\s*:\s*", "", value, flags=re.IGNORECASE)
    return value


def _neutralize_pronouns(value: str) -> str:
    replacements = [
        (r"\bich\b", ""),
        (r"\bdu\b", ""),
        (r"\bwir\b", ""),
        (r"\bdein(e|en|er|em)?\b", ""),
        (r"\bmein(e|en|er|em)?\b", ""),
        (r"\bunser(e|en|er|em)?\b", ""),
    ]
    for pattern, replacement in replacements:
        value = re.sub(pattern, replacement, value, flags=re.IGNORECASE)
    return re.sub(r"\s{2,}", " ", value).strip()


def _remove_exclamations_emojis(value: str) -> str:
    value = re.sub(r"[!]+", ".", value)
    value = re.sub(r"[:;]-?[\)\(DP]", "", value)
    value = re.sub(r"[\u2600-\u26FF\u2700-\u27BF\U0001F300-\U0001FAFF]", "", value)
    return value


def _strip_fillers(value: str) -> str:
    return re.sub(rf"^({'|'.join(_FILLERS)})[,!\.:]?\s+", "", value, flags=re.IGNORECASE)


def _compact_style(value: str) -> str:
    value = re.sub(r"\s{2,}", " ", value)
    value = re.sub(r"\s*([,;:\.])\s*", r"\1 ", value)
    value = re.sub(r"\s+\.", ".", value)
    return value.strip()


def neutralize(text: str) -> str:
    cleaned = text.strip()
    cleaned = _strip_roleplay_markers(cleaned)
    cleaned = _remove_exclamations_emojis(cleaned)
    sentences = split_sentences(cleaned)
    sentences = [_strip_fillers(sentence).strip() for sentence in sentences]
    cleaned = " ".join(sentences)
    cleaned = _neutralize_pronouns(cleaned)
    return cleaned


def compact(text: str) -> str:
    return _compact_style(text)


def _load_policy_file(path: str) -> Dict[str, Any]:
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle)
    except Exception:
        return {}


def _merge_terms(base: Iterable[str], overlay: Iterable[str]) -> List[str]:
    seen: Dict[str, None] = {}
    result: List[str] = []
    for term in list(base) + list(overlay):
        try:
            value = str(term)
        except Exception:
            continue
        if value and value not in seen:
            seen[value] = None
            result.append(value)
    return result


def _merge_rewrite_map(base: Mapping[str, Any], overlay: Mapping[str, Any]) -> Dict[str, str]:
    merged: Dict[str, str] = {str(key): str(value) for key, value in dict(base).items()}
    for key, value in dict(overlay).items():
        merged[str(key)] = str(value)
    return merged


def _get_policies(*, mode: str = "default", profile_id: Optional[str] = None) -> Dict[str, Any]:
    policies: Dict[str, Any] = {}
    if settings is None:
        return policies
    try:
        if getattr(settings, "POLICIES_ENABLED", False):
            path = getattr(settings, "POLICY_FILE", None)
            if isinstance(path, str) and path:
                file_rules = _load_policy_file(path)
                if not isinstance(file_rules, dict):
                    return {}
                if "default" in file_rules or "profiles" in file_rules:
                    base_raw = file_rules.get("default")
                    profiles_raw = file_rules.get("profiles")
                    base: Dict[str, Any] = {}
                    if isinstance(base_raw, dict):
                        base = cast(Dict[str, Any], base_raw)
                    profiles: Dict[str, Any] = {}
                    if isinstance(profiles_raw, dict):
                        profiles = cast(Dict[str, Any], profiles_raw)
                    pid = profile_id or ("eval" if mode == "eval" else None)
                    overlay: Dict[str, Any] = {}
                    if pid and isinstance(profiles, dict):
                        candidate = profiles.get(pid)
                        if isinstance(candidate, dict):
                            overlay = cast(Dict[str, Any], candidate)
                    forb_base = [str(x) for x in cast(List[Any], base.get("forbidden_terms", [])) if isinstance(x, str)]
                    forb_overlay = [
                        str(x) for x in cast(List[Any], overlay.get("forbidden_terms", [])) if isinstance(x, str)
                    ]
                    rw_base: Dict[str, Any] = {}
                    base_rw_raw = base.get("rewrite_map")
                    if isinstance(base_rw_raw, dict):
                        rw_base = cast(Dict[str, Any], base_rw_raw)
                    rw_overlay: Dict[str, Any] = {}
                    overlay_rw_raw = overlay.get("rewrite_map")
                    if isinstance(overlay_rw_raw, dict):
                        rw_overlay = cast(Dict[str, Any], overlay_rw_raw)
                    policies["forbidden_terms"] = _merge_terms(forb_base, forb_overlay)
                    policies["rewrite_map"] = _merge_rewrite_map(rw_base, rw_overlay)
                else:
                    policies.update(file_rules)
    except Exception:
        return {}
    return policies


def _should_bypass_policies(unrestricted_mode: bool) -> bool:
    try:
        if settings is None:
            return False
        if unrestricted_mode and getattr(settings, "POLICY_STRICT_UNRESTRICTED_BYPASS", True):
            return True
    except Exception:
        pass
    return False


def apply_pre(
    messages: List[Mapping[str, Any]],
    *,
    mode: str = "default",
    profile_id: Optional[str] = None,
) -> PreResult:
    if _should_bypass_policies(unrestricted_mode=(mode == "unrestricted")):
        return PreResult(action="allow")
    if settings is None or not getattr(settings, "POLICIES_ENABLED", False):
        return PreResult(action="allow")
    try:
        rules = _get_policies(mode=mode, profile_id=profile_id)
        forbidden = [str(x) for x in rules.get("forbidden_terms", []) if isinstance(x, str)]
        rewrite_map = {str(k): str(v) for k, v in dict(rules.get("rewrite_map", {})).items()}
        changed = False
        new_msgs: List[Dict[str, str]] = []
        for message in messages:
            role = str(message.get("role", "user"))
            content = str(message.get("content", ""))
            if role == "user":
                for bad, good in rewrite_map.items():
                    if bad in content:
                        content = content.replace(bad, good)
                        changed = True
                if any(term for term in forbidden if term and term in content):
                    return PreResult(action="block", reason="forbidden_term")
            new_msgs.append({"role": role, "content": content})
        if changed:
            return PreResult(action="rewrite", messages=new_msgs, reason="rewrite_map_applied")
        return PreResult(action="allow")
    except Exception:
        return PreResult(action="allow")


def apply_post(
    text: str,
    *,
    mode: str = "default",
    profile_id: Optional[str] = None,
) -> PostResult:
    if _should_bypass_policies(unrestricted_mode=(mode == "unrestricted")):
        return PostResult(action="allow")
    if settings is None or not getattr(settings, "POLICIES_ENABLED", False):
        return PostResult(action="allow")
    try:
        if mode == "eval" and getattr(settings, "EVAL_POST_REWRITE_ENABLED", True):
            t0 = text
            transformed = neutralize(t0)
            try:
                max_sentences = int(getattr(settings, "EVAL_POST_MAX_SENTENCES", 2))
            except Exception:
                max_sentences = 2
            try:
                max_chars = int(getattr(settings, "EVAL_POST_MAX_CHARS", 240))
            except Exception:
                max_chars = 240
            transformed = limit_sentences(transformed, max_sentences)
            transformed = trim_length(transformed, max_chars)
            transformed = compact(transformed)
            if transformed != t0:
                return PostResult(action="rewrite", text=transformed, reason="eval_post")

        rules = _get_policies(mode=mode, profile_id=profile_id)
        forbidden = [str(x) for x in rules.get("forbidden_terms", []) if isinstance(x, str)]
        rewrite_map = {str(k): str(v) for k, v in dict(rules.get("rewrite_map", {})).items()}
        output = text
        changed = False
        for bad, good in rewrite_map.items():
            if bad in output:
                output = output.replace(bad, good)
                changed = True
        if any(term for term in forbidden if term and term in output):
            return PostResult(action="block", reason="forbidden_term")
        if changed:
            return PostResult(action="rewrite", text=output, reason="rewrite_map_applied")
        return PostResult(action="allow")
    except Exception:
        return PostResult(action="allow")


__all__ = [
    "check_content_allowed",
    "modify_prompt_for_freedom",
    "create_unrestricted_prompt",
    "apply_pre",
    "apply_post",
    "split_sentences",
    "trim_length",
    "limit_sentences",
    "neutralize",
    "compact",
    "PreResult",
    "PostResult",
]
