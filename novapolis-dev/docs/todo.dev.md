---
stand: 2025-11-12 01:17
update: Docs-Hub Ergänzungen vermerkt; Redirect-/Index-Aufgabe ergänzt
checks: keine
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument bündelt Aufgaben für das Dev‑Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP‑Aufgaben liegen in `docs/todo.rp.md`. Agent‑Aufgaben liegen in `docs/todo.agent.md`.
- Archivierte, vollständig erledigte Abschnitte (H2/H3, alle [x]) bitte manuell nach `novapolis-dev/archive/todo.dev.archive.md` verschieben (neuester oben), mit `archived_at: YYYY-MM-DD HH:MM` unter der Abschnittsüberschrift.

Offene Aufgaben (Dev)
---------------------

- [ ] (Platzhalter) Sammle Dev‑Aufgaben hier. Falls bisher in Root `todo.root.md` oder Agent‑TODO gepflegt, bitte verschieben.
- [ ] MCP-Server-Prototyp vorbereiten (`novapolis-dev/integrations/`): Minimalen lokalen MCP-Server aufsetzen, Launch/Docs ergänzen, Verbindungstest mit Web-Client dokumentieren.
- [x] Betriebsmodi „Standardlauf“/„Sicherheitsprotokoll“ konsolidieren (Prozess-Docs, Logging-Template, Anpassung Copilot-Instruktionen) (2025-11-03)
 - [x] Docs/READMEs: Hub-README erweitert (TL;DR, direkte Tool-Links, Beispiele); Stubs Phase 1 konsolidiert (2025-11-12 01:12)
 - [ ] Redirect-/Index-Strategie finalisieren: Rolle `WORKSPACE_INDEX.md` definieren oder durch Hub‑Verweis ersetzen; Duplikate vermeiden

Neue Aufgaben – Zeitmodell & TTS (2025-11-01 22:24)
---------------------------------------------------

- [ ] Annotation‑Spec (1 Seite) anlegen: Knowledge‑Schema (Quelle/Kanal/Confidence/Freshness/Visibility), Action‑Schema (base_duration/locks/interruptible/may_trigger_event), Skill‑Ableitung aus Verhaltensmatrix (Formel + Beispiel‑Gewichte).
  - [ ] Ablagevorschlag: `novapolis-dev/docs/specs/annotation-spec.md` (YAML‑Snippets inklusive).
  - [ ] Link: Siehe `novapolis-dev/docs/specs/annotation-spec.md`.
- [ ] Scheduler‑Spec (tick‑los, Min‑Heap): Mikro‑Turns innerhalb 1‑h‑Epochen (Hybrid‑Modell) – Inputs/Outputs/Fehlerpfade + 3 Beispielaktionen.
  - [ ] Link: Siehe `novapolis-dev/docs/specs/scheduler-spec.md`.
- [ ] TTS‑Tooling (Build‑Time): VS Code Task‑Entwurf „TTS: export (Coqui→OGG)“ ohne Code – nur Task‑Skelett/README notieren; eigentliche Implementierung folgt im Agent/Tools.
  - [ ] Link: Siehe `novapolis-dev/docs/specs/tts-exporter-coqui.md`.
- [ ] Templates: Minimal‑YAML‑Snippets für `knowledge:` und `actions:` bereitstellen (Copy/Paste in Canvases).

Bereinigung Alt‑TODOs (nur SSOT behalten)
-----------------------------------------

- [ ] Kandidatenliste prüfen und löschen, sobald alle Referenzen entfernt sind:
  - Root‑Redirect: `TODO.md` (verweist auf `todo.root.md`)
  - Agent‑Redirect: `novapolis_agent/docs/TODO.md` (verweist auf `novapolis-dev/docs/todo.agent.md`)
  - Historischer Redirect: `novapolis-dev/docs/todo.md` (verweist auf `docs/todo.index.md`)
  - Mirror/Stub: `novapolis-rp/Main/novapolis-dev/docs/todo.md` (Redirect‑Stub, Mirror‑Policy beachten)

Hinweise
--------

- SSOT‑Dateien bleiben: `novapolis-dev/docs/todo.{agent,dev,rp,sim}.md`, `todo.root.md`, `novapolis-dev/docs/todo.index.md` sowie die Archive unter `novapolis-dev/archive/`.
- Redirect/Mirror‑Stubs nach Freigabe entfernen; vorherige Suche nach eingehenden Links durchführen.

