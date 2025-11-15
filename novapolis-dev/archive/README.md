---
stand: 2025-11-15 06:26
update: Archiv-Anleitung ergänzt; Ziele & Ablauf präzisiert
checks: keine
---

Archiv-Ordner: Zweck & Ablauf
================================

Dieser Ordner (`novapolis-dev/archive`) sammelt vollständig abgeschlossene Inhalte aus den Arbeitsbereichen. Ziel ist eine reproduzierbare, revisionssichere Ablage von erledigten TODOs, Reports und Skripten.

Wichtige Unterordner (Erklärung / Verwendung)
- `docs/donelogs` : Fertige DONELOG-Einträge oder komplette DONELog-Dateien (module-spezifische Receipts).
- `docs/others`  : Sonstige archivierte Dokumente (Guides, READMEs ohne aktive Pflege).
- `docs/todos`   : Vollständig abgeschlossene TODO-Listen (Archiv-Kopien).
- `reports/<script-name>/` : Je Skript ein eigener Ordner mit allen erzeugten Reports (z. B. `reports/scan_links/`).
- `scripts/.ps1-scripts`  : Archivierte PowerShell-Skripte.
- `scripts/.py-scripts`   : Archivierte Python-Skripte.
- `scripts/wrapper`       : Archivierte Wrapper-Skripte (z. B. `run_checks_and_report.py` Kopien für Audit).

Grundprinzip der Archivierung (manuell oder per Script)
------------------------------------------------------
Für jede zu archivierende Datei gilt dieser Ablauf (exakt und reproduzierbar):

1) Ziel wählen
    - Wähle einen der gültigen Archive-Ziele (Beispiele):
        - `novapolis-dev/archive/docs/donelogs`
        - `novapolis-dev/archive/docs/others`
        - `novapolis-dev/archive/docs/todos`
        - `novapolis-dev/archive/reports/<script-name>/`
        - `novapolis-dev/archive/scripts/.ps1-scripts`
        - `novapolis-dev/archive/scripts/.py-scripts`
        - `novapolis-dev/archive/scripts/wrapper`

2) Kopie erzeugen und Frontmatter ergänzen
    - Erzeuge eine Kopie der Originaldatei im gewählten Ziel und ergänze eine YAML-Frontmatter (oberste Datei-Zeilen) mit mindestens folgenden Schlüsseln:

        ```yaml
        ---
        archived: true
        archived_at: "YYYY-MM-DD HH:mm"
        original_path: "<relativer/origin-pfad>"
        original_sha256: "<sha256-hash-der-originaldatei>"
        ---
        ```

    - `archived_at` MUSS die lokale Systemzeit im Format `YYYY-MM-DD HH:mm` verwenden.

3) Integritätsvergleich (Original vs. Archiv-Kopie)
    - Vergleiche die Kopie mit dem Original so, dass nur die zusätzliche Frontmatter toleriert wird. Vorgehen (empfohlen):
     - a. Berechne SHA256 des Originals: `sha256_orig`.
     - b. Extrahiere aus der Archiv-Kopie den Body ohne Frontmatter (alle Zeilen nach dem schließenden `---`) und berechne SHA256 dieser Body-Datei: `sha256_arch_body`.
     - c. Vergleiche `sha256_orig == sha256_arch_body`. Wenn gleich → Inhalt ist 1:1 (nur Frontmatter wurde ergänzt).

    - Alternativ (einfacher): Nutze ein Skript, das Frontmatter erkennt und beim Vergleich ignoriert (siehe Beispiele unten).

4) Original entfernen
    - Wenn der Integritätscheck PASS ergibt, entferne das Original aus seinem Ursprungsort. Behalte immer eine Kopie im Archiv-Ordner.

5) DONELOG / Audit aktualisieren
    - Füge einen Receipt-Eintrag in die passenden DONELOG(s) ein. Mögliche Ziele (je nach Modul):
        - `novapolis-dev/docs/DONELOG.md` (zentrale Archiv-DONELOGs)
        - `novapolis_agent/docs/DONELOG.txt` (Agent-spezifisch)
        - oder in `novapolis-dev/archive/docs/donelogs/<module>-archive-donelog.md` (je Archivvorgang eine Datei)

    - Ein Receipt sollte mindestens enthalten:
        - Timestamp (`YYYY-MM-DD HH:mm`), Autor, Aktion (z. B. `archived file X to <archive-path>`), `original_path`, `archived_path`, `original_sha256`, Prüfstatus (`IntegrityCheck: PASS`)

