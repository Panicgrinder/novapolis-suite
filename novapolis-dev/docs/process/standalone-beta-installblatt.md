---
stand: 2026-03-19 11:09
update: Extern lesbares Installblatt fuer die Standalone-Beta mit Voraussetzungen, Setup, Start, Verifikation und Troubleshooting angelegt.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260318_052318.md
---

Standalone-Beta Installblatt
============================

Ziel
----

Dieses Dokument beschreibt den kuerzesten reproduzierbaren Weg, um die Standalone-Beta lokal zu starten und zu verifizieren, ohne implizites Projektwissen vorauszusetzen.

Getesteter Zielpfad
-------------------

- Python-Umgebung unter `.venv`
- API-Start ueber `novapolis_agent/run_server.py`
- Sim-Hub ueber `novapolis-sim/project.godot` und `Main.tscn`
- Verifikation ueber `scripts/run_checks_and_report.py` plus `scripts/check_sim_epoch_assets.py`

Voraussetzungen
---------------

- Windows-System mit PowerShell
- Git
- Python 3 mit lokaler virtueller Umgebung unter `.venv`
- Godot 4.x fuer `novapolis-sim/project.godot`

Workspace vorbereiten
---------------------

Im Repo-Root ausfuehren:

```powershell
Set-Location .
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
```

Optional:

```powershell
& .\.venv\Scripts\python.exe -m pip install -e packages/novapolis_common
```

Beta starten
------------

1. API starten:

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\run_server.py
```

Erwartung:

- Der Prozess bleibt aktiv.
- Die lokale API ist anschliessend unter `http://127.0.0.1:8000/docs` erreichbar.

2. Sim-Hub starten:

- Godot 4 oeffnen.
- `novapolis-sim/project.godot` laden.
- `Main.tscn` ausfuehren.

Erwartung:

- Der Hub startet ohne zusaetzliche Assets oder manuelle Datenkopien.
- Ohne API bleibt die Sim responsiv; mit API aktualisieren sich Status und Chat-Funktionen.

Verifikation
------------

Im Repo-Root in fester Reihenfolge ausfuehren:

```powershell
& .\.venv\Scripts\python.exe scripts\run_checks_and_report.py
& .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency
```

Erwartetes Ergebnis:

- `scripts/run_checks_and_report.py` meldet `overall=PASS`.
- `scripts/check_sim_epoch_assets.py` meldet keine harten Fehler (`fail:0`).

Go / No-Go
----------

- `GO`: beide Verifikationsschritte sind gruen.
- `NO-GO`: mindestens ein Pflichtcheck faellt oder der Sim-Check meldet harte Fehler.

Bei einem echten Entscheid muessen Reportpfad und Ergebnis in `novapolis-dev/docs/donelog.md` und `DONELOG.md` protokolliert werden.

Troubleshooting
---------------

API startet nicht
-----------------

- Pruefen, ob `.venv` existiert und die Dependencies installiert sind.
- Den API-Start immer aus dem Repo-Root mit dem kanonischen Aufruf ausfuehren.

`/docs` ist nicht erreichbar
----------------------------

- Pruefen, ob `novapolis_agent/run_server.py` noch aktiv laeuft.
- Falls Port oder Firewall lokal blockieren, zuerst die lokale Erreichbarkeit `127.0.0.1:8000` pruefen.

Godot startet das falsche Projekt
---------------------------------

- Sicherstellen, dass wirklich `novapolis-sim/project.godot` geladen wurde.
- Nicht das historisch archivierte verschachtelte Projekt unter `Backups/` verwenden.

Checks schlagen fehl
--------------------

- Zuerst den Pfad zum letzten Report unter `.tmp/results/reports/` notieren.
- Danach nur die gemeldeten Blocker beheben, nicht parallel Nebenbaustellen oeffnen.

Schnellreferenz
---------------

```powershell
# Setup
python -m venv .venv
& .\.venv\Scripts\python.exe -m pip install -r requirements.txt
& .\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt

# API
& .\.venv\Scripts\python.exe novapolis_agent\run_server.py

# Verifikation
& .\.venv\Scripts\python.exe scripts\run_checks_and_report.py
& .\.venv\Scripts\python.exe scripts\check_sim_epoch_assets.py --repo-root . --allow-empty --check-slot-consistency
```

Verwandte Dokumente
-------------------

- `README.md`
- `novapolis-dev/docs/process/standalone-beta-gates.ssot.md`
- `novapolis_agent/README.md`
- `novapolis-sim/README.md`