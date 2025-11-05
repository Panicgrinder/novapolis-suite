#!/usr/bin/env python
"""
Validate OPENAI_API_KEY from ../.env using the OpenAI Python SDK without leaking secrets.
Exit codes:
  0 = OK (authentication succeeded)
  1 = Missing key
  2 = Invalid key (authentication error)
  3 = Network or API connectivity issue
  4 = SDK not installed / other error
"""
from __future__ import annotations
import os
import sys
from typing import Optional

try:
    from dotenv import load_dotenv
except Exception:
    load_dotenv = None  # type: ignore

# Load .env next to project root (../.env relative to scripts/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
ENV_PATH = os.path.join(BASE_DIR, ".env")
if load_dotenv:
    load_dotenv(dotenv_path=ENV_PATH, override=False)

key: Optional[str] = os.getenv("OPENAI_API_KEY")
if not key:
    print("OPENAI_API_KEY: MISSING")
    sys.exit(1)

try:
    import httpx
except Exception as e:
    print(f"HTTPX: NOT_INSTALLED ({e})")
    sys.exit(4)

try:
    url = "https://api.openai.com/v1/models"
    headers = {"Authorization": f"Bearer {key}", "Accept": "application/json"}
    with httpx.Client(timeout=10) as client:
        r = client.get(url, headers=headers)
        if r.status_code == 200:
            try:
                data = r.json()
                count = len(data.get("data", [])) if isinstance(data, dict) else 0
            except Exception:
                count = -1
            print(f"OPENAI_API_KEY: OK (models={count})")
            sys.exit(0)
        elif r.status_code == 401:
            print("OPENAI_API_KEY: INVALID (401)")
            sys.exit(2)
        elif r.status_code in (403, 404):
            # Could be org/project scoping issues or endpoint restrictions
            print(f"OPENAI_API_KEY: ERROR ({r.status_code})")
            sys.exit(4)
        elif r.status_code == 429:
            print("OPENAI_API_KEY: RATE_LIMIT (429)")
            sys.exit(0)
        else:
            print(f"OPENAI_API_KEY: ERROR ({r.status_code})")
            sys.exit(4)
except httpx.HTTPError as e:
    print(f"OPENAI_API_KEY: NETWORK ({type(e).__name__})")
    sys.exit(3)
except Exception as e:
    print(f"OPENAI_API_KEY: ERROR ({type(e).__name__})")
    sys.exit(4)
