---
stand: 2026-06-13 15:20
update: Phase 3 ist abgeschlossen: Die Root-Governance ist minimal auf KI-operative Framework-Semantik und die Phase-2-Abgrenzung synchronisiert. Phase 4 (Read-only-Audit der VS-Code-Settings) abgeschlossen: kein Drift; keine Settings-Mutation erforderlich.
checks: snapshot-lock PASS (2026-06-13 15:20); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc novapolis-dev/docs/todo.dev.md PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-dev/docs/todo.dev.md PASS (EXITCODE=0); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . PASS
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

- Aktuell offene Dev-Aufgaben: `0` (Quelle: `novapolis-dev/docs/todo.index.md`, Board-Metadaten).
- Dieses Board fuehrt damit derzeit keine operativen Checkbox-Tasks, sondern den freigegebenen Governance-Umsetzungsplan als Startgrundlage fuer den naechsten mutativen Lauf.

Geplanter, mehrstufiger Umsetzungsplan (Kurzfassung)
--------------------------------------------------

- Phase 0 — Baseline + VS-Code-Governance-Surface + Hook-Audit (Evidenzaufnahme)
  - Aufgabe: Reproduzierbare Ist-Aufnahme erstellen: geladene Instructions/Agents/Hooks/Prompt-Files, `chat`-Settings, Hook-Logs, aktuelle TODO/DONELOG-Eintraege.
  - Akzeptanzkriterium: Startbefund enthaelt Prioritaetenpfad (Always-on Instructions -> scoped Instructions -> Agents/Hooks/Prompts/MCP -> Workspace/User/Org-Settings) und Hook-Risikoampel.
  - Status: Abgeschlossen (2026-06-13 09:57).
  - Evidenz: `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `.github/agents/*.agent.md`, `.github/hooks/rp-runtime-loop-guard.json`, `scripts/rp_runtime_loop_guard.py`, `scripts/pre_commit.py`, `.vscode/settings.json`, `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/donelog.md`.

- Phase 1 — Zielvertrag (Dev-SSOT) praezisieren
  - Aufgabe: Soll-Vertrag in `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` auf AI-Credits-Logik und Mini-first-Eskalation schaerfen.
  - Akzeptanzkriterium: Klarer Eskalationspfad (`GPT-5 mini` zuerst, `GPT-5.3-Codex` nur mit belegter Begruendung und reviewbarem Handoff).
  - Status: Abgeschlossen (2026-06-13 10:51).
  - Evidenz: `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` fuehrt jetzt einen verbindlichen Phase-1-Zielvertrag mit Mini-first-Pflicht, Eskalationskriterien, Handoff-Standard (`send:false`) und Rueckfuehrungspflicht in den Mini-Flow.

- Phase 2 — Logging-Waechter haerten (Agent-Datei)
  - Aufgabe: `.github/agents/novapolis-workspace-navigator.agent.md` konkretisieren (`mini-first.required`, `codex-handoff.requires`, `diagnostics.level`, `hook-budget-guard`).
  - Akzeptanzkriterium: Keine widerspruechlichen Modell-/Handoff-Regeln mehr zwischen Dev-SSOT, Agent-Datei und Root-Governance.
  - Status: Abgeschlossen als Agent-Policy-Schicht (2026-06-13 11:25).
  - Evidenz: `.github/agents/novapolis-workspace-navigator.agent.md` fuehrt die normativen Policy-Felder im Agent-Body.
  - Abgrenzung: Noch nicht abgeschlossen ist die technische Enforcement-Integration (keine automatische VS-Code-Frontmatter-Auswertung, keine Runtime-Hook-Enforcement-Implementierung in diesem Schritt).

- Phase 3 — Root-Governance synchronisieren
  - Aufgabe: Nur notwendige Klarstellungen in `.github/copilot-instructions.md` vornehmen; keine Scope-Ausweitung.
  - Akzeptanzkriterium: Root-Regeln bleiben minimal, aber deckungsgleich zum gehaerteten Agent- und Dev-Plan.
  - Status: Abgeschlossen (2026-06-13 13:23).
  - Evidenz: `.github/copilot-instructions.md` fuehrt KI-operative Steuersemantik fuer aktive Normtexte und die Phase-2-Abgrenzung (Agent-Body normativ, keine automatische Frontmatter-/Runtime-Enforcement).

- Phase 4 — VS-Code-Settings (nur bei belegtem Drift)
  - Aufgabe: Settings ausschliesslich dann nachziehen, wenn aus Phase 0 Drift-Reduktion belegbar wird.
  - Akzeptanzkriterium: Keine hostgebundenen Pfade in aktiven SSOT-/Policy-Texten; Settings-Aenderungen sind direkt evidenzverknuepft.

- Phase 5 — Konsistenz- und Verifikationslauf
  - Aufgabe: Vollstaendiger Konsistenzcheck: Agent-Dateien vs Root-SSOT vs Dev-SSOT vs TODO/DONELOG vs Settings vs Hook-Logs.
  - Akzeptanzkriterium: `markdownlint`, `check_frontmatter.py`, `check_todo_index_sync.py` und Full-Check-Report ohne Governance-Widerspruch.

- Phase 6 — Staged Rollout & Monitoring
  - Aufgabe: Rollout in kleinen Commits; nach jeder Phase: Lint, Frontmatter, TODO-Index-Sync, Snapshot-Lock und Postflight-Receipt in DONELOG.
  - Akzeptanzkriterium: Jede Mutation ist minimal, rueckverfolgbar und im passenden DONELOG dokumentiert.

Sonstige Hinweise
-----------------

- Phase-0-Befund ist abgeschlossen; verbleibende Phasen bauen auf dem dokumentierten Prioritaetenpfad und der Hook-Risikoampel auf.
- Hooks zuerst auditieren; Hooks sind die hauptkritische Credit‑Risikoquelle.
- Mini‑first ist Pflicht: breite Suche, Befund, Planung, Diff‑Review, Check‑Auswertung und Handoff‑Prompt werden zuerst mit `GPT-5 mini` erledigt.
- `send:true` nur mit ausdruecklicher Begruendung; Handoffs standardmaessig `review`/`send:false`.
- Jede Aenderung einzeln committen und mit Snapshot‑Lock/Freshness pruefen.

Abgeschlossene Eintraege
------------------------

- Alle abgeschlossenen Einträge wurden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben. Dort sind Kurzbeschreibungen, Evidenz‑Links und archived_at‑Timestamps abgelegt.

Hinweis zu Validatoren
----------------------

- Validatoren laufen im Governance-Pfad verpflichtend pro mutativem Lauf: `markdownlint`, `scripts/check_frontmatter.py`, `scripts/check_todo_index_sync.py` sowie bei Bedarf der Full-Check-Wrapper.
