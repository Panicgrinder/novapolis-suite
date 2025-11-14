"""Services für die Anwendung."""

from typing import Any

from app.services.llm import generate_completion, get_llm_options

__all__: list[Any] = [
    "generate_completion",
    "get_llm_options",
]
