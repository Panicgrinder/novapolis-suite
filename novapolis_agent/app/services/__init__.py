"""Services für die Anwendung."""

from typing import Any as _Any
from typing import List as _List

from app.services.llm import generate_completion, get_llm_options

__all__: _List[_Any] = [
    "get_llm_options",
    "generate_completion",
]
