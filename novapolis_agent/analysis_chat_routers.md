---
stand: 2026-01-11 03:44
update: checks aktualisiert (Basis-Stabilisierung)
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md' PASS (2026-01-11 03:44); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis_agent\analysis_chat_routers.md novapolis_agent\scripts\README.md novapolis_agent\eval\README.md novapolis_agent\eval\DEPRECATIONS.md novapolis_agent\eval\config\context.notes\README.md PASS (2026-01-11 03:44)
---
"""
Vergleich und Zusammenführung der Chat-Router aus routers/chat.py und api/endpoints/chat.py

Analyse:
  - APIRouter mit Präfix "/chat"
  - System-Prompts werden aus `app/core/prompts.py` bezogen (keine system.txt mehr)
  - Fügt Systemprompt direkt hinzu, wenn keiner vorhanden ist
  - Ruft generate_reply() direkt auf

- Altstruktur (entfernt): APIRouter ohne Präfix, eigene Helper-Funktion
  - Heutiger Stand: zentrale Verarbeitung in `app/api/chat.py` inkl. Systemprompt-Injektion und Modus-Handling

Hauptunterschiede:

1. Pfad: "/chat" vs "/"
2. Systemprompt-Handling: direkt vs über Hilfsfunktion
3. Fehlerbehandlung: Keine vs. explizite Prüfung auf leere Nachrichten

Empfehlung:

- Altes Router-Setup wurde entfernt.
- Aktuelle Chat-Verarbeitung: `app/api/chat.py` mit `process_chat_request` und Modus-Handling (eval/unrestricted).
"""

