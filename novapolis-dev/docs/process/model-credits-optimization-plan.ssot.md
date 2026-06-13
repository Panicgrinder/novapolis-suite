---
stand: 2026-06-13 11:22
update: Phase 1 ist als verbindlicher Zielvertrag nachgezogen: Mini-first-Pflicht, belegte Codex-Eskalation und reviewbarer Handoff sind jetzt explizit als Soll-Regeln dokumentiert.
checks: snapshot-lock PASS (2026-06-13 10:51); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc changed-phase1-docs PASS; .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-phase1-docs PASS (EXITCODE=0)
---

Model-Credits Optimization Plan (Dev SSOT)
==========================================

Ziel
----

- Governance- und Behavior-Dokumente so nachziehen, dass Modellwahl und Toolnutzung credits-effizient, reproduzierbar und minimalinvasiv erfolgen.
- Arbeitsannahme aus dem aktuellen Lauf: `GPT-5 mini` fuer schnelle Broad-Pass-Analyse, `GPT-5.3-Codex` fuer praezise Umsetzung und Abschlusslaeufe.
- Aktiver Kostenrahmen ist kuenftig AI-Credits-/Token-basiert, nicht primar `premium requests`-basiert.

Phase-1-Zielvertrag (verbindlich)
---------------------------------

- Standardmodell fuer Governance-Arbeit ist `GPT-5 mini`.
- `GPT-5.3-Codex` ist nur als begruendete Eskalation zulaessig und darf nicht als Standard oder Default laufen.
- Vor jeder Codex-Eskalation ist belegte Mini-Ausschoepfung Pflicht: Befund, fokussierte Suche, Patch-Plan, Diff-Review und Check-Auswertung wurden mit `GPT-5 mini` bereits versucht.
- Zulaessige Eskalationsgruende sind nur qualitaetskritische Engstellen, die mit Mini nicht robust loesbar waren (z. B. komplexe Mehrdatei-Mutation mit hoher Regelintegration, wiederholte fehlgeschlagene Mini-Patchzyklen, unaufgeloeste Widersprueche trotz Mini-Befund).
- Nicht zulaessige Gruende fuer Codex: reine Routine-Doku-Edits, pauschales "zur Sicherheit", unpraezise Komforteskalation oder fehlende Mini-Vorarbeit.
- Handoff-Policy: Standard ist reviewbar (`send:false` bzw. kein Auto-Submit). `send:true` ist Ausnahmefall und braucht explizite Begruendung im Lauf.
- Jeder Codex-Handoff muss einen kompakten Nachweisblock enthalten: Scope, Mini-Befund, Eskalationsgrund, erwartetes Ergebnis, Rueckfuehrung in den Mini-Flow nach Umsetzung.
- Rueckfuehrungspflicht: Nach Codex-Ausfuehrung werden Validatoren, Board/Index/DONELOG-Sync und Abschlussbericht wieder im regulaeren Mini-Flow abgeschlossen.

Scope
-----

- In Scope: Governance-/Behavior-Leittexte, die Agent-Verhalten, Modellwahl, Kontextumfang und Tool-Intensitaet steuern.
- Out of Scope: Fachliche RP-/Sim-Inhalte ohne direkten Bezug zur Modell-/Credits-Policy.

Erfasste betroffene Dateien (Initial)
-------------------------------------

- `.github/agents/novapolis-workspace-navigator.agent.md`
- `.github/agents/novapolis-rp-szenenlabor.agent.md`
- `.github/copilot-instructions.md`
- `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md`
- `novapolis-dev/docs/copilot-vscode-usage.md`
- `novapolis-dev/docs/todo.dev.md`
- `novapolis-dev/docs/todo.index.md`
- `novapolis-dev/docs/donelog.md`

Belastbare Grundannahmen (Stand 2026-06-13)
-------------------------------------------

- GitHub Copilot rechnet im aktuellen Modell ueber AI Credits auf Basis von Input-, Output- und Cached Tokens sowie Modellpreis ab.
- `premium requests` und Modell-Multiplikatoren sind fuer Legacy-Jahresplaene weiter dokumentiert, aber nicht der primaere operative Kostenrahmen fuer neue Governance-Entscheidungen.
- VS Code steuert Governance nicht nur ueber `.github/copilot-instructions.md`, sondern ueber eine kombinierte Customization-Surface aus Always-on Instructions, scoped `*.instructions.md`, Custom Agents, Hooks, Prompt Files, MCP-Servern und Workspace-/User-/Org-Einstellungen.
- Der Logging-Waechter ist damit die operative Orchestrierungsinstanz: Credits-Effizienz ist nicht sauber umgesetzt, solange er keine explizite Modell-, Handoff-, Hook- und Kontextbudget-Strategie fuehrt.
- Deutsch bleibt als Arbeitssprache sinnvoll; der primaere Kostentreiber ist nicht "Uebersetzung", sondern Tokenmenge, Kontextgroesse, Reasoning-Level, Modellwahl und Wiederholungsdiagnostik.

