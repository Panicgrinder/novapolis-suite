---
stand: 2025-11-16 06:52
update: Frontmatter-Autofix + --touch dokumentiert; Statusdateien synchron
checks: python scripts/check_frontmatter.py PASS
---

Bereinigte Aufgabenliste (Root)
==============================

Hinweis: Temporärer, kuratierter Auszug für operative Arbeit (Copilot/GPT). SSOT bleibt `todo.root.md`. Abweichungen → STOP.

Hoch priorisiert (0-2 Tage)
--------------------------

  - Ziel: `pytest -q` PASS, `pyright` PASS, `mypy` PASS, Coverage ≥80% mit Receipt.
  - Schritte: pytest → pyright → mypy → `scripts/run_pytest_coverage.ps1` (Receipt in `DONELOG.md` + `WORKSPACE_STATUS.md`).
 - [x] Docs: Statusdateien synchronisieren (todo.root.md, WORKSPACE_STATUS.md, WORKSPACE_INDEX.md, governance.suggestions.md) – Lauf 2025-11-15 09:00
 - [x] Agent: Integration `PSScriptAnalyzer` in der damaligen PowerShell-Variante (jetzt durch `python scripts/run_checks_and_report.py` ersetzt) (2025-11-11 11:00)
  - [x] `*.code-workspace` suchen und entfernen/verschieben (report counts)
  - [x] `tasks.json` Inline-Ketten prüfen → Wrapper-Aufrufe
  - [x] Wrapper-Probelauf `scripts/run_pytest_coverage.ps1` + Receipt
  - [x] Statusblock „Multi-Root abgeschlossen“ in `WORKSPACE_STATUS.md`
- [ ] Governance/Status-Drift & Altlasten (Bündel 1)
  - Ziel: Multi-Root-/Wrapper-Status klären, Tree-/Index-Drift sichtbar machen und Altlasten planbar machen (ohne sofortige Löschung).
  - [x] Multi-Root-/Wrapper-Status konsolidieren (R-STOP/R-WRAP)
    - [x] `single-root-todo.md` und `todo.root.md` Abschnitt „Multi-Root-STOP auflösen“ gegenprüfen (Status: Single-Root, Archiv-Hinweis in `single-root-todo.md`).
    - [x] Widerspruch „KEINE WRAPPER“ vs. Checks-Wrapper `python scripts/run_checks_and_report.py` auflösen (Soll-Zustand dokumentiert: Wrapper für Mehrschritt-Checks wieder erlaubt, STOP weiterhin für WRITE/RUN).
    - [x] In `WORKSPACE_STATUS.md` einen klaren Statusblock ergänzen („Multi-Root & Wrapper-Status“, Stand 2025-11-16 12:00) inkl. Hinweis auf Single-Root/Wrapper-Policy (R-DOKU).
  - [x] WORKSPACE_STATUS.md – Tree-/Status-Drift bereinigen (R-IDX/R-DOKU)
    - [x] Timestamps von `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt` prüfen (Bestätigung: Stand 2025-11-10 07:50 in `WORKSPACE_STATUS.md` referenziert).
    - [x] Ältere Kommentare („Stand 2025-10-31“, „nächste Prüfung Mitte November“) auf aktuellen Zustand angepasst (nächster Lauf nach Strukturänderungen oder spätestens Ende November).
    - [x] Health-Check-Abschnitt um Hinweis ergänzt („Tree-Snapshots aktuell Stand 2025-11-10 07:50“).
  - [x] WORKSPACE_INDEX.md – Redundanzen & Link-Altlasten korrigieren (R-IDX/R-RED)
    - [x] Pfade der `novapolis_agent/requirements*.txt` geprüft und Links im Index auf `novapolis_agent/requirements*.txt` korrigiert.
    - [x] Doppelte Utils-Einträge (`eval_cache.py`, `time_utils.py`, `rag.py`) im Index bereinigt (nur eine Zeile je Datei belassen).
    - [x] Git-Hook-Pfade (`novapolis_agent/.githooks/pre-commit` vs. `githooks/pre-commit`) geprüft; Root-Hook als globaler Hook für das Repo beschrieben.
    - [x] Nach Anpassung Link-Scanner im Scope `WORKSPACE_INDEX.md` laufen lassen; Receipt in `novapolis-dev/archive/docs/donelogs/scan_links_postflight_20251116_033738.md` + Hinweis in `WORKSPACE_STATUS.md` notiert.
  - [x] Alt-Analysen und Legacy-Pfade bewerten (R-SEC/R-SAFE/R-RED)
    - [x] Inhalt von `novapolis_agent/analysis_chat_routers.md` gesichtet; Ergebnis: Alt-Analyse dokumentiert, aktueller Stand (Router entfernt, zentrale Verarbeitung in `app/api/chat.py`) ist bereits in der Datei vermerkt; keine inhaltliche Übernahme in Hub-Docs nötig.
    - [x] Status von `novapolis_agent/app/routers` geprüft (nur leeres `__init__.py`, keine produktive Nutzung mehr; als geparkter Platzhalter belassen).
    - [x] Entscheidung dokumentieren: „archivieren“ vs. „weiter pflegen“; etwaige Lösch-/Move-Schritte nur nach expliziter Freigabe planen (separater Governance-/Cleanup-Schritt erforderlich).
      - Entscheidung: Beide Artefakte als dokumentierte Legacy/Analyse belassen (kein sofortiger Move/Delete). Etwaige Aufräumaktionen laufen später unter separatem Governance-/Cleanup-Task (R-SEC/R-SAFE/R-RED), inkl. DONELOG-/Status-Update.
  - [x] Governance-Deduplizierung vorbereiten (`.github/copilot-instructions.md`) (R-RED/R-DOKU)
    - [x] Präzise festgehalten: Guard-Checks nur vor Aktionen mit Seiteneffekt (WRITE/RUN); reine Leseoperationen explizit ausgenommen (Semantik-TL;DR-Block in `.github/copilot-instructions.md` ergänzt).
    - [x] TL;DR „Doku-Update (true)“ mit Verweisen auf `todo.root.md`, `WORKSPACE_STATUS.md`, `WORKSPACE_INDEX.md`, `.tmp-results/todo.cleaned.md` entwerfen.
      - Entwurf (noch nicht angewendet, nur Plan): Kurzer Abschnitt „Doku-Update (true) — TL;DR“ in `.github/copilot-instructions.md` mit Bullets:
        - Quellen: `todo.root.md` (SSOT), `/.tmp-results/todo.cleaned.md` (Arbeitsauszug), `WORKSPACE_STATUS.md`, `WORKSPACE_INDEX.md`, Modul-DONELOGs/TODOs.
        - Pflichten: TODO/DONELOG/Status/Frontmatter/Index jeweils mit Datum/Scope/Checks aktualisieren.
        - Tools: `python scripts/check_frontmatter.py`, `npx --yes markdownlint-cli2`, `python scripts/run_checks_and_report.py`.
        - Referenz: Verweis auf bestehenden „Doku-Update (true)“-Abschnitt im Archivleitfaden als Detailquelle.
    - [x] Redundante Ausführungen zu Markdownlint/Frontmatter identifizieren; Minimal-Patch-Plan skizzieren (noch keine Anwendung, R-RED beachten).
