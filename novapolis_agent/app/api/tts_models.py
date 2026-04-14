from __future__ import annotations

from enum import StrEnum
from typing import Any

from pydantic import BaseModel, Field, field_validator

from .models import TEXT_RPG_LOG_CHANNELS, TEXT_RPG_SESSION_CONTRACT_VERSION


class TtsOutputFormat(StrEnum):
    wav = "wav"
    ogg = "ogg"


class TtsSynthesizeRequest(BaseModel):
    text: str = Field(min_length=1)
    voice: str = "dummy-de"
    language: str = "de"
    output_format: TtsOutputFormat = TtsOutputFormat.ogg
    sample_rate_hz: int = 22050
    settings: dict[str, Any] = {}
    contract_version: str | None = None
    session_id: str | None = None
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    turn_id: str | None = None
    channel: str = "pc"

    @field_validator("text")
    @classmethod
    def _normalize_text(cls, value: str) -> str:
        normalized = value.strip()
        if not normalized:
            raise ValueError("text must not be empty")
        return normalized

    @field_validator("contract_version")
    @classmethod
    def _validate_contract_version(cls, value: str | None) -> str | None:
        if value is None:
            return value
        normalized = value.strip()
        if normalized != TEXT_RPG_SESSION_CONTRACT_VERSION:
            raise ValueError("unsupported contract_version")
        return normalized

    @field_validator("channel")
    @classmethod
    def _validate_channel(cls, value: str) -> str:
        normalized = value.strip().lower()
        if normalized not in TEXT_RPG_LOG_CHANNELS:
            raise ValueError("unsupported channel")
        return normalized

    @field_validator("session_id", "campaign_id", "scene_id", "slot_id", "turn_id")
    @classmethod
    def _normalize_optional_ids(cls, value: str | None) -> str | None:
        if value is None:
            return value
        normalized = value.strip()
        return normalized or None


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
    contract_version: str | None = None
    session_id: str | None = None
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    turn_id: str | None = None
    channel: str | None = None
    log_channels: list[str] | None = None
    tts_manifest_path: str | None = None
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
