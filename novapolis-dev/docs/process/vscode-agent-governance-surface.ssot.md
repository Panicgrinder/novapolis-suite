---
stand: 2026-06-13 06:28
update: VS-Code-Customization-Surface, Credits-Hebel und lokale Governance-Anker sind als eigener Datensatz dokumentiert.
checks: snapshot-lock PASS (2026-06-13 06:28); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc changed-dev-md PASS (2026-06-13 06:24); .\.venv\Scripts\python.exe scripts\check_frontmatter.py changed-dev-md PASS (EXITCODE=0, 2026-06-13 06:24).
---

VS Code Agent Governance Surface (Dev SSOT)
===========================================

Zweck
-----

- Diese SSOT haelt fest, wie VS Code Insiders die aktive Copilot-/Agent-Governance tatsaechlich einbindet.
- Ziel ist Maschinenlesbarkeit und Aktualitaet: spaetere Umbauten der Repo-Governance sollen auf belastbaren Editor-Fakten statt auf alten Copilot-Annahmen beruhen.

Belastbare externe Kernbefunde
------------------------------

- VS Code behandelt `custom instructions`, `custom agents`, `prompt files`, `agent skills`, `hooks`, `language models` und `MCP servers` als getrennte Customization-Typen.
- `.github/copilot-instructions.md` ist eine Always-on-Instruction-Datei und wird automatisch auf alle Chat-Requests im Workspace angewendet.
- `*.instructions.md` unter `.github/instructions/` werden datei- oder aufgabenbezogen geladen; mehrere Dateien werden kombiniert, eine feste Reihenfolge ist nicht garantiert.
- `AGENTS.md` ist ein zusaetzlicher Always-on-Mechanismus, aber optional; mehrere `AGENTS.md` in Unterordnern sind experimentell.
- `.agent.md`-Dateien unter `.github/agents/` definieren benannte Custom Agents mit eigenen Tools, Modellen, Handoffs und optionalen agent-scoped Hooks.
- VS Code-Hooks koennen deterministisch vor/nach Toolnutzung, bei Subagent-Starts/-Stops und beim Session-Stop eingreifen; sie sind damit ein eigener Governance-Hebel statt nur ein Doku-Thema.
- GitHub Copilot rechnet im neuen Modell ueber AI Credits ab; Kosten haengen an Input-, Output- und Cached Tokens sowie am gewaelten Modell. `premium requests` und Modell-Multiplikatoren sind fuer alte Legacy-Jahresplaene dokumentiert, aber nicht die aktuelle Primarlogik.

Lokale aktive Governance-Flaechen
---------------------------------

- Always-on Repo-Instruction: `.github/copilot-instructions.md`
- File-based Instructions: `.github/instructions/*.instructions.md`
- Workspace-Custom-Agents: `.github/agents/*.agent.md`
- Workspace-Hooks: `.github/hooks/*.json`
- Workspace-Settings-Anker: `.vscode/settings.json`

Lokale Settings-Lage
--------------------

- In `.vscode/settings.json` ist `github.copilot.chat.workspaceInstructions` aktuell explizit auf `.github/copilot-instructions.md` gesetzt.
- Der Workspace nutzt derzeit keinen expliziten Block fuer `chat.instructionsFilesLocations`, `chat.agentFilesLocations`, `chat.promptFilesLocations` oder `chat.hookFilesLocations`; damit greifen primaer VS-Code-Defaults.
- `github.copilot.chat.codebase.enabled` ist aktiv; Codebase-Kontext ist damit verfuegbar und muss credits-seitig bewusst sparsam genutzt werden.

Aktive Prioritaeten und Konfliktquellen
---------------------------------------

