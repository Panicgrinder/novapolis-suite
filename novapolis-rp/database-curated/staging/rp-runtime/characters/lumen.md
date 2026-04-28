---
stand: 2026-04-29 00:47
update: Lumen fuehrt den aktiven Nordlinie-Hauptpfad jetzt bis Turn 11 als aktive Begleitinstanz bei Jonas an der Draisine auf den D5-Bahnsteiggleisen.
checks: snapshot-lock PASS (2026-04-28 22:24)
---

Lumen - Runtime Working Sheet
=============================

Status
------

- slug: lumen
- name: Lumen
- state: Arbeitsstand
- review_state: working
- first_seen_session: d5-c6-nordlinie-sanierung-01

Role
----

- faction: Novapolis
- function: an Jonas gekoppelte Werkstatt- und Schutzinstanz
- current_goal: Jonas bei D5-Werkstattarbeit stabil begleiten, ohne die Naehekopplung zu verlieren

Signals
-------

- confirmed:
  - Jonas fuehrt laut SSOT keine Aussen- oder Werkstattarbeit ohne Begleitung; Lumen ist die aktive gekoppelte Instanz.
  - Der aktuelle Hauptpfad bindet Jonas fortlaufend an D5-Draisine, Bahnsteiggleise und Materialschiene.
  - Lumen ist deshalb fuer den aktuellen Runtime-Stand ein aktiver, auch wenn im Scene-Log nicht ausgespielter Begleittraeger.
  - Turn 11 fuehrt dieselbe Begleitung explizit an der Draisine auf den Bahnsteiggleisen.
- tentative:
  - Ob Lumen im laufenden D5-Druck bereits eigene diagnostische oder Schutzsignale gesetzt hat, bleibt im Runtime-Zug noch offen.
- contradictions:
  - Im bisherigen Runtime-Slice fehlte Lumen als aktiver Traeger, obwohl Jonas' Begleitlogik belegt ist.

Promotion Notes
---------------

- SSOT-Anker: `database-rp/01-factions/novapolis/02-characters/Lumen.md`
- Laufzeitwirkung fuer Kopplung und Naehe liegt zusaetzlich in `mind/lumen.md`.