Rollout-Phasen
--------------

1. Phase 0 - VS-Code-Governance-Surface absichern (abgeschlossen)

- Vor eigentlichem Policy-Umbau die aktive VS-Code-Customization-Surface explizit als Datensatz pflegen: Instructions, Agents, Hooks, Prompt Files, MCP, relevante Settings und Prioritaeten.
- Sicherstellen, dass kuenftige Governance-Arbeit nicht nur auf Repo-SSOT, sondern auf tatsaechlicher VS-Code-Lade- und Orchestrierungslogik basiert.
- Ergebnisstand: Prioritaetenpfad und Hook-Risikoampel sind in `novapolis-dev/docs/process/vscode-agent-governance-surface.ssot.md` dokumentiert.

2. Phase 1 - Zielvertrag (Dev-SSOT) praezisieren (abgeschlossen)

- Credits-Effizienz als explizite Leitplanke in Agent- und Guidance-Texten einfuegen.
- Modell-Eskalation klar benoeten: erst `GPT-5 mini`, bei Komplexitaet/Qualitaetsbedarf auf `GPT-5.3-Codex`.
- Logging-Waechter explizit als Orchestrator benennen: STOP, Handoffs, Kontextbegrenzung, Modellwechsel und Validierungslast werden dort gesteuert.
- Ergebnisstand: Mini-first-Pflicht, Codex-Eskalationskriterien und reviewbare Handoff-Policy sind in dieser SSOT als Soll-Vertrag verankert.

3. Phase 2 - Logging-Waechter haerten

- Toolcall-Budget und Kontext-Budget als feste Guardrails dokumentieren.
- Vollscans nur bei Evidenzbedarf; sonst fokussierte Suchpfade.
- Handoffs standardmaessig reviewbar statt automatisch sendend halten; `send: true` nur mit ausdruecklicher Begruendung.
- Hooks darauf pruefen, ob sie unnoetige Zusatzturns erzeugen oder `Stop`-Schleifen mit weiteren AI-Credit-Kosten verursachen koennen.

4. Phase 3 - Root-Governance synchronisieren

5. Phase 4 - VS-Code-Settings nur bei belegtem Drift

6. Phase 5 - Verifikation

7. Phase 6 - Staged Rollout und Monitoring

- Konsistenzcheck zwischen Agent-Dateien, Root-Governance und Dev-Guidance.
- Konsistenzcheck gegen VS-Code-Customization-Surface: keine impliziten Konflikte zwischen Repo-SSOT, Agent-Frontmatter, Hooks und Workspace-Settings.
- Doku-Sync in `todo.dev.md`, `todo.index.md` und `novapolis-dev/docs/donelog.md`.

Akzeptanzkriterien
------------------

- Credits- und Modellstrategie ist in allen betroffenen Leitdokumenten konsistent.
- VS-Code-spezifische Governance-Flaechen und Prioritaeten sind in einer eigenen Dev-SSOT dokumentiert und werden nicht still vorausgesetzt.
- Keine widerspruechlichen Modell-Empfehlungen zwischen Agent-Mode und Guidance.
- Keine Rueckfaelle auf Legacy-Annahmen wie `premium requests` als Primaerlogik oder `workspaceInstructions` als alleinigen Governance-Anker.
- Aenderungen bleiben minimal und klar nachvollziehbar geloggt.

Phase-1-Abnahmekriterien (spezifisch)
-------------------------------------

- Der Soll-Vertrag nennt `GPT-5 mini` explizit als Pflicht-Startmodell fuer Governance-Arbeit.
- Der Soll-Vertrag nennt klare Muss-Kriterien fuer zulaessige `GPT-5.3-Codex`-Eskalation und verbietet Komfort-Eskalation.
- Der Soll-Vertrag setzt reviewbaren Handoff als Standard und `send:true` als begruendungspflichtige Ausnahme.
- Der Soll-Vertrag verankert die Rueckfuehrung in den Mini-Flow inklusive Pflicht-Validatoren und Doku-Sync.
