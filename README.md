# Novapolis Suite

Die Novapolis Suite fasst Agent-Backend, Rollenspiel-Datenbasis, Dev-Dokumentation und Simulation unter einem gemeinsamen Repository zusammen. Ziel ist, doppelte Module zu konsolidieren, Arbeitsablaeufe zu vereinheitlichen und einen schnellen Ueberblick ueber alle laufenden Aufgaben zu behalten.

## Projekte im Repository

- **novapolis_agent** – FastAPI-Backend, Eval-Tooling und Trainingsskripte fuer den produktiven Novapolis Agent.
- **novapolis-rp** – Weltbau-Daten, Rollenspiel-Workflows und begleitende Tools (ohne Agent-Laufzeit).
- **novapolis-dev** – Kuratierte Datensaetze, Prozess- und Policy-Dokumentation als Arbeits-Hub.
- **novapolis-sim** – Godot-Szene und Skripte fuer den Simulations-Prototypen.

## Gemeinsames Python-Paket

Geteilte Python-Helfer leben in `packages/novapolis_common`. Installiere das Repository als Editable, damit das Paket im Interpreter verfuegbar ist:

```powershell
Set-Location "F:/VS Code Workspace/Main"
F:\VS Code Workspace\Main\.venv\Scripts\python.exe -m pip install -e .
```

Module, die aktuell mehrfach in den Projekten vorkommen, sollten nach `packages/novapolis_common` wandern. Projektspezifische Verdrahtung (API, Policies, Szenenlogik) verbleibt in den jeweiligen Ordnern.

## Abhaengigkeiten

Die Root-Dateien `requirements.txt` und `requirements-dev.txt` sammeln die Pins aller Teilprojekte. Fuer einzelne Bereiche koennen weiterhin die lokalen Requirements-Dateien genutzt werden.

## Zentrale Arbeitsrichtlinien

- `.github/copilot-instructions.md` enthaelt die konsolidierten Behaviour-Vorgaben fuer alle Teilprojekte.
- Root `TODO.md` und `DONELOG.md` liefern einen Gesamtueberblick ueber offene Aufgaben und erledigte Arbeiten ohne die Projekt-spezifischen Dateien oeffnen zu muessen.
- Nicht-triviale Aenderungen werden weiterhin im jeweiligen DONELOG des Projekts dokumentiert (`novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`).
- Der Agent-Workspace nutzt jetzt den Paketnamen `novapolis_agent`; aeltere Referenzen mit Bindestrich bitte bei Gelegenheit bereinigen (siehe Aufgaben in `TODO.md`).

## Aktuelle Statusdokumente

- [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md) – Stand 2025-11-01, fasst Health-Checks, Risiken und Artefakte zusammen.
- [`TODO.md`](TODO.md) – Zentraler Aufgabenueberblick (Stand 2025-11-01) inklusive Folgeaufgaben fuer Tree-Snapshots.
- [`workspace_tree_full.txt`](workspace_tree_full.txt) – Vollstaendiger Verzeichnisbaum (Stand 2025-10-31; naechste Regeneration geplant).

## Naechste Schritte

1. Doppelte Module identifizieren und schrittweise in `packages/novapolis_common` verschieben.
2. Tests und Typpruefungen nach jeder Migration laufen lassen (`pytest`, `pyright`, `mypy`).
3. Nach jedem groesseren Schritt DONELOG aktualisieren und Root-Uebersichten synchron halten.
