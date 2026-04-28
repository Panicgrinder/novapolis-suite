---
stand: 2026-04-28 13:21
update: Das Root-README verweist jetzt fuer den ersten Text-RPG-Vertikalslice auf den gemeinsamen Release-Evidence-Pfad und dessen Pflichtbelege.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp/results/reports/checks_report_20260423_155606.md; snapshot-lock PASS (2026-04-28 13:21)
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

Kurzfassung (human-readable):

- Code im Repo steht unter MIT, sofern kein Unterpfad explizit abweichend geregelt ist (`LICENSE`, optional untergeordnete Lizenzdateien).
- RP-Content in `novapolis-rp/` steht unter der restriktiven Inhalts-/Datenlizenz `NCDL v1.0` (`novapolis-rp/LICENSE`).
- Eval-/Trainingsdaten unter `novapolis_agent/eval/datasets/` sind separat restriktiv geregelt (`novapolis_agent/eval/datasets/LICENSE.txt`).

Technische Zuordnung (machine-readable):

- Die verbindliche Pfad-zu-Lizenz-Matrix liegt in `LICENSES.md`.
- Bei Konflikten gilt: spezifischere, untergeordnete Lizenzdateien haben Vorrang vor allgemeineren Regeln.

Ergaenzende Governance:

- Marken-/Namensnutzung ist separat geregelt in `TRADEMARKS.md`.
- Beitragspfad und Sign-off-Regeln stehen in `CONTRIBUTING.md`.
- Support- und Meldewege stehen in `SUPPORT.md`.
- Security-Prozess und Responsible Disclosure stehen in `SECURITY.md`.
- Verhaltensleitlinien fuer Collaboration stehen in `CODE_OF_CONDUCT.md`.
- Maintainer-Rahmen steht in `MAINTAINERS.md`; Release-Rahmen in `RELEASE.md`.
- Ownership-Reviewpfade sind in `.github/CODEOWNERS` dokumentiert.
- Root-Issue- und PR-Templates liegen unter `.github/ISSUE_TEMPLATE/` und `.github/pull_request_template.md`.
- Release-notable Aenderungen werden in `CHANGELOG.md` zusammengefasst.
- Architekturentscheidungen werden in `docs/adr/` gefuehrt.

Zentrale Arbeitsrichtlinien
---------------------------

- `.github/copilot-instructions.md` enthaelt die konsolidierten Behaviour-Vorgaben fuer alle Teilprojekte.
- Ausfuehrliche Copilot-/VS-Code-Nutzung: [`novapolis-dev/docs/copilot-vscode-usage.md`](novapolis-dev/docs/copilot-vscode-usage.md).
- Root `todo.root.md` und `DONELOG.md` liefern einen Gesamtueberblick ueber offene Aufgaben und erledigte Arbeiten ohne die Projekt-spezifischen Dateien oeffnen zu muessen.
- Nicht-triviale Aenderungen werden weiterhin im jeweiligen DONELOG des Projekts dokumentiert (`novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`).
- Build-Time-/Runtime-TTS liegen kanonisch unter `novapolis_agent/` (Scripts, API, Konfiguration).
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
----------------

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
- Aktive Regelquelle fuer historische Doku bleibt das Dev-Archiv; Archivpfade in Modulen sind nur zulaessig fuer technische/operative Artefakte im jeweiligen Modul.
- Zulässige operative Modularchive (nicht SSOT fuer Governance-Doku):
  - `novapolis_agent/archive/` (Agent-interne technische Artefakte)
  - `Backups/` (forensische Backup-/Restore-Artefakte auf Root-Ebene)
- Bei Dokument-Archivierung immer zuerst pruefen, ob der Inhalt in `novapolis-dev/archive/` gehoert; nur falls klar modulintern technisch, in den jeweiligen Modularchivpfad ablegen.

Archiv-Matrix (verbindlich)

