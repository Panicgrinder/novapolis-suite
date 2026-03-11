---
stand: 2026-03-11 07:07
update: Punkt-3-Strategie gestartet; 90%-Coverage-Ziel im Dev-Prozess verbindlich verankert.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc README.md novapolis-dev/README.md DONELOG.md novapolis-dev/docs/donelog.md SECURITY.md CODE_OF_CONDUCT.md CHANGELOG.md docs/adr/README.md PASS (2026-03-11 04:49); .\.venv\Scripts\python.exe scripts/check_frontmatter.py README.md novapolis-dev/README.md DONELOG.md novapolis-dev/docs/donelog.md SECURITY.md CODE_OF_CONDUCT.md CHANGELOG.md docs/adr/README.md PASS (EXITCODE=0, 2026-03-11 04:49)
---

DONELOG (Root Summary)
======================

Hinweis
-------

- Diese Datei ist der Root-Summary-/Release-Log (kurz und scanbar).
- Detailhistorie liegt unter `novapolis-dev/archive/docs/donelogs/donelog_root.md`.
- Technische Laufdetails liegen in Reports unter `.tmp/results/reports/`.

Aktuelle Eintraege (Summary)
----------------------------

- 2026-03-11 07:07: Auf User-Freigabe mit Punkt 3 gestartet. Dev-Teststrategie auf moderne Coverage-Governance umgestellt und 90%-Qualitaetsziel verbindlich verankert (`novapolis-dev/docs/tests.md`, `novapolis-dev/docs/process/abschluss-routine.ssot.md`).
- 2026-03-11 06:57: Neuer Dev-Optimierungszyklus gestartet und in `novapolis-dev/docs/todo.dev.md` aufgenommen. Punkt 1 (`ruff`/`black`/`pytest+coverage`) wurde begonnen; Ruff/Black-Befunde bereinigt, verbleibender Blocker ist Coverage (`76.24%` vs. Ziel `>=80%`).
- 2026-03-11 06:49: Letzter offener Dev-Optimierungspunkt geschlossen. Woechentliche 60-Minuten-Hygiene-Cadence mit KPI-Protokoll in `novapolis-dev/docs/process/abschluss-routine.ssot.md` verankert; Dev-Board und TODO-Index auf `offen: 0` synchronisiert.
- 2026-03-11 06:43: Rueckwaertskompatibilitaet fuer TODO-Index-CLI wiederhergestellt. `scripts/check_todo_index_sync.py` akzeptiert erneut `--root` als Alias zu `--repo-root` und toleriert `--strict` als Deprecated-Noop, damit bestehende Aufrufe nicht fehlschlagen.
- 2026-03-11 05:12: Beide Folgepunkte umgesetzt. `README.md` und `novapolis-dev/README.md` auf aktive Kurzoberflaeche gestrafft; `scripts/check_todo_index_sync.py` auf Auto-Write von Open-Counts/Board-Metadaten erweitert und in `scripts/run_checks_and_report.py` sowie `.vscode/tasks.json` eingebunden.
- 2026-03-11 04:49: Receipt-Hygiene abgeschlossen. Neue Governance-Dokumente (`SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, `docs/adr/README.md`) enthalten jetzt echte Gate-Receipts statt temporaerer `checks: pending`-Marker.
- 2026-03-11 04:46: README-Finish fuer aktive Lesbarkeit umgesetzt. Root-README verlinkt nun explizit `SECURITY.md`, `CODE_OF_CONDUCT.md`, `.github/CODEOWNERS`, `CHANGELOG.md` und `docs/adr/`; `novapolis-dev/README.md` wurde von einem veralteten Receipt-Block bereinigt und den Abschnitt `Checks & Reports` auf dauerhafte, scanbare Form gebracht.
- 2026-03-11 04:46: Root-DONELOG auf Summary-Ebene reduziert (Informationsarchitektur Schritt 2). Historische Detailketten in den Root-Archivpfad ausgelagert/verankert; aktive Root-Ansicht bleibt bewusst kurz.
- 2026-03-11 04:27: Doku-Informationsarchitektur geschaerft: aktive Oberflaechen in `novapolis-dev/docs` reduziert, Archiv-/Log-Matrix in Root/Dev-README verankert, TODO-Index-Guard und DONELOG-Workflow gehaertet.
- 2026-03-10 15:40: Wochenabschluss gemaess SSOT ausgefuehrt; Governance-Gates PASS, Restpunkte bei `ruff`, `black`, `pytest` im Full-Check.

Archiv-Verweise
---------------

- Root-Detailhistorie: `novapolis-dev/archive/docs/donelogs/donelog_root.md`
- Dev-Current-Window: `novapolis-dev/docs/donelog.md`
- Historische Dev-Window-Archive: `novapolis-dev/archive/docs/donelogs/`
