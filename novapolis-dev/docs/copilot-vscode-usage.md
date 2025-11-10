---
stand: 2025-11-10 07:21
update: Tabs entfernt, Frontmatter korrigiert, Lint PASS
checks: markdownlint PASS, frontmatter PASS (scoped)
---

VS Code + GitHub Copilot – Projektleitfaden
===========================================

Zweck: So kommunizierst du effektiv mit Copilot/GPT in VS Code und bindest die KI projektkonform ein, bis unsere eigene AI live ist.

TL;DR
-----
- Nutze Chat-Modi kontextgerecht: Agent (autonom, mehrschrittig), Ask (Fragen), Edit (gezielte Code-Edits), Inline Chat (Ctrl+I für selektierte Stellen).
- Liefere Kontext: `#file`, `#selection`, `#codebase`, `#terminalSelection` sowie kurze Ziele/Constraints und Akzeptanzkriterien.
- Verwende `/`-Kommandos (z. B. `/explain`, `/new`) und Prompt‑Vorlagen (Prompt Files) für Standards.
- Halte unsere Governance ein: `.github/copilot-instructions.md` (Sprache DE, Preambles, Wrapper‑Policy, STOP‑Gate, Frontmatter, Lint/Validator, Postflight‑Receipts).
- Modelle bewusst wählen (Geschwindigkeit vs. Reasoning) und bei Bedarf kontextreich iterieren statt Einmal‑Prompts.

Kommunikationsmuster (Prompts)
-----------------------------
- Rolle+Ziel: „Du bist Pair Programmer. Ziel: <kurz>.“
- Kontext: Verweise mit `#file`, `#selection`, `#codebase`, `#terminalSelection` und nenne relevante Pfade in Backticks.
Voraussetzungen & Setup
-----------------------
- VS Code installiert (stable oder Insiders) und Copilot eingerichtet (Statusleisten‑Icon → „Set up Copilot“).
- GitHub‑Login mit Copilot‑Plan (Free, Pro, Team/Business/Enterprise je nach Bedarf).
- Erweiterungen: Copilot ist in VS Code integriert; zusätzliche Tools/Server nur bei Bedarf installieren.
- Erstschritte in VS Code:
  - Schritt 1: Code Completions testen (Ghost‑Text; Tab zum Akzeptieren).
  - Schritt 2: Chat öffnen (`Ctrl+Alt+I`), Modus „Agent“ wählen, erste Aufgabe formulieren.
  - Schritt 3: Inline‑Chat (`Ctrl+I`) für kleine, selektive Edits nutzen.

Kernfähigkeiten (Überblick)
---------------------------
- Code Completions: Einzeiler bis ganze Funktionen auf Basis deines Kontexts.
- Natural‑Language Chat: Fragen stellen, erklären lassen, Änderungen anfordern.
- Agent Mode (autonom): Mehrschritt‑Workflows inkl. Terminal und Dateiedits planen/ausführen.
- Smart Actions: Kontextuelle KI‑Aktionen (Commit‑Botschaften, Fix‑Vorschläge, Umbenennen u. a.).

Chat‑Modi im Detail
-------------------
- Agent: Für Features/Migrationen/Refactors; kann Tools/Terminal nutzen und Dateien ändern.
- Ask: Reine Q&A/Erklärungen ohne Änderungen.
- Edit: Präzise Anpassungen in der aktuellen Datei, reviewbar.
- Plan (Preview): Ideen/Archi‑Planung ohne direkte Edits.
- Inline‑Chat: Direkt am Code, ideal bei selektierten Blöcken; minimiert Kontextwechsel.

- Constraints: Framework/Libs, Stil, Tests/Typen (z. B. „mypy/pyright grün“, „pytest ≥ 80 % Coverage“).
- Akzeptanz: „Ergebnis: PR‑fertiger Patch; keine unbeteiligten Dateien; Lint/Validator PASS.“
- Iteration: Folgefragen/Verfeinerung statt zu langer Erst‑Prompts.


