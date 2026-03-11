from __future__ import annotations

import json
from pathlib import Path

from app.api import chat as mod
from app.api.models import ChatRequest


def test_bool_from_unknown_variants() -> None:
    assert mod._bool_from_unknown(True) is True
    assert mod._bool_from_unknown(0) is False
    assert mod._bool_from_unknown(" yes ") is True
    assert mod._bool_from_unknown("off") is False
    assert mod._bool_from_unknown("x", default=True) is True


def test_safe_sha256_nonempty() -> None:
    digest = mod._safe_sha256("abc")
    assert isinstance(digest, str)
    assert len(digest) == 64


def test_redact_preview_on_and_off(monkeypatch) -> None:
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_PREVIEW_MAX_CHARS", 40, raising=False)
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_REDACT_PREVIEW_ENABLED", True, raising=False)
    red = mod._redact_preview("mail a@b.de url https://x.y 123456")
    assert "<EMAIL>" in red
    assert "<URL>" in red
    assert "<NUM>" in red

    monkeypatch.setattr(mod.settings, "SHADOW_MODE_REDACT_PREVIEW_ENABLED", False, raising=False)
    plain = mod._redact_preview("a   b")
    assert plain == "a b"


def test_shadow_mode_enabled_paths(monkeypatch) -> None:
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_LOGGING_ENABLED", True, raising=False)
    req = ChatRequest(messages=[{"role": "user", "content": "h"}], options={"shadow_mode": "true"})
    assert mod._shadow_mode_enabled(req, eval_mode=False) is True

    req2 = ChatRequest(messages=[{"role": "user", "content": "h"}], options={"shadow_mode": "off"})
    assert mod._shadow_mode_enabled(req2, eval_mode=True) is False

    req3 = ChatRequest(messages=[{"role": "user", "content": "h"}], options=None)
    assert mod._shadow_mode_enabled(req3, eval_mode=True) is True

    monkeypatch.setattr(mod.settings, "SHADOW_MODE_LOGGING_ENABLED", False, raising=False)
    assert mod._shadow_mode_enabled(req3, eval_mode=True) is False


def test_append_shadow_mode_event_writes_file(monkeypatch, tmp_path: Path) -> None:
    out = tmp_path / "shadow.jsonl"
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_LOGGING_ENABLED", True, raising=False)
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_LOG_PATH", str(out), raising=False)
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_PREVIEW_MAX_CHARS", 120, raising=False)
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_REDACT_PREVIEW_ENABLED", True, raising=False)
    monkeypatch.setattr(mod.settings, "RAG_ENABLED", False, raising=False)
    monkeypatch.setattr(mod.settings, "RAG_INDEX_PATH", "", raising=False)

    req = ChatRequest(messages=[{"role": "user", "content": "x"}], options={"shadow_mode": True})
    mod._append_shadow_mode_event(
        request=req,
        eval_mode=False,
        unrestricted_mode=False,
        request_id="rid-1",
        stream=False,
        messages=[{"role": "user", "content": "contact me a@b.de"}],
        response_text="https://example.org 123456",
        policy_post="allow",
    )

    assert out.exists()
    line = out.read_text(encoding="utf-8").strip()
    payload = json.loads(line)
    assert payload["request_id"] == "rid-1"
    assert payload["policy_post"] == "allow"


def test_append_shadow_mode_event_skips_unrestricted(monkeypatch, tmp_path: Path) -> None:
    out = tmp_path / "shadow.jsonl"
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_LOGGING_ENABLED", True, raising=False)
    monkeypatch.setattr(mod.settings, "SHADOW_MODE_LOG_PATH", str(out), raising=False)
    req = ChatRequest(messages=[{"role": "user", "content": "x"}], options={"shadow_mode": True})

    mod._append_shadow_mode_event(
        request=req,
        eval_mode=False,
        unrestricted_mode=True,
        request_id="rid-2",
        stream=False,
        messages=[{"role": "user", "content": "x"}],
        response_text="y",
        policy_post="allow",
    )

    assert not out.exists()
