---
stand: 2026-05-20 06:28
update: Kora-Sheet fuehrt jetzt die Eigenpruefung des Schuttkeils nach ihrer Funkbestaetigung aus Turn 13.
checks: snapshot-lock PASS (2026-05-20 06:28); npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc RP-Runtime-turn13-slice PASS (2026-05-20 06:22); .\.venv\Scripts\python.exe scripts\check_frontmatter.py RP-Runtime-turn13-slice PASS (EXITCODE=0, 2026-05-20 06:22)
---
Kora Malenkov - Runtime Working Sheet
====================================

Status
------

- slug: kora-malenkov
- name: Kora Malenkov
- state: Arbeitsstand
- review_state: working
- first_seen_session: d5-c6-nordlinie-sanierung-01

Role
----

- faction: Novapolis
- function: Leitung von C6 sowie lokale Logistik-, Empfangs- und Sicherheitskoordination
- current_goal: C6 als enge Annahme- und Stagingkante stabil halten, ohne unter Nordlinie-Druck freie Entlastung zu versprechen

Signals
-------

- confirmed:
  - Kora traegt im aktuellen Hauptpfad die lokale C6-Arbeits- und Annahmekante.
  - Sie oeffnet in Turn 9 kein breites Versorgungsversprechen, sondern haelt Empfang, Sichtung und Schutzdisziplin eng.
  - Echo bleibt dabei an ihrer Seite als lokale Schutzinstanz.
  - Turn 11 fuehrt Kora weiter in Verteilung und Berichtsauswertung des `C6-Tunneltrupps`, nicht in Ronjas D5-Perspektive.
  - Turn 13 fuehrt Kora selbst an den Funkraum von `C6`: Sie bestaetigt Ronjas Bitte, macht aber keine Fernentscheidung, sondern geht selbst an die Kante, um den `Schuttkeil Kontaktseite` mit eigener Sicht zu pruefen.
- tentative:
  - Wenn aus D5 ein formal enger Materialabruf kommt, koennte Kora denselben in ein kontrolliertes C6-Stagingfenster uebersetzen.
- contradictions:
  - keine direkte Widerspruchslage im aktuellen Hauptweltpfad

Promotion Notes
---------------

- Sessionbezug: `sessions/d5-c6-nordlinie-sanierung-01/scene-log.md`, Turn 9, 11
- Detailwirkung auf Schutz-, Kontroll- und Logistikachsen liegt zusaetzlich in `mind.md`.
