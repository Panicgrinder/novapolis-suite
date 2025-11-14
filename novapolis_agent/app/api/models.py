from typing import Any, cast

from pydantic import BaseModel, field_validator


class ChatOptions(BaseModel):
    host: str | None = None
    session_id: str | None = None

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
