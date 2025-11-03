# GPT Hybrid Metadata

Dieses Tool erzeugt zu jeder Markdown-Datei (`*.md`) eine gleichnamige JSON-Metadatendatei im selben Ordner.

- Markdown bleibt unverändert (Inhalt/Links unangetastet)
- Ordnerstruktur bleibt erhalten
- JSON-Shape:

```json
{
  "chapter": "",
  "characters": [],
  "location": "",
  "tags": [],
  "source": "relative/path/to/file.md"
}
```

## Nutzung

- Dry-Run (zeigt nur an, was erstellt würde):

```powershell
node coding/tools/metadata/init-metadata.js --dry-run
```

- Schreiben (legt fehlende JSON-Dateien an):

```powershell
node coding/tools/metadata/init-metadata.js
```

- Overwrite (vorhandene JSON-Dateien überschreiben):

```powershell
node coding/tools/metadata/init-metadata.js --overwrite
```

> Hinweis: Ordner wie `node_modules/`, `.git/`, `.venv/` und `database-raw/99-exports/` werden übersprungen.

## Integration mit lokalem GPT Agent (persistentes Gedächtnis)

- Agent liest/aktualisiert die JSON-Dateien neben den `.md`-Dateien.
- Empfohlen: Agent schreibt nur Felder wie `chapter`, `characters`, `location`, `tags` oder zusätzliche Felder (z. B. `storyState`, `relations`, `summary`).
- Markdown-Dateien bleiben Quelle der Wahrheit für den Textinhalt; JSON hält Struktur/State.

## Tipps

- Keine bestehenden JSONs überschreiben, außer wenn bewusst gewünscht (Flag `--overwrite`).
- Für Batch-Läufe in VS Code kann ein Task genutzt werden (siehe `.vscode/tasks.json`).

