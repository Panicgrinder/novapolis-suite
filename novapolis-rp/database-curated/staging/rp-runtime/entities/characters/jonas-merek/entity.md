---
stand: 2026-05-20 06:28
update: Jonas-Sheet fuehrt jetzt die konservative Hand-/Schubdebatte der Draisine aus Turn 13.
checks: snapshot-lock PASS (2026-05-20 06:28); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc RP-Runtime-turn13-slice PASS (2026-05-20 06:22); .\.venv\Scripts\python.exe scripts\check_frontmatter.py RP-Runtime-turn13-slice PASS (EXITCODE=0, 2026-05-20 06:22)
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
  - Turn 13 fuehrt Jonas in dieselbe Nuechternheit auch bei der Antriebsfrage: Schieben auf gesicherter Strecke liest er als ehrlichste Anfangsvariante, waehrend eine Hebel-/Handdraisine nur als moegliche, noch unfertige Arbeitsrichtung stehenbleibt.
- tentative:
  - Die verlaessliche Bau- und Materialrolle an der Draisine koennte Jonas' Vertrauensstellung im D5-Kernteam weiter stabilisieren.
- contradictions:
  - keine direkte Widerspruchslage; die Begleitung durch Lumen war bisher nur im Runtime-Slice untererfasst

Promotion Notes
---------------

- Sessionbezug: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 1, 2, 6, 7, 11
- Begleit- und Kopplungslogik liegt zusaetzlich in `../lumen/entity.md` und `mind.md`.
