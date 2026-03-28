---
stand: 2026-03-28 06:51
update: Phase-2-Konsistenzlauf zieht die Beta-Gates auf den aktuellen PASS-Kontext und explizite Root-Wrapper nach.
checks: markdownlint PASS; frontmatter PASS; path-portability PASS; logs-policy PASS (2026-03-28 01:31)
---

Standalone Beta Gates (SSOT)
============================

Zweck
-----

- Einheitliche, nachvollziehbare Go/No-Go Entscheidung fuer Standalone-Beta-Laeufe.
- Verbindliche Mindestkriterien fuer Checks, Sim-Validierung und Dokumentation.

Gate-Kriterien
--------------

- `GO` nur wenn alle Pflichtpunkte erfuellt sind:
  - `& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py` ohne Pflicht-FAIL.
  - `& .\.venv\Scripts\python.exe scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency` mit `fail:0`.
  - Aktueller Reportpfad ist in `novapolis-dev/docs/donelog.md` und `DONELOG.md` protokolliert.
- `NO-GO` sobald ein Pflichtkriterium fehlschlaegt.

Pflicht-Checks (Beta)
---------------------

- `markdownlint`
- `frontmatter`
- `path-portability`
- `namingpolicy`
- `ruff`
- `black`
- `pytest`
- `pyright`
- `mypy`
- `coverage >= 80`

Protokollpflicht
----------------

- Jeder Beta-Entscheidlauf enthaelt:
  - Zeitstempel,
  - Reportpfad,
  - Ergebnis (`GO`/`NO-GO`),
  - kurze Begruendung bei `NO-GO`.
- Ablage: `novapolis-dev/docs/donelog.md` (operativ) und `DONELOG.md` (Root-Ueberblick).

Beta-Tagging-Konvention (verbindlich)
-------------------------------------

- `beta_tag` Format: `beta-v<MAJOR>.<MINOR>.<PATCH>-r<YYYYMMDD-HHMM>`.
- Beispiel: `beta-v1.0.0-r20260304-2129`.
- Report-Alias in DONELOG-Eintraegen:
  - `checks_report=<checks_report_YYYYMMDD_HHMMSS.{md|json}>`
  - `beta_tag=<beta-vX.Y.Z-rYYYYMMDD-HHMM>`
- Laufzeit-/Build-Artefakte unter `outputs/` folgen demselben Suffix:
  - `<artifact>-<beta-vX.Y.Z-rYYYYMMDD-HHMM>`

Reihenfolge (kanonisch)
-----------------------

1. API starten (`novapolis_agent/run_server.py`).
2. Sim-Hub starten (`novapolis-sim/project.godot`, `Main.tscn`).
3. Vollcheck starten (`& .\.venv\Scripts\python.exe scripts/run_checks_and_report.py`).
4. Sim-Offline-Check ausfuehren (`& .\.venv\Scripts\python.exe scripts/check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency`).
5. Go/No-Go entscheiden und protokollieren.


