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


@pytest.mark.unit
def test_normalize_ollama_options_covers_clamps_truthy_strings_and_defaults(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat_helpers

    monkeypatch.setattr(
        chat_helpers,
        "settings",
        SimpleNamespace(
            TEMPERATURE=0.9,
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

    options, host = chat_helpers.normalize_ollama_options(
        {
            "max_tokens": "9999",
            "top_p": 2.5,
            "top_k": "11",
            "num_ctx": "4096",
            "repeat_penalty": "1.2",
            "presence_penalty": "0.4",
            "frequency_penalty": "0.3",
            "seed": "123",
            "repeat_last_n": "0",
            "stop": "END",
            "min_p": -1,
            "typical_p": 3,
            "tfs_z": -4,
            "mirostat": "9",
            "mirostat_tau": "7.5",
            "mirostat_eta": "0.2",
            "penalize_newline": "yes",
            "host": "http://custom-host",
        },
        eval_mode=True,
    )

    assert host == "http://custom-host"
    assert options["temperature"] == 0.25
    assert options["num_predict"] == 64
    assert options["top_p"] == 1.0
    assert options["top_k"] == 11
    assert options["num_ctx"] == 4096
    assert options["repeat_penalty"] == 1.2
    assert options["presence_penalty"] == 0.4
    assert options["frequency_penalty"] == 0.3
    assert options["seed"] == 123
    assert options["repeat_last_n"] == 0
    assert options["stop"] == ["END"]
    assert options["min_p"] == 0.0
    assert options["typical_p"] == 1.0
    assert options["tfs_z"] == 0.0
    assert options["mirostat"] == 2
    assert options["mirostat_tau"] == 7.5
    assert options["mirostat_eta"] == 0.2
    assert options["penalize_newline"] is True
    assert chat_helpers._coerce_bool(True) is True
    assert chat_helpers._coerce_bool("true") is True


@pytest.mark.unit
def test_normalize_ollama_options_omits_invalid_optional_fields(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.api import chat_helpers

    monkeypatch.setattr(
        chat_helpers,
        "settings",
        SimpleNamespace(
            TEMPERATURE=0.4,
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

    options, host = chat_helpers.normalize_ollama_options(
        {
            "top_p": object(),
            "top_k": object(),
            "num_ctx": object(),
            "repeat_penalty": object(),
            "presence_penalty": object(),
            "frequency_penalty": object(),
            "seed": object(),
            "repeat_last_n": object(),
            "min_p": object(),
            "typical_p": object(),
            "tfs_z": object(),
            "mirostat": object(),
            "mirostat_tau": object(),
            "mirostat_eta": object(),
            "penalize_newline": object(),
        }
    )

    assert host == "http://default-host"
    assert options["temperature"] == 0.4
    assert options["num_predict"] == 64
    assert "top_p" not in options
    assert "top_k" not in options
    assert "num_ctx" not in options
    assert "repeat_penalty" not in options
    assert "presence_penalty" not in options
    assert "frequency_penalty" not in options
    assert "seed" not in options
    assert "repeat_last_n" not in options
    assert "min_p" not in options
    assert "typical_p" not in options
    assert "tfs_z" not in options
    assert "mirostat" not in options
    assert "mirostat_tau" not in options
    assert "mirostat_eta" not in options
    assert "penalize_newline" not in options


@pytest.mark.unit
def test_resolve_ollama_think_defaults_for_qwen35_and_respects_explicit_override() -> None:
    from app.api import chat_helpers

    assert chat_helpers.resolve_ollama_think({}, model_name="qwen3.5:4b") is False
    assert chat_helpers.resolve_ollama_think({"think": True}, model_name="qwen3.5:4b") is True
    assert chat_helpers.resolve_ollama_think({}, model_name="qwen2.5:7b") is None
