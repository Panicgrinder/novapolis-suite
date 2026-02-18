---
stand: 2026-02-18 07:03
update: Archivierungs-Feinschliff ergänzt (Outputs->Backups Gruppierung, Rotations-Cadence, sichere Apply-Regeln) und Dry-Run-Befund dokumentiert.
checks: "F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe -m scripts.rotate_backups --include-subdirectories DRY-RUN PASS (2026-02-18 06:58, Keep 7 / Delete 75); F:/VS-Code-Workspace/Main/.venv/Scripts/python.exe -m scripts.update_backups_manifest --include-subdirectories PASS (2026-02-18 06:58, Entries 82)"
---

Backups & Releases Leitfaden
============================

Dieses Dokument beschreibt Pflege und Verifikation der Inhalte im Ordner `Backups/`.

Struktur (Soll)
---------------

- `manifest.v1.json` - maschinenlesbare Übersicht aller Artefakte (SHA-256, Timestamps, Metadaten)
- `manifest.v1.sha256sum.txt` - Prüfliste im klassischen `sha256sum`-Format
- `rotation.log` - Protokoll ausgeführter Löschläufe
- `README.md` - vorliegendes Dokument
- `AUDIT.md` - Dokumentierter Status/Empfehlungen
- Backup-Artefakte (z. B. `*.bundle`, `*.zip`, `*.tar.gz`, `*.7z`)

Manifest erzeugen
------------------

Das Skript `scripts/update_backups_manifest.py` erstellt Manifest und Checksummen-Datei.

```powershell
& .\.venv\Scripts\python.exe -m scripts.update_backups_manifest
```

Optional:
- `<backups_path>` als Argument zum Überschreiben des Ordners
- `--include-subdirectories` für rekursive Auflistung

Nach dem Lauf liegen `manifest.v1.json` und `manifest.v1.sha256sum.txt` aktualisiert im `Backups/`-Ordner. Beide Dateien sind deterministisch (Sortierung nach Dateiname, Kleinbuchstaben-SHA-256).

Checksummen verifizieren
------------------------

Die Checksummen-Datei kann wie gewohnt geprüft werden. Beispiel (PowerShell):

```powershell
Get-ChildItem Backups -File | ForEach-Object {
    $expected = Select-String -Path Backups/manifest.v1.sha256sum.txt -Pattern "$_" | Select-Object -First 1
    if ($null -eq $expected) { return }
    $hash = Get-FileHash -Algorithm SHA256 -LiteralPath $_.FullName
    "{0}  {1}" -f $hash.Hash.ToLower(), $_.Name
}
```

Alternativ unter WSL/Unix: `sha256sum -c manifest.v1.sha256sum.txt`.

Rotation ausführen
-------------------

Das Skript `scripts/rotate_backups.py` implementiert die tiered Retention (Daily/Weekly/Monthly/Yearly) mit Sicherheitsnetz (mindestens 5 neueste Artefakte).

```powershell
# Dry-run (empfohlen)
& .\.venv\Scripts\python.exe -m scripts.rotate_backups

# Löschlauf anwenden
& .\.venv\Scripts\python.exe -m scripts.rotate_backups --apply
```

Standardparameter:
- Daily: 14 Tage
- Weekly: 8 Wochen (über Daily hinaus)
- Monthly: 6 Monate (über Weekly hinaus)
- Yearly: 2 Jahre (über Monthly hinaus)
- MinimumKeep: 5 Artefakte (älteste zuerst schützen)

Anpassungen über Parameter `--daily-retention-days`, `--weekly-retention-weeks`, `--monthly-retention-months`, `--yearly-retention-years`, `--minimum-keep`. Mit `--include-subdirectories` werden auch Unterordner berücksichtigt.

Löschläufe schreiben ein Logfile `rotation.log` im `Backups/`-Ordner (UTC-Timestamp, Liste der entfernten Dateien).

Archivierungs-Feinschliff (Outputs + Rotation)
----------------------------------------------

Status 2026-02-18 (evidenzbasiert):
- Rotations-Dry-Run rekursiv (`--include-subdirectories`) durchgeführt: `Keep: 7`, `Delete: 75`.
- Haupttreffer lagen in archivierten Sim-Caches (`novapolis-sim-archived-20251104/.godot/**`).
- Ergebnis: Kein `--apply` im rekursiven Scope; stattdessen sichere Regel „Apply nur Top-Level-Backups".

Sichere Apply-Regel:
- **Standard:** `scripts.rotate_backups.py` ohne `--include-subdirectories`.
- **Rekursiv:** nur als Dry-Run für Sichtprüfung; `--apply --include-subdirectories` ausschließlich nach expliziter Freigabe.

Outputs -> Backups Gruppierung (MVP-Prozess)
-------------------------------------------

Ziel: ältere `outputs/lora-*` Läufe paketieren und nach `Backups/model-runs/` auslagern, ohne aktive Läufe zu berühren.

Empfohlener Ablauf (manuell, nicht-destruktiv zuerst):

```powershell
# 1) Kandidatenliste (älter als 14 Tage)
Get-ChildItem outputs -Directory -Filter 'lora-*' |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-14) } |
    Select-Object FullName, LastWriteTime
```

```powershell
# 2) Bündeln in Backups/model-runs (pro Datum/Batch)
New-Item -ItemType Directory -Force -Path Backups/model-runs | Out-Null
Compress-Archive -Path "outputs/lora-202511*" -DestinationPath "Backups/model-runs/lora-202511-batch.zip"
```

```powershell
# 3) Nach dem Bündeln Manifest erneuern (rekursiv)
& .\.venv\Scripts\python.exe -m scripts.update_backups_manifest --include-subdirectories
```

```powershell
# 4) Rotation nur auf Top-Level sicher anwenden
& .\.venv\Scripts\python.exe -m scripts.rotate_backups --apply
```

Cadence (empfohlen)
-------------------

- Wöchentlich: Outputs-Kandidatenliste + ggf. Bündelung nach `Backups/model-runs/`.
- Wöchentlich danach: `update_backups_manifest --include-subdirectories`.
- Monatlich: `rotate_backups` Dry-Run; Apply nur Top-Level.
- Quartalsweise: `AUDIT.md` gegen Manifest/rotation.log querprüfen.

Restore-Checkliste
------------------

1. Manifest aktualisieren (`update_backups_manifest.py`), falls nicht frisch.
2. Checksummen verifizieren (`manifest.v1.sha256sum.txt`).
3. Gewünschtes Artefakt extrahieren/restore durchführen (Format beachten, z. B. `git bundle verify` oder `tar -xf`).
4. Optional: Nach dem Restore Manifest erneut erzeugen, um Veränderungen festzuhalten.

Optional: Verschlüsselung
--------------------------

Für externe/off-site Ablage kann Verschlüsselung via AGE oder GPG ergänzt werden. Schlüsselverwaltung erfolgt außerhalb des Repos; dieses Dokument verweist lediglich auf den zusätzlichen Schritt.


