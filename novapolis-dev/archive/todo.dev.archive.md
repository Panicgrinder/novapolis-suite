---
stand: 2026-02-21 08:08
update: Abgeschlossene Dev-Bloecke aus todo.root ueberfuehrt; Root-Backlog auf aktive Punkte reduziert.
checks: markdownlint-cli2 PASS; check_frontmatter.py PASS
---

TODO-Archiv - Dev
=================

Zweck: Vollständig abgeschlossene TODO-Abschnitte aus `novapolis-dev/docs/todo.md` aufnehmen.

Regeln (kurz)
- Nur vollständig abgehakte Abschnitte ([x] überall) verschieben.
- Inhalt nicht umformulieren; nur `archived_at: YYYY-MM-DD HH:MM` direkt unter der Abschnitts-Überschrift ergänzen.
- Headings in diesem Archiv: Setext (MD003 konform, H1/H2).
- Präsentation: Lint-Läufe mit PRESENTATION=SHARED.

Ablage
- Neueste Einträge oben einfügen.

<!-- Hier unterhalb neue, vollständig erledigte Blöcke einfügen (neu zuerst). -->

Dev-Folgepunkt (2026-02-22) - abgeschlossen
-------------------------------------------

archived_at: 2026-02-22 23:40

Quelle: `novapolis-dev/docs/todo.dev.md` (Block `Offene Aufgaben (Dev)`, Stand 2026-02-22 21:40).

- [x] Naechste Dev-Aufgabe erfasst und abgeschlossen.
	- Beschreibung: Doku-Gates fuer Markdownlint/Frontmatter auch auf Branch-Pushes ohne PR aktiv halten.
	- Ziel: fruehe Rueckmeldung bei Doku-Drift vor PR-Erstellung.
	- Pruefkriterium: `.github/workflows/markdownlint.yml` triggert auf `push` fuer alle Branches.

Root-Uebernahme: novapolis-dev Block aus todo.root
-------------------------------------------------

archived_at: 2026-02-21 04:52

Quelle: `todo.root.md` (Abschnitte `novapolis-dev`, `Multi-Root-STOP`).

- [x] Dev-Root-Aufgabenblock als abgeschlossen archiviert.
- [x] Multi-Root-STOP-Abschlussblock als abgeschlossen archiviert.
- [x] Aktiver Dev-Backlog bleibt unter `novapolis-dev/docs/todo.dev.md`.

DONELOG-Konsolidierung (Root + 4 Module)
----------------------------------------
archived_at: 2026-02-20 00:45

Quelle: `novapolis-dev/docs/todo.dev.md`

- [x] DONELOG-Konsolidierung aufsetzen (Root + 4 Module) mit Sortierung "neuester oben".
- [x] Zentrale Ziellogs unter `novapolis-dev/archive/docs/donelogs/` festlegen und anlegen (`donelog_root.md`, `donelog_agent.md`, `donelog_dev.md`, `donelog_rp.md`, `donelog_sim.md`).
- [x] Inventur/Mappings/Dedupe umgesetzt (via `scripts/consolidate_donelogs.py`).
- [x] Sortierung/Format vereinheitlicht (`timestamp | author | summary | source`, absteigend).
- [x] Stichprobe/Sortierungscheck PASS (alle 5 Ziellogs `sorted_desc=True`).
- [x] Frontmatter-Checks der 5 Ziellogs PASS.
- [x] Querverweise ergänzt (`novapolis-dev/archive/docs/donelogs/INDEX.md`, `novapolis-dev/docs/todo.index.md`).

Snapshot aus `novapolis-dev/docs/todo.dev.md` (vollständig grün)
---------------------------------------------------------------
archived_at: 2026-02-19 23:59

Quelle: `novapolis-dev/docs/todo.dev.md`

