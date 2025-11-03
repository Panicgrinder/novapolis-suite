---
stand: 2025-11-02 03:29
update: MCP-Server-Prototyp initialisiert; Ordnerstruktur angelegt.
checks: keine
---

# MCP OpenAI Eval Bridge (Prototyp)

Dieser Ordner enthält den geplanten MCP-Server, der sich mit der OpenAI-Evaluationsplattform verbindet.

## Zielsetzung

- Lokalen MCP-Endpunkt bereitstellen (zum Beispiel `http://localhost:4000`).
- Zugriff auf das Evaluations-Dataset `dset_6906606af85c819785c5f5c2f1b285ba0b644e29bb295151` vorbereiten.
- Generator `6d63de16-ff87-48d8-b82d-8ca214a2b2cd` anbinden (Authentifizierung folgt).

## Vorgehensplan

1. Virtuelle Umgebung erstellen (`python -m venv .venv`).
2. Dependencies installieren (`pip install -e .`).
3. Server starten (`python -m mcp_openai_eval.server`).
4. MCP-Client (zum Beispiel das Webinterface) mit `http://localhost:4000` verbinden.

## Nächste Schritte

- Authentifizierung gegen die OpenAI-Plattform definieren (API-Key, Header).
- MCP-spezifische Schnittstellen implementieren (Tools/Resources).
- Verbindungstests dokumentieren.

