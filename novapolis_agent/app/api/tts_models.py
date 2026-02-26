from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator


class TtsOutputFormat(str, Enum):
    wav = "wav"
    ogg = "ogg"


class TtsSynthesizeRequest(BaseModel):
    text: str = Field(min_length=1)
    voice: str = "dummy-de"
    language: str = "de"
    output_format: TtsOutputFormat = TtsOutputFormat.ogg
    sample_rate_hz: int = 22050
    settings: dict[str, Any] = {}

    @field_validator("text")
    @classmethod
    def _normalize_text(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("text must not be empty")
        return normalized


class TtsHealthResponse(BaseModel):
    status: str
    provider: str
    synthesize_ready: bool
    cache_ready: bool


class TtsVoice(BaseModel):
    voice_id: str
    label: str
    language: str
    provider: str


class TtsVoicesResponse(BaseModel):
    provider: str
    voices: list[TtsVoice]


class TtsSynthesizeResponse(BaseModel):
    status: str
    provider: str
    output_format: TtsOutputFormat
    mime_type: str
    is_placeholder: bool
    request_hash: str
    cache_key: str | None = None
    cache_hit: bool
    artifact_path: str | None = None
    detail: str


class TtsCacheStatsResponse(BaseModel):
    enabled: bool
    entries: int
    size_bytes: int
    ttl_sec: int
    max_entries: int
    max_bytes: int
    hits: int
    misses: int
    evictions_ttl: int
    evictions_size: int


class TtsCacheCleanupResponse(BaseModel):
    status: str
    removed_expired: int
    removed_size: int
    entries: int
    size_bytes: int
