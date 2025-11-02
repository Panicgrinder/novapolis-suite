---
stand: 2025-11-02 18:23
update: YAML-Frontmatter ergänzt
checks: markdownlint-cli2 PASS
---

# Novapolis Suite

Die Novapolis Suite fasst Agent-Backend, Rollenspiel-Datenbasis, Dev-Dokumentation und Simulation unter einem gemeinsamen Repository zusammen. Ziel ist, doppelte Module zu konsolidieren, Arbeitsablaeufe zu vereinheitlichen und einen schnellen Ueberblick ueber alle laufenden Aufgaben zu behalten.

## Projekte im Repository

- **novapolis_agent** – FastAPI-Backend, Eval-Tooling und Trainingsskripte fuer den produktiven Novapolis Agent.
- **novapolis-rp** – Weltbau-Daten, Rollenspiel-Workflows und begleitende Tools (ohne Agent-Laufzeit).
- **novapolis-dev** – Kuratierte Datensaetze, Prozess- und Policy-Dokumentation als Arbeits-Hub.
- **novapolis-sim** – Godot-Szene und Skripte fuer den Simulations-Prototypen.

## Gemeinsames Python-Paket

Geteilte Python-Helfer leben in `packages/novapolis_common`. Installiere das Shared‑Paket bei Bedarf als Editable (nicht mehr das gesamte Repo):

```powershell
Set-Location "F:/VS Code Workspace/Main"
# venv aktiv (falls noch nicht):
F:/VS Code Workspace/Main/.venv/Scripts/Activate.ps1

# Dependencies (Root):
F:\VS Code Workspace\Main\.venv\Scripts\python.exe -m pip install -r requirements.txt
F:\VS Code Workspace\Main\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt

# Optional: Shared-Paket als Editable
F:\VS Code Workspace\Main\.venv\Scripts\python.exe -m pip install -e packages/novapolis_common
```

Module, die aktuell mehrfach in den Projekten vorkommen, sollten nach `packages/novapolis_common` wandern. Projektspezifische Verdrahtung (API, Policies, Szenenlogik) verbleibt in den jeweiligen Ordnern. Packaging/Build‑Konfigurationen verbleiben in den Modul-/Paketpfaden; das Root `pyproject.toml` ist tools‑only.

## Abhaengigkeiten

Die Root-Dateien `requirements.txt` und `requirements-dev.txt` sammeln die Pins aller Teilprojekte. Fuer einzelne Bereiche koennen weiterhin die lokalen Requirements-Dateien genutzt werden.

## Zentrale Arbeitsrichtlinien

- `.github/copilot-instructions.md` enthaelt die konsolidierten Behaviour-Vorgaben fuer alle Teilprojekte.
- Root `todo.root.md` und `DONELOG.md` liefern einen Gesamtueberblick ueber offene Aufgaben und erledigte Arbeiten ohne die Projekt-spezifischen Dateien oeffnen zu muessen.
- Nicht-triviale Aenderungen werden weiterhin im jeweiligen DONELOG des Projekts dokumentiert (`novapolis_agent/docs/DONELOG.txt`, `novapolis-dev/docs/donelog.md`).
- Der Agent-Workspace nutzt jetzt den Paketnamen `novapolis_agent`; aeltere Referenzen mit Bindestrich bitte bei Gelegenheit bereinigen (siehe Aufgaben in `todo.root.md`).

## Workspace öffnen

1. VS Code über den Root-Ordner `Main/` öffnen (Single‑Root). Die frühere Multi‑Root‑Workspace-Datei wird nicht mehr verwendet.
2. Workflows laufen ausschließlich zentral aus dem Root (`/.github/workflows`). Modulverzeichnisse enthalten keine eigenen `.github/workflows` mehr.
3. Automatisierte Läufe erfolgen über das Tasks-Panel (Shared‑Panel); spontane Shell‑Kommandos gehören ins User‑Terminal.

### Hinweise für Mitarbeit (Moduswechsel & Stop‑Gate)

- Moduswahl: Redaktion/Kanon bitte im General‑Modus (GPT‑5) arbeiten; Code‑Aufgaben (Skripte/Validatoren, Tests/CI, API/Services) im Codex‑Modus.
- Details & Regeln: siehe `.github/copilot-instructions.md` (Abschnitt „Modell‑Profile & Moduswechsel“ und „STOP‑Gate vor Code‑Aktionen“); Spiegel im Dev‑Hub: `novapolis-dev/docs/copilot-behavior.md`.
- Stop‑Gate: Vor Code‑Aktionen wird ein hartes Stop‑Gate gesetzt (explizit „Wechsel: Modus Codex“ oder „Weiter: Modus General“).
- Erinnerungen: Bei Code‑Triggern weise ich auf den Moduswechsel hin; „Bitte nicht erinnern“ deaktiviert Hinweise bis zur Reaktivierung.
- Aktueller Status (Modus/Stop‑Gate): siehe `WORKSPACE_STATUS.md`.
 - Unklarheiten‑STOP: „Grün“ gilt nur bis zur nächsten Abweichung/Unsicherheit – dann STOP, Rückfrage, weiter nach Freigabe. Details: `.github/copilot-instructions.md` → „Unklarheiten‑STOP (global, immer gültig)“.

## Aktuelle Statusdokumente

- [`WORKSPACE_STATUS.md`](WORKSPACE_STATUS.md) – Stand 2025-11-02, fasst Health-Checks, Risiken und Artefakte zusammen.
- [`todo.root.md`](todo.root.md) – Zentraler Aufgabenueberblick (Stand 2025-11-02) inklusive Folgeaufgaben fuer Tree-Snapshots.
- [`workspace_tree_full.txt`](workspace_tree_full.txt) – Vollstaendiger Verzeichnisbaum (Stand 2025-11-02 02:11; regenerierbar via Tasks `Workspace tree: full/directories/summary (dirs)`).

## Naechste Schritte

1. Doppelte Module identifizieren und schrittweise in `packages/novapolis_common` verschieben.
2. Tests und Typpruefungen nach jeder Migration laufen lassen (`pytest`, `pyright`, `mypy`).
3. Nach jedem groesseren Schritt DONELOG aktualisieren und Root-Uebersichten synchron halten.
