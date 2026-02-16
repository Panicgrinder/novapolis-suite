---
stand: 2026-02-16 14:49
update: Konkreter Migrationsplan 00-admin ↔ 01-factions/novapolis mit Abschnitts-Matrix erstellt.
checks: not run (plan creation)
slug: migrationsplan-admin-novapolis
category: admin
canvas: migration-plan
status: draft
version: "0.1"
---

Migrationsplan 00-admin ↔ Novapolis
===================================

Ziel
----

Trennung nach Scope:

- `00-admin`: nur allgemein gültige Regeln, Schemata, Prozesse, globale Indizes.
- `01-factions/novapolis`: fraktionsspezifische Inhalte (Personen, Orte, Projekte, Missionsstatus, laufende Lage).

Zielpfade (neu vs. bestehend)
-----------------------------

### Bestehende Zieldateien (weiterverwenden)

- `novapolis-rp/database-rp/01-factions/novapolis/Novapolis.md`
- `novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-history.md`
- `novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-logistics.md`
- `novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-diplomacy.md`
- `novapolis-rp/database-rp/01-factions/novapolis/03-locations/README.md`

### Neu anzulegen (Schema-konform)

- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.md`
- `novapolis-rp/database-rp/01-factions/novapolis/05-projects/Missionslog-Novapolis.json`
- `novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-campaign-state.md`
- `novapolis-rp/database-rp/01-factions/novapolis/00-doctrine/novapolis-campaign-state.json`

Abschnitts-Matrix (exakt: extrahieren vs. verschieben)
------------------------------------------------------

| Quelle | Exakter Abschnitt | Aktion | Zielpfad | Zielabschnitt |
| --- | --- | --- | --- | --- |
| `00-admin/memory-bundle.md` | `Charaktere`, `Orte`, `Projekte`, `Offene Fäden (Core-kurz)` | **extrahieren** | `01-factions/novapolis/Novapolis.md` | neue Blöcke `Kernfiguren`, `Kernorte`, `Offene Fäden` |
| `00-admin/memory-bundle.md` | `Core-Status (eingefroren)`, `Referenzstandard (slug-only)` | **verschieben** | `00-admin/index-rules.md` (bestehend) | Abschnitt `RP-Referenzstandard` |
| `00-admin/Current-State.md` | `Snapshot (kurz, abgeleitet)`, `Aktive Projekte (Kurzliste)`, `Hauptorte (Kurzstatus)` | **extrahieren** | `01-factions/novapolis/Novapolis.md` | Abschnitt `Aktueller Stand (Snapshot)` |
| `00-admin/Current-State.md` | `Namensdrift (separat behandeln)` | **verschieben** | `00-admin/index-rules.md` | Abschnitt `Naming/Token-Regel` |
| `00-admin/Current-State.md` | `Arbeitsfluss (SSOT/RAW/curated)`, `Validatoren (Gates)`, `Referenzstandard (slug-only)` | **verschieben** | `00-admin/Process-Workflow.md` | Abschnitt `SSOT-Flow & Gates` |
| `00-admin/Missionslog.md` | kompletter Inhalt ab `Missionslog (Novapolis)` bis Dateiende | **verschieben (komplett)** | `01-factions/novapolis/05-projects/Missionslog-Novapolis.md` (neu) | Vollinhalt (1:1, Frontmatter angepasst) |
| `00-admin/Reference-Campaign-State.md` | `<!-- id: doc-reference-campaign-state -->`, `<!-- id: fsm-campaign -->` | **extrahieren** | `01-factions/novapolis/00-doctrine/novapolis-campaign-state.md` (neu) | `Campaign-State` |
| `00-admin/Reference-Campaign-State.md` | `<!-- id: project-draisine -->` | **extrahieren** | `01-factions/novapolis/05-projects/Draisine-Transportmodul.md` | Abschnitt `Canonical Constraints` |
| `00-admin/Reference-Campaign-State.md` | `<!-- id: economy-kugeln -->` | **extrahieren** | `01-factions/novapolis/07-economy/novapolis-pricebands.md` | Abschnitt `Währung/KUGELN (Reference)` |
| `00-admin/Reference-Campaign-State.md` | `<!-- id: rule-se-pools -->`, `<!-- id: rule-instances -->`, `<!-- id: rule-proximity -->`, `<!-- id: rule-reflex-speech -->`, `<!-- id: rule-reflex-control -->`, `<!-- id: rule-detach -->`, `<!-- id: rule-jealousy-gloves -->`, `<!-- id: policy-new-entities -->` | **belassen (global)** | `00-admin/Reference-Campaign-State.md` | bleibt zentrale Mechanik-SSOT |
| `00-admin/Ortsgraph.md` | gesamte lokale D5/C6/E3-Liste | **verschieben (inhaltlich)** | `01-factions/novapolis/03-locations/README.md` | Abschnitt `Topologie / Ortsgraph` |
| `00-admin/Curated-Konfliktliste.md` | Top-10-Blöcke mit Charakterbezug (Punkte 1–10) | **extrahieren** | `01-factions/novapolis/00-doctrine/novapolis-history.md` | Abschnitt `Offene Konfliktlinien` |
| `00-admin/AI-Behavior-Mapping.md` | globale Cluster/Skala/Modifikatoren | **belassen (global)** | `00-admin/AI-Behavior-Mapping.md` | bleibt globaler Referenzrahmen |
| `00-admin/AI-Behavior-Mapping.md` | Anchor-Register-Zeilen mit Novapolis-Charakteren | **extrahieren (optional Phase 2)** | jeweilige `01-factions/novapolis/02-characters/*.md` | Abschnitt `Behavior-Signatur` |

Umkehrprüfung (aus Novapolis nach 00-admin)
-------------------------------------------

Diese Inhalte werden aus Fraktionsdateien **nicht** erneut als Volltext gehalten, sondern nur als Verweis auf globale SSOT:

- Mechaniktext zu `PROXIMITY`/`DETACH`/`JEALOUSY-GLOVES` in Charakterdateien → nur Kurzform + Link auf `00-admin/Reference-Campaign-State.md`.
- Globale Preisband-Definition (Band S/N/M/H/X) → einmal global definieren; in `novapolis-pricebands.md` nur Novapolis-Abweichungen.

Ablauf (Implementierungsreihenfolge)
------------------------------------

1. Neue Zieldateien anlegen (`Missionslog-Novapolis.*`, `novapolis-campaign-state.*`).
2. Abschnittsweise Inhalte extrahieren/einfügen laut Matrix.
3. Querverweise umstellen (`00-admin` → neue Novapolis-Pfade).
4. Alte Admin-Dateien auf globalen Restinhalt reduzieren (kein Personen-/Fraktionsdetail).
5. Validierung: markdownlint + Frontmatter-Validator + Crossrefs.

Abnahmekriterien
----------------

- In `00-admin` keine rein Novapolis-spezifischen Inhaltsblöcke mehr (außer globale Referenzbeispiele).
- In `01-factions/novapolis` liegen alle fraktionsspezifischen Zustands-/Missions-/Ortsdetails.
- Alle umgestellten Links sind auflösbar, Frontmatter konsistent, Sidecars vorhanden.
