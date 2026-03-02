"""Package-level compatibility module for ``novapolis_agent.run_server``.

Import-safe by design: heavy runtime dependency imports happen in ``main``.
"""

from __future__ import annotations

import logging
import warnings

from app.core.settings import settings


def main() -> None:
    """Run the development ASGI server."""
    import uvicorn

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    logging.getLogger("asyncio").setLevel(logging.WARNING)
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    warnings.filterwarnings("ignore", category=ResourceWarning)

    print("Starte CVN Agent Server auf http://localhost:8000")
    print("API Dokumentation: http://localhost:8000/docs")
    print(f"Verwende Modell: {settings.MODEL_NAME}")

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
