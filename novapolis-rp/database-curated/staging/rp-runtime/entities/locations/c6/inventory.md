---
stand: 2026-04-29 03:56
update: In entity-centric Runtime-Dossier migriert; Inhalt bleibt Arbeitsstand ohne Kanon-Promotion.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260429_035444.md
---
Runtime Inventory - C6
======================

Status
------

- slug: c6
- holder_or_location: C6
- state: Arbeitsstand
- review_state: working
- continuity_status: aktueller Hauptweltpfad fuer `d5-c6-nordlinie-sanierung-01`; alter H-47-Probeanker bleibt unten nur als Historie gefuehrt

Aktueller Arbeitsbestand
------------------------

| Item | Menge | Herkunft | Runtime-Lesart |
| --- | --- | --- | --- |
| Luftfilter (Gasmasken) | `3` | `legacy` | harte Schutzreserve, nicht breit verfuegbar |
| Ersatzrohr | `10` | `legacy,current` | Baustellen- und Leitungsreserve, aber nicht DN60-Ersatz |
| Kabelspule | `5` | `legacy,current` | Montagepuffer fuer C6-nahe Arbeit |
| Schmieroel | `4` | `legacy,current` | Werkstatt- und Verschleissgut unter Druck |
| Strommodul | `2` | `legacy` | keine breite Redundanz |
| Wasserkanister | `6` | `legacy,evac_e3` | operative Reserve, fuer 27 Personen knapp |
| Wasserflasche | `28` | `legacy,evac_e3` | mobiler Bestand fuer Schicht- und Evaklagen |
| Rationen | `25` | `legacy,evac_e3` | fuer 27 Personen angespannt, kein Komfortpuffer |
| Werkzeugkit | `3 Sets` | `legacy,evac_e3` | arbeitsfaehig, davon `1` improvisiert |
| Wartungsschluessel | `2` | `legacy` | stationsnahes Werkzeug |
| Druckmesser | `1` | `legacy` | Messreserve ohne Backup |
| Schweissgeraet | `1` | `legacy` | werkbankgebunden und feldschwach; operative Schweißausruestung bleibt kritisch |
| Sensorpaket | `1 Set` | `legacy` | kleiner Monitoringkern |
| Schutzanzug | `2` | `legacy` | zu wenig fuer breite Einsatzfreigabe |
| Ersatzmaske | `5` | `legacy,evac_e3` | kleine Atemschutzreserve |
| Medkit (Standard) | `1 Set` | `legacy,current` | Ersthilfe vorhanden, keine Komfortreserve |
| Verbandmaterial (Set) | `3 Sets` | `legacy,evac_e3` | endlich und schichtabhaengig |
| Hygienepaket (Basis) | `10 Sets` | `evac_e3,current` | druckempfindlicher Evakposten |
| Notdecke | `12` | `evac_e3,current` | Schlaf- und Quarantaenepuffer |
| Wechselkleidung (Set) | `8 Sets` | `evac_e3,current` | nicht fuer alle integriert vor Ort |
| Kochgeschirr (Set) | `3 Sets` | `evac_e3,current` | Gruppenbetrieb statt Vollausstattung |

Staging und offene Bewegungen
-----------------------------

- `C6` ist im aktuellen Hauptpfad arbeitsfaehig, aber fuer `27` humanoide Personen klar knapp.
- Der belegte Prozess fuer Material aus D5 bleibt `Eintreffen -> Bestandsaufnahme -> Empfangsbestaetigung -> spaeterer Baustellenabgang`; konkrete Itemmengen fuer diesen Stagingpfad bleiben `tbd`.
- Turn 11 erzeugt keinen neuen Materialeingang in `C6`; Kora verarbeitet den Bericht des `C6-Tunneltrupps` als Stationsaufgabe.
- `DN60`, operative Schweißausruestung, Anschlusssicherung, Verbindungsmaterial und C6-seitige Raeumkapazitaet bleiben offene Nordlinie-/C6-Blocker, nicht still vorhandener Bestand.

Bewohner- und Schichtdruck
--------------------------

- Bewohner-/Vor-Ort-Roster: `roster.md`.
- C6 fuehrt Versorgung, Hygiene, Wache, Lagerlauf, Kueche und Entlastung als knappe Schichtflaeche; diese Aufgaben sind durch `state.md` und den Roster getragen, nicht durch freie Einzelaktionen aller Bewohner.
- Individuelle Bewohneraktionen brauchen vor dem Zug eigene `characters/`- und, falls mind-relevant oder ein Cluster existiert, `mind/`-Runtime.

Alter Probeanker
----------------

- Die fruehere Session `c6-h47-handelsfenster-01` bleibt ein verworfener Einstiegspunkt. Ihre Probe-Eintraege `Filter`, `Grundbedarfsgueter` und `Werkzeugsichtung` duerfen nicht still als aktueller Hauptpfad-Transfer gelesen werden.

Recent Changes
--------------

- 2026-04-29: Aktueller C6-Hauptpfad-Inventartraeger aus `C6-inventar.md`, `state.md` und Turn 11 nachgezogen.
- Der alte H-47-Probeanker bleibt sichtbar isoliert, damit keine Zeitlinienmischung entsteht.
- Keine neue Mengenbuchung aus Turn 11; nur Konsolidierung des vorhandenen SSOT-/Runtime-Stands.

Promotion Notes
---------------

- Promotion in das RP-SSOT erst nach belegtem Materialeingang, konkreter C6-Zielbuchung oder ausdruecklicher Review-Freigabe.
- Der aktuelle Bestand ist aus [C6-inventar](../../../../../../database-rp/01-factions/novapolis/04-inventory/C6-inventar.md) abgeleitet und bleibt Runtime-Arbeitsstand fuer den aktuellen Hauptpfad.
