from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from app.api.tts_models import TtsOutputFormat, TtsSynthesizeRequest, TtsVoice


@dataclass
class ProviderSynthesisResult:
    mime_type: str
    detail: str
    is_placeholder: bool = True


class TtsProviderProtocol(Protocol):
    provider_id: str
    supports_synthesis: bool

    def voices(self) -> list[TtsVoice]: ...

    def synthesize(self, request: TtsSynthesizeRequest) -> ProviderSynthesisResult: ...


class DummyTtsProvider:
    provider_id = "dummy"
    supports_synthesis = True

    def voices(self) -> list[TtsVoice]:
        return [
            TtsVoice(
                voice_id="dummy-de",
                label="Dummy German",
                language="de",
                provider=self.provider_id,
            ),
            TtsVoice(
                voice_id="dummy-en",
                label="Dummy English",
                language="en",
                provider=self.provider_id,
            ),
        ]

    def synthesize(self, request: TtsSynthesizeRequest) -> ProviderSynthesisResult:
        mime = "audio/ogg" if request.output_format == TtsOutputFormat.ogg else "audio/wav"
        return ProviderSynthesisResult(
            mime_type=mime,
            detail="Dummy provider response for offline contract tests.",
            is_placeholder=True,
        )


class NullTtsProvider:
    provider_id = "null"
    supports_synthesis = True

    def voices(self) -> list[TtsVoice]:
        return []

    def synthesize(self, request: TtsSynthesizeRequest) -> ProviderSynthesisResult:
        mime = "audio/ogg" if request.output_format == TtsOutputFormat.ogg else "audio/wav"
        return ProviderSynthesisResult(
            mime_type=mime,
            detail="Null provider active. No real synthesis backend attached.",
            is_placeholder=True,
        )


class AdapterScaffoldProvider:
    supports_synthesis = True

    def __init__(self, provider_id: str) -> None:
        self.provider_id = provider_id

    def voices(self) -> list[TtsVoice]:
        return []

    def synthesize(self, request: TtsSynthesizeRequest) -> ProviderSynthesisResult:
        mime = "audio/ogg" if request.output_format == TtsOutputFormat.ogg else "audio/wav"
        return ProviderSynthesisResult(
            mime_type=mime,
            detail=(
                "Provider adapter scaffold active ("
                + self.provider_id
                + "). Real backend wiring follows in a later step."
            ),
            is_placeholder=True,
        )


def build_tts_provider(provider_name: str) -> TtsProviderProtocol:
    normalized = provider_name.strip().lower()
    if normalized == "dummy":
        return DummyTtsProvider()
    if normalized == "null":
        return NullTtsProvider()
    if normalized in {"coqui", "ollama", "openai"}:
        return AdapterScaffoldProvider(normalized)
    return DummyTtsProvider()