- VS Code priorisiert bei mehreren Instruction-Quellen hoechstwahrscheinlich: User-/Personal-Instructions vor Repo-Instructions vor Organization-Instructions.
- Repo-intern bleibt fuer Novapolis die SSOT-Behauptung bestehen: `.github/copilot-instructions.md` ist der bindende Kern, scoped `.instructions.md` praezisieren innerhalb ihres `applyTo`-Scopes.
- Da VS Code mehrere passende Instructions kombiniert und keine feste Reihenfolge garantiert, duerfen aktive Runtime-Regeln nicht auf implizite Lade-Reihenfolge angewiesen sein.

Credits-relevante Hebel in VS Code
----------------------------------

- Always-on-Dateien vergroessern den Input-Kontext jeder Chat-Anfrage.
- Lange Agent-Dateien vergroessern den Kontext jedes Runs, sobald der Agent aktiv ist.
- Handoffs koennen weitere Modelllaeufe ausloesen; `send: true` ist credits-intensiver als `send: false`.
- Groessere Kontextfenster und hoehere Reasoning-Level verbrauchen mehr Tokens und damit mehr AI Credits.
- `Stop`-Hooks koennen einen Agenten am Beenden hindern; dadurch entstehen zusaetzliche Modellturns und weitere AI-Credit-Kosten.
- Das neue Billing belohnt deshalb kurze Always-on-Kerne, gezielte Scoped Rules, begrenzte Tool- und Kontextnutzung und bewusst gesetzte Handoffs.

Sprache und Credits
-------------------

- Es gibt keinen belastbaren Hinweis darauf, dass Deutsch als Sprache einen separaten Abrechnungsposten fuer "Uebersetzung" erzeugt.
- Belastbar ist nur: Abgerechnet werden Tokens. Mehr Kontext, laengere Antworten, hoeherer Reasoning-Level und teurere Modelle kosten mehr.
- Fuer Novapolis bleibt Deutsch sinnvoll, solange aktive Runtime-Dateien kurz, klar und maschinenlesbar bleiben; der primaere Kostentreiber ist nicht die Sprache selbst, sondern Textmenge und Modellwahl.

Folgerungen fuer den Logging-Waechter
-------------------------------------

- Der `Novapolis Workspace Navigator und Logging-Waechter` ist nicht nur eine betroffene Datei, sondern die operative Orchestrierungsinstanz fuer die Credits-Optimierung.
- Er muss kuenftig explizit steuern:
  - welche Pflichtdateien geladen werden,
  - wann STOP-Gates frueh greifen,
  - wann Handoffs sinnvoll sind,
  - wann statt Vollscan nur fokussierte Suche erlaubt ist,
  - wann ein teureres Modell begruendet eskaliert werden darf.
- Die Credits-Umstellung ist daher nicht vollstaendig, wenn nur Root-Governance und Guidance gekuerzt werden, aber der Logging-Waechter weiter breit und ohne Modell-/Handoff-Policy arbeitet.

Diagnostik-Pflichten fuer kuenftige Governance-Arbeit
-----------------------------------------------------

- Chat Diagnostics pruefen: welche Instructions, Agents, Prompts und Hooks wurden geladen?
- Hook-Logs pruefen: wurden `Load Hooks`, `PreToolUse`, `PostToolUse`, `SubagentStart` oder `Stop` wie erwartet ausgefuehrt?
- Bei Konflikten oder Drift immer explizit unterscheiden zwischen:
  - Repo-SSOT,
  - lokalen User-Instructions,
  - Organization-Instructions,
  - Hook-/Agent-Frontmatter,
  - Workspace-Settings.

Explizite Nicht-Annahmen
------------------------

- `premium requests` sind nicht mehr der richtige Primarrahmen fuer die aktive Kostenlogik; sie bleiben nur als Legacy-Hintergrund relevant.
- `workspaceInstructions` allein beschreibt nicht mehr die gesamte Governance-Surface in VS Code.
- `AGENTS.md` wird derzeit im Repo nicht als primaere aktive Governance-SSOT genutzt; ein spaeterer Einsatz waere eine zusaetzliche Always-on-Kontextquelle und muss credits-seitig bewusst bewertet werden.