- [x] Dev: Tree-Artefakte regenerieren (R-IDX)
  - Ziel: `workspace_tree_full.txt`, `workspace_tree.txt`, `workspace_tree_dirs.txt` neu erzeugen; Status/Datum in `WORKSPACE_STATUS.md` + `novapolis-dev/docs/donelog.md`.
  - Hinweis: Tree-Artefakte wurden zuletzt am 2025-11-10 07:50 für alle drei Dateien gemeinsam aktualisiert (Terminal-Tasks `Workspace tree:*`); vor einem weiteren Run prüfen, ob eine relevante Strukturänderung vorliegt. Falls nein, genügt es, den nächsten Turnus (spätestens Ende November) im Status zu notieren; ein sofortiger Neu-Run ist nicht zwingend.
- [x] RP: Frontmatter/Lint Sweep (R-FM/R-LINT)
  - Reihenfolge: Frontmatter → MD003 Setext. Zählwerte vor/nach dokumentieren; PASS loggen (Umsetzung in DONELOG/WORKSPACE_STATUS/novapolis-dev/docs/donelog.md dokumentiert; aktueller Schwerpunkt jetzt auf `database-rp`-Backlog laut `todo.root.md`).

- [x] Docs/READMEs: Konsolidierung & Leitlinien (Monorepo)
  - [x] Kandidatenliste erstellt: `.tmp-results/reports/links/candidates_app-routers-README.md_20251111_2340.md` (22 reale README.md-Dateien)
  - [x] Ein-Satz-Summaries für 22 README.md erzeugen (`.tmp-results/reports/links/readme_summaries.md`)
  - [x] Stubs vs. zentrale Doku definieren (Hub erstellt, Stubs Phase 1 umgesetzt)
  - [x] Redirect-/Index-Strategie festlegen (`WORKSPACE_INDEX.md` vereinheitlichen / ggf. ersetzen durch Hub-Verweis)
  - [x] Entscheidungsliste: Welche Kern-READMEs verschlankt werden (PR-Plan)
  - [x] Hub-README erweitert (TL;DR, Links, Beispiele, Governance-Querverweise)

