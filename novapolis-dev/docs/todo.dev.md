---
stand: 2026-06-19 15:40
update: Der Governance-Umbau wird als Korrektur-Planlauf neu gefasst: vollstaendiger Problemraum statt kuenstlicher Nummernpakete, klare Rollenableitung und Trennung von Kernarbeit vs. technischer Folgearbeit.
checks: snapshot-lock PASS (2026-06-19 15:40); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc "**/*.md" PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-dev/docs/todo.dev.md PASS; .\.venv\Scripts\python.exe scripts\check_todo_index_sync.py --repo-root . PASS
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

- Aktuell offene Dev-Aufgaben: `6` (Quelle: `novapolis-dev/docs/todo.index.md`, Board-Metadaten).

- [ ] [Jetzt] Kettenregel verbindlich machen: Plantraeger vor Analyse und Mutation.
  - Ziel: Der Umbau folgt fuer mutative Laeufe einem festen Ablauf (Plantraeger zuerst), damit Board-/Index-/DONELOG-Sync kein Nachgedanke bleibt.
  - Akzeptanzkriterien:
    1) Plantraeger fuer Root/Dev/Agent/RP/Sim sind vor mutativen Schritten explizit referenziert,
    2) Startreihenfolge (Plan -> Analyse -> Mutation -> Sync) ist dokumentiert und in TODO/Index sichtbar,
    3) keine verdeckte Scope-Ausweitung in Fachmodule.
  - Evidenz: `.github/copilot-instructions.md`, `todo.root.md`, `novapolis-dev/docs/todo.index.md`.

- [ ] [Jetzt] Bootstrap-Regel fuer den ersten Governance-Umbau als explizite Leitplanke nachziehen.
  - Ziel: Der erste Umbau wird als Sonderfall sauber gefuehrt, damit keine bereits laufenden Folgearbeiten als Kernplan missverstanden werden.
  - Akzeptanzkriterien:
    1) Erstumbau-Regeln sind von regularem Betriebsmodus getrennt beschrieben,
    2) Kernarbeit und Folgearbeit sind als solche gekennzeichnet,
    3) Root/Index/Board fuehren denselben Bootstrap-Status.
  - Evidenz: `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`, `todo.root.md`, `novapolis-dev/docs/todo.index.md`.

- [ ] [Jetzt] Reportvertraege in `abschluss-routine.ssot.md` auf heutigen Arbeitsmodus aktualisieren.
  - Ziel: Workspace-Abschluss, Modulstatus, technischer Checkbericht und Postflight-Receipt sind als getrennte Berichtstypen verbindlich und verwechselungsfrei dokumentiert.
  - Akzeptanzkriterien:
    1) Berichtstypen sind klar getrennt und benannt,
    2) Zustaendigkeit je Berichtstyp ist festgezogen,
    3) Board-/Index-Claims verweisen nicht mehr auf fremde Berichtstypen.
  - Evidenz: `novapolis-dev/docs/process/abschluss-routine.ssot.md`, `WORKSPACE_STATUS.md`, `novapolis-dev/docs/donelog.md`, `DONELOG.md`.

- [ ] [Jetzt] `workspace-audit-segmente.ssot.md` fuer Scope-/Wiring-Audit aller aktiven Steuerflaechen nachziehen.
  - Ziel: Vollstaendiger Audit der aktiven Steuerflaechen, nicht nur Freshness, sondern Autoritaetsrolle, Verdrahtung und Delta-Routing.
  - Akzeptanzkriterien:
    1) alle aktiven Steuerflaechen sind mit Rolle/Autoritaet/Folgebezug erfasst,
    2) Delta-Routing- und Vertiefungsregeln sind als Arbeitsvertrag sichtbar,
    3) Schnittstellen zwischen Root/Dev/Agent/RP/Sim sind ohne Luecken markiert.
  - Evidenz: `novapolis-dev/docs/process/workspace-audit-segmente.ssot.md`, `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md`, `.github/agents/*.agent.md`.

- [ ] [Als naechstes] Semantische Verdrahtung von Index, Status und SSOT nach Autoritaetsrolle konsolidieren.
  - Ziel: Nicht nur zeitliche Freshness, sondern semantische Fuehrung (wer ist autoritativ fuer was) bleibt eindeutig.
  - Akzeptanzkriterien:
    1) `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md`, `todo.root.md` und Prozess-SSOTs fuehren keine konkurrierenden Autoritaetsaussagen,
    2) Modulstatus und Root-Querschnitt sind klar getrennt,
    3) Konflikte werden als STOP-/Klärpunkt markiert statt implizit ueberschrieben.
  - Evidenz: `novapolis-dev/docs/todo.index.md`, `WORKSPACE_STATUS.md`, `todo.root.md`, `novapolis-dev/docs/process/model-credits-optimization-plan.ssot.md`.

- [ ] [Als naechstes] Technische Folgearbeit: Hook-Ereignislogging als laufende Evidenzschiene standardisieren.
  - Ziel: Der technische Rest bleibt sichtbar, aber nachrangig hinter der strategischen Kernkorrektur.
  - Akzeptanzkriterien:
    1) Loggingpfad und Pflichtfelder sind festgezogen,
    2) Nachweise lassen sich in Dev-DONELOG und Auditlaeufen referenzieren,
    3) keine Kollision mit bestehender Hook-/Pre-Commit-Logik.
  - Evidenz: `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`, `.github/hooks/rp-runtime-loop-guard.json`, `scripts/rp_runtime_loop_guard.py`.

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
