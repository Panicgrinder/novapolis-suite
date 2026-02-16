---
stand: 2026-02-16 12:01
update: Economy-Subdocs (Märkte, Preisbänder) ergänzt und verlinkt.
checks: not run (not requested)
slug: novapolis-economy
category: Economy
schemaVersion: 1
language: de
tags: [rp, economy, faction]
status: active
owners: [admin-novapolis]
relatedSlugs: [reference-campaign-state, current-state, memory-bundle, index-rules, novapolis-markets, novapolis-pricebands]
---

Wirtschaft (Novapolis)
======================

Zweck
-----
Fraktionsbezogene, dynamische Wirtschaftsdaten für die Metro-Ökonomie. Globale Regeln siehe 00-admin (z. B. Index-Handel-Diplomatie, Reference-Campaign-State → Währung/KUGELN, Handels-/Diplomatie-Richtlinien).

Bausteine
---------
- Währungen/Einheiten: Siehe Reference (KUGELN neu/gebraucht). Anpassungen/Abweichungen hier dokumentieren.
- Märkte/Handelsplätze: Orte, Tauschbeziehungen, Zugangsvoraussetzungen.
- Preisliste (Heuristik): Artikel → Preisbereich (neu/gebraucht), Varianz, Angebotslage.
- Verträge/Absprachen: Kurzbeschreibung, Parteien, Laufzeit, Abhängigkeiten.
- Log-Verweis: Siehe fraktionsbezogenes 06-handel-diplomatie/ für Transaktionen.

Dateien
-------
- Märkte & Handelsplätze: ./novapolis-markets.md
- Preisbänder (Heuristik): ./novapolis-pricebands.md

Verweise
--------
- Handel/Diplomatie (Logs): ../06-handel-diplomatie/
- Regeln (global): ../../00-admin/Index-Handel-Diplomatie.md
- Referenzen: ../../00-admin/Reference-Campaign-State.md