from __future__ import annotations

import pytest
from pydantic import ValidationError

from app.api.models import TEXT_RPG_SESSION_CONTRACT_VERSION
from app.api.tts_models import TtsSynthesizeRequest


def test_tts_synthesize_request_normalizes_valid_fields() -> None:
    request = TtsSynthesizeRequest(
        text="  hallo  ",
        contract_version=TEXT_RPG_SESSION_CONTRACT_VERSION,
        channel=" PC ",
        session_id="  sess-1  ",
        campaign_id="  camp-1  ",
        scene_id="  scene-a  ",
        slot_id="  slot-01  ",
        turn_id="  turn-0001  ",
    )

    assert request.text == "hallo"
    assert request.contract_version == TEXT_RPG_SESSION_CONTRACT_VERSION
    assert request.channel == "pc"
    assert request.session_id == "sess-1"
    assert request.campaign_id == "camp-1"
    assert request.scene_id == "scene-a"
    assert request.slot_id == "slot-01"
    assert request.turn_id == "turn-0001"


@pytest.mark.parametrize(
    ("payload", "message"),
    [
        ({"text": "   "}, "text must not be empty"),
        ({"text": "ok", "contract_version": "wrong"}, "unsupported contract_version"),
        ({"text": "ok", "channel": "wrong"}, "unsupported channel"),
    ],
)
def test_tts_synthesize_request_rejects_invalid_values(payload: dict[str, str], message: str) -> None:
    with pytest.raises(ValidationError, match=message):
        TtsSynthesizeRequest(**payload)


def test_tts_synthesize_request_normalizes_blank_optional_ids_to_none() -> None:
    request = TtsSynthesizeRequest(
        text="ok",
        session_id="   ",
        campaign_id="   ",
        scene_id="   ",
        slot_id="   ",
        turn_id="   ",
    )

    assert request.session_id is None
    assert request.campaign_id is None
    assert request.scene_id is None
    assert request.slot_id is None
    assert request.turn_id is None


def test_tts_synthesize_request_accepts_none_contract_and_optional_ids() -> None:
    request = TtsSynthesizeRequest(
        text="ok",
        contract_version=None,
        session_id=None,
        campaign_id=None,
        scene_id=None,
        slot_id=None,
        turn_id=None,
    )

    assert request.contract_version is None
    assert request.session_id is None
    assert request.campaign_id is None
    assert request.scene_id is None
    assert request.slot_id is None
    assert request.turn_id is None