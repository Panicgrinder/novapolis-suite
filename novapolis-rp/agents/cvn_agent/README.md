# CVN Agent Runtime (RP Bundle)

Dieses Verzeichnis enthält ausschließlich die Laufzeitkomponenten des CVN Agents, wie sie vom RP-Workspace benötigt werden:

- `app/` und `utils/` mit den produktiven Modulen
- `run_server.py` zum lokalen Start
- `requirements.txt` für die Minimalinstallation
- `.env` (Hardlink zur zentralen Datei in `novapolis-agent/.env`)

## Entwicklung & Tests

Alle Entwicklungsressourcen – Tests, Skripte, Evaluierungen, Reports und erweiterte Dokumentation –
befinden sich ab sofort im Schwester-Workspace `../novapolis-agent/`.

Arbeitsablauf:

1. Öffne `novapolis-agent/` für Implementierung, Tests und Auswertungen.
2. Führe dort `pytest`, Evaluations-Skripte und Tooling aus.
3. Synchronisiere Änderungen der produktiven Module nach Bedarf in dieses Runtime-Bundle (z. B. über Git oder gezielte Kopien).

## Umgebungsdatei

Die Datei `.env` in diesem Ordner ist ein Hardlink auf `../novapolis-agent/.env`.
Änderungen wirken somit in beiden Workspaces identisch. Bitte gehe sorgsam mit dem enthaltenen
API-Key um – keine Kopien oder Commits.

## Hinweise

- Für zusätzliche Dev-Abhängigkeiten verwende `novapolis-agent/requirements-dev.txt`.
- Dieser Ordner bleibt absichtlich schlank, damit das RP-Repository nur produktionsrelevante Artefakte enthält.
- Dokumentation zur Einbettung in Novapolis-RP steht in `novapolis-dev/docs/`.
