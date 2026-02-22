---
stand: 2026-02-22 01:49
update: Vollständig erledigte RP-Abschnitte aus todo.rp.md archiviert (Aktiv jetzt, Priorität B, Priorität C).
checks: markdownlint-cli2 via Repo-Config auf Archive-Pfad ausgeschlossen (`novapolis-dev/archive/**`); .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py 'novapolis-dev/docs/todo.rp.md' 'novapolis-dev/archive/todo.rp.archive.md' 'novapolis-dev/docs/donelog.md' PASS (2026-02-22 00:33)
---

TODO-Archiv - RP
================

Zweck: Kanonisierte, vollständig abgeschlossene TODO-Abschnitte aus RP-bezogenen TODOs (primär `novapolis-rp/**`) aufnehmen.

Kanon-Only (verbindlich)

- In dieses Archiv dürfen ausschließlich Abschnitte mit kanonisierten Inhalten. RAW/unstetige/unsichere Inhalte bleiben im Dev-/Working-Kontext.
- Quellenangaben bleiben erhalten; idealerweise mit Verweis auf Commit/PR/Issue.

Regeln (kurz)

- Nur vollständig abgehakte Abschnitte ([x] überall) verschieben.
- Inhalt unverändert übernehmen; direkt unter der Abschnitts-Überschrift: `archived_at: YYYY-MM-DD HH:MM`.
- Headings in diesem Archiv: Setext (MD003 konform, H1/H2).
- Präsentation: Lint-Läufe mit PRESENTATION=SHARED.

Ablage

- Neueste Einträge oben einfügen.

<!-- Hier unterhalb neue, vollständig erledigte und kanonisierte Blöcke einfügen (neu zuerst). -->

Aktiv jetzt (sicher)
--------------------

archived_at: 2026-02-22 00:31

- [x] `inventar_c6_v2`: `database-rp/01-factions/novapolis/04-inventory/C6-inventar.*` inhaltlich vervollständigen (nur belegte Daten, keine Strukturänderung). *(erledigt 2026-02-21)*
- [x] `logistik_c6_v2`: bestehendes `00-admin/Logistik.md` um belegte C6-Logistikstände ergänzen; Mixed-Version-Referenzen bereinigen. *(erledigt 2026-02-21)*
- [x] `logistik_novapolis_v2`: Lagerstände/Wochenzyklen in `00-admin/Logistik.md` ergänzen; Tagesreport konsistent nachziehen. *(erledigt 2026-02-21)*
- [x] `station_d5_v2.1` + Legacy D5: bestehendes D5-Standortcanvas faktisch nachziehen (Lastenaufzug, Grundfläche, Historie) ohne neue Nebenstrukturen. *(erledigt 2026-02-21)*
- [x] Inventar-Deltas (`Novapolis-inventar`, `D5-inventar`) mit Missionslog-Links abgleichen und synchronisieren. *(erledigt 2026-02-21)*
- [x] Ereignislog Weltgeschehen im bestehenden Admin-Canvas nachschärfen (`[SECRECY]`, H-47-Status konsistent). *(erledigt 2026-02-21)*
- [x] Relationslog Novapolis im bestehenden Canvas nachschärfen (Senn-Daru-Querverweise und ID-Schema auf aktuelle SSOT-Logistikreferenz bereinigt). *(erledigt 2026-02-21)*
- [x] Meta-Cluster-Index im bestehenden Admin-Canvas ausbauen (Spannungen/PsyLinks gegen Kanon verifizieren). *(erledigt 2026-02-21)*

Priorität B - Logistik & Inventar
---------------------------------

archived_at: 2026-02-22 00:31

- [x] `inventar_c6_v2` → bestehendes SSOT `database-rp/01-factions/novapolis/04-inventory/C6-inventar.*` inhaltlich vervollständigen; Systemlinks auf v2 aktualisieren. *(erledigt 2026-02-21)*
- [x] `logistik_c6_v2` → Inhalte nach `00-admin/Logistik.md` übernehmen; Mixed-Version-Referenzen bereinigen. *(erledigt 2026-02-21)*
- [x] `logistik_novapolis_v2` → Lagerstände/Wochenzyklen in Logistik-Canvas einpflegen; Tagesreport ergänzen. *(erledigt 2026-02-21)*
- [x] `station_d5_v2.1` + Legacy D5 → Standort-Canvas aktualisieren; Lastenaufzug, Grundfläche, Historie kennzeichnen. *(erledigt 2026-02-21)*
- [x] Inventar-Deltas (`Novapolis-inventar`, `D5-inventar`) synchronisieren; Links zu Missionslog prüfen. *(erledigt 2026-02-21)*

