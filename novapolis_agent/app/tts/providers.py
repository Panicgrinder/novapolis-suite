from __future__ import annotations

import base64
import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol
from urllib import error as _urlerror
from urllib import request as _urlrequest

from app.api.tts_models import TtsOutputFormat, TtsSynthesizeRequest, TtsVoice
from app.core.settings import settings


@dataclass
class ProviderSynthesisResult:
    mime_type: str
    detail: str
    is_placeholder: bool = True
    artifact_path: str | None = None


class TtsProviderUnavailableError(RuntimeError):
    pass


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


def _coqui_join_url(base_url: str, path: str) -> str:
    left = base_url.rstrip("/")
    right = path if path.startswith("/") else "/" + path
    return left + right


def _coqui_request_synthesis(
    *,
    base_url: str,
    synth_path: str,
    timeout_sec: float,
    payload: dict[str, object],
) -> tuple[bytes, str]:
    endpoint = _coqui_join_url(base_url, synth_path)
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = _urlrequest.Request(
        endpoint,
        data=body,
        headers={"Content-Type": "application/json", "Accept": "application/json, audio/*"},
        method="POST",
    )
    try:
        with _urlrequest.urlopen(req, timeout=timeout_sec) as response:
            raw = response.read()
            content_type = response.headers.get("Content-Type", "").split(";", 1)[0].strip()
    except _urlerror.HTTPError as exc:
        detail = "HTTP " + str(exc.code) + " from Coqui endpoint"
        raise TtsProviderUnavailableError(detail) from exc
    except _urlerror.URLError as exc:
        raise TtsProviderUnavailableError("Coqui endpoint not reachable") from exc

    if content_type.startswith("audio/") and raw:
        return raw, content_type

    try:
        payload_json = json.loads(raw.decode("utf-8"))
    except Exception as exc:
        raise TtsProviderUnavailableError("Invalid Coqui response payload") from exc

    encoded = None
    mime_type = "audio/ogg"
    if isinstance(payload_json, dict):
        encoded = payload_json.get("audio_base64") or payload_json.get("audio")
        mime_type = str(payload_json.get("mime_type") or mime_type)
        data_obj = payload_json.get("data")
        if not encoded and isinstance(data_obj, dict):
            encoded = data_obj.get("audio_base64") or data_obj.get("audio")
            mime_type = str(data_obj.get("mime_type") or mime_type)

    if not isinstance(encoded, str) or not encoded.strip():
        raise TtsProviderUnavailableError("Coqui response does not contain audio data")

    try:
        audio = base64.b64decode(encoded)
    except Exception as exc:
        raise TtsProviderUnavailableError("Coqui response audio decode failed") from exc
    if not audio:
        raise TtsProviderUnavailableError("Coqui response audio is empty")
    return audio, mime_type


def _coqui_request_voices(*, base_url: str, voices_path: str, timeout_sec: float) -> list[TtsVoice]:
    endpoint = _coqui_join_url(base_url, voices_path)
    req = _urlrequest.Request(endpoint, headers={"Accept": "application/json"}, method="GET")
    try:
        with _urlrequest.urlopen(req, timeout=timeout_sec) as response:
            raw = response.read()
        payload = json.loads(raw.decode("utf-8"))
    except Exception:
        return []

    raw_items: list[object] = []
    if isinstance(payload, list):
        raw_items = payload
    elif isinstance(payload, dict):
        value = payload.get("voices")
        if isinstance(value, list):
            raw_items = value

    voices: list[TtsVoice] = []
    for item in raw_items:
        if isinstance(item, str):
            voice_id = item.strip()
            if not voice_id:
                continue
            voices.append(
                TtsVoice(
                    voice_id=voice_id,
                    label=voice_id,
                    language="de",
                    provider="coqui",
                )
            )
            continue
        if not isinstance(item, dict):
            continue
        voice_id = str(item.get("voice_id") or item.get("id") or "").strip()
        if not voice_id:
            continue
        label = str(item.get("label") or item.get("name") or voice_id).strip() or voice_id
        language = str(item.get("language") or item.get("lang") or "de").strip() or "de"
        voices.append(
            TtsVoice(
                voice_id=voice_id,
                label=label,
                language=language,
                provider="coqui",
            )
        )
    return voices


class CoquiRuntimeProvider:
    provider_id = "coqui"
    supports_synthesis = True

    def __init__(self) -> None:
        self.base_url = str(settings.TTS_COQUI_BASE_URL)
        self.synth_path = str(settings.TTS_COQUI_SYNTH_PATH)
        self.voices_path = str(settings.TTS_COQUI_VOICES_PATH)
        self.timeout_sec = float(settings.REQUEST_TIMEOUT)
        self.runtime_output_dir = Path(str(settings.TTS_RUNTIME_OUTPUT_DIR))

    def voices(self) -> list[TtsVoice]:
        voices = _coqui_request_voices(
            base_url=self.base_url,
            voices_path=self.voices_path,
            timeout_sec=self.timeout_sec,
        )
        if voices:
            return voices
        return [
            TtsVoice(
                voice_id="coqui-default",
                label="Coqui Default",
                language="de",
                provider=self.provider_id,
            )
        ]

    def synthesize(self, request: TtsSynthesizeRequest) -> ProviderSynthesisResult:
        payload = {
            "text": request.text,
            "speaker": request.voice,
            "language": request.language,
            "sample_rate": request.sample_rate_hz,
            "output_format": request.output_format.value,
            "settings": request.settings,
        }
        audio_bytes, mime_type = _coqui_request_synthesis(
            base_url=self.base_url,
            synth_path=self.synth_path,
            timeout_sec=self.timeout_sec,
            payload=payload,
        )

        key_payload = {
            "provider": self.provider_id,
            "text": request.text,
            "voice": request.voice,
            "language": request.language,
            "output_format": request.output_format.value,
            "sample_rate_hz": request.sample_rate_hz,
            "settings": request.settings,
            "contract_version": request.contract_version,
            "session_id": request.session_id,
            "campaign_id": request.campaign_id,
            "scene_id": request.scene_id,
            "slot_id": request.slot_id,
            "turn_id": request.turn_id,
            "channel": request.channel,
        }
        key_raw = json.dumps(key_payload, ensure_ascii=False, sort_keys=True)
        request_key = hashlib.sha256(key_raw.encode("utf-8")).hexdigest()
        ext = "ogg" if request.output_format == TtsOutputFormat.ogg else "wav"
        if request.session_id:
            safe_session = re.sub(r"[^A-Za-z0-9._-]+", "_", request.session_id).strip("._-")
            safe_session = safe_session or "session"
            artifact_dir = (
                self.runtime_output_dir / "sessions" / safe_session / request.channel / request_key[:2]
            )
        else:
            artifact_dir = self.runtime_output_dir / self.provider_id / request_key[:2]
        artifact_path = artifact_dir / f"{request_key}.{ext}"
        artifact_dir.mkdir(parents=True, exist_ok=True)
        artifact_path.write_bytes(audio_bytes)

        return ProviderSynthesisResult(
            mime_type=mime_type,
            detail="Coqui runtime synthesis completed.",
            is_placeholder=False,
            artifact_path=str(artifact_path),
        )


def build_tts_provider(provider_name: str) -> TtsProviderProtocol:
    normalized = provider_name.strip().lower()
    if normalized == "dummy":
        return DummyTtsProvider()
    if normalized == "null":
        return NullTtsProvider()
    if normalized == "coqui":
        return CoquiRuntimeProvider()
    if normalized in {"ollama", "openai"}:
        return AdapterScaffoldProvider(normalized)
    return DummyTtsProvider()
