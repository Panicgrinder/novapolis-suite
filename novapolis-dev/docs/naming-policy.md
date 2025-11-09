---
stand: 2025-11-06 02:47
update: Markdownlint geprüft; Format auf YAML-Frontmatter standardisiert
checks: markdownlint-cli2 (single file) PASS
---

<!-- Migration: Quelle aus dem frueheren coding-Hub, uebernommen am 2025-10-29 -->
<!-- Relocated aus dem ehemaligen Novapolis-RP Development-Hub nach `novapolis-dev/docs/naming-policy.md` am 2025-10-29 -->

Benennung – Regeln (Dateien/Ordner)
===================================

Geltungsbereich: `database-rp/**` (Admin, Canon, Characters, Locations, Inventory, Projects, Scenes)

Ziele
-----

- Lesbar, stabil, ASCII-kompatibel; Links funktionieren in allen Umgebungen.
- Einheitliche Trennung per Bindestrich.

Regeln
------

- Zeichensatz: A–Z, a–z, 0–9, Bindestrich `-`, Punkt `.` (für die Endung). Keine Leerzeichen/Unterstriche/Klammern.
- Umlaute: `ä→ae`, `ö→oe`, `ü→ue`, `ß→ss`. Großbuchstaben `Ä→Ae`, `Ö→Oe`, `Ü→Ue`.
- Trennung: Wörter mit `-` verbinden; mehrere Bindestriche vermeiden (`--` → `-`).
- Endungen: Kleinbuchstaben (`.md`, `.txt`).
- Groß-/Kleinschreibung: Eigennamen dürfen Großbuchstaben tragen (z. B. `Jonas-Merek.md`, `C6.md`, `Verbindungstunnel-D5-C6.md`).

Beispiele
---------

- OK: `Ronja-Kerschner.md`, `Verbindungstunnel-D5-C6.md`, `Novapolis-inventar.md`
- Nicht OK: `Ronja Kerschner.md`, `Novapolis_inventar.MD`, `C6 (Tunnel).md`

Durchsetzung
------------

- Linter: `coding/tools/validators/src/check-names.js` (Dry-Run in CI). Mit `--apply` werden Umbenennungen durchgeführt und Links in `database-rp/**.md` angepasst.
- Scope: Vorerst nur `database-rp/**`. `database-curated/**` bleibt unverändert (Staging/Artefaktnamen).

Vorgehen bei Altbestand
-----------------------

- Erst Dry-Run ausführen und Liste prüfen.
- Danach gezielt `--apply` verwenden (Commit in kleinem Batch), Review.