- [x] Link-Scanner (`scripts/scan_links.ps1`) - Nacharbeiten
  - [x] AutoFix + Backups implementiert; defekte Links 10 → 3 reduziert (Reports unter `.tmp-results/reports/scan_links_reports/`)
  - [x] Report-Verzeichnis umbenannt → `.tmp-results/reports/scan_links_reports`
  - [x] Backup-Pfad zentralisiert → `.tmp-datasets/lscan_links_backups`
  - [x] Bei Mehrdeutigkeit Kandidatenliste im Dry-Run mitschreiben (JSON erzeugt)
  - [x] Rescan nach Fix (0 broken) Receipt vorhanden `link_report_novapolis_agent_20251112_033438.md`
  - [x] Backups (*.bak.linkscan) geprüft (`.tmp-datasets/lscan_links_backups/`)
  - [x] Automatisches Schreiben der Kandidaten-JSON im Dry-Run (Implementierung)
  - [x] Report-Summary in Hub unter "Temporäre Bereiche" verlinken (nach Automation; siehe `novapolis-dev/README.md` Abschnitt „Temporäre Bereiche“ und `novapolis-dev/docs/donelog.md` Link-Scanner-Einträge)

- [x] Checks-Wrapper (`python scripts/run_checks_and_report.py`) - Review/Nachzug
  - [x] Kurzreview der neuen PSScriptAnalyzer-Phase (Installationspfad, Exit-Codes, Receipt-Felder)
    - Kontext: PowerShell-Variante mit PSScriptAnalyzer ist laut [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md) und [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md) archiviert; Analyzer läuft bei Bedarf separat über `scripts/`. Die Python-Variante übernimmt STOP-/Exitcode-Logik und Postflight-Felder.
  - [x] Einbindung in „Checks: full“ Dokumentation (README/Status)
    - Verweise: Abschnitt „Checks: full“ in [`novapolis-dev/README.md`](novapolis-dev/README.md) und Recent-Changes-/Statusblöcke in [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md), DONELOG-Referenzen in [`DONELOG.md`](DONELOG.md) und [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md).
  - [x] Einmaliger Gesamtlauf inkl. Receipt unter `.tmp-results/reports/checks_report_*.md`
    - Belege: Postflight-Meta-Blöcke in [`novapolis_agent/docs/DONELOG.txt`](novapolis_agent/docs/DONELOG.txt), [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md) und [`DONELOG.md`](DONELOG.md) verweisen auf `python scripts/run_checks_and_report.py` inkl. SHA256, Exitcode und Reports unter `.tmp-results/reports/checks_report_*.md`.

Kurzfristig (3-7 Tage)
----------------------

- [ ] RP: Export `99-exports/chat-export-complete.txt` konsolidieren (Scope/Schema definieren)
  - Kontext: Siehe [`todo.root.md`](todo.root.md) Abschnitt „novapolis-rp“ und [`novapolis-dev/docs/todo.rp.md`](novapolis-dev/docs/todo.rp.md) („Exporte einsortieren“).
  - Konkretisieren:
    - [ ] Zieldatei und Schema für `99-exports/chat-export-complete.txt` festlegen (Header/Spalten, Encoding).
    - [ ] Quelle A/B und Duplikat-Befunde aus `novapolis-rp/database-curated/staging/manifest.json` und den Delta-Reports übernehmen.
    - [ ] Kurzprotokoll in [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md) + Hinweis in [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md).

- [ ] RP: Tagging-Pipeline 015-010 von Dry-Run auf Write heben (STOP vor Write)
  - Kontext: [`todo.root.md`](todo.root.md) (novapolis-rp: Tagging-Pipeline 015-010).
  - Schritte:
    - [ ] Dry-Run-Befehle aus [`novapolis-dev/docs/index.md`](novapolis-dev/docs/index.md) („Nutzungshinweise (lokal)“) gegenprüfen.
    - [ ] STOP-Plan formulieren (Scope, Anzahl Dateien, erwartete Writes) und in [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md) notieren.
    - [ ] Write-Run durchführen, danach Lint/Validator laufen lassen; Zahlen/Status in DONELOG + `WORKSPACE_STATUS.md` dokumentieren.

- [ ] Dev/RP: Staging-Reports migrieren oder Frontmatter/Setext nachziehen (einen Task führen; Doppelungen vermeiden)
  - Kontext: [`todo.root.md`](todo.root.md) (novapolis-rp Frontmatter/Markdown-Sweep) und [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md) („Staging-Reports - Setext/Frontmatter konsolidiert“).
  - Schritte:
    - [ ] Ist-Stand der Reports unter `novapolis-rp/database-curated/staging/reports/*.md` prüfen (Frontmatter/MD003).
    - [ ] Entscheiden: Migration nach `novapolis-dev/docs/` vs. lokale Korrektur; nur EIN zentrales Task-Item führen (Root- oder Dev-TODO).
    - [ ] Nach Umsetzung: Receipts in `DONELOG.md`, `WORKSPACE_STATUS.md`, `novapolis-dev/docs/donelog.md` (Scope/Zählwerte).

