#!/usr/bin/env python
from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from collections.abc import Mapping
from typing import Any, cast

import httpx

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


DEFAULT_PROMPT = (
    "Bitte formuliere eine versandfaehige deutschsprachige Support-Antwort: "
    "Die Rechnungsnummer fehlt noch, wir brauchen sie fuer die weitere Pruefung."
)

EXIT_SUCCESS = 0
EXIT_HTTP_ERROR = 1
EXIT_PAYLOAD_ERROR = 2
EXIT_NETWORK_ERROR = 3


def build_payload(
    *,
    prompt: str,
    profile_id: str,
    candidate_models: list[str] | None,
    judge_model: str | None,
    force_judge: bool,
    host_override: str | None,
) -> dict[str, Any]:
    options: dict[str, Any] = {"support_ab_enabled": True}
    if candidate_models:
        options["support_candidate_models"] = list(candidate_models)
    if judge_model:
        options["support_judge_model"] = judge_model
    if force_judge:
        options["support_force_judge"] = True
    if host_override:
        options["host"] = host_override
    return {
        "messages": [{"role": "user", "content": prompt}],
        "profile_id": profile_id,
        "options": options,
    }


def emit_result(payload: Mapping[str, Any]) -> None:
    print(json.dumps(dict(payload), ensure_ascii=False, indent=2))


def extract_error_detail(data: Mapping[str, Any]) -> str | None:
    detail = data.get("detail")
    if isinstance(detail, str) and detail.strip():
        return detail.strip()
    error = data.get("error")
    if isinstance(error, str) and error.strip():
        return error.strip()
    return None


async def post_support_request(
    *,
    client: httpx.AsyncClient,
    api_url: str,
    payload: Mapping[str, Any],
) -> tuple[int, dict[str, Any]]:
    response = await client.post(api_url, json=dict(payload))
    content_type = response.headers.get("content-type", "")
    if not content_type.startswith("application/json"):
        raise RuntimeError(f"unexpected content-type: {content_type or '<empty>'}")
    try:
        response_payload = response.json()
    except ValueError as exc:
        raise RuntimeError("response body is not valid JSON") from exc
    if not isinstance(response_payload, dict):
        raise RuntimeError("response JSON must be an object")
    return int(response.status_code), cast(dict[str, Any], response_payload)


async def run_support_smoke(args: argparse.Namespace) -> int:
    payload = build_payload(
        prompt=str(args.prompt),
        profile_id=str(args.profile_id),
        candidate_models=list(args.candidate_model or []),
        judge_model=(str(args.judge_model).strip() or None) if args.judge_model else None,
        force_judge=bool(args.force_judge),
        host_override=(str(args.host).strip() or None) if args.host else None,
    )
    output: dict[str, Any] = {
        "status": "pending",
        "profile_id": payload.get("profile_id"),
        "mode": "asgi" if args.asgi else "http",
        "api_url": "/chat" if args.asgi else str(args.api_url),
        "used_judge": bool(payload.get("options", {}).get("support_judge_model")),
    }

    try:
        if args.asgi:
            from novapolis_agent.app.main import app as fastapi_app

            transport = httpx.ASGITransport(app=cast(Any, fastapi_app))
            async with httpx.AsyncClient(
                transport=transport,
                base_url="http://asgi",
                timeout=float(args.timeout),
            ) as client:
                status_code, data = await post_support_request(
                    client=client,
                    api_url="/chat",
                    payload=payload,
                )
        else:
            async with httpx.AsyncClient(timeout=float(args.timeout)) as client:
                status_code, data = await post_support_request(
                    client=client,
                    api_url=str(args.api_url),
                    payload=payload,
                )
    except httpx.RequestError as exc:
        output["status"] = "network_error"
        output["error"] = str(exc)
        emit_result(output)
        return EXIT_NETWORK_ERROR
    except RuntimeError as exc:
        output["status"] = "payload_error"
        output["error"] = str(exc)
        emit_result(output)
        return EXIT_PAYLOAD_ERROR

    content = str(data.get("content", ""))
    model = str(data.get("model", ""))
    output["status_code"] = status_code
    output["selected_model"] = model
    output["content"] = content

    if status_code != 200:
        output["status"] = "http_error"
        output["error"] = extract_error_detail(data) or f"HTTP {status_code}"
        emit_result(output)
        return EXIT_HTTP_ERROR

    if not model or not content.strip():
        output["status"] = "payload_error"
        output["error"] = "missing model or content in JSON response"
        emit_result(output)
        return EXIT_PAYLOAD_ERROR

    output["status"] = "ok"
    emit_result(output)
    return EXIT_SUCCESS


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fuehrt einen kleinen Smoke-Lauf fuer profile_id=support_de_ab gegen /chat aus."
    )
    parser.add_argument("--api-url", default="http://localhost:8000/chat")
    parser.add_argument("--asgi", action="store_true")
    parser.add_argument("--prompt", default=DEFAULT_PROMPT)
    parser.add_argument("--profile-id", default="support_de_ab")
    parser.add_argument("--candidate-model", action="append", default=[])
    parser.add_argument("--judge-model")
    parser.add_argument("--force-judge", action="store_true")
    parser.add_argument("--host")
    parser.add_argument("--timeout", type=float, default=180.0)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    return asyncio.run(run_support_smoke(parse_args(argv)))


if __name__ == "__main__":
    raise SystemExit(main())
