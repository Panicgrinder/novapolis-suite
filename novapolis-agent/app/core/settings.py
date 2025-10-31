from __future__ import annotations

import os
from pathlib import Path
from typing import Any, List, Optional, cast

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


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

    OLLAMA_HOST: str = "http://localhost:11434"
    MODEL_NAME: str = "llama3.1:8b"
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
    NUM_CTX_DEFAULT: Optional[int] = None

    EVAL_DIRECTORY: str = "eval"
    EVAL_DATASET_DIR: str = os.path.join("eval", "datasets")
    EVAL_RESULTS_DIR: str = os.path.join("eval", "results")
    EVAL_CONFIG_DIR: str = os.path.join("eval", "config")
    EVAL_FILE_PATTERN: str = "eval-*.json*"

    BACKEND_CORS_ORIGINS: List[str] = []

    REQUEST_TIMEOUT: float = 60.0
    REQUEST_MAX_INPUT_CHARS: int = 16000
    REQUEST_MAX_TOKENS: int = 512

    RATE_LIMIT_ENABLED: bool = False
    RATE_LIMIT_REQUESTS_PER_MINUTE: int = 60
    RATE_LIMIT_BURST: int = 30
    RATE_LIMIT_WINDOW_SEC: float = 60.0
    RATE_LIMIT_TRUSTED_IPS: List[str] = ["127.0.0.1", "::1"]
    RATE_LIMIT_EXEMPT_PATHS: List[str] = ["/health", "/docs", "/openapi.json"]

    LOG_JSON: bool = False
    LOG_TRUNCATE_CHARS: int = 200
    REQUEST_ID_HEADER: str = "X-Request-ID"

    CONTEXT_NOTES_ENABLED: bool = False
    CONTEXT_NOTES_PATHS: List[str] = [
        os.path.join("eval", "config", "context.local.md"),
        os.path.join("eval", "config", "context.local.jsonl"),
        os.path.join("eval", "config", "context.local.json"),
        os.path.join("eval", "config", "context.notes"),
        os.path.join("data", "context.local.md"),
    ]
    CONTEXT_NOTES_MAX_CHARS: int = 12000

    CONTENT_POLICY_ENABLED: bool = False
    POLICIES_ENABLED: bool = False
    POLICY_FILE: Optional[str] = None
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
    TOOLS_WHITELIST: List[str] = []

    RAG_ENABLED: bool = False
    RAG_INDEX_PATH: str = str(Path("eval/results/rag/index.json"))
    RAG_TOP_K: int = 3

    AUTO_MODE_DEFAULT: str = "rpg"
    AUTO_MODE_MEMORY_TTL_MIN: int = 120
    AUTO_MODE_MEMORY_MAX: int = 1000

    @staticmethod
    def _to_nonempty_str(value: Any) -> Optional[str]:
        try:
            string_value = str(value).strip()
        except Exception:
            return None
        return string_value if string_value else None

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")
    @classmethod
    def _coerce_cors(cls, value: Any) -> List[str]:
        if value is None or value == "":
            return []
        if isinstance(value, list):
            result: List[str] = []
            for entry in cast(List[Any], value):
                string_value = cls._to_nonempty_str(entry)
                if string_value is not None:
                    result.append(string_value)
            return result
        if isinstance(value, str):
            try:
                import json

                parsed = json.loads(value)
                if isinstance(parsed, list):
                    result2: List[str] = []
                    for entry in cast(List[Any], parsed):
                        string_value = cls._to_nonempty_str(entry)
                        if string_value is not None:
                            result2.append(string_value)
                    return result2
            except Exception:
                pass
            return [item.strip() for item in value.split(",") if item.strip()]
        return []


settings = Settings()

__all__ = ["settings", "Settings"]
