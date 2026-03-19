from __future__ import annotations

import base64
import json
from pathlib import Path
from urllib import error as _urlerror

import pytest
from app.api.tts_models import TtsSynthesizeRequest
from app.tts import providers as mod


class _FakeResponse:
    def __init__(self, payload: bytes, content_type: str = "application/json") -> None:
        self._payload = payload
        self.headers = {"Content-Type": content_type}

    def read(self) -> bytes:
        return self._payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None


def test_coqui_join_url_variants() -> None:
    assert mod._coqui_join_url("http://a", "v") == "http://a/v"
    assert mod._coqui_join_url("http://a/", "/v") == "http://a/v"


def test_coqui_request_synthesis_audio_response(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        mod._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeResponse(b"OggS\x00", "audio/ogg"),
    )
    data, mime = mod._coqui_request_synthesis(
        base_url="http://x",
        synth_path="/api/tts",
        timeout_sec=2.0,
        payload={"text": "a"},
    )
    assert data.startswith(b"OggS")
    assert mime == "audio/ogg"


def test_coqui_request_synthesis_json_base64_nested(monkeypatch: pytest.MonkeyPatch) -> None:
    audio = b"RIFFdata"
    payload = {
        "data": {"audio_base64": base64.b64encode(audio).decode("ascii"), "mime_type": "audio/wav"}
    }
    monkeypatch.setattr(
        mod._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeResponse(json.dumps(payload).encode("utf-8"), "application/json"),
    )
    out, mime = mod._coqui_request_synthesis(
        base_url="http://x",
        synth_path="/api/tts",
        timeout_sec=2.0,
        payload={"text": "a"},
    )
    assert out == audio
    assert mime == "audio/wav"


@pytest.mark.parametrize(
    "payload",
    [
        b"not-json",
        json.dumps({"x": 1}).encode("utf-8"),
        json.dumps({"audio_base64": "%%%"}).encode("utf-8"),
    ],
)
def test_coqui_request_synthesis_invalid_payloads(
    monkeypatch: pytest.MonkeyPatch, payload: bytes
) -> None:
    monkeypatch.setattr(
        mod._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeResponse(payload, "application/json"),
    )
    with pytest.raises(mod.TtsProviderUnavailableError):
        mod._coqui_request_synthesis(
            base_url="http://x",
            synth_path="/api/tts",
            timeout_sec=2.0,
            payload={"text": "a"},
        )


def test_coqui_request_synthesis_http_and_url_errors(monkeypatch: pytest.MonkeyPatch) -> None:
    def _http(*args, **kwargs):
        raise _urlerror.HTTPError("u", 503, "down", hdrs=None, fp=None)

    monkeypatch.setattr(mod._urlrequest, "urlopen", _http)
    with pytest.raises(mod.TtsProviderUnavailableError):
        mod._coqui_request_synthesis(
            base_url="http://x", synth_path="/api/tts", timeout_sec=2.0, payload={}
        )

    def _url(*args, **kwargs):
        raise _urlerror.URLError("down")

    monkeypatch.setattr(mod._urlrequest, "urlopen", _url)
    with pytest.raises(mod.TtsProviderUnavailableError):
        mod._coqui_request_synthesis(
            base_url="http://x", synth_path="/api/tts", timeout_sec=2.0, payload={}
        )


def test_coqui_request_voices_parsing(monkeypatch: pytest.MonkeyPatch) -> None:
    payload = [
        "voice-a",
        {"id": "voice-b", "name": "Voice B", "lang": "en"},
        {"voice_id": "voice-c", "label": "Voice C", "language": "de"},
        {},
    ]
    monkeypatch.setattr(
        mod._urlrequest,
        "urlopen",
        lambda req, timeout: _FakeResponse(json.dumps(payload).encode("utf-8"), "application/json"),
    )
    voices = mod._coqui_request_voices(base_url="http://x", voices_path="/voices", timeout_sec=2.0)
    assert [v.voice_id for v in voices] == ["voice-a", "voice-b", "voice-c"]


def test_coqui_request_voices_error_returns_empty(monkeypatch: pytest.MonkeyPatch) -> None:
    def _boom(*args, **kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(mod._urlrequest, "urlopen", _boom)
    assert (
        mod._coqui_request_voices(base_url="http://x", voices_path="/voices", timeout_sec=2.0) == []
    )


def test_coqui_provider_voices_fallback(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(mod, "_coqui_request_voices", lambda **kwargs: [])
    p = mod.CoquiRuntimeProvider()
    voices = p.voices()
    assert voices[0].voice_id == "coqui-default"


def test_coqui_provider_synthesize_writes_artifact(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    monkeypatch.setattr(mod, "_coqui_request_synthesis", lambda **kwargs: (b"OggS", "audio/ogg"))
    p = mod.CoquiRuntimeProvider()
    p.runtime_output_dir = tmp_path
    req = TtsSynthesizeRequest(
        text="hallo", voice="v", language="de", output_format="ogg", sample_rate_hz=22050
    )
    res = p.synthesize(req)
    assert res.is_placeholder is False
    assert res.artifact_path is not None
    assert Path(res.artifact_path).exists()


def test_build_tts_provider_variants() -> None:
    assert isinstance(mod.build_tts_provider("dummy"), mod.DummyTtsProvider)
    assert isinstance(mod.build_tts_provider("null"), mod.NullTtsProvider)
    assert isinstance(mod.build_tts_provider("ollama"), mod.AdapterScaffoldProvider)
    assert isinstance(mod.build_tts_provider("openai"), mod.AdapterScaffoldProvider)
    assert isinstance(mod.build_tts_provider("unknown"), mod.DummyTtsProvider)
