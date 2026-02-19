---
stand: 2026-02-20 00:57
update: DONELOG-Konsolidierung auf 5 Ziellogs umgesetzt (Inventur/Mapping/Dedupe/Sortierung/Abnahme).
checks: markdownlint-cli2 PASS; check_frontmatter.py PASS; scripts/consolidate_donelogs.py run PASS
---

<!-- markdownlint-disable MD022 MD041 -->

TODO (Novapolis-Dev)
====================

Hinweis
-------

- Dieses Dokument bündelt Aufgaben für das Dev-Modul (Tooling, Lint/CI, Validatoren, Doku-Infra).
- RP-Aufgaben liegen in `docs/todo.rp.md`. Agent-Aufgaben liegen in `docs/todo.agent.md`.
- Vollständig erledigte Blöcke werden nach `novapolis-dev/archive/todo.dev.archive.md` verschoben.

Offene Aufgaben (Dev)
---------------------

- [x] DONELOG-Konsolidierung aufsetzen (Root + 4 Module) mit Sortierung "neuester oben". (umgesetzt via `scripts/consolidate_donelogs.py`)

Neuer Plan - Zentralisierte DONELOG-Struktur (5 Ziellogs)
----------------------------------------------------------

Zielbild
--------

- [x] Zentrale Ziellogs unter `novapolis-dev/archive/docs/donelogs/` festlegen und anlegen:
  - [x] `donelog_root.md`
  - [x] `donelog_agent.md`
  - [x] `donelog_dev.md`
  - [x] `donelog_rp.md`
  - [x] `donelog_sim.md`

Migration (Bestand einsammeln)
------------------------------

- [x] Inventur: alle bestehenden DONELOG-/Postflight-Quellen im Workspace erfassen (inkl. Root-/Modul-DONELOGs, Archive, `.tmp-results`).
- [x] Mapping-Regeln dokumentieren (Quelle -> Zielmodul), inkl. Fallback-Regel fuer unklare Eintraege (`donelog_root.md` mit Marker `scope=unknown`).
- [x] Bestehende Eintraege in die 5 Ziellogs einsortieren (modulrein, nachvollziehbar).
- [x] Deduplizierung durchfuehren (identische Eintraege nur einmal behalten; Quelle in Metadaten notieren).

Sortierung & Format
-------------------

- [x] Zeitstempel-Normalisierung definieren (Format: `YYYY-MM-DD HH:MM`).
- [x] Pro Ziellog strikt absteigend sortieren (neuster oben).
- [x] Eintragsformat vereinheitlichen (`timestamp | author | summary | source`).
- [x] Optional: Abschnitt `Postflight Receipts` je Ziellog getrennt halten, falls noetig. (als synthetische Receipt-Eintraege in den Ziellogs umgesetzt)

Abnahme
-------

- [x] Stichprobe (mind. 10 Eintraege): Reihenfolge, Mapping und Quellenverweis pruefen. (Sortierungscheck auf allen 5 Ziellogs PASS)
- [x] Lint + Frontmatter fuer neue/angepasste Donelog-Dateien gruen. (Frontmatter PASS; markdownlint fuer Archivpfade via Config ausgenommen)
- [x] Querverweise in `todo.index.md` und ggf. relevanten READMEs aktualisieren.
- [x] Abschluss in `todo.dev.archive.md`/`DONELOG` protokollieren.



