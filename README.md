---
stand: 2026-03-02 22:24
update: Hybrid-Lizenzmodell eingefuehrt: Code bleibt MIT, RP-Content/Eval-Daten sind separat restriktiv geregelt; Contributing- und Markenhinweise verlinkt.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'README.md' 'LICENSES.md' 'CONTRIBUTING.md' 'TRADEMARKS.md' 'DONELOG.md' 'novapolis-rp/README.md' 'novapolis-dev/docs/donelog.md' PASS (2026-03-02 22:18); .\.venv\Scripts\python.exe scripts/check_frontmatter.py 'README.md' 'LICENSES.md' 'CONTRIBUTING.md' 'TRADEMARKS.md' 'DONELOG.md' 'novapolis-rp/README.md' 'novapolis-dev/docs/donelog.md' PASS (EXITCODE=0, 2026-03-02 22:18)
---
Novapolis Suite
===============

Die Novapolis Suite fasst Agent-Backend, Rollenspiel-Datenbasis, Dev-Dokumentation und Simulation unter einem gemeinsamen Repository zusammen. Ziel ist, doppelte Module zu konsolidieren, Arbeitsablaeufe zu vereinheitlichen und einen schnellen Ueberblick ueber alle laufenden Aufgaben zu behalten. Der zentrale Conversational Agent heisst "Chronistin von Novapolis".

Projekte im Repository
----------------------

- **novapolis_agent** - FastAPI-Backend, Eval-Tooling und Trainingsskripte fuer den produktiven Novapolis Agent ("Chronistin von Novapolis").
- **novapolis-rp** - Weltbau-Daten, Rollenspiel-Workflows und begleitende Tools (ohne Agent-Laufzeit).
- **novapolis-dev** - Kuratierte Datensaetze, Prozess- und Policy-Dokumentation als Arbeits-Hub.
- **novapolis-sim** - Godot-Szene und Skripte fuer den Simulations-Prototypen.
- **TTS** - Externes Coqui-TTS-Upstream-Repository als lokales Vendor-/Referenz-Mirror (`TTS/`, eigenes `.git`, eigene Workflows/Tests).
  - Vormerkung: `TTS/` ist nur temporaer im Root, damit nichts vergessen wird. Es werden ausschließlich benoetigte Teile entnommen und ins Modul `novapolis_agent/` ueberfuehrt; danach wird `TTS/` wieder entfernt.

Gemeinsames Python-Paket
-------------------------

Geteilte Python-Helfer leben in `packages/novapolis_common`. Installiere das Shared-Paket bei Bedarf als Editable (nicht mehr das gesamte Repo):

```powershell
Set-Location .
# Dependencies (Root):
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt

# Optional: Shared-Paket als Editable
& .\.venv\Scripts\python.exe -m pip install -e packages/novapolis_common
```

Module, die aktuell mehrfach in den Projekten vorkommen, sollten nach `packages/novapolis_common` wandern. Projektspezifische Verdrahtung (API, Policies, Szenenlogik) verbleibt in den jeweiligen Ordnern. Packaging/Build-Konfigurationen verbleiben in den Modul-/Paketpfaden; das Root `pyproject.toml` ist tools-only.

Abhaengigkeiten
---------------

Die Root-Dateien `requirements.txt` und `requirements-dev.txt` sammeln die Pins aller Teilprojekte. Fuer einzelne Bereiche koennen weiterhin die lokalen Requirements-Dateien genutzt werden.

Lizenzmodell (Hybrid-Schutz)
----------------------------

- Code bleibt im Kern unter MIT (`LICENSE`).
- RP-Content in `novapolis-rp/` ist ab sofort separat als Inhalts-/Datenmaterial lizenziert (`novapolis-rp/LICENSE`) und nicht mehr unter MIT freigegeben.
- Eval-Datasets unter `novapolis_agent/eval/datasets/` sind separat restriktiv geregelt (`novapolis_agent/eval/datasets/LICENSE.txt`).
- Uebergreifende Zuordnung (Pfad -> Lizenz) steht in `LICENSES.md`.
- Marken-/Namensnutzung ist separat geregelt in `TRADEMARKS.md`.
- Beitragspfad und Sign-off-Regeln stehen in `CONTRIBUTING.md`.

Zentrale Arbeitsrichtlinien
---------------------------

