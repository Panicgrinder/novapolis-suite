Database Curated
=================

Dieser Bereich dient als Arbeitszone für die Aufbereitung (Curation) der Exporte aus `database-raw/99-exports/`.

Wichtige Leitlinien:
- RAW-Only: Ungefilterte Exporte bleiben unter `database-raw/99-exports/` (nicht verschieben).
- Staging: Vorläufige, manuell geprüfte Artefakte entstehen unter `database-curated/staging/`.
- Final: Abgenommene, konsolidierte Artefakte landen unter `database-curated/final/` und werden erst danach nach `database-rp/` übertragen/zusammengeführt.

Struktur:
- staging/ – In Bearbeitung (unstabil, human-in-the-loop)
- final/ – Abgenommen (stabil, referenzfähig)

Empfohlener Workflow (hochlevel):
1) Quelle(n) im `staging/manifest.json` eintragen (Status: pending).
2) Normalisieren (TXT -> normalized.txt) und optional in JSONL konvertieren.
3) Extrakte erzeugen (Fakten, Szenenanker, Charakter-/Ort-/Projekt-Notizen).
4) Manuelle Stichproben/Querprüfung (z. B. gegen PDF).
5) Status in Manifest auf `reviewed`/`approved` setzen und Artefakte nach `final/` kopieren.
6) Synchronisierung in `database-rp/` (Memory-Bundle, Charaktere, Orte, Projekte, Szenen).

Benennungsempfehlungen:
- <basename>.normalized.txt – Zeilenbereinigt, Duplikate reduziert
- <basename>.jsonl – strukturierte Form (speaker, ts?, text)
- <basename>.facts.md – extrahierte Fakten/Anker

Hinweis: Für Parser/Importer siehe `coding/tools/curation/ingest_jsonl.py` und `coding/tools/chat-exporter/`.

