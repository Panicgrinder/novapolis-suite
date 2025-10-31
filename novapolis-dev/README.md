# Novapolis Dev Hub

Dieser Arbeitsbereich bündelt teamübergreifende Dokumentation, ToDos, DoneLogs und Migrationsnotizen für alle Novapolis-Projekte.
Der Dev Hub fungiert als gemeinsame Schaltstelle für Agent-, Sim- und RP-Teams und ersetzt die früheren verteilten „development“-Bereiche.

## Zweck

- Zentraler Anlaufpunkt für Entwicklungsunterlagen (Agent, Sim, RP)
- Gemeinsame Policies, Roadmaps, Integrationen
- Verweise auf produktive Repositories:
  - `novapolis-agent/`
  - `novapolis-sim/`
  - `novapolis-rp/`

## Scope & Repos

Der Dev Hub verknüpft die Arbeitsstände aus `novapolis-agent/`, `novapolis-sim/` und `novapolis-rp/`. Alle teamweiten Policies, Planungen und Integrationen landen zentral hier und werden von dort aus in die Produktiv-Repositories gespiegelt.

## Primary Docs

- `docs/donelog.md` – tägliche Fortschritte und Beschlüsse
- `docs/todo.md` – offene Aufgaben, Follow-ups und Prioritäten
- `docs/copilot-behavior.md` – Arbeitsweise, Stil, Sicherheitsleitplanken
- `docs/naming-policy.md` – verbindliche Dateibenennung im Verbund
- `docs/tests.md` – Testabdeckung und Sim-/Client-Checkliste

## Contributor Workflow

- Änderungen zuerst hier dokumentieren, anschließend in den Ziel-Repos umsetzen.
- Fortschritt stets in `docs/donelog.md` loggen, Aufgaben in `docs/todo.md` pflegen.
- Vor Commits die Leitlinien aus `docs/copilot-behavior.md` gegenprüfen.

## Struktur

- `docs/` – Arbeitsdokumente (ToDos, DoneLogs, Policies, Testpläne)
- `docs/meta/` – Metadaten zu den Arbeitsdokumenten
- `migrations/` – Änderungs- und Umzugshistorie
- `roadmaps/` – Langfristige Planungen (Platzhalter)
- `integrations/` – Schnittstellen- und Abstimmungsdokumente (Platzhalter)
- `raw/`, `curated/` – optionale lokale Skizzen; produktive Datenpools liegen unter `../novapolis-rp/database-*`

Bitte dokumentiert neue Arbeitsstände ausschließlich hier und verweist in den Produktiv-Repositories auf dieses Hub.