- `.github/copilot-instructions.md` enthaelt die konsolidierten Behaviour-Vorgaben fuer alle Teilprojekte.
- Ausfuehrliche Copilot-/VS-Code-Nutzung: [`novapolis-dev/docs/copilot-vscode-usage.md`](novapolis-dev/docs/copilot-vscode-usage.md).
- Root `todo.root.md` und `DONELOG.md` liefern einen Gesamtueberblick ueber offene Aufgaben und erledigte Arbeiten ohne die Projekt-spezifischen Dateien oeffnen zu muessen.
- Nicht-triviale Aenderungen werden weiterhin im jeweiligen DONELOG des Projekts dokumentiert (`novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`).
- `TTS/` ist kein kanonisches SSOT-Modul der Novapolis-Suite; Anpassungen dort nur bei explizitem Auftrag und mit separatem Upstream-Abgleich.
- Verbindliche Entnahmeregel fuer `TTS/`: nur notwendige Artefakte/Codepfade uebernehmen, in `novapolis_agent/` integrieren, `TTS/` anschließend aus dem Root entfernen.
- Der Agent-Workspace nutzt jetzt den Paketnamen `novapolis_agent`; aeltere Referenzen mit Bindestrich bitte bei Gelegenheit bereinigen (siehe Aufgaben in `todo.root.md`).

### Copilot Instructions (kanonisch)

- Die verbindlichen Arbeits-/Antwortrichtlinien liegen zentral unter `.github/copilot-instructions.md` (dieses Repo, Root/.github). Ergänzende Navigation: `novapolis-dev/docs/index.md`.
- In VS Code sind diese Dokumente als primärer Kontext hinterlegt (siehe `/.vscode/settings.json` → `github.copilot.chat.workspaceInstructions`).

### Lint/Format & EOL-Policy (Root)

- Markdownlint: Konfiguration unter `.markdownlint-cli2.jsonc` (Root). Optionales Ignore-File `.markdownlintignore`.
- Editorconfig: `.editorconfig` definiert Spaces (2), EOL und Markdown-Listen-Indent; `*.ps1` erzwingt CRLF.
- Python: Black/Ruff über `pyproject.toml` (tools-only im Root; Packaging bleibt in den Modulpfaden).
- Git EOL: `.gitattributes` erzwingt LF für Text/Markdown, CRLF für Windows-Scripts (`*.ps1`, `*.cmd`, `*.bat`, `*.psm1`), und markiert Binärdateien mit `-text` (keine Fake-Diffs).

Lint ausführen (optional, lokal):

```powershell
Set-Location .
npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc '**/*.md'
```

Workspace öffnen
-----------------

1. VS Code über den Root-Ordner `Main/` öffnen (Single-Root). Die frühere Multi-Root-Workspace-Datei wird nicht mehr verwendet.
2. Workflows laufen ausschließlich zentral aus dem Root (`/.github/workflows`). Modulverzeichnisse enthalten keine eigenen `.github/workflows` mehr.
3. Automatisierte Läufe erfolgen über das Tasks-Panel (Shared-Panel); spontane Shell-Kommandos gehören ins User-Terminal.
4. CI-Workflows sind pfad-gefiltert: Sie laufen nur bei relevanten Änderungen (z. B. `ci.yml` für `novapolis_agent/**`, `enforce-donelog.yml` für Agent-Code/DONELOG, `validate-rp.yml` für `novapolis-rp/**`; `markdownlint.yml` bereits mit `paths`).

### Godot (Simulation)

- Kanonische Projektdatei: `novapolis-sim/project.godot` (Option A gewählt).
- Das vormals verschachtelte Projekt unter `novapolis-sim/novapolis-sim/` wurde archiviert: `Backups/novapolis-sim-archived-20251104/`.
- Editor-Pfad ist in `.vscode/settings.json` hinterlegt; Tasks/Repo verweisen nur auf die kanonische Datei.

Verbindungsprüfung
------------------

2025-11-10 12:12 — Verbindung zwischen der lokalen Godot-Instanz und dem Agent-API (`POST /world/step`) wurde erfolgreich verifiziert. Headless-Verifier (`novapolis-sim/scripts/verify_sim.gd`) und ein lokaler Smoke-Check (`POST /world/step`) liefen lokal durch. Siehe `novapolis-sim/README.md` für Ausführungsbefehle und Audit-Hinweise.

### Archiv

- Historisierte oder ältere Planungs-/Prozessdokumente werden zentral unter `novapolis-dev/archive/` abgelegt.
- Bitte keine Archive in Unterprojekten anlegen; verlinke stattdessen nach `novapolis-dev/archive/`.

