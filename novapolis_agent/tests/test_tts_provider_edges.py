from __future__ import annotations

import base64
import importlib
import json
from pathlib import Path
from urllib import error as _urlerror

import pytest


def _load_providers_module():
    return importlib.reload(importlib.import_module("app.tts.providers"))


class _FakeHttpResponse:
    def __init__(self, raw: bytes, content_type: str = "application/json") -> None:
        self._raw = raw
        self.headers = {"Content-Type": content_type}

    def read(self) -> bytes:
        return self._raw

    def __enter__(self) -> _FakeHttpResponse:
        return self

    def __exit__(self, exc_type, exc, tb) -> bool:
        return False


@pytest.mark.unit
def test_provider_helpers_cover_join_coerce_and_factory_fallback() -> None:
    providers = _load_providers_module()

    assert providers._coerce_json_object({1: "a"}) == {"1": "a"}
    assert providers._coerce_json_object([1, 2]) is None
    assert providers._coqui_join_url("http://host/", "voices") == "http://host/voices"
    assert providers.build_tts_provider("unknown").provider_id == "dummy"


@pytest.mark.unit
def test_coqui_request_synthesis_covers_audio_json_nested_and_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    providers = _load_providers_module()

    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeHttpResponse(b"OggS", "audio/ogg"),
    )
    audio, mime = providers._coqui_request_synthesis(
        base_url="http://host",
        synth_path="/synth",
        timeout_sec=1.0,
        payload={"text": "hi"},
    )
    assert audio == b"OggS"
    assert mime == "audio/ogg"

    nested_payload = {
        "data": {
            "audio": base64.b64encode(b"nested-audio").decode("ascii"),
            "mime_type": "audio/wav",
        }
    }
    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeHttpResponse(
            json.dumps(nested_payload).encode("utf-8"),
            "application/json",
        ),
    )
    nested_audio, nested_mime = providers._coqui_request_synthesis(
        base_url="http://host",
        synth_path="/synth",
        timeout_sec=1.0,
        payload={"text": "hi"},
    )
    assert nested_audio == b"nested-audio"
    assert nested_mime == "audio/wav"

    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: (_ for _ in ()).throw(_urlerror.URLError("down")),
    )
    with pytest.raises(providers.TtsProviderUnavailableError, match="not reachable"):
        providers._coqui_request_synthesis(
            base_url="http://host",
            synth_path="/synth",
            timeout_sec=1.0,
            payload={"text": "hi"},
        )

    http_error = _urlerror.HTTPError("http://host", 503, "down", hdrs=None, fp=None)
    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: (_ for _ in ()).throw(http_error),
    )
    with pytest.raises(providers.TtsProviderUnavailableError, match="HTTP 503"):
        providers._coqui_request_synthesis(
            base_url="http://host",
            synth_path="/synth",
            timeout_sec=1.0,
            payload={"text": "hi"},
        )

    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeHttpResponse(b"not-json", "application/json"),
    )
    with pytest.raises(
        providers.TtsProviderUnavailableError, match="Invalid Coqui response payload"
    ):
        providers._coqui_request_synthesis(
            base_url="http://host",
            synth_path="/synth",
            timeout_sec=1.0,
            payload={"text": "hi"},
        )

    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeHttpResponse(json.dumps({}).encode("utf-8"), "application/json"),
    )
    with pytest.raises(providers.TtsProviderUnavailableError, match="does not contain audio data"):
        providers._coqui_request_synthesis(
            base_url="http://host",
            synth_path="/synth",
            timeout_sec=1.0,
            payload={"text": "hi"},
        )

    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeHttpResponse(
            json.dumps({"audio": "%%%"}).encode("utf-8"),
            "application/json",
        ),
    )
    monkeypatch.setattr(
        providers.base64, "b64decode", lambda _value: (_ for _ in ()).throw(ValueError("bad"))
    )
    with pytest.raises(providers.TtsProviderUnavailableError, match="audio decode failed"):
        providers._coqui_request_synthesis(
            base_url="http://host",
            synth_path="/synth",
            timeout_sec=1.0,
            payload={"text": "hi"},
        )

    monkeypatch.setattr(providers.base64, "b64decode", lambda _value: b"")
    with pytest.raises(providers.TtsProviderUnavailableError, match="audio is empty"):
        providers._coqui_request_synthesis(
            base_url="http://host",
            synth_path="/synth",
            timeout_sec=1.0,
            payload={"text": "hi"},
        )


