from __future__ import annotations

from typing import Any, cast

from app.api.models import ChatOptions, ChatRequest


def test_chat_options_schema_accepts_and_dumps() -> None:
    opts = ChatOptions(
        host="http://localhost:11434",
        session_id="sid123",
        campaign_id="camp-1",
        scene_id="scene-1",
        slot_id="slot-02",
        turn_id="turn-9",
        orchestrator_enabled=True,
        retrieval_query="D5 Materiallauf Reflex",
        public_context="Sichtbar",
        hidden_context="Verdeckt",
        scheduler_hints=["folge dem Pfad"],
        state_patch_hints=["mission.progress +1"],
        temperature=0.7,
        top_p=0.9,
        num_ctx=2048,
        stop=["\n\n", "<END>"],
    )
    req = ChatRequest(messages=[{"role": "user", "content": "hi"}], options=opts)
    dumped = req.model_dump()
    # options should be dumped as dict with expected keys
    assert isinstance(dumped.get("options"), dict)
    o: dict[str, Any] = dumped["options"]
    assert o["session_id"] == "sid123"
    assert o["campaign_id"] == "camp-1"
    assert o["scene_id"] == "scene-1"
    assert o["slot_id"] == "slot-02"
    assert o["turn_id"] == "turn-9"
    assert o["orchestrator_enabled"] is True
    assert o["retrieval_query"] == "D5 Materiallauf Reflex"
    assert o["public_context"] == "Sichtbar"
    assert o["hidden_context"] == "Verdeckt"
    assert o["scheduler_hints"] == ["folge dem Pfad"]
    assert o["state_patch_hints"] == ["mission.progress +1"]
    assert o["temperature"] == 0.7
    assert o["num_ctx"] == 2048
    assert o["stop"] == ["\n\n", "<END>"]


def test_chat_options_allows_dict_backcompat() -> None:
    opts: dict[str, Any] = {"session_id": "s42", "temperature": 0.5}
    req = ChatRequest(messages=[{"role": "user", "content": "hi"}], options=opts)
    d = req.model_dump()
    assert d["options"]["session_id"] == "s42"


def test_chat_request_message_coercion_handles_various_inputs() -> None:
    from app.api.models import ChatMessage

    class Dummy:
        def __init__(self) -> None:
            self.role = "system"
            self.content = "attrs"

    msg = ChatMessage(role="assistant", content="model")
    req = ChatRequest(messages=[msg, {"role": "user", "content": "dict"}, cast(Any, Dummy())])
    serialized = req.model_dump()
    roles = [item["role"] for item in serialized["messages"]]
    assert roles == ["assistant", "user", "system"]
