---
stand: 2025-11-16 06:52
update: Frontmatter auf YAML migriert; markdownlint PASS
checks: markdownlint-cli2 PASS
---

TTS-Exporter (Build-Time) - Coqui → OGG
======================================

Ziel: Vorproduzierte Audio-Summaries pro Epoche/Slot (world_log/pc_log) offline erzeugen. Diese Seite definiert den Kontrakt und die Aufrufe - die eigentliche Implementierung folgt im Agent/Tools.

- Scope: Build-Time Batch (kein Live-TTS). Live-Dialoge laufen separat (Runtime-Service) und sind hier nicht Bestandteil.
- Referenzen: `novapolis-dev/docs/specs/annotation-spec.md` (Audio-Namensschema), `novapolis-dev/docs/specs/scheduler-spec.md` (Epochen/Slots).

Kontrakt (Kurz)
---------------

- Input
  - Quelle: Textdateien/Chunks (z. B. stündliche Summaries aus `world_log`/`pc_log`) - UTF-8
  - Stimme: Preset-ID oder Voice-Config (z. B. `de-female-01`)
  - Format: OGG/Vorbis (mono, 22.05-24 kHz; final TBD)
  - Zielordner: pro Epoche/Slot
- Output
  - Datei je Slot nach Schema: `epoch{dd}_slot{hh}_{channel}.ogg` (z. B. `epoch03_slot14_pc.ogg`)
  - Metadatei optional: `*.json` mit Hash(Text+Voice), Dauer (Sek.), Samplingrate
- Erfolgskriterien
  - Deterministische Cache-Treffer (Hash(Text+Voice) → identischer Dateiname/Reuse)
  - Idempotent: Wiederholter Lauf ohne Textänderung erzeugt keine neuen Dateien
  - Robust gegen leere/zu kurze Texte (skip/0-Byte verhindern)

CLI-Skizze (geplant)
--------------------

```powershell
# Noch nicht implementiert - Platzhalter-Signatur
python novapolis_agent/scripts/tts_export_coqui.py `
  --input "novapolis-rp/database-rp/02-epoch/epoch03/slot14_pc.txt" `
  --voice de-female-01 `
  --sr 24000 `
  --out "outputs/audio/epoch03/epoch03_slot14_pc.ogg"
```

Parameter (geplant):
- --input: Pfad zu Textdatei oder Ordner (batch)
- --voice: Voice-Preset/Config
- --sr: Sample-Rate (Hz)
- --out/--out-dir: Zieldatei oder Zielordner (bei Batch)
- --cache: Pfad für Cache (Default: `.cache/tts/`)
- --normalize: einfache Normalisierung (Trim, Unicode NFC, Whitespace)

Umgebung/Prereqs (geplant)
--------------------------

- Python Env: `novapolis_agent/requirements.txt` wird um Coqui-Pakete ergänzt (später)
- Lokaler Cache: `.cache/tts/` (Hash(Text+Voice) → OGG)
- Windows/PowerShell kompatible Pfade/Beispiele

VS Code Task (Skeleton)
-----------------------

Diese Task dient als Platzhalter, bis das Skript existiert. Sie schreibt nur eine TODO-Meldung ins Terminal.

- Label: `TTS: export (Coqui→OGG)`
- Gruppe: build
- Aufruf: PowerShell `Write-Host` Hinweis

Notes
-----

- Live-Service Schnittstelle (separat): Text→Audio-Stream, Voice-Preset, OGG Output
- Audio-Lautheit/Limiter erst in der Implementierung definieren (RMS/LUFS Zielwerte)
- OGG vs. WAV: OGG bevorzugt (Dateigröße); WAV optional für Mastering

Try it (Task)
-------------

So startest du den Platzhalter in VS Code:

1) Menü: Terminal → Run Task…
2) Wähle: `TTS: export (Coqui→OGG)`
3) Ergebnis: Eine Hinweiszeile im gemeinsamen Tasks-Terminal; keine Dateien werden erzeugt.



