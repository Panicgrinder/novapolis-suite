from __future__ import annotations

from types import SimpleNamespace

import pytest


class _BadStr:
    def __str__(self) -> str:
        raise RuntimeError("nope")


@pytest.mark.unit
def test_ensure_system_message_keeps_existing_system_and_prompt_is_stripped(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat_helpers
    from app.api.models import ChatMessage

    chat_helpers.get_system_prompt.cache_clear()
    monkeypatch.setattr(chat_helpers, "DEFAULT_SYSTEM_PROMPT", "  System Prompt  ", raising=False)

    assert chat_helpers.get_system_prompt() == "System Prompt"

    messages = [
        ChatMessage(role="system", content="existing"),
        ChatMessage(role="user", content="hi"),
    ]
    assert chat_helpers.ensure_system_message(messages) == messages


@pytest.mark.unit
def test_normalize_ollama_options_covers_falsey_and_filtered_values(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat_helpers

    monkeypatch.setattr(
        chat_helpers,
        "settings",
        SimpleNamespace(
            TEMPERATURE=0.7,
            REQUEST_MAX_TOKENS=64,
            TOP_P=0.8,
            TOP_K=20,
            NUM_CTX_DEFAULT=2048,
            REPEAT_PENALTY=1.05,
            MIN_P=0.2,
            TYPICAL_P=0.7,
            TFS_Z=0.9,
            MIROSTAT=0,
            MIROSTAT_TAU=5.0,
            MIROSTAT_ETA=0.1,
            PENALIZE_NEWLINE=True,
            REPEAT_LAST_N=32,
            OLLAMA_HOST="http://default-host",
        ),
        raising=False,
    )

    options, host = chat_helpers.normalize_ollama_options(
        {
            "top_k": 0,
            "num_ctx": 0,
            "repeat_last_n": -5,
            "stop": [],
            "penalize_newline": "off",
            "host": "http://custom-host",
        }
    )

    assert host == "http://custom-host"
    assert options["temperature"] == 0.7
    assert options["num_predict"] == 64
    assert options["penalize_newline"] is False
    assert "top_k" not in options
    assert "num_ctx" not in options
    assert "repeat_last_n" not in options
    assert "stop" not in options


@pytest.mark.unit
def test_chat_helper_coercion_skips_bad_str_and_temperature_falls_back(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat_helpers

    monkeypatch.setattr(
        chat_helpers,
        "settings",
        SimpleNamespace(
            TEMPERATURE=0.55,
            REQUEST_MAX_TOKENS=64,
            TOP_P=0.8,
            TOP_K=20,
            NUM_CTX_DEFAULT=1024,
            REPEAT_PENALTY=1.05,
            MIN_P=0.1,
            TYPICAL_P=0.7,
            TFS_Z=0.9,
            MIROSTAT=0,
            MIROSTAT_TAU=5.0,
            MIROSTAT_ETA=0.1,
            PENALIZE_NEWLINE=False,
            REPEAT_LAST_N=32,
            OLLAMA_HOST="http://default-host",
        ),
        raising=False,
    )

    assert chat_helpers._coerce_str_list(["ok", _BadStr()]) == ["ok"]
    options, _host = chat_helpers.normalize_ollama_options({"temperature": object()})
    assert options["temperature"] == 0.55
