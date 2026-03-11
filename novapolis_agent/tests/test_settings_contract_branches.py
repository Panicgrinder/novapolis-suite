from __future__ import annotations

from app.core.settings import Settings


def test_settings_many_fallback_branches_and_aliases() -> None:
    s = Settings(
        REQUEST_TIMEOUT=0,
        REQUEST_MAX_INPUT_CHARS=0,
        REQUEST_MAX_TOKENS=0,
        RATE_LIMIT_REQUESTS_PER_MINUTE=0,
        RATE_LIMIT_BURST=-1,
        RATE_LIMIT_WINDOW_SEC=0,
        TTS_RATE_LIMIT_REQUESTS_PER_MINUTE=0,
        TTS_RATE_LIMIT_BURST=-1,
        TTS_RATE_LIMIT_WINDOW_SEC=0,
        TTS_CACHE_TTL_SEC=0,
        TTS_CACHE_MAX_ENTRIES=0,
        TTS_CACHE_MAX_BYTES=0,
        TTS_PROVIDER="invalid-provider",
        CONTEXT_NOTES_MAX_CHARS=0,
        CANARY_PCT=200,
        RAG_ON=True,
        SHADOW_ON=False,
    )

    assert s.REQUEST_TIMEOUT == 60.0
    assert s.REQUEST_MAX_INPUT_CHARS == 16000
    assert s.REQUEST_MAX_TOKENS == 512
    assert s.RATE_LIMIT_REQUESTS_PER_MINUTE == 60
    assert s.RATE_LIMIT_BURST == 30
    assert s.RATE_LIMIT_WINDOW_SEC == 60.0
    assert s.TTS_RATE_LIMIT_REQUESTS_PER_MINUTE == 30
    assert s.TTS_RATE_LIMIT_BURST == 5
    assert s.TTS_RATE_LIMIT_WINDOW_SEC == 60.0
    assert s.TTS_CACHE_TTL_SEC == 300
    assert s.TTS_CACHE_MAX_ENTRIES == 500
    assert s.TTS_CACHE_MAX_BYTES == 2_000_000
    assert s.TTS_PROVIDER == "dummy"
    assert s.CONTEXT_NOTES_MAX_CHARS == 12000
    assert s.CANARY_PCT == 100
    assert s.RAG_ENABLED is True
    assert s.SHADOW_MODE_LOGGING_ENABLED is False
    assert len(s.SETTINGS_CONTRACT_ISSUES) >= 10


def test_settings_missing_required_and_canary_lower_bound() -> None:
    s = Settings(
        OLLAMA_HOST="",
        MODEL_NAME="",
        RUNTIME_ENV_REQUIRED=["OLLAMA_HOST", "MODEL_NAME", "MISSING_KEY"],
        CANARY_PCT=-5,
    )

    assert s.CANARY_PCT == 0
    assert any("Missing required runtime settings" in issue for issue in s.SETTINGS_CONTRACT_ISSUES)


def test_settings_strict_raises_on_invalid_rate_limit_burst() -> None:
    try:
        Settings(STRICT_CONFIG=True, RATE_LIMIT_BURST=-1)
    except ValueError as exc:
        assert "RATE_LIMIT_BURST" in str(exc)
    else:
        raise AssertionError("Expected ValueError for strict invalid config")
