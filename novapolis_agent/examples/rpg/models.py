from typing import Any

from pydantic import BaseModel, Field


class RollRequest(BaseModel):
    dice_expression: str = Field(..., description="z.B. '2d6+3' oder 'd20'")
    reason: str | None = Field(None, description="Optionale Beschreibung des Wurfs")


class RollResponse(BaseModel):
    expression: str
    result: int
    details: list[int] = Field(..., description="Einzelne Würfelergebnisse")
    reason: str | None = None


class StateApplyRequest(BaseModel):
    changes: dict[str, Any] = Field(..., description="Änderungen am Weltzustand")


class StateResponse(BaseModel):
    state: dict[str, Any] = Field(..., description="Der aktuelle Weltzustand")
