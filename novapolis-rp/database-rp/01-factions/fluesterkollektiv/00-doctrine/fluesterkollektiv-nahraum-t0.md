---
stand: 2026-04-27 02:30
update: Fluesterkollektiv fuehrt jetzt den unmittelbaren Nahraum T0 fuer K4 und indirekte Kanalpfade konservativ aus.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: fluesterkollektiv-nahraum-t0
category: canon
version: "0.1"
---

Fluesterkollektiv - Nahraum T0
==============================

Zweck
-----

- Dieser SSOT zieht den unmittelbaren Nahraum des Fluesterkollektivs konservativ um `K4` nach.
- Er verdichtet den aktiven Kern und die belegten indirekten Kanal- und Signalpfade, ohne unbelegte Nachbarstationen oder feste Gegenparteien zu erfinden.

Scope
-----

- Kernknoten: [K4](../03-locations/K4.md)
- indirekte Kontakt-, Signal- und Einflusspfade ohne ortsscharfe Ausformung

Raumringe
---------

| Ring | Bereich | Lesart |
| --- | --- | --- |
| 0 | `K4` | aktiver Fluesterkollektiv-Kern aus Leitstand, Handelszelle und Sicherheitsfreigabe |
| 1 | indirekte Kanalpfade | riskoarme Uebergaben, Signale und Einflussfenster ohne feste Ortsbindung |

Ausbau- und Zustandsstatus
--------------------------

| Bereich | Kontrolle | Status | Zustandslesart | Funktionswert im Nahraum |
| --- | --- | --- | --- | --- |
| [K4](../03-locations/K4.md) | Fluesterkollektiv | aktiv | stabilster Punkt des lokalen Blocks | Leitstand, indirekte Kontaktsteuerung, Sicherheitsfreigabe |
| indirekte Kanalpfade | kein eigener Kern, aber belegte Funktionslogik | aktiv als Rahmen, nicht ortsscharf | nutzbar, aber absichtlich unfixiert | Kontakt-, Signal- und Einflussachsen |

Korridore und Pfade
-------------------

### Kern `K4`

- `K4` ist der einzige belastbare Fluesterkollektiv-Kern im unmittelbaren Nahraum.
- Leitstand, Kanalfreigabe und Sicherheitslogik liegen dichter beieinander als in einem offenen Kontaktgeflecht.

### Indirekte Kanaele

- Die Pfade des Fluesterkollektivs bleiben absichtlich indirekt, schmal und trust-basiert.
- Gerade diese Unschärfe ist Teil des belastbaren Rahmens und kein Lueckenfehler.

Gefahren- und Druckachsen
-------------------------

| Achse | Bereich | Lesart | Schwere |
| --- | --- | --- | --- |
| Signalrauschen | `K4` plus Kanaele | unbekannte Signale sind Chance und Risiko zugleich | mittel bis hoch |
| Kanalverunreinigung | indirekte Pfade | zu breite oder unklare Kontakte gefaehrden Tarnung und Einflusslinien | hoch |
| Gegenaufklaerungsdruck | `K4` | Freigaben, Zutritte und sensible Uebergaben muessen eng gefiltert bleiben | hoch |
| Unklare Aussenlage | Gesamtbild | gegen Novapolis ist nur `unbekannt` belastbar; jeder Schritt kann Fehlsignal oder Chance sein | mittel |

Verdeckte Orte (konservativ)
----------------------------

Hinweise

- Die folgenden Raumtypen sind Funktionslesarten und keine bereits belegten Unterraeume.

| Bereich | Wahrscheinlicher Raumtyp | Lesart | Guardrail |
| --- | --- | --- | --- |
| `K4` | Leitnischen, Briefingpunkte, kontrollierte Signalraeume | Fuehrung, Kanaltrennung und Sicherheit greifen eng ineinander | keine konkrete Innenarchitektur erfinden |
| indirekte Kanaele | Uebergabepunkte, Signalfenster, kurze Kontaktzonen | kontaktarme, reparierbare Netzpfade statt offener Wege | keine festen Nachbarorte oder Routen setzen |

Guardrails
----------

- `K4` bleibt der aktive Kern; indirekte Kanaele begruenden keine weiteren Orts- oder Fraktionskerne.
- Der Nahraum-SSOT ersetzt keine Ortsdatei, sondern ordnet die belegte Kontakt- und Signalstruktur.
- Keine harten Spezialgut-, Technik- oder Kontaktlisten ohne neue Evidenz.
