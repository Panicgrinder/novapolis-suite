"""Package-level compatibility module for ``novapolis_agent.test_settings``.

This keeps legacy import paths import-safe for smoke tests.
"""

from __future__ import annotations

from app.core.settings import settings


def main() -> None:
    """Print a minimal settings summary for manual debugging."""
    print(f"PROJECT_NAME={getattr(settings, 'PROJECT_NAME', 'n/a')}")
    print(f"MODEL_NAME={getattr(settings, 'MODEL_NAME', 'n/a')}")


__all__ = ["main", "settings"]
