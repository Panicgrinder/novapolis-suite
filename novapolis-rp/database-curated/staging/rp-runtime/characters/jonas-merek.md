---
stand: 2026-04-29 00:47
update: Jonas Merek fuehrt den aktiven Nordlinie-Hauptpfad jetzt bis Turn 11 an der Draisine auf den D5-Bahnsteiggleisen statt nur als allgemeine Werkstattkante.
checks: snapshot-lock PASS (2026-04-28 22:24)
---

Jonas Merek - Runtime Working Sheet
===================================

Status
------

- slug: jonas-merek
- name: Jonas Merek
- state: Arbeitsstand
- review_state: working
- first_seen_session: d5-c6-nordlinie-sanierung-01

Role
----

- faction: Novapolis
- function: Werkstatt-, Material- und Rueckmeldepfad in D5
- current_goal: Nordlinie-Bedarf in belastbare Werkstattantworten und kleine reale Teilbereitstellungen uebersetzen, ohne harte Blocker weichzureden

Signals
-------

- confirmed:
  - Jonas bleibt im aktuellen Hauptpfad mit Pahl an die D5-Draisine und die Materialschiene gebunden.
  - Er beantwortet Ronjas Bedarf ueber knappe, belastbare Rueckmeldungen statt ueber freie Zusagen.
  - Jonas laeuft im laufenden Hauptpfad nicht allein, sondern mit der an ihn gekoppelten Begleitinstanz Lumen.
  - Turn 11 fuehrt ihn sichtbar an der Draisine auf den Gleisen am D5-Bahnsteig, nicht in einem abgeschlossenen Werkstattinnenraum.
- tentative:
  - Die verlaessliche Bau- und Materialrolle an der Draisine koennte Jonas' Vertrauensstellung im D5-Kernteam weiter stabilisieren.
- contradictions:
  - keine direkte Widerspruchslage; die Begleitung durch Lumen war bisher nur im Runtime-Slice untererfasst

Promotion Notes
---------------

- Sessionbezug: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 1, 2, 6, 7, 11
- Begleit- und Kopplungslogik liegt zusaetzlich in `characters/lumen.md` und `mind/jonas-merek.md`.