Skriptbeispiele
---------------
PowerShell (Beispiel: archiviere `README.md` → `docs/others`)

```powershell
$orig = 'novapolis-dev/README.md'
$archdir = 'novapolis-dev/archive/docs/others'
mkdir $archdir -Force | Out-Null
$time = (Get-Date -Format 'yyyy-MM-dd HH:mm')
$sha = (Get-FileHash -Algorithm SHA256 $orig).Hash
$basename = [IO.Path]::GetFileName($orig)
$archpath = Join-Path $archdir $basename

# Lese Originalinhalt
$origBody = Get-Content -Raw $orig -Encoding UTF8

# Schreibe Archiv-Kopie mit Frontmatter
@"---
archived: true
archived_at: "$time"
original_path: "$orig"
original_sha256: "$sha"
---
"@ | Out-File -FilePath $archpath -Encoding UTF8

$origBody | Out-File -FilePath $archpath -Encoding UTF8 -Append

# Integritätsprüfung: Body der Archiv-Kopie extrahieren und SHA vergleichen
$archBody = Get-Content -Raw $archpath -Encoding UTF8 -Delimiter "`n" | Select-String -Pattern '(?s)(?<=---\s).*' -NotMatch
# (vereinfachte Variante unten empfohlen - besser: use a script that strips frontmatter before hashing)

"Archiv erstellt: $archpath (original sha256: $sha)"
```

Python (robuster, empfohlen für batch/CI)

```python
import pathlib, hashlib, datetime, sys

def sha256_text_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

orig = pathlib.Path('novapolis-dev/README.md')
archdir = pathlib.Path('novapolis-dev/archive/docs/others')
archdir.mkdir(parents=True, exist_ok=True)
time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
sha = sha256_text_bytes(orig.read_bytes())
archpath = archdir / orig.name

front = f"---\narchived: true\narchived_at: \"{time}\"\noriginal_path: \"{orig.as_posix()}\"\noriginal_sha256: \"{sha}\"\n---\n\n"
archpath.write_text(front + orig.read_text(encoding='utf-8'), encoding='utf-8')

# Integritäts-Check: vergleiche sha(orig) mit sha(archpath without frontmatter)
text = archpath.read_text(encoding='utf-8')
if text.startswith('---'):
    # strip frontmatter
    parts = text.split('\n---\n', 1)
    body = parts[1] if len(parts) > 1 else ''
else:
    body = text

if sha256_text_bytes(body.encode('utf-8')) == sha:
    print('IntegrityCheck: PASS')
else:
    print('IntegrityCheck: FAIL')
    sys.exit(2)

print(f"Archived {orig} -> {archpath} (sha={sha})")
```

Empfehlungen & Regeln
---------------------
- Immer zuerst eine Kopie in den Archiv-Ordner schreiben, niemals direkt verschieben ohne Prüfung.
- `archived_at` immer mit lokaler Zeit im Format `YYYY-MM-DD HH:mm` setzen.
- Archivierte Skripte: `.ps1` nach `scripts/.ps1-scripts`, `.py` nach `scripts/.py-scripts`, Wrapper in `scripts/wrapper`.
- Reports: lege pro Reporterzeuger einen eigenen Ordner unter `reports/` an (z. B. `reports/scan_links/`) und behalte alle erzeugten Artefakte dort.
- Für Massen-Archivierungen erst einen Dry-Run durchführen und Receipts sammeln.

Hinweis zu Audit & Postflight
-----------------------------
Nach jeder seriösen Archiv-Operation ist ein kurzer Postflight-Receipt zu erzeugen (siehe Projekt-Policy `.github/copilot-instructions.md`). Der Receipt kommt idealerweise in `novapolis-dev/archive/docs/donelogs/` oder in der zentralen DONELOG-Datei des betreffenden Moduls.

Beispiel-Receipt-Eintrag (kurz):

```text
2025-11-15 06:26 - archived: novapolis-dev/README.md -> novapolis-dev/archive/docs/others/README.md; sha=...; IntegrityCheck=PASS; by=yourname
```

Wenn du willst, kann ich dieses README in eine PR packen oder ein kleines Automatisierungs-Skript (`scripts/archiver.py`) erzeugen, das Dry-Run / Apply-Modi bietet und automatisch Receipts schreibt. Sag mir kurz, welche Option du bevorzugst.

---
archived_notice: Anleitung ergänzt (automatisch, Agent)


