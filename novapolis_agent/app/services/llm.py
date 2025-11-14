from __future__ import annotations

import os
from typing import Any

import httpx

from ..api.models import ChatMessage, ChatResponse
from ..core.settings import settings


async def generate_reply(messages: list[ChatMessage]) -> ChatResponse:
    url = f"{settings.OLLAMA_HOST}/api/chat"
    ollama_msgs: list[dict[str, str]] = [
        {"role": msg.role, "content": msg.content} for msg in messages
    ]

    payload: dict[str, Any] = {
        "model": settings.MODEL_NAME,
        "messages": ollama_msgs,
        "stream": False,
    }

    headers: dict[str, str] = {"Content-Type": "application/json"}

    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(30.0)) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            try:
                content = response.json()["message"]["content"]
            except (KeyError, ValueError):
                content = response.text
            return ChatResponse(content=content)
    except httpx.HTTPStatusError as exc:
        error_msg = f"LLM HTTP-Fehler {exc.response.status_code}: Bitte Ollama prüfen."
        return ChatResponse(content=error_msg)
    except httpx.RequestError:
        part1 = "Die Verbindung zum LLM ist fehlgeschlagen. Prüfe, ob Ollama läuft und "
        part2 = str(settings.MODEL_NAME) + " gepullt ist."
        error_msg = part1 + part2
        return ChatResponse(content=error_msg)


def system_message(text: str) -> ChatMessage:
    return ChatMessage(role="system", content=text)


def get_llm_options() -> dict[str, Any]:
    options: dict[str, Any] = {}
    if "LLM_NUM_CTX" in os.environ:
        try:
            options["num_ctx"] = int(os.environ["LLM_NUM_CTX"])
        except ValueError:
            pass
    if "LLM_TEMPERATURE" in os.environ:
        try:
            options["temperature"] = float(os.environ["LLM_TEMPERATURE"])
        except ValueError:
            pass
    return options


async def generate_completion(prompt: str, options: dict[str, Any] | None = None) -> str:
    url = f"{settings.OLLAMA_HOST}/api/generate"
    payload: dict[str, Any] = {
        "model": settings.MODEL_NAME,
        "prompt": prompt,
        "stream": False,
    }
    if options:
        payload.update(options)

    try:
        async with httpx.AsyncClient() as client:
            headers: dict[str, str] = {"Content-Type": "application/json"}
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data.get("response", "")
    except Exception as exc:
        print(f"Fehler bei der Generierung: {exc}")
        return ""
