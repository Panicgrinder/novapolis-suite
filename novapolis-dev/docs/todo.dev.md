---
stand: 2026-06-19 15:26
update: Phase 3 ist abgeschlossen: Die Root-Governance ist minimal auf KI-operative Framework-Semantik und die Phase-2-Abgrenzung synchronisiert. Phase 4 (Read-only-Audit der VS-Code-Settings) abgeschlossen: kein Drift; keine Settings-Mutation erforderlich.
checks: snapshot-lock PASS (2026-06-13 21:52); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc novapolis-dev/docs/todo.dev.md PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-dev/docs/todo.dev.md PASS (EXITCODE=0); .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . PASS
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument bündelt Aufgaben für das Dev-Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent-board.md`.
- Vollständig erledigte Blöcke werden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben.

Offene Aufgaben (Dev)
---------------------

- Aktuell offene Dev-Aufgaben: `4` (Quelle: `novapolis-dev/docs/todo.index.md`, Board-Metadaten).

- [ ] [Jetzt] GOV-STRANG-04: Phase-5-Verifikation vom Vertragsstand auf technische Runtime-Projektion heben.
  - Ziel: Der bestehende Governance-Plan führt nicht nur Soll-Regeln, sondern belegte technische Ausleitung für mini-first, Codex-Eskalation, Hook-Budget und Nachweisfluss.
  - Akzeptanzkriterien:
    1) für die offenen Phase-5-Punkte liegen explizite technische Zielpfade vor,
    2) die Ausleitung bleibt konsistent zu `.github/copilot-instructions.md` und `.github/agents/novapolis-workspace-navigator.agent.md`,
    3) kein stiller Scope-Sprung in RP-/Sim-Fachdaten.
  - Evidenz: `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`, `.github/agents/novapolis-workspace-navigator.agent.md`.

- [ ] [Jetzt] GOV-STRANG-05: Hook-Ereignislogging als laufende Evidenzschiene standardisieren.
  - Ziel: Hook-Entscheidungen (`allow/ask/deny`) werden für Governance-Audits reproduzierbar als Dev-Evidenz lesbar.
  - Akzeptanzkriterien:
    1) Loggingpfad und Pflichtfelder sind festgezogen,
    2) Nachweise lassen sich in Dev-DONELOG und Auditläufen referenzieren,
    3) keine Kollision mit bestehender Hook-/Pre-Commit-Logik.
  - Evidenz: `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `.github/hooks/rp-runtime-loop-guard.json`, `scripts/rp_runtime_loop_guard.py`.

- [ ] [Als nächstes] GOV-STRANG-06: Board-/Status-Freshness zwischen Root, Modulboards, Index und DONELOG harmonisieren.
  - Ziel: Aktive Flächen führen keinen divergierenden Check-/Freshness-Stand.
  - Akzeptanzkriterien:
    1) Root- und Modulboards verweisen auf denselben gültigen Laufstand,
    2) `novapolis-dev/docs/todo.index.md` bleibt synchron,
    3) stale Claims werden explizit nachgezogen statt implizit toleriert.
  - Evidenz: `todo.root.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/todo.agent-board.md`, `novapolis-dev/docs/todo.rp.md`, `novapolis-dev/docs/todo.sim.md`.

- [ ] [Als nächstes] GOV-STRANG-07: Mini-Lamas-Architekturvertrag auf Runtime-/Governance-Schnitt und Validierungsstand konsolidieren.
  - Ziel: Die Mini-Lamas-SSOT bleibt als Architekturquelle aktiv, aber ihre Ausführungskette und ihr Validierungsstatus sind gegen Root-/Dev-Governance eindeutig gespiegelt.
  - Akzeptanzkriterien:
    1) Rollenabgrenzung kollidiert nicht mit mini-first/Codex-Policy,
    2) offene Validierungs-/Projektionsthemen sind als klare Folgearbeit markiert,
    3) keine Umwandlung in Instructions ohne belegten Bedarf.
  - Evidenz: `novapolis-dev/docs/process/mini-lamas-architecture.ssot.md`, `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`.

Geplanter, mehrstufiger Umsetzungsplan (Kurzfassung)
---------------------------------------------------