| Ablageort | Zweck | Zaehlt als aktive Regelquelle |
| --- | --- | --- |
| `novapolis-dev/docs/**` | Aktive Arbeits- und Governance-Dokumente | ja |
| `novapolis-dev/archive/**` | Historisierte Doku-/Governance-Historie | nein |
| `novapolis_agent/archive/**` | Modulintern technische/operative Artefakte | nein |
| `Backups/**` | Forensische Backup-/Restore-Artefakte | nein |

DONELOG-Ebenen (normalisiert)

| Ebene | Datei | Zweck |
| --- | --- | --- |
| A | `novapolis-dev/docs/donelog.md` | Kurzform fuer operative Entscheidungen/Fortschritt (menschenlesbar) |
| B | `.tmp/results/reports/**` | Technische Laufbelege und Detailreports (maschinenlesbar) |
| C | `DONELOG.md` | Root-Summary und Release-/Governance-Zusammenfassung |

### Hinweise für Mitarbeit (Moduswechsel & STOP-Gate)

- Moduswahl: Redaktion/Kanon bitte im General-Modus (GPT-5) arbeiten; Code-Aufgaben (Skripte/Validatoren, Tests/CI, API/Services) im Codex-Modus.
- Details & Regeln: siehe `.github/copilot-instructions.md` (Abschnitt „Modell-Profile & Moduswechsel“ und „STOP-Gate vor Code-Aktionen“).
- STOP-Gate: Vor Code-Aktionen wird ein hartes STOP-Gate gesetzt (explizit „Wechsel: Modus Codex“ oder „Weiter: Modus General“).
- Erinnerungen: Bei Code-Triggern weise ich auf den Moduswechsel hin; „Bitte nicht erinnern“ deaktiviert Hinweise bis zur Reaktivierung.
- Aktueller Status (Modus/STOP-Gate): siehe `WORKSPACE_STATUS.md`.
- Unklarheiten-STOP: "Gruen" gilt nur bis zur naechsten Abweichung/Unsicherheit. Dann STOP, Rueckfrage, weiter nach Freigabe.

Aktive Oberflaeche (kurz)
-------------------------

- Historische/temporäre Betriebsdetails sind aus der Root-Oberflaeche ausgelagert.
- Detailhistorie liegt in `novapolis-dev/archive/docs/donelogs/donelog_root.md` und den Modularchiven.
- Fuer den laufenden Systemzustand sind `WORKSPACE_STATUS.md` und `novapolis-dev/docs/donelog.md` fuehrend.

Aktuelle Statusdokumente
------------------------

- [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md) - laufender Betriebsstatus mit aktuellem Stand (Single-Root, Wrapper, Health-Checks).
- [`todo.root.md`](todo.root.md) - aktive Root-Aufgabenübersicht und Querschnitts-Backlog.
- [`WORKSPACE_INDEX.md`](WORKSPACE_INDEX.md) - Workspace-/Dateiindex zur schnellen Orientierung.
- [`novapolis-dev/docs/process/workspace-audit-segmente.ssot.md`](novapolis-dev/docs/process/workspace-audit-segmente.ssot.md) - kanonische Zerlegung des Workspaces in feste Pruefsegmente fuer kuenftige Gesamt-Audits.
- [`workspace_tree.txt`](workspace_tree.txt) - aktiver Reader-Baum mit gefilterter Root-Surface fuer Navigation.
- [`workspace_tree_dirs.txt`](workspace_tree_dirs.txt) - aktive Verzeichnis-Summary derselben Reader-Surface.
- [`workspace_tree_full.txt`](workspace_tree_full.txt) - ueberwachter repo-sichtbarer Vollbaum; regenerierbar via Tasks `Workspace tree:*`.
- [`workspace_tree_local.txt`](workspace_tree_local.txt) - expliziter lokaler Maschinenbaum fuer den echten On-Disk-Zustand; bewusst getrennt vom Freshness-Gate der drei kanonischen Trees.
- Backups befinden sich zentral unter `Backups/` (keine tool-lesbaren Backups neben aktiven Configs).

Naechste Schritte
-----------------

