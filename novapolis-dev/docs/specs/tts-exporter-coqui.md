---
stand: 2026-03-05 01:00
update: Spec auf Iststand der implementierten Coqui-Exporter-CLI im Agent-Modul nachgezogen (kein Platzhalter-Narrativ).
checks: scripts/run_checks_and_report.py overall=FAIL; markdownlint=PASS; frontmatter=PASS; path-portability=FAIL; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260305_005843.md
---

TTS-Exporter (Build-Time) - Coqui → OGG
======================================

Ziel: Vorproduzierte Audio-Summaries pro Epoche/Slot (world_log/pc_log) offline erzeugen. Diese Seite dokumentiert den aktuellen CLI-Vertrag der implementierten Exporter-Entry im Agent-Modul.

- Scope: Build-Time Batch (kein Live-TTS). Live-Dialoge laufen separat ueber Runtime-Endpunkte und sind hier nicht Bestandteil.
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

CLI (Iststand)
--------------

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\scripts\tts_coqui_export.py `
  --input "novapolis-rp/database-rp/02-epoch/epoch03/slot14_pc.txt" `
  --voice-map "novapolis_agent/config/tts_voice_map.sample.yaml" `
  --model-id "coqui/xtts-v2" `
  --allowlist "novapolis_agent/config/tts_model_allowlist.json" `
  --lang de `
  --output-dir "novapolis-sim/assets/voiceovers/de" `
  --dry-run
```

Verfuegbare Parameter (Iststand):

- `--input`: Pfad zu `jsonl|yaml|txt` Quelle.
- `--voice-map`: YAML-Mapping fuer Sprecherzuordnung.
- `--model-id`: Modellkennung, wird gegen Allowlist validiert.
- `--allowlist`: JSON-Allowlist fuer freigegebene Modelle.
- `--lang`: Sprachcode (Default `de`).
- `--output-dir`: Zielordner fuer OGG-Exports.
- `--dry-run`: validiert Vertrag/Policies ohne Synthese.
- `--manifest`: Dateiname fuer Laufmanifest im Zielordner.

Umgebung/Prereqs (Iststand)
---------------------------

- Python Env: Root-`.venv` mit Agent-Abhaengigkeiten.
- Compliance-Gate: Modell muss in `novapolis_agent/config/tts_model_allowlist.json` enthalten sein.
- Lokaler Cache/Manifest wird durch Exporter-Vertrag gesteuert.
- Windows/PowerShell kompatible Pfade/Beispiele

VS Code Task
------------

- Label: `TTS: export (coqui)`.
- Aufruf: `novapolis_agent/scripts/tts_coqui_export.py --help` (operativer Entrypoint vorhanden).

Notes
-----

- Live-Service Schnittstelle (separat): `/tts/health`, `/tts/voices`, `/tts/synthesize`.
- OGG bleibt Build-Time-Ziel fuer Sim-Assets; WAV ist nicht Teil des aktuellen Exporter-Vertrags.

Try it
------

1. Menü: Terminal -> Run Task...
2. Waehle: `TTS: export (coqui)`.
3. Fuer einen realen Dry-Run im Terminal:

```powershell
& .\.venv\Scripts\python.exe novapolis_agent\scripts\tts_coqui_export.py --help
```





