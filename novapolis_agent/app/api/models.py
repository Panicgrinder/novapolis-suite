from typing import Any, cast

from pydantic import BaseModel, field_validator

TEXT_RPG_SESSION_CONTRACT_VERSION = "text_rpg_session_v1"
TEXT_RPG_LOG_CHANNELS = ("world", "pc", "ally", "sys")
TEXT_RPG_DEFAULT_TURN_WINDOW_MINUTES = 30
TEXT_RPG_DENSE_TICK_MINUTES = 1


class TurnContext(BaseModel):
    turn_mode: str = "standard"
    turn_window_minutes: int = TEXT_RPG_DEFAULT_TURN_WINDOW_MINUTES
    tick_minutes: int | None = None
    budget_class: str | None = None


class CarryOverItem(BaseModel):
    task_id: str
    state: str
    resume_hint: str
    prepared_assets: list[str] | None = None


class ChatOptions(BaseModel):
    host: str | None = None
    session_id: str | None = None
    orchestrator_enabled: bool | None = None
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    turn_id: str | None = None
    retrieval_query: str | None = None
    public_context: str | None = None
    hidden_context: str | None = None
    scheduler_hints: list[str] | str | None = None
    state_patch_hints: list[str] | str | None = None
    turn_mode: str | None = None
    turn_window_minutes: int | None = None
    tick_minutes: int | None = None
    budget_class: str | None = None
    carry_over: list[CarryOverItem] | None = None

    temperature: float | None = None
    top_p: float | None = None
    num_predict: int | None = None
    max_tokens: int | None = None
    num_ctx: int | None = None
    repeat_penalty: float | None = None
    presence_penalty: float | None = None
    frequency_penalty: float | None = None
    seed: int | None = None
    repeat_last_n: int | None = None
    stop: list[str] | str | None = None
    top_k: int | None = None
    min_p: float | None = None
    typical_p: float | None = None
    tfs_z: float | None = None
    mirostat: int | None = None
    mirostat_tau: float | None = None
    mirostat_eta: float | None = None
    penalize_newline: bool | None = None


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage | dict[str, str]]
    model: str | None = None
    options: dict[str, Any] | ChatOptions | None = None
    profile_id: str | None = None
    session_id: str | None = None

    @field_validator("messages", mode="before")
    @classmethod
    def _coerce_messages(cls, value: Any) -> Any:
        try:
            if isinstance(value, list | tuple):
                seq = list(cast(list[Any], value))
            else:
                return cast(Any, value)
        except Exception:
            return cast(Any, value)
        out: list[ChatMessage | dict[str, str]] = []
        for entry in seq:
            if isinstance(entry, ChatMessage):
                out.append(entry)
            elif isinstance(entry, dict):
                data = cast(dict[Any, Any], entry)
                role = str(data.get("role", "user"))
                content = str(data.get("content", ""))
                out.append({"role": role, "content": content})
            else:
                role = str(getattr(entry, "role", "user"))
                content = str(getattr(entry, "content", ""))
                out.append({"role": role, "content": content})
        return out


class ChatResponse(BaseModel):
    content: str
    model: str | None = None
    contract_version: str | None = None
    session_id: str | None = None
    campaign_id: str | None = None
    scene_id: str | None = None
    slot_id: str | None = None
    turn_id: str | None = None
    session_status: str | None = None
    resume_checkpoint_id: str | None = None
    replay_checkpoint_id: str | None = None
    log_channels: list[str] | None = None
    turn_context: TurnContext | None = None
    carry_over: list[CarryOverItem] | None = None


class ApiErrorResponse(BaseModel):
    detail: str