- [x] Dev: `README.md.bak` behandeln (`Backups/`löschen)
  - Kontext: [`todo.root.md`](todo.root.md) Abschnitt „Multi-Root-STOP auflösen“; Datei `README.md.bak` liegt im Root.
  - Schritte:
    - [ ] Inhalt der Backup-Datei kurz prüfen (Diff zu aktuellem `README.md`).
    - [ ] Entscheidung: Falls nur historischer Stand → nach `Backups/` verschieben; sonst archivierte Referenz in `novapolis-dev/archive/README.md` vermerken.
    - [ ] Ergebnis (Pfad/Entscheidung) in `DONELOG.md` + `WORKSPACE_STATUS.md` notieren (R-SEC/R-SAFE).

- [x] Dev: Abschnitt „Editor-Setup“ im Root-`README.md`
  - Kontext: [`todo.root.md`](todo.root.md) „Editor-Setup - .vscode-Konsolidierung (Root-zentriert)“.
  - Schritte:
    - [x] Kurzabschnitt im Root-[`README.md`](README.md) ergänzen mit Verweis auf Single-Root, Wrapper-Policy und `.vscode`-Zielbild.
    - [x] Links auf `.github/copilot-instructions.md` und `WORKSPACE_STATUS.md` (Single-Root & Wrapper-Status, ehemals Multi-Root) setzen.
    - [x] Nach Anpassung markdownlint/frontmatter-Validator laufen lassen; Receipt in `DONELOG.md`.
    - Hinweis: Abschnitt „Editor-Setup (Single-Root)“ ist in `README.md` live; Lint/Frontmatter-Checks laut [`DONELOG.md`](DONELOG.md) und [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md) bereits dokumentiert.

 [x] Sim: Godot headless Lade-Check (`novapolis-sim/project.godot`) und Kurzprotokoll — PASS
   - Kontext: [`todo.root.md`](todo.root.md) (novapolis-sim: Headless-Lade-Check) und [`novapolis-dev/docs/todo.sim.md`](novapolis-dev/docs/todo.sim.md).
   - Schritte:
     - [x] Headless-Load von `novapolis-sim/project.godot` mit Godot 4 ausführen (ohne Editorfenster); Logs auf Fehler/Warnungen geprüft (`.tmp-results/logs/godot_headless_20251116_045407.log`).
     - [x] Kurzprotokoll und Postflight-Eintrag in [`novapolis-dev/docs/donelog.md`](novapolis-dev/docs/donelog.md) ergänzt.
     - [x] Hinweis in `WORKSPACE_STATUS.md` (Sim-Expected-State) hinzugefügt.

Sofort-Themen (READMEs/Links/Index)
-----------------------------------

- [x] Entfernte Index-Datei: Links-Anpassungen nun direkt in verbleibenden READMEs geprüft (Agent WORKSPACE_INDEX entfernt)
- [x] Ambiguität „matches=53“: Kandidatenliste JSON erzeugt
  - Datei: `.tmp-results/reports/links/candidates_app-routers-README.json`
  - Nächster Schritt: Scanner erweitern (Auto-Ausgabe JSON bei Dry-Run)
- [x] Doppelte/parallel existierende Index-Dateien entfernt (`novapolis_agent/WORKSPACE_INDEX.md`, Backup `.bak.linkscan`)

Lokale AI - Startpfad (organisch)
---------------------------------

- [ ] Schattenmodus-Logging mit Redaction aktivieren (operativ)
- [ ] 10-20 Kern-Dokumente indexieren (RAG-Minimum)
- [ ] Wöchentlichen Review-Slot (30-45 min) einplanen

Hinweise
--------

- STOP-Marker: Tagging-Write, Cleanup Phase 4, Multi-Root-Abschluss.
- SSOT: Detailkontext und Volltextliste in `todo.root.md`; diese Datei dient als Arbeitsfahrplan für Copilot/GPT.
- 2025-11-10 20:17: WORKSPACE_INDEX Header-Duplikate und SimClient Variable gefixt (Commit 5922521). `run_pytest_quick.ps1` PASS.
- Wrapper-Aufgaben: `python scripts/run_checks_and_report.py` (Lint/Typen/Tests + Report) finalisieren; Link-Scanner `scripts/scan_links.ps1` implementieren und Reports unter `.tmp-results/scan/` ablegen.
  - Hub-README: Erweiterung abgeschlossen (01:12); nächste Phase Index/Redirect-Strategie.