Priorität C - Systeme, Indizes, Ereignisse
-----------------------------------------

archived_at: 2026-02-22 00:31

- [x] Ereignislog Weltgeschehen → bestehendes Admin-Canvas nachschärfen; Begriff "Allianz" gegen `[SECRECY]` prüfen; H-47-Status konsistent kennzeichnen. *(erledigt 2026-02-21)*
- [x] Relationslog Novapolis → bestehendes Canvas nachschärfen; Händlerkontakt "Senn Daru"/Querverweise prüfen; ID-Schema auf aktuelle SSOT-Logistikreferenz angleichen. *(erledigt 2026-02-21)*
- [x] AI-Behavior-Index → `AI-Behavior-Mapping.md` + JSON-Sidecar erweitert (2025-11-01T17:40+01:00); Cluster, Modifikatoren, Anchor-Register, Psymatrix-Abgleich dokumentiert.
- [x] Validator „behavior_matrix_check.py“ → Anchor-Register + `ai_psymatrix_index_v1` Diff-Report erzeugen; Automation vorbereiten. *(2025-11-02T12:40+01:00 - Skript `coding/tools/validators/behavior_matrix_check.py` angelegt, Format-Checks aktiv; Psymatrix-Diff folgt sobald Quelle vorliegt.)*
- [x] Hub-README Querverweis geprüft: Behavior-Matrix Abschnitt im Validator-Tools-Teil vorhanden; Terminologie konsistent (validiert 2026-02-21).
- [x] Meta-Cluster-Index → bestehendes Admin-Canvas weiter ausbauen; Spannungen/PsyLinks gegen Kanon verifizieren. *(erledigt 2026-02-21)*
- [x] Missionslog Querverweise gezielt prüfen/ergänzen (nur falls Rohdaten neue relevante Ereignisse tragen). *(erledigt 2026-02-21)*

Priorität A - Charaktere & Führung
----------------------------------

archived_at: 2025-11-01 19:10

- [x] Varek Solun → Canvas `database-rp/02-characters/Varek-Solun.{md,json}` angelegt (2025-11-01T15:45+01:00); Standort H12 harmonisiert, Novapolis-Wissen auf Gerüchte begrenzt.
- [x] Liora Navesh → Canvas `database-rp/02-characters/Liora-Navesh.{md,json}` angelegt (2025-11-01T16:20+01:00); Novapolis/D5 als unbekannt markiert, Taxonomie Arkologie A1 harmonisiert, SÜDFRAGMENT-Fokus übertragen.
- [x] Kora Malenkov → bestehendes Canvas auf Version 1.0 heben; Rollen laut `[CARAVAN-LEADERSHIP]` klarziehen; paranoide Vorsicht + Echo-Notizen übernehmen. *(2025-11-02T14:20+01:00 erledigt)*
- [x] Marven Kael → neues Canvas; Flags beachten (Konvoi-/Handelsleitung extern, keine Doppelrolle mit Kora). *(2025-11-02T14:45+01:00 erledigt)*
- [x] Arlen Dross → neues Canvas; Rolle als Händler/Vermittler präzisieren; Reflex-Einschätzung aufnehmen. *(2025-11-02T15:05+01:00 erledigt)*
- [x] Pahl → neues Canvas; Gesundheitsstatus (Atembeschwerden) verifizieren; Beziehungen/Risiken dokumentieren. *(2025-11-02T15:25+01:00 erledigt)*
- [x] Ronja Kerschner → Canvas `database-rp/02-characters/Ronja-Kerschner.{md,json}` auf Version 1.0 gehoben (2025-11-01T17:10+01:00); RAW-Signatur/Status übernommen, Drift "Vallin" dokumentiert.
- [x] Reflex (Primärinstanz) → Canvas + Wissensstand erweitern; Frequenzband 7.3-8.0 Hz und Detachment-Regeln aus RAW übernehmen; `[REFLEX-*]` prüfen. *(2025-11-02T16:05+01:00 erledigt)*
- [x] Jonas Merek → Canvas anreichern; Schwester-Status auf "vermisst/unklar" normalisieren; Schuldflag als Kommentar kennzeichnen. *(2025-11-02T13:55+01:00 erledigt)*


