from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any, cast

from pydantic import field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

AGENT_EVAL_ROOT = os.path.join("novapolis_agent", "eval")

if __name__ == "app.core.settings":
    sys.modules.setdefault("novapolis_agent.app.core.settings", sys.modules[__name__])
elif __name__ == "novapolis_agent.app.core.settings":
    sys.modules.setdefault("app.core.settings", sys.modules[__name__])


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "CVN Agent"
    PROJECT_DESCRIPTION: str = "Conversational Agent mit Ollama"
    PROJECT_VERSION: str = "0.1.1"
    CONFIG_CONTRACT_VERSION: str = "2026-02-23"
    STRICT_CONFIG: bool = False

    # Step 2 contract: required vars must be present for production mode.
    # Dev mode remains safe by default with controlled fallbacks.
    RUNTIME_ENV_REQUIRED: list[str] = ["OLLAMA_HOST", "MODEL_NAME"]
    RUNTIME_ENV_OPTIONAL: list[str] = [
        "BACKEND_CORS_ORIGINS",
        "REQUEST_TIMEOUT",
        "REQUEST_MAX_INPUT_CHARS",
        "REQUEST_MAX_TOKENS",
        "TTS_AUTH_ENABLED",
        "TTS_AUTH_HEADER",
        "TTS_AUTH_TOKEN",
        "TTS_PROVIDER",
        "TTS_COQUI_BASE_URL",
        "TTS_COQUI_SYNTH_PATH",
        "TTS_COQUI_VOICES_PATH",
        "TTS_RUNTIME_OUTPUT_DIR",
        "RATE_LIMIT_ENABLED",
        "RATE_LIMIT_REQUESTS_PER_MINUTE",
        "RATE_LIMIT_BURST",
        "RATE_LIMIT_WINDOW_SEC",
        "TTS_RATE_LIMIT_ENABLED",
        "TTS_RATE_LIMIT_REQUESTS_PER_MINUTE",
        "TTS_RATE_LIMIT_BURST",
        "TTS_RATE_LIMIT_WINDOW_SEC",
        "TTS_CACHE_ENABLED",
        "TTS_CACHE_TTL_SEC",
        "TTS_CACHE_MAX_ENTRIES",
        "TTS_CACHE_MAX_BYTES",
    ]
    SETTINGS_CONTRACT_ISSUES: list[str] = []

    OLLAMA_HOST: str = "http://localhost:11434"
    MODEL_NAME: str = "qwen2.5:7b"
    TEMPERATURE: float = 0.7
    TOP_P: float = 0.9
    TOP_K: int = 40
    MIN_P: float = 0.0
    TYPICAL_P: float = 1.0
    TFS_Z: float = 1.0
    MIROSTAT: int = 0
    MIROSTAT_TAU: float = 5.0
    MIROSTAT_ETA: float = 0.1
    PENALIZE_NEWLINE: bool = False
    REPEAT_PENALTY: float = 1.1
    REPEAT_LAST_N: int = 64
    NUM_CTX_DEFAULT: int | None = None

    EVAL_DIRECTORY: str = AGENT_EVAL_ROOT
    EVAL_DATASET_DIR: str = os.path.join(AGENT_EVAL_ROOT, "datasets")
    EVAL_RESULTS_DIR: str = os.path.join(AGENT_EVAL_ROOT, "results")
    EVAL_CONFIG_DIR: str = os.path.join(AGENT_EVAL_ROOT, "config")
    EVAL_FILE_PATTERN: str = "eval-*.json*"

    BACKEND_CORS_ORIGINS: list[str] = []

    REQUEST_TIMEOUT: float = 60.0
    REQUEST_MAX_INPUT_CHARS: int = 16000
    REQUEST_MAX_TOKENS: int = 512

    TTS_AUTH_ENABLED: bool = False
    TTS_AUTH_HEADER: str = "X-TTS-Token"
    TTS_AUTH_TOKEN: str | None = None
    TTS_PROVIDER: str = "dummy"
    TTS_COQUI_BASE_URL: str = "http://127.0.0.1:5002"
    TTS_COQUI_SYNTH_PATH: str = "/api/tts"
    TTS_COQUI_VOICES_PATH: str = "/api/voices"
    TTS_RUNTIME_OUTPUT_DIR: str = os.path.join("novapolis_agent", "outputs", "tts", "runtime")

    RATE_LIMIT_ENABLED: bool = False
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = 60
    RATE_LIMIT_BURST: int = 30
    RATE_LIMIT_WINDOW_SEC: float = 60.0
    RATE_LIMIT_TRUSTED_IPS: list[str] = ["127.0.0.1", "::1"]
    RATE_LIMIT_EXEMPT_PATHS: list[str] = ["/health", "/docs", "/openapi.json"]

    TTS_RATE_LIMIT_ENABLED: bool = False
    TTS_RATE_LIMIT_REQUESTS_PER_MINUTE: int = 30
    TTS_RATE_LIMIT_BURST: int = 5
    TTS_RATE_LIMIT_WINDOW_SEC: float = 60.0
    TTS_RATE_LIMIT_PATHS: list[str] = ["/tts/voices", "/tts/synthesize"]

    TTS_CACHE_ENABLED: bool = False
    TTS_CACHE_TTL_SEC: int = 300
    TTS_CACHE_MAX_ENTRIES: int = 500
    TTS_CACHE_MAX_BYTES: int = 2_000_000

    LOG_JSON: bool = False
    LOG_TRUNCATE_CHARS: int = 200
    REQUEST_ID_HEADER: str = "X-Request-ID"

    CONTEXT_NOTES_ENABLED: bool = False
    CONTEXT_NOTES_PATHS: list[str] = [
        os.path.join(AGENT_EVAL_ROOT, "config", "context.local.md"),
        os.path.join(AGENT_EVAL_ROOT, "config", "context.local.jsonl"),
        os.path.join(AGENT_EVAL_ROOT, "config", "context.local.json"),
        os.path.join(AGENT_EVAL_ROOT, "config", "context.notes"),
        os.path.join("data", "context.local.md"),
    ]
    CONTEXT_NOTES_MAX_CHARS: int = 12000

    CONTENT_POLICY_ENABLED: bool = False
    POLICIES_ENABLED: bool = False
    POLICY_FILE: str | None = None
    POLICY_STRICT_UNRESTRICTED_BYPASS: bool = True

    EVAL_POST_REWRITE_ENABLED: bool = True
    EVAL_POST_MAX_SENTENCES: int = 2
    EVAL_POST_MAX_CHARS: int = 240
    EVAL_POST_RULES: dict[str, bool] = {
        "neutralize_pronouns": True,
        "strip_roleplay": True,
        "no_exclamations": True,
        "no_emojis": True,
        "no_storytelling": True,
        "compact_style": True,
    }

    SESSION_MEMORY_ENABLED: bool = False
    SESSION_MEMORY_MAX_MESSAGES: int = 20
    SESSION_MEMORY_MAX_CHARS: int = 12000

    MEMORY_ENABLED: bool = True
    MEMORY_STORE: str = "inmemory"
    MEMORY_MAX_TURNS: int = 20
    MEMORY_MAX_CHARS: int = 8000
    MEMORY_DIR: Path = Path(".data/memory")

    TOOLS_ENABLED: bool = False
    TOOLS_WHITELIST: list[str] = []

    RAG_ENABLED: bool = False
    RAG_INDEX_PATH: str = str(Path(AGENT_EVAL_ROOT) / "results" / "rag" / "index.json")
    RAG_TOP_K: int = 3

    # Backward-compatible aliases used in root TODO/checklists.
    RAG_ON: bool | None = None
    SHADOW_ON: bool | None = None
    CANARY_PCT: int = 0

    SHADOW_MODE_LOGGING_ENABLED: bool = True
    SHADOW_MODE_LOG_PATH: str = str(Path(".tmp/results/logs/shadow_mode.jsonl"))
    SHADOW_MODE_REDACT_PREVIEW_ENABLED: bool = True
    SHADOW_MODE_PREVIEW_MAX_CHARS: int = 280

    AUTO_MODE_DEFAULT: str = "rpg"
    AUTO_MODE_MEMORY_TTL_MIN: int = 120
    AUTO_MODE_MEMORY_MAX: int = 1000

    @staticmethod
    def _add_issue_or_raise(strict: bool, issues: list[str], message: str) -> None:
        if strict:
            raise ValueError(message)
        issues.append(message)

    @staticmethod
    def _to_nonempty_str(value: Any) -> str | None:
        try:
            string_value = str(value).strip()
        except Exception:
            return None
        return string_value if string_value else None

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def _coerce_cors(cls, value: Any) -> list[str]:
        if value is None or value == "":
            return []
        if isinstance(value, list):
            result: list[str] = []
            for entry in cast(list[Any], value):
                string_value = cls._to_nonempty_str(entry)
                if string_value is not None:
                    result.append(string_value)
            return result
        if isinstance(value, str):
            try:
                import json

                parsed = json.loads(value)
                if isinstance(parsed, list):
                    result2: list[str] = []
                    for entry in cast(list[Any], parsed):
                        string_value = cls._to_nonempty_str(entry)
                        if string_value is not None:
                            result2.append(string_value)
                    return result2
            except Exception:
                pass
            return [item.strip() for item in value.split(",") if item.strip()]
        return []

    @field_validator("OLLAMA_HOST", mode="before")
    @classmethod
    def _normalize_ollama_host(cls, value: Any) -> str:
        string_value = cls._to_nonempty_str(value)
        if string_value is None:
            return "http://localhost:11434"
        host = string_value.rstrip("/")
        if "//" not in host:
            host = f"http://{host}"
        return host

    @field_validator("MODEL_NAME", mode="before")
    @classmethod
    def _normalize_model_name(cls, value: Any) -> str:
        string_value = cls._to_nonempty_str(value)
        return string_value if string_value is not None else "qwen2.5:7b"

    @model_validator(mode="after")
    def _apply_flag_aliases(self) -> Settings:
        issues: list[str] = []

        if self.RAG_ON is not None:
            self.RAG_ENABLED = bool(self.RAG_ON)
        if self.SHADOW_ON is not None:
            self.SHADOW_MODE_LOGGING_ENABLED = bool(self.SHADOW_ON)

        if self.REQUEST_TIMEOUT <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "REQUEST_TIMEOUT must be > 0; fallback to 60.0",
            )
            self.REQUEST_TIMEOUT = 60.0

        if self.REQUEST_MAX_INPUT_CHARS <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "REQUEST_MAX_INPUT_CHARS must be > 0; fallback to 16000",
            )
            self.REQUEST_MAX_INPUT_CHARS = 16000

        if self.REQUEST_MAX_TOKENS <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "REQUEST_MAX_TOKENS must be > 0; fallback to 512",
            )
            self.REQUEST_MAX_TOKENS = 512

        if self.RATE_LIMIT_REQUESTS_PER_MINUTE <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "RATE_LIMIT_REQUESTS_PER_MINUTE must be > 0; fallback to 60",
            )
            self.RATE_LIMIT_REQUESTS_PER_MINUTE = 60

        if self.RATE_LIMIT_BURST < 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "RATE_LIMIT_BURST must be >= 0; fallback to 30",
            )
            self.RATE_LIMIT_BURST = 30

        if self.RATE_LIMIT_WINDOW_SEC <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "RATE_LIMIT_WINDOW_SEC must be > 0; fallback to 60.0",
            )
            self.RATE_LIMIT_WINDOW_SEC = 60.0

        if self.TTS_RATE_LIMIT_REQUESTS_PER_MINUTE <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "TTS_RATE_LIMIT_REQUESTS_PER_MINUTE must be > 0; fallback to 30",
            )
            self.TTS_RATE_LIMIT_REQUESTS_PER_MINUTE = 30

        if self.TTS_RATE_LIMIT_BURST < 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "TTS_RATE_LIMIT_BURST must be >= 0; fallback to 5",
            )
            self.TTS_RATE_LIMIT_BURST = 5

        if self.TTS_RATE_LIMIT_WINDOW_SEC <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "TTS_RATE_LIMIT_WINDOW_SEC must be > 0; fallback to 60.0",
            )
            self.TTS_RATE_LIMIT_WINDOW_SEC = 60.0

        if self.TTS_CACHE_TTL_SEC <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "TTS_CACHE_TTL_SEC must be > 0; fallback to 300",
            )
            self.TTS_CACHE_TTL_SEC = 300

        if self.TTS_CACHE_MAX_ENTRIES <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "TTS_CACHE_MAX_ENTRIES must be > 0; fallback to 500",
            )
            self.TTS_CACHE_MAX_ENTRIES = 500

        if self.TTS_CACHE_MAX_BYTES <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "TTS_CACHE_MAX_BYTES must be > 0; fallback to 2000000",
            )
            self.TTS_CACHE_MAX_BYTES = 2_000_000

        provider = (self.TTS_PROVIDER or "dummy").strip().lower()
        allowed_providers = {"dummy", "null", "coqui", "ollama", "openai"}
        if provider not in allowed_providers:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "TTS_PROVIDER invalid; fallback to dummy",
            )
            provider = "dummy"
        self.TTS_PROVIDER = provider

        if self.CONTEXT_NOTES_MAX_CHARS <= 0:
            self._add_issue_or_raise(
                self.STRICT_CONFIG,
                issues,
                "CONTEXT_NOTES_MAX_CHARS must be > 0; fallback to 12000",
            )
            self.CONTEXT_NOTES_MAX_CHARS = 12000

        if self.CANARY_PCT < 0:
            self.CANARY_PCT = 0
        elif self.CANARY_PCT > 100:
            self.CANARY_PCT = 100

        missing_required: list[str] = []
        for key in self.RUNTIME_ENV_REQUIRED:
            val = getattr(self, key, None)
            if isinstance(val, str):
                if not val.strip():
                    missing_required.append(key)
            elif val is None:
                missing_required.append(key)

        if missing_required:
            msg = "Missing required runtime settings: " + ", ".join(missing_required)
            self._add_issue_or_raise(self.STRICT_CONFIG, issues, msg)

        self.SETTINGS_CONTRACT_ISSUES = issues
        return self


settings = Settings()

__all__ = ["Settings", "settings"]
