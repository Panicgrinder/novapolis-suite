---
stand: 2026-04-27 02:30
update: Schienenbund fuehrt jetzt den unmittelbaren Nahraum T0 fuer den Korridor B1-B2-C3 konservativ aus.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: schienenbund-nahraum-t0
category: canon
version: "0.1"
---

Schienenbund - Nahraum T0
=========================

Zweck
-----

- Dieser SSOT zieht den unmittelbaren Schienenbund-Nahraum konservativ um `B2` nach.
- Er verdichtet den belegten Korridor `B1 -> B2 -> C3`, ohne freie Zusatzgeographie oder unbestaetigte Stationskontrolle zu erfinden.

Scope
-----

- Kernknoten: [B2](../03-locations/B2.md)
- Zulaufpuffer: [B1](../../../03-locations/B1.md)
- Nachlaufpuffer: [C3](../../../03-locations/C3.md)

Raumringe
---------

| Ring | Bereich | Lesart |
| --- | --- | --- |
| 0 | `B2` | aktiver Schienenbund-Kern aus Netzhoheit, Freigabe und Reparatursteuerung |
| 1 | `B1`, `C3` | neutrale Vor- und Nachpuffer, die den Kern entlasten, abbremsen oder verletzlich machen |

Ausbau- und Zustandsstatus
--------------------------

| Bereich | Kontrolle | Status | Zustandslesart | Funktionswert im Nahraum |
| --- | --- | --- | --- | --- |
| [B2](../03-locations/B2.md) | Schienenbund | aktiv | stabilster Punkt des Korridors | Kommandoknoten, Leitstand, Freigabefenster |
| [B1](../../../03-locations/B1.md) | neutral | aktiv | vorgeschalteter, aber unsicherer Vorraum | Sichtung, Timing, Zulauf unter Reparaturdruck |
| [C3](../../../03-locations/C3.md) | neutral | teilaktiv | benutzbarer, aber ermuedeter Nachlauf | Zwischenhalt, Weiterlauf unter Hazard-Risiko |

Korridore
---------

### Zulauf `B1 -> B2`

- Der Zulauf bleibt partiell und zwingt den Schienenbund in eine defensive Engpasslogik.
- `B1` puffert Unsicherheit, bevor sie in den Kern kommt; genau dadurch bleibt der Raum funktional wichtig, ohne zum Fraktionskern zu werden.

### Kern `B2`

- `B2` ist der einzige belastbare Schienenbund-Kernknoten im unmittelbaren Nahraum.
- Hier werden Betrieb, Sperrung, Reparatur und Transit miteinander verkoppelt statt getrennt gedacht.

### Nachlauf `B2 -> C3`

- Der Weiterlauf ist aktiv, aber nicht entspannt: `C3` fuehrt den Anschluss nur unter Teilaktivitaet und bereits sichtbarer Strukturermuedung.
- Hinter dem Kern beginnt also kein sicherer Ruecken, sondern ein zusaetzlicher Belastungsraum.

Gefahren- und Druckachsen
-------------------------

| Achse | Bereich | Lesart | Schwere |
| --- | --- | --- | --- |
| Reparaturdruck | `B1 -> B2` | der partielle Zulauf erzeugt dauernde Instandsetzungs- und Timingkonflikte | hoch |
| Durchsatzdruck | `B2` | Handel, Netzbetrieb und Sicherheit konkurrieren um dieselben Fenster | hoch |
| Anschlussrisiko | `B2 -> C3` | der aktive Weiterlauf fuehrt in einen schon geschwaechten Raum statt in Ruhe | mittel bis hoch |
| Hazard-Nachlauf | `C3` | Mikro-Kollaps und Teilaktivitaet begrenzen Aufenthalt und Weiterfahrt | mittel |

Verdeckte Orte (konservativ)
----------------------------

Hinweise

- Die folgenden Raumtypen sind konservative Funktionslesarten und keine bereits belegten Unterraeume.

| Bereich | Wahrscheinlicher Raumtyp | Lesart | Guardrail |
| --- | --- | --- | --- |
| `B1 -> B2` | Kontrollnischen, Wartebuchten, Sichtungszonen | Vorfilter vor dem Kernzugang | keine exakten Sperrkammern oder Personallisten setzen |
| `B2` | Materialvorhaenge, Reparaturbuchten, Leitstandsnahe Umschlagpunkte | Betrieb und Freigabe liegen dicht beieinander | keine freie Architektur von B2 erfinden |
| `B2 -> C3` | Zwischenhalte, Engstellen, ausgeduennte Servicebereiche | Nachlauf mit sinkender Stabilitaet | keine festen Lager oder Schutzraeume behaupten |

Guardrails
----------

- `B2` bleibt der aktive Kern; aus `B1` oder `C3` folgt keine nachtraegliche Schienenbund-Kontrolle ohne neue Evidenz.
- Der Nahraum-SSOT ersetzt keine Ortsdateien, sondern ordnet ihre Korridorlogik.
- Keine harten Materialmengen, Dienstplaene oder Ausbaugrade ohne neue Missions- oder Inventarbelege.
