---
stand: 2026-04-27 02:30
update: Schattenbund fuehrt jetzt den unmittelbaren Nahraum T0 fuer F9 und den Korridor F9-G6 konservativ aus.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: schattenbund-nahraum-t0
category: canon
version: "0.1"
---

Schattenbund - Nahraum T0
=========================

Zweck
-----

- Dieser SSOT zieht den unmittelbaren Schattenbund-Nahraum konservativ um `F9` nach.
- Er verdichtet den aktiven Kern und den belegten Korridor `F9 -> G6`, ohne unbelegte Nachbarstationen oder tiefe Tarnstrukturen als feste Orte zu setzen.

Scope
-----

- Kernknoten: [F9](../03-locations/F9.md)
- Bewegungs- und Tarnungskorridor: `F9 -> G6`

Raumringe
---------

| Ring | Bereich | Lesart |
| --- | --- | --- |
| 0 | `F9` | aktiver Schattenbund-Kern aus Fuehrung, Beschaffung und Abschirmung |
| 1 | `F9 -> G6` | aktiver Korridor fuer Bewegung, Tarnung und gestaffelte Uebergaben |

Ausbau- und Zustandsstatus
--------------------------

| Bereich | Kontrolle | Status | Zustandslesart | Funktionswert im Nahraum |
| --- | --- | --- | --- | --- |
| [F9](../03-locations/F9.md) | Schattenbund | aktiv | stabilster Punkt des lokalen Blocks | Fuehrungszelle, Handelszelle, Sicherheitszentrale |
| `F9 -> G6` | kein eigener Kern, aber aktiv nutzbar | aktiv | begeh- und bespielbar, aber nur unter Tarnungsdruck | Bewegungs-, Uebergabe- und Risikoachse |

Korridore
---------

### Kern `F9`

- `F9` ist der einzige belastbare Schattenbund-Kern im unmittelbaren Nahraum.
- Fuehrung, Beschaffung und Gegenaufklaerung liegen dichter beieinander als in einem offenen Verteilnetz.

### Bewegungsachse `F9 -> G6`

- Der Korridor ist aktiv, aber nur als Tarnungs- und Bewegungsanker lesbar, nicht als offene Hauptstrasse.
- Gerade die Aktivitaet des Pfads macht Gegenaufklaerung und Kanaldisziplin zum Dauerproblem.

Gefahren- und Druckachsen
-------------------------

| Achse | Bereich | Lesart | Schwere |
| --- | --- | --- | --- |
| Leak-Druck | `F9` | schwache Kanaldisziplin kippt Beschaffung sofort in Abschottung | hoch |
| Entdeckungsrisiko | `F9 -> G6` | jeder aktive Lauf vergroessert das Risiko fuer Mustererkennung | hoch |
| Aussenfeindschaft | Gesamtlage | besonders die feindselige Eisenkonklave-Lage verschaerft Fehltritte | mittel bis hoch |
| Verdeckte Beziehungsrisiken | Gesamtlage | Arkologie-Bezuege duerfen nicht sichtbar aufreissen | mittel |

Verdeckte Orte (konservativ)
----------------------------

Hinweise

- Die folgenden Raumtypen sind Funktionslesarten und keine bereits belegten Unterraeume.

| Bereich | Wahrscheinlicher Raumtyp | Lesart | Guardrail |
| --- | --- | --- | --- |
| `F9` | Abschirmnischen, Zellzugaenge, verdeckte Briefingpunkte | Fuehrung und Gegenaufklaerung greifen eng ineinander | keine konkrete Innenarchitektur erfinden |
| `F9 -> G6` | Uebergabepunkte, Beobachtungsnischen, Ausweichsegmente | aktiver, aber riskanter Schattenpfad | kein fixes Routennetz oder weitere Orte behaupten |

Guardrails
----------

- `F9` bleibt der aktive Kern; der Korridor begruendet keinen zweiten Orts- oder Fraktionskern.
- Der Nahraum-SSOT ersetzt keine Ortsdatei, sondern ordnet die belegte Korridorlogik.
- Keine harten Mengen, Partnerlisten oder Schmuggelrouten ohne neue Evidenz.