- Phase 0 — Baseline + VS-Code-Governance-Surface + Hook-Audit (Evidenzaufnahme)
  - Aufgabe: Reproduzierbare Ist-Aufnahme erstellen: geladene Instructions/Agents/Hooks/Prompt-Files, `chat`-Settings, Hook-Logs, aktuelle TODO/DONELOG-Einträge.
  - Akzeptanzkriterium: Startbefund enthält Prioritätenpfad (Always-on Instructions -> scoped Instructions -> Agents/Hooks/Prompts/MCP -> Workspace/User/Org-Settings) und Hook-Risikoampel.
  - Status: Abgeschlossen (2026-06-13 09:57).
  - Evidenz: `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `.github/agents/*.agent.md`, `.github/hooks/rp-runtime-loop-guard.json`, `scripts/rp_runtime_loop_guard.py`, `scripts/pre_commit.py`, `.vscode/settings.json`, `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `novapolis-dev/docs/todo.index.md`, `novapolis-dev/docs/donelog.md`.

- Phase 1 — Zielvertrag (Dev-SSOT) präzisieren
  - Aufgabe: Soll-Vertrag in `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` auf AI-Credits-Logik und Mini-first-Eskalation schärfen.
  - Akzeptanzkriterium: Klarer Eskalationspfad (`GPT-5 mini` zuerst, `GPT-5.3-Codex` nur mit belegter Begründung und reviewbarem Handoff).
  - Status: Abgeschlossen (2026-06-13 10:51).
  - Evidenz: `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md` führt jetzt einen verbindlichen Phase-1-Zielvertrag mit Mini-first-Pflicht, Eskalationskriterien, Handoff-Standard (`send:false`) und Rückführungspflicht in den Mini-Flow.

- Phase 2 — Logging-Wächter härten (Agent-Datei)
  - Aufgabe: `.github/agents/novapolis-workspace-navigator.agent.md` konkretisieren (`mini-first.required`, `codex-handoff.requires`, `diagnostics.level`, `hook-budget-guard`).
  - Akzeptanzkriterium: Keine widersprüchlichen Modell-/Handoff-Regeln mehr zwischen Dev-SSOT, Agent-Datei und Root-Governance.
  - Status: Abgeschlossen als Agent-Policy-Schicht (2026-06-13 11:25).
  - Evidenz: `.github/agents/novapolis-workspace-navigator.agent.md` führt die normativen Policy-Felder im Agent-Body.
  - Abgrenzung: Noch nicht abgeschlossen ist die technische Enforcement-Integration (keine automatische VS-Code-Frontmatter-Auswertung, keine Runtime-Hook-Enforcement-Implementierung in diesem Schritt).

- Phase 3 — Root-Governance synchronisieren
  - Aufgabe: Nur notwendige Klarstellungen in `.github/copilot-instructions.md` vornehmen; keine Scope-Ausweitung.
  - Akzeptanzkriterium: Root-Regeln bleiben minimal, aber deckungsgleich zum gehärteten Agent- und Dev-Plan.
  - Status: Abgeschlossen (2026-06-13 13:23).
  - Evidenz: `.github/copilot-instructions.md` führt KI-operative Steuersemantik für aktive Normtexte und die Phase-2-Abgrenzung (Agent-Body normativ, keine automatische Frontmatter-/Runtime-Enforcement).

- Phase 4 — VS-Code-Settings (nur bei belegtem Drift)
  - Aufgabe: Settings ausschließlich dann nachziehen, wenn aus Phase 0 Drift-Reduktion belegbar wird.
  - Akzeptanzkriterium: Keine hostgebundenen Pfade in aktiven SSOT-/Policy-Texten; Settings-Änderungen sind direkt evidenzverknüpft.
  - Status: Abgeschlossen — Read‑only Settings‑Audit ergab keine notwendige Settings‑Mutation.
  - Evidenz: novapolis-dev/docs/donelog.md (DONELOG‑Eintrag, 2026-06-13 15:20).
  - Abgrenzung: Ergebnisnotiz; spätere Mutationen benötigen frischen Snapshot‑Lock, reguläre Checks und einen Eintrag in novapolis-dev/docs/donelog.md im selben Änderungslauf.

- Phase 5 — Konsistenz- und Verifikationslauf
  - Aufgabe: Vollständiger Konsistenzcheck: Agent-Dateien vs Root-SSOT vs Dev-SSOT vs TODO/DONELOG vs Settings vs Hook-Logs.
  - Akzeptanzkriterium: `markdownlint`, `check_frontmatter.py`, `check_todo_index_sync.py` und Full-Check-Report ohne Governance-Widerspruch.

- Phase 6 — Staged Rollout & Monitoring
  - Aufgabe: Rollout in kleinen Commits; nach jeder Phase: Lint, Frontmatter, TODO-Index-Sync, Snapshot-Lock und Postflight-Receipt in DONELOG.
  - Akzeptanzkriterium: Jede Mutation ist minimal, rückverfolgbar und im passenden DONELOG dokumentiert.

Sonstige Hinweise
-----------------

- Phase-0-Befund ist abgeschlossen; verbleibende Phasen bauen auf dem dokumentierten Prioritätenpfad und der Hook-Risikoampel auf.
- Hooks zuerst auditieren; Hooks sind die hauptkritische Credit‑Risikoquelle.
- Mini‑first ist Pflicht: breite Suche, Befund, Diff‑Review, Check‑Auswertung und Handoff‑Prompt werden zuerst mit `GPT-5 mini` erledigt.
- `send:true` nur mit ausdrücklicher Begründung; Handoffs standardmäßig `review`/`send:false`.
- Jede Änderung einzeln committen und mit Snapshot‑Lock/Freshness prüfen.

Abgeschlossene Einträge
-----------------------

- Alle abgeschlossenen Einträge wurden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben. Dort sind Kurzbeschreibungen, Evidenz‑Links und archived_at‑Timestamps abgelegt.

Hinweis zu Validatoren
----------------------

- Validatoren laufen im Governance-Pfad verpflichtend pro mutativem Lauf: `markdownlint`, `scripts/check_frontmatter.py`, `scripts/check_todo_index_sync.py` sowie bei Bedarf der Full-Check-Wrapper.

---
