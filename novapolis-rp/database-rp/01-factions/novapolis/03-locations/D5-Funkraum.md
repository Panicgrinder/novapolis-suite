---
stand: 2026-01-14 12:32
update: "Neu: POI (Funkraum) ergänzt. Receipts aktualisiert (Gates PASS)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 12:32); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:rp PASS (2026-01-14 12:32); npm --prefix novapolis-rp\\coding\\tools\\validators run validate:crossrefs PASS (2026-01-14 12:32)

title: D5 Funkraum
last_updated: 2026-01-14T10:15:02+01:00
category: location
slug: d5-funkraum
version: "0.1"
affiliations: [novapolis]
status: aktiv
connections: ["d5"]
tags: ["poi", "d5", "funk"]
---

D5 - Funkraum
-------------

Status
------
- Aktiv; priorisierte Kommunikationszelle (D5↔C6)

Funktion
--------
- Funk-/Signalabgleich, Protokollierung von Callsigns, Zeitfenster-Planung
- Schnittstelle für externe Kontakte (nur nach Freigabe)

Zugang
------
- Zugang nur mit Rollenfreigabe; Mitschnitt/Meta-Log ist Pflicht

Risiken
-------
- „Offene“ Frequenzen → Leaks/Ortung
- Störsender/Interferenz → Fehlinterpretationen

Hooks
-----
- Unbekannter Ping im Zeitfenster (nur Meta-Daten) → Analyse vs. Lockdown
- Widersprüchliche Log-Zeilen zwischen Funklog und Missionslog → Konsistenzprüfung

Verlinkungen
------------
- D5 → ./D5.md
- Missionslog → ../05-projects/Missionslog-Novapolis.md