Modelle gezielt wählen
----------------------
- Schnelle Modelle: Für zügige Vorschläge/kleine Edits.
- Reasoning‑Modelle: Für komplexe Planung/Refactor/Fehlersuche.
- Wechsel direkt im Chat‑Eingabefeld (Modell‑Picker); ggf. alternative Provider hinzufügen.
Kontext hinzufügen
------------------
- `#file`: einzelne Datei als Kontext.
- `#selection`: die aktuell markierte Auswahl im Editor.
- `#codebase`: projektweite Sicht (sparsam nutzen; ggf. auf Ordner/Dateien einschränken).
- `#terminalSelection`: relevante Terminal‑Ausgaben (Fehler, Testlogs).
- Tipp: In Chat‑Eingabe `#` tippen, um verfügbare Kontexte/Tools zu sehen.

Chat‑Erlebnis in VS Code
------------------------
- Chat‑View: Ctrl+Alt+I – mehrturnige Unterhaltungen, Moduswahl, Modellwahl.
Kontexte & Tools in Prompts
---------------------------
- `#file`, `#selection`, `#codebase`, `#terminalSelection` für gezielte Kontextgabe.
- `/`‑Kommandos (z. B. `/explain`, `/new`) und eigene Prompt‑Vorlagen einsetzen.
- Tool‑Referenzen via `#` (z. B. `#fetch`, `#githubRepo`) – nur aktivieren, was gebraucht wird.

- Inline‑Chat: Ctrl+I – gezielte Edits/Erklärungen direkt am Code (mit Auswahl).
- Quick‑Chat: kurze Einwürfe ohne View‑Wechsel (Statusleiste/Command Center).

Chat‑Modi (Auswahl)
-------------------
- Agent: autonom, plant/führt Schritte aus (inkl. Terminal/Datei‑Änderungen). Für Features/Refactors.
Custom Instructions (VS Code)
-----------------------------
- Definiere projektweite Leitplanken (Stil, Frameworks, Muster) als persistente Hinweise.
- Beispiel:

```markdown
---
applyTo: "**"
---
# Projekt Coding‑Style
- TypeScript‑Typen verpflichtend; 
- Fehlertolerante APIs mit klare Rückgabewerte;
- Nur `pwsh -File` für Builds/Tests.
```

Prompt‑Dateien (Slash‑Kommandos)
--------------------------------
- Wiederverwendbare Prompts unter `.github/prompt-files/` anlegen und per `/` aufrufen.
- Beispiel: `/create-api-endpoint` standardisiert Pfade, Tests, Fehlerbehandlung.

Eigene Chat‑Modi
----------------
- `.github/chatmodes/` → Rollen/Leitplanken/Werkzeugzugriff definieren.
- Beispiel „Code Reviewer“: Nur Analyse, kein Schreiben; Tools: usages, problems, fetch, githubRepo.
- Nutzen: Einheitliche Reviews/Architektur‑Diskussionen ohne Code‑Mutation.

MCP‑Server & Tools
------------------
- Chat um spezialisierte Fähigkeiten erweitern (DB‑Abfragen, externe APIs).
- Auswahl sparsam: Nur notwendige Tools freischalten; Datenschutz beachten.
- In VS Code konfigurierbar; passt gut zum Agent‑Modus.

- Ask: Fragen/Erklärungen ohne Änderungen.
- Edit: fokussierte Code‑Anpassungen im aktuellen File.
- Plan (Preview/Insiders): Planerischer Entwurf, kein direkter Code‑Edit.

Modelle & Tools
---------------

Sicherheit & Compliance
-----------------------
- Content‑Exclusion prüfen/konfigurieren (Ausschlüsse verwalten, Änderungen auditieren).
- Keine Secrets/PII in Prompts; bei Tools/MCP Minimalprinzip.
- Trust/Privacy: Copilot Trust Center FAQ beachten.

