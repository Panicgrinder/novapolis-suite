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
    return int(response.status_code), cast(dict[str, Any], response.json())


async def run_support_smoke(args: argparse.Namespace) -> int:
    payload = build_payload(
        prompt=str(args.prompt),
        profile_id=str(args.profile_id),
        candidate_models=list(args.candidate_model or []),
        judge_model=(str(args.judge_model).strip() or None) if args.judge_model else None,
        force_judge=bool(args.force_judge),
        host_override=(str(args.host).strip() or None) if args.host else None,
    )

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

    content = str(data.get("content", ""))
    model = str(data.get("model", ""))
    output = {
        "status_code": status_code,
        "profile_id": payload.get("profile_id"),
        "selected_model": model,
        "content": content,
        "used_judge": bool(args.judge_model),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))

    if status_code != 200:
        return 1
    if not model or not content.strip():
        return 2
    return 0


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