1. Modulmigrationen und technische Backlogs nur noch ueber aktive Boards (`todo.root.md` plus Modul-TODOs) steuern.
2. Nach jedem groesseren Schritt Quality-Run, DONELOG-Summary und Board-Sync im selben Lauf pflegen.

Editor-Setup (Single-Root)
--------------------------

- Workspace immer über den Root-Ordner `Main/` öffnen (Single-Root, keine `.code-workspace` mehr im Einsatz).
- Zentrales VS-Code-Setup liegt unter `/.vscode/` (Interpreter `.venv`, Tasks für Lint/Tests/Coverage, Copilot-Workspace-Instructions).
- Wrapper-Policy: Mehrschritt-Checks laufen über Skript-Wrapper (z. B. `& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py`, `& .\.venv\Scripts\python.exe scripts/run_pytest_coverage.py --fail-under 80`); STOP-Gate bleibt fuer alle Aktionen mit Seiteneffekt aktiv.
- Sim-Offlinetest: Task `Checks: sim epoch assets` prüft tunnel-sicher die Epoch-Logs und OGG-Namenskonvention via `scripts/check_sim_epoch_assets.py`.
- Details zum aktuellen Status siehe `.github/copilot-instructions.md` und `WORKSPACE_STATUS.md` (Block „Single-Root & Wrapper-Status“).

Wochen- und Monatsabschluss
---------------------------

- Verbindlicher SSOT: `novapolis-dev/docs/process/abschluss-routine.ssot.md`.
- Wochenabschluss: Abschlusslauf in der dort definierten Reihenfolge (Checks -> Tree bei Strukturdelta -> Doku-Sync).
- Monatsabschluss: am ersten Montag des Monats zusaetzlich zum Wochenabschluss, inklusive Monats-Drift-/Hygienepruefung.
- Fuer kuenftige Gesamtpruefungen des Repos ist der feste Workspace-Zuschnitt in `novapolis-dev/docs/process/workspace-audit-segmente.ssot.md` massgeblich.

Standalone-Beta Startpfad (kanonisch)
-------------------------------------

- Fuer externe Tester ohne implizites Projektwissen: `novapolis-dev/docs/process/standalone-beta-installblatt.md`.

1. API starten:

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\run_server.py
```

2. Sim-Hub starten (Godot): `novapolis-sim/project.godot` im Editor oeffnen und `Main.tscn` ausfuehren.

3. Verifikationslauf in fester Reihenfolge:

```powershell
& .\.venv\Scripts\python.exe scripts\run_checks_and_report.py
& .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency
```

`--allow-empty` ist dabei der kanonische Clean-Checkout-Modus fuer `novapolis-sim/data/epochs/` und `novapolis-sim/assets/audio/`; ohne dieses Flag prueft derselbe Check den artefaktbelegten Vollstand.

Release Go/No-Go (Standalone Beta)
----------------------------------

- `GO`: `Checks: full` ist gruen und Sim-Offline-Check meldet `fail:0`.
- `NO-GO`: ein Pflichtcheck faellt oder Sim-Check meldet harte Fehler.
- Jeder Entscheid muss mit Reportpfad in `novapolis-dev/docs/donelog.md` und `DONELOG.md` protokolliert sein.

Text-RPG Release-Evidence-Pfad
------------------------------

- Fuer den ersten suiteweiten Text-RPG-Vertikalslice ist der kanonische Freigabepfad `novapolis-dev/docs/process/text-rpg-release-evidence-bundle-v1.ssot.md`.
- Dieser Pfad bindet `Checks: full`, `Checks: text-rpg product gate`, die deterministischen Referenzfaelle, den Sim-Export-Smoke und `WORKSPACE_STATUS.md` zu derselben Release-Kette.
- Ohne lokale Modellruntime fuer den `gm_session`-Anteil oder ohne exportierten Windows-Smoke unter `novapolis-sim/exports/windows/NovapolisSim.exe` gilt derselbe Slice nicht als release-reif.