Troubleshooting
---------------
- Häufige Probleme: Modell wechseln, Chat‑Kontext erneuern, Copilot‑Login prüfen.
- Logs prüfen (VS Code Ausgabe), Firewall/Netzwerk‑Einstellungen verifizieren.
- Bei anhaltenden Problemen: Offizielle Troubleshooting‑Seiten folgen.
- Modelle: Im Chat‑Eingabefeld wählbar (Speed vs. Reasoning). Für komplexe Aufgaben Reasoning‑Modelle erwägen.
- Tools: Erweiterbar via MCP‑Server/Extensions (z. B. Datenbankabfragen, externe APIs). Nur aktivieren, was gebraucht wird.

Projekt‑Regeln (wichtig)
------------------------
- Sprache: Deutsch. Kurze, präzise Antworten.
- Preambles vor Tool‑Aktionen: kurz ankündigen, was/warum.
- Planung: Für mehrschrittige Aufgaben ToDo‑Liste (manage_todo_list) nutzen und Schrittweise abhaken.
- Wrapper‑Policy (R‑WRAP): Mehrschrittläufe nur via `pwsh -File <script.ps1>`, kein verschachteltes `-Command`.
- Chat Prompt‑Beispiele: <https://code.visualstudio.com/docs/copilot/chat/prompt-examples>
- Modelle in VS Code: <https://code.visualstudio.com/docs/copilot/customization/language-models>
- Copilot Sicherheit: <https://copilot.github.trust.page/faq>
- Copilot Tipps & Tricks: <https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks>
- Copilot Preise/Pläne: <https://docs.github.com/en/copilot/get-started/plans>
- Kontexte & Tools im Chat: <https://code.visualstudio.com/docs/copilot/chat/chat-tools>
- Kontext hinzufügen: <https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context>
- Content‑Exclusion: <https://docs.github.com/en/copilot/how-tos/configure-content-exclusion>
- Validierung: Frontmatter (stand/update/checks) pflegen; `markdownlint-cli2` + `scripts/run_frontmatter_validator.ps1` ausführen.
- Receipts: Nach abgeschlossenen Arbeitsvorgängen kompakter Postflight‑Block; relevante DONELOGs ergänzen.
- STOP‑Gate: Bei Unklarheit/Sicherheitsfragen stoppen und Freigabe einholen.

Customizing für dieses Repo
---------------------------
- Custom Instructions: `.github/copilot-instructions.md` ist SSOT (Regeln/IDs/Flows). Änderungen dort sind bindend.
- Prompt Files & Chat‑Modes: Optionale Ablage unter `.github/prompt-files/` bzw. `.github/chatmodes/` für wiederkehrende Flows (z. B. „Code Reviewer“, „Docs TL;DR“). Nur minimal‑invasiv einführen.
- Wissensquellen: `.tmp-results/` für kuratierte, temporäre Arbeitsgrundlagen (keine SSOT). Nach Änderungen an `todo.root.md` synchron halten.

Bewährte Praktiken
------------------
- Passenden Modus wählen (Completions vs. Chat vs. Inline vs. Agent).
- Klein anfangen, iterativ verfeinern; Kontexte explizit verlinken.
- Code‑Änderungen in kleinen Diffs, nur betroffene Dateien.
- Nach Edits: Lint/Typen/Tests lokal; Artefakte/Ergebnisse kurz notieren.

Quellen
-------
- VS Code Copilot – Überblick: <https://code.visualstudio.com/docs/copilot/overview>
- VS Code Copilot Chat: <https://code.visualstudio.com/docs/copilot/copilot-chat>
- VS Code Getting Started: <https://code.visualstudio.com/docs/copilot/getting-started>
- GitHub Copilot – How‑tos: <https://docs.github.com/en/copilot/how-tos>
- MCP‑Server/Tools: <https://code.visualstudio.com/docs/copilot/customization/mcp-servers>
- Custom Instructions: <https://code.visualstudio.com/docs/copilot/customization/custom-instructions>

Hinweise
--------
- Funktionen/Modelle können sich ändern (Abos/Versionen). Bei Abweichungen bitte Quellen prüfen und lokal anpassen.