### Hinweise für Mitarbeit (Moduswechsel & STOP-Gate)

- Moduswahl: Redaktion/Kanon bitte im General-Modus (GPT-5) arbeiten; Code-Aufgaben (Skripte/Validatoren, Tests/CI, API/Services) im Codex-Modus.
- Details & Regeln: siehe `.github/copilot-instructions.md` (Abschnitt „Modell-Profile & Moduswechsel“ und „STOP-Gate vor Code-Aktionen“).
- STOP-Gate: Vor Code-Aktionen wird ein hartes STOP-Gate gesetzt (explizit „Wechsel: Modus Codex“ oder „Weiter: Modus General“).
- Erinnerungen: Bei Code-Triggern weise ich auf den Moduswechsel hin; „Bitte nicht erinnern“ deaktiviert Hinweise bis zur Reaktivierung.
- Aktueller Status (Modus/STOP-Gate): siehe `WORKSPACE_STATUS.md`.
 - Unklarheiten-STOP: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit - dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → „Unklarheiten-STOP (global, immer gültig)“.

Bekannte Einschränkungen (temporär)
-----------------------------------

- Single-Root ist produktiv aktiv; Multi-Root-Verweise existieren nur noch als Historie. Guard: `python scripts/multi_root_cleanup.py --whatif` meldet neue `*.code-workspace`-/Schatten-Dateien. Fallakte bleibt dokumentiert (`novapolis-dev/logs/open-case-terminal-multi-root-20251103.md`).
- Wrapper-Tasks laufen wieder zuverlässig über das Root-`.vscode/tasks.json` (Interpreter `.venv`). Trotzdem gilt weiterhin R-WRAP/R-STOP: Bei Aktionen mit Seiteneffekt vorher kurz den Plan abstimmen und Receipt schreiben.

Aktuelle Statusdokumente
------------------------

- [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md) - laufender Betriebsstatus mit aktuellem Stand (Single-Root, Wrapper, Health-Checks).
- [`todo.root.md`](todo.root.md) - aktive Root-Aufgabenübersicht und Querschnitts-Backlog.
- [`WORKSPACE_INDEX.md`](WORKSPACE_INDEX.md) - Workspace-/Dateiindex zur schnellen Orientierung.
- [`workspace_tree_full.txt`](workspace_tree_full.txt) - vollständiger Verzeichnisbaum; regenerierbar via Tasks `Workspace tree:*`.
- Backups befinden sich zentral unter `Backups/` (keine tool-lesbaren Backups neben aktiven Configs).

Naechste Schritte
-----------------

1. Doppelte Module identifizieren und schrittweise in `packages/novapolis_common` verschieben.
2. Tests und Typpruefungen nach jeder Migration laufen lassen (`pytest`, `pyright`, `mypy`).
3. Nach jedem groesseren Schritt DONELOG aktualisieren und Root-Uebersichten synchron halten.

Editor-Setup (Single-Root)
--------------------------

- Workspace immer über den Root-Ordner `Main/` öffnen (Single-Root, keine `.code-workspace` mehr im Einsatz).
- Zentrales VS-Code-Setup liegt unter `/.vscode/` (Interpreter `.venv`, Tasks für Lint/Tests/Coverage, Copilot-Workspace-Instructions).
- Wrapper-Policy: Mehrschritt-Checks laufen über Skript-Wrapper (z. B. `python scripts/run_checks_and_report.py`, `python scripts/run_pytest_coverage.py --fail-under 80`); STOP-Gate bleibt für alle Aktionen mit Seiteneffekt aktiv.
- Sim-Offlinetest: Task `Checks: sim epoch assets` prüft tunnel-sicher die Epoch-Logs und OGG-Namenskonvention via `scripts/check_sim_epoch_assets.py`.
- Details zum aktuellen Status siehe `.github/copilot-instructions.md` und `WORKSPACE_STATUS.md` (Block „Single-Root & Wrapper-Status“).

Wochenabschluss-Routine
-----------------------

1. Lint/Typen/Tests/Coverage in dieser Reihenfolge laufen lassen (`Checks: full`, optional `Checks: sim epoch assets`, dann `Tests: coverage (fail-under)`).
2. Bei Strukturänderungen Tree-Artefakte aktualisieren (`Workspace tree:*`).
3. Danach `todo.root.md`, `WORKSPACE_STATUS.md`, `DONELOG.md` und `novapolis-dev/docs/donelog.md` im selben Lauf synchronisieren.



