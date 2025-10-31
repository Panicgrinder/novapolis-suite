from typing import Any, Dict, List, Optional, Union, cast

from pydantic import BaseModel, field_validator


class ChatOptions(BaseModel):
    host: Optional[str] = None
    session_id: Optional[str] = None

    temperature: Optional[float] = None
    top_p: Optional[float] = None
    num_predict: Optional[int] = None
    max_tokens: Optional[int] = None
    num_ctx: Optional[int] = None
    repeat_penalty: Optional[float] = None
    presence_penalty: Optional[float] = None
    frequency_penalty: Optional[float] = None
    seed: Optional[int] = None
    repeat_last_n: Optional[int] = None
    stop: Optional[Union[List[str], str]] = None
    top_k: Optional[int] = None
    min_p: Optional[float] = None
    typical_p: Optional[float] = None
    tfs_z: Optional[float] = None
    mirostat: Optional[int] = None
    mirostat_tau: Optional[float] = None
    mirostat_eta: Optional[float] = None
    penalize_newline: Optional[bool] = None


class ChatMessage(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Union[ChatMessage, Dict[str, str]]]
    model: Optional[str] = None
    options: Optional[Union[Dict[str, Any], ChatOptions]] = None
    profile_id: Optional[str] = None
    session_id: Optional[str] = None

    @field_validator("messages", mode="before")
    @classmethod
    def _coerce_messages(cls, value: Any) -> Any:
        try:
            if isinstance(value, (list, tuple)):
                seq = list(cast(List[Any], value))
            else:
                return cast(Any, value)
        except Exception:
            return cast(Any, value)
        out: List[Union[ChatMessage, Dict[str, str]]] = []
        for entry in seq:
            if isinstance(entry, ChatMessage):
                out.append(entry)
            elif isinstance(entry, dict):
                data = cast(Dict[Any, Any], entry)
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
    model: Optional[str] = None