@pytest.mark.unit
def test_coqui_request_voices_and_runtime_provider_cover_fallback_paths(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    providers = _load_providers_module()
    monkeypatch.setattr(providers.settings, "TTS_RUNTIME_OUTPUT_DIR", str(tmp_path), raising=False)

    voices_payload = {
        "voices": [
            "voice-a",
            {"id": "voice-b", "name": "Voice B", "lang": "en"},
            {"voice_id": "", "name": "ignored"},
            123,
        ]
    }
    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeHttpResponse(
            json.dumps(voices_payload).encode("utf-8"),
            "application/json",
        ),
    )
    voices = providers._coqui_request_voices(
        base_url="http://host",
        voices_path="/voices",
        timeout_sec=1.0,
    )
    assert [voice.voice_id for voice in voices] == ["voice-a", "voice-b"]
    assert voices[1].label == "Voice B"
    assert voices[1].language == "en"

    monkeypatch.setattr(
        providers._urlrequest,
        "urlopen",
        lambda req, timeout: (_ for _ in ()).throw(RuntimeError("down")),
    )
    assert (
        providers._coqui_request_voices(
            base_url="http://host",
            voices_path="/voices",
            timeout_sec=1.0,
        )
        == []
    )

    provider = providers.CoquiRuntimeProvider()
    monkeypatch.setattr(providers, "_coqui_request_voices", lambda **kwargs: [])
    fallback_voices = provider.voices()
    assert fallback_voices[0].voice_id == "coqui-default"

    monkeypatch.setattr(
        providers, "_coqui_request_synthesis", lambda **kwargs: (b"WAVE", "audio/wav")
    )
    request = providers.TtsSynthesizeRequest(
        text="hello",
        voice="coqui-default",
        language="de",
        output_format=providers.TtsOutputFormat.wav,
        sample_rate_hz=22050,
        settings={},
    )
    result = provider.synthesize(request)
    assert result.is_placeholder is False
    assert result.mime_type == "audio/wav"
    assert result.artifact_path is not None
    assert "/coqui/" in result.artifact_path.replace("\\", "/")


@pytest.mark.unit
def test_placeholder_providers_and_session_sanitizing_paths(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    providers = _load_providers_module()

    null_provider = providers.NullTtsProvider()
    null_result = null_provider.synthesize(
        providers.TtsSynthesizeRequest(
            text="hello",
            voice="null-default",
            language="de",
            output_format=providers.TtsOutputFormat.wav,
            sample_rate_hz=22050,
            settings={},
        )
    )
    assert null_provider.voices() == []
    assert null_result.is_placeholder is True
    assert null_result.mime_type == "audio/wav"

    adapter = providers.AdapterScaffoldProvider("openai")
    adapter_result = adapter.synthesize(
        providers.TtsSynthesizeRequest(
            text="hello",
            voice="openai-default",
            language="de",
            output_format=providers.TtsOutputFormat.ogg,
            sample_rate_hz=22050,
            settings={},
        )
    )
    assert adapter.voices() == []
    assert adapter_result.is_placeholder is True
    assert adapter_result.mime_type == "audio/ogg"
    assert "openai" in adapter_result.detail

    monkeypatch.setattr(providers.settings, "TTS_RUNTIME_OUTPUT_DIR", str(tmp_path), raising=False)
    monkeypatch.setattr(providers, "_coqui_request_synthesis", lambda **kwargs: (b"OggS", "audio/ogg"))

    coqui_provider = providers.CoquiRuntimeProvider()
    sanitized_result = coqui_provider.synthesize(
        providers.TtsSynthesizeRequest(
            text="hello",
            voice="coqui-default",
            language="de",
            output_format=providers.TtsOutputFormat.ogg,
            sample_rate_hz=22050,
            settings={},
            session_id="!!!",
            channel="pc",
        )
    )
    assert sanitized_result.artifact_path is not None
    assert "/sessions/session/pc/" in sanitized_result.artifact_path.replace("\\", "/")
