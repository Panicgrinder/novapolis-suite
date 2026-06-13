---
stand: 2026-06-13 09:03
update: Das Dev-Board fuehrt jetzt die Mini-first-Regel: GPT-5 mini muss die credits-effiziente Vorarbeit maximal leisten, bevor ein reviewbarer GPT-5.3-Codex-Handoff angeboten wird.
checks: snapshot-lock PASS (2026-06-13 07:10); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc changed-dev-md PASS (2026-06-13 07:08); C:/Users/FloAu/AppData/Local/Programs/Python/Python313/python.exe scripts/check_frontmatter.py changed-dev-md PASS (EXITCODE=0, 2026-06-13 07:08); C:/Users/FloAu/AppData/Local/Programs/Python/Python313/python.exe scripts/check_todo_index_sync.py PASS (2026-06-13 07:08).
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument buendelt Aufgaben fuer das Dev-Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Vollstaendig erledigte Bloecke werden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben.

- Hinweis 2026-06-13 07:14: Fuenf abgeschlossene Dev‑Eintraege (CPU‑Schonmodus, Sim Export Smoke, Sim Headless Verify, Sim Hub‑Prefs Contract, Training Release Gate) wurden validiert und in `novapolis-dev/archive/todo.dev.archive.md` verschoben.


Offene Aufgaben (Dev)
---------------------

- Derzeit sind keine als erledigt markierten Eintraege im Board. Offene Tasks werden im zentralen Index und in Modul-Boards gehalten: siehe `novapolis-dev/docs/todo.index.md`.

- Wenn du möchtest, kann ich die offenen Einträge aus `todo.index.md` hier eintragen oder priorisiert nachtragen. Sag mir kurz, wie du die Darstellung bevorzugst (kompakt / nach Priorität / nach Modul).

Geplanter, mehrstufiger Umsetzungsplan (Kurzfassung)
--------------------------------------------------

- Phase 0 — Baseline, Hook-Risiko & Befund (Evidenzaufnahme)
  - Aufgabe: Reproduzierbare Ist-Aufnahme erstellen: geladene Instructions/Agents/Hooks/Prompt-Files, `chat`-Settings, Hook-Logs, aktuelle TODO/DONELOG-Eintraege.

- Phase 1 — Zielvertrag (Dev-SSOT)
  - Aufgabe: Soll-Vertrag in `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` erweitern (Mini-first, Modell-Eskalation, Handoff-Policy).

- Phase 2 — Logging-Wächter härten (Agent-Datei)
  - Aufgabe: `.github/agents/novapolis-workspace-navigator.agent.md` konkretisieren (mini-first.required, codex-handoff.requires, diagnostics.level).

- Phase 3 — Root-Governance synchronisieren
  - Aufgabe: Nur notwendige Klarstellungen in `.github/copilot-instructions.md` vornehmen; keine Scope‑Ausweitung.

- Phase 4 — VS-Code-Settings (optional)
  - Aufgabe: Optionales Hinzufuegen von Settings, falls Drift reduziert wird.

- Phase 5 — Hooks auditieren
  - Aufgabe: Hook-Risiken pruefen und ggf. minimal patchen.

- Phase 6 — Konsistenz- und Verifikationslauf
  - Aufgabe: Vollständiger Konsistenzcheck: Agent-Dateien vs Root-SSOT vs Dev-SSOT vs TODO/DONELOG vs Settings vs Hook-Logs.

- Phase 7 — Staged Rollout & Monitoring
  - Aufgabe: Rollout in kleinen Commits; nach jeder Phase: Lint, Frontmatter, TODO-Index-Sync, Snapshot-Lock und Postflight-Receipt in DONELOG.

Sonstige Hinweise
-----------------

- Hooks zuerst auditieren; Hooks sind die hauptkritische Credit‑Risikoquelle.
- Mini‑first ist Pflicht: breite Suche, Befund, Planung, Diff‑Review, Check‑Auswertung und Handoff‑Prompt werden zuerst mit `GPT-5 mini` erledigt.
- `send:true` nur mit ausdruecklicher Begruendung; Handoffs standardmaessig `review`/`send:false`.
- Jede Aenderung einzeln committen und mit Snapshot‑Lock/Freshness pruefen.

Abgeschlossene Eintraege
------------------------

- Alle abgeschlossenen Einträge wurden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben. Dort sind Kurzbeschreibungen, Evidenz‑Links und archived_at‑Timestamps abgelegt.

Hinweis zu Validatoren
----------------------

- Post‑archive Validatoren (`markdownlint` und `scripts/check_frontmatter.py`) wurden auf Wunsch deferred und sind nicht automatisch ausgeführt. Soll ich sie jetzt laufen lassen und bei grün die Änderungen committen und pushen?
