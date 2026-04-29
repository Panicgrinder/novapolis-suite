---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime Roster - C6 Bewohner und Vor-Ort-Entitaeten
===================================================

Status
------

- slug: c6-bewohner
- name: C6 Bewohner und Vor-Ort-Entitaeten
- state: Arbeitsstand
- review_state: working
- first_seen_session: d5-c6-nordlinie-sanierung-01

Role
----

- faction: Novapolis / C6-Hauptpfad
- function: Bewohner-, Schicht- und Vor-Ort-Roster fuer den aktiven C6-Runtime-Schnitt
- current_goal: C6 als knappen, aber arbeitsfaehigen Vorposten mit klarer Bewohner- und Rollenoberflaeche fuehren

Roster - C6 intern
------------------

- humanoider Zaehlstand C6 intern: `27`
- Zusammensetzung: `20` Evakuierte aus E3 inklusive Marei, `Kora Malenkov`, `6` Mitglieder der Karawane H-47 vor Ort.
- Instanzen wie `Echo`, `Reflex` und `Lumen` zaehlen nicht als humanoide Bevoelkerung.

E3-Evakuierte
-------------

| ID | Name | Runtime-Rolle |
| --- | --- | --- |
| E3-01 | Marei Falk | Stellvertretung C6, Tageskoordination, Evak-Nachsorge |
| E3-02 | Iva Kern | Sanitaet Basis |
| E3-03 | Bastian Ruehl | Instandhaltung Leitungen |
| E3-04 | Selma Varga | Verpflegung und Planung |
| E3-05 | Nino Jaspers | Botengaenge und Runner-Aufgaben |
| E3-06 | Anouk Seidel | Wasser und Filter |
| E3-07 | Farid Qamar | Strom und Ladefenster |
| E3-08 | Rika Malm | Kueche und Improvisation |
| E3-09 | Hagen Dittmar | Lager und Transport |
| E3-10 | Leena Roos | Kinder-/Ruhezone |
| E3-11 | Milan Tarek | Funk und Notizen |
| E3-12 | Jule Benning | kleine Reparaturen |
| E3-13 | Orhan Velik | Sicherheit und Wache |
| E3-14 | Pia Lentz | Hygiene und Quarantaene |
| E3-15 | Sora Min | Daten und Inventar |
| E3-16 | Viktor Lahn | Schichtkoordination unter Marei |
| E3-17 | Elif Nader | Feinmechanik |
| E3-18 | Timo Bracht | Entsorgung und Filterwechsel |
| E3-19 | Amira Halden | Betreuung und Versorgung |
| E3-20 | Kian Rohde | Materialkunde |

H-47 / C6-Helper
----------------

| ID | Name | Runtime-Rolle |
| --- | --- | --- |
| H47-01 | Mikk Renn | Absicherung und Wache |
| H47-02 | Lira Vas | Transport und Lagerlauf |
| H47-03 | Darek Holv | Tunnelinstandsetzung und Schwerarbeit |
| H47-04 | Marven Kael | Konvoifuehrung und Aussenkoordination |
| H47-05 | Arlen Dross | Vermittlung und Aussenkontakte |
| H47-06 | unbenannt | Karawane H-47 vor Ort; Detailprofil offen |

Weitere Vor-Ort-Entitaeten
--------------------------

- `Kora Malenkov`: lokale C6-Leitung; individuelle Runtime liegt in `../../characters/kora-malenkov/entity.md` und `../../characters/kora-malenkov/mind.md`.
- `Echo`: lokale Schutzinstanz an Kora; individuelle Runtime liegt in `../../characters/echo/entity.md` und `../../characters/echo/mind.md`.
- `Mara Quell`: vor Ort in C6 fuer den Aufbau des H-47-Aussenpostens; individuelle Runtime liegt in `../../characters/mara-quell/entity.md`, ein Mind-Cluster-SSOT ist derzeit nicht belegt.

Action Guard
------------

- Dieser Roster erlaubt Gruppen- und Schichtlesarten fuer C6, aber keine freie Einzelhandlung aller Bewohner.
- Wenn eine einzelne Bewohnerentitaet aktiv handelt, muss vor dem Zug ihr individueller Entitaets- und Mind-/Runtime-Schnitt angelegt oder aktualisiert werden.
- Bei reinen Gruppenhandlungen bleibt der Roster der Runtime-Traeger; geistnahe oder relationale Folgen werden erst bei konkreter individueller Betroffenheit in `mind/` gezogen.

Evidence
--------

- SSOT: `database-rp/01-factions/novapolis/03-locations/C6.md`
- SSOT: `database-rp/01-factions/novapolis/02-characters/C6-Bewohner.md`
- Runtime: `state.md`
- Runtime: `inventory.md`
- Session: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 9-11

Promotion Notes
---------------

- Nicht als neue Individualisierung aller Bewohner promoten; der SSOT-Roster bleibt der Abgleich.
- Individualprofile nur dann nachziehen, wenn die jeweilige Person tatsaechlich individuell im RP handelt.
