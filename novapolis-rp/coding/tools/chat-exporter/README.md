---
stand: 2025-11-06 15:22
update: MD003 Setext + YAML Frontmatter
checks: markdownlint-cli2 PASS (single file)
---

Chat-Exporter (Browser-Konsole)
================================

Dieses Skript sammelt Chat-Nachrichten von Seiten, die Nachrichtenknoten als Elemente mit `data-message-author-role` rendern (z. B. Chat-Apps im Browser). Es scrollt automatisch weiter und stoppt, wenn 20 Sekunden keine neuen Nachrichten geladen wurden. Der Export ist speicher-optimiert: Wenn möglich, schreibt das Skript direkt in eine Datei (File System Access API). Andernfalls lädt es mehrere kleinere Teile (Chunks) herunter, um RAM zu sparen.

WICHTIG: Exporte immer nur nach `database-raw/99-exports/` speichern. Ungefilterte Daten gehören nicht in `database-rp/`.

Features
--------
- Auto-Scroll startet nach 10 Sekunden
- MutationObserver: Erfasst neue Nachrichten ohne ständige Vollscans
- Deduplizierung pro Node (keine Doppel-Exports)
- Stoppt automatisch nach 20 Sekunden ohne neue Nachrichten (oder nach 10 Minuten Maximaldauer)
- Export speicherarm:
  - Direktes Dateistreaming via File System Access API (Chrome/Edge)
  - Fallback: Chunked-Downloads (mehrere Teile) statt alles im RAM zu halten
  - TXT mit Headern und optionalen Block-Trennern

Nutzung
-------
1. Öffne die Zielseite im Browser (mit allen sichtbaren Nachrichten).
2. Öffne die Entwicklerkonsole (F12) und wechsle auf den Tab „Console“.
3. Kopiere den kompletten Inhalt von `chat-exporter.js` und füge ihn in die Konsole ein; Enter drücken.
  - Mit File System Access API wirst du nach einem Speicherort gefragt; wähle bitte `database-raw/99-exports/`.
  - Ohne FS-API lädt der Browser stattdessen mehrere Teil-Dateien (z. B. `…-part-001.txt`).
4. Warte, bis der Auto-Scroll seinen Job gemacht hat und der/die Download(s) automatisch starten.

Anpassungen
-----------
- Du kannst im Skript die `SETTINGS` anpassen (Batch-Größe, Intervalle, Timeouts, Chunk-Größe).
- Selektor für Nachrichtentext: `.markdown.prose, [data-testid="markdown"]` – passe das an deine Zielseite an, falls nötig.

Hinweise
--------
- Sicherheitslimits sind eingebaut (`MAX_SAFE`, `MAX_DURATION_MS`), um Hänger zu vermeiden.
- Weniger RAM-Verbrauch durch Streaming/Chunks; glattes Scrollen (smooth) ist aus Performancegründen deaktiviert.
- Manche Seiten laden Inhalte erst beim Scrollen langsam nach; der Auto-Scroll ist darauf optimiert.
- Dieses Tool arbeitet rein im Browser – keine Daten werden ins Netz gesendet.

Raw → Curated Flow:
- Roh-Exporte liegen ausschließlich unter `database-raw/99-exports/`.
- Für die Übernahme ins RP (z. B. `database-rp/06-scenes/`) erst ein Curation-/Ingest-Script verwenden (siehe `coding/tools/curation/`).

