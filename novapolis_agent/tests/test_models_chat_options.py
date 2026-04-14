from __future__ import annotations

from typing import Any, cast

from app.api.models import (
    TEXT_RPG_SESSION_CONTRACT_VERSION,
    CarryOverItem,
    ChatOptions,
    ChatRequest,
    ChatResponse,
    TurnContext,
)


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
        turn_mode="dense",
        turn_window_minutes=30,
        tick_minutes=1,
        budget_class="slightly_over",
        carry_over=[
            CarryOverItem(
                task_id="task-1",
                state="begonnen",
                resume_hint="Werkzeug liegt bereit",
            )
        ],
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
    assert o["turn_mode"] == "dense"
    assert o["turn_window_minutes"] == 30
    assert o["tick_minutes"] == 1
    assert o["budget_class"] == "slightly_over"
    assert o["carry_over"][0]["task_id"] == "task-1"
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


def test_chat_response_contract_fields_dump_cleanly() -> None:
    response = ChatResponse(
        content="Szene: Test",
        model="unit-model",
        contract_version=TEXT_RPG_SESSION_CONTRACT_VERSION,
        session_id="sess-1",
        campaign_id="camp-1",
        scene_id="scene-1",
        slot_id="slot-02",
        turn_id="turn-0002",
        session_status="active",
        resume_checkpoint_id="rcp-slot-02-turn-0002",
        replay_checkpoint_id="turn-0002",
        log_channels=["world", "pc", "ally", "sys"],
        turn_context=TurnContext(turn_mode="standard", turn_window_minutes=30),
        carry_over=[
            CarryOverItem(
                task_id="task-2",
                state="offen",
                resume_hint="noch nicht begonnen",
            )
        ],
    )

    dumped = response.model_dump()
    assert dumped["contract_version"] == TEXT_RPG_SESSION_CONTRACT_VERSION
    assert dumped["session_id"] == "sess-1"
    assert dumped["slot_id"] == "slot-02"
    assert dumped["session_status"] == "active"
    assert dumped["resume_checkpoint_id"] == "rcp-slot-02-turn-0002"
    assert dumped["turn_context"]["turn_window_minutes"] == 30
    assert dumped["carry_over"][0]["task_id"] == "task-2"