- [x] (Platzhalter) Sammle Dev-Aufgaben hier. Falls bisher in Root `todo.root.md` oder Agent-TODO gepflegt, bitte verschieben. (Housekeeping 2026-02-19: konkrete Dev-Aufgaben sind in diesem Board geführt; kein Sammel-Platzhalter mehr erforderlich)
- [x] MCP-Server-Prototyp vorbereiten (`novapolis-dev/integrations/`): Minimalen lokalen MCP-Server aufsetzen, Launch/Docs ergänzen, Verbindungstest mit Web-Client dokumentieren. (erledigt 2026-02-19: Launch + Task ergänzt, Health-Check `GET /health` = `{"status":"ok"}`)
- [x] Betriebsmodi „Standardlauf“/„Sicherheitsprotokoll“ konsolidieren (Prozess-Docs, Logging-Template, Anpassung Copilot-Instruktionen) (2025-11-03)
 - [x] Docs/READMEs: Hub-README erweitert (TL;DR, direkte Tool-Links, Beispiele); Stubs Phase 1 konsolidiert (2025-11-12 01:12)
 - [x] Redirect-/Index-Strategie finalisieren: Rolle `WORKSPACE_INDEX.md` definieren oder durch Hub-Verweis ersetzen; Duplikate vermeiden (Rolle dokumentiert: Agent-spezifischer Detailkatalog mit Hub-Verweis in `WORKSPACE_INDEX.md`, Abschnitt „Monorepo Redirect / Konsolidierung“)

Neue Aufgaben - Zeitmodell & TTS (2025-11-01 22:24)
---------------------------------------------------

- [x] Annotation-Spec (1 Seite) anlegen: Knowledge-Schema (Quelle/Kanal/Confidence/Freshness/Visibility), Action-Schema (base_duration/locks/interruptible/may_trigger_event), Skill-Ableitung aus Verhaltensmatrix (Formel + Beispiel-Gewichte). (erledigt; siehe Spec)
	- [x] Ablagevorschlag: `novapolis-dev/docs/specs/annotation-spec.md` (YAML-Snippets inklusive).
	- [x] Link: Siehe `novapolis-dev/docs/specs/annotation-spec.md`.
- [x] Scheduler-Spec (tick-los, Min-Heap): Mikro-Turns innerhalb 1-h-Epochen (Hybrid-Modell) - Inputs/Outputs/Fehlerpfade + 3 Beispielaktionen. (erledigt; siehe Spec)
	- [x] Link: Siehe `novapolis-dev/docs/specs/scheduler-spec.md`.
- [x] TTS-Tooling (Build-Time): VS Code Task-Entwurf „TTS: export (Coqui→OGG)“ ohne Code - nur Task-Skelett/README notieren; eigentliche Implementierung folgt im Agent/Tools. (erledigt: Task-Skelett + Spec vorhanden)
	- [x] Link: Siehe `novapolis-dev/docs/specs/tts-exporter-coqui.md`.
- [x] Templates: Minimal-YAML-Snippets für `knowledge:` und `actions:` bereitstellen (Copy/Paste in Canvases). (erledigt in `annotation-spec.md`)

Bereinigung Alt-TODOs (nur SSOT behalten)
-----------------------------------------

- [x] Kandidatenliste prüfen und löschen, sobald alle Referenzen entfernt sind: (erledigt 2026-02-19; alle 4 Kandidat-Dateien fehlen bereits, aktive TODO-Verweise bereinigt; verbleibende Erwähnungen nur in Historie/Migrations-/Eval-Artefakten)
	- Root-Redirect: `TODO.md` (verweist auf `todo.root.md`)
	- Agent-Redirect: `novapolis_agent/docs/TODO.md` (verweist auf `novapolis-dev/docs/todo.agent-board.md`)
	- Historischer Redirect: `novapolis-dev/docs/todo.md` (verweist auf `docs/todo.index.md`)
	- Mirror/Stub: `novapolis-rp/Main/novapolis-dev/docs/todo.md` (Redirect-Stub, Mirror-Policy beachten)


