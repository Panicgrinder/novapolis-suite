---
stand: 2026-04-27 01:53
update: Schienenbund fuehrt jetzt zusaetzlich einen konservativen Stationssockel fuer B2 samt Lager- und Instandsetzungsanker.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_015145.md
canvas: Inventar Schienenbund
last_updated: 2026-04-27T01:05:00+02:00
category: inventory
slug: schienenbund-inventar
owner: schienenbund
scope: faction
version: "0.1"
---

Inventar - Schienenbund (Fraktion)
==================================

Bestände (Auszug)
-----------------
- Kugeln (neu): hochwertig (1 neu ≈ 10 gebraucht; Bestand nicht quantifiziert)
- Kugeln (gebraucht): Alltagswährung/Hauptmunition (Qualität streut; Bestand nicht quantifiziert)
- Schienen-/Baukomponenten: variabel (keine Stückzahlen)
- Werkzeuge: variabel (keine Stückzahlen)
- Reparaturgüter: belastbarer Rollenrahmen, aber nicht quantifiziert

Stationssockel B2 (konservativ, belegt)
---------------------------------------

Hinweise

- B2 ist nicht nur abstrakter Fraktionsraum, sondern aktiver Kernknoten mit Betriebs-, Sperr- und Reparaturfokus.
- Der Sockel bleibt bewusst mengenoffen; belastbar sind Raumfunktion, Lagerart und Produktionsnahe, nicht konkrete Stueckzahlen.

| Bereich | Lesart | Bestands-/Funktionsrahmen |
| --- | --- | --- |
| Betriebslager | stationsnaher Reserve- und Umlaufpuffer | Schienen-/Baukomponenten, Werkzeugsaetze, Reparaturgut und Sicherungsmaterial muessen lokal vorgehalten werden, weil `B1 -> B2` unter Reparaturdruck steht und `B2 -> C3` aktiv bleibt |
| Transit- / Freigabelager | kontrollierter Durchsatzraum | Gueter fuer freigegebene Transitfenster laufen ueber B2, bevor sie weitergehen; die Handelszentrale impliziert damit keinen freien Markt, aber einen kontrollierten Umschlagpuffer |
| Sicherheitsreserve | zugriffsbeschraenkter Stationssockel | Sperr-, Leitstands- und Zugangskontrollbedarf verlangt lokal verfuegbare Sicherheits- und Abschirmmittel, ohne dass daraus ein voll quantifiziertes Arsenal folgt |

Produktions- und Instandsetzungsanker B2 (konservativ, belegt)
--------------------------------------------------------------

| Anker | Lesart | Guardrail |
| --- | --- | --- |
| Instandsetzung | B2 fuehrt einen belastbaren Reparatur- und Baukontext; daraus folgt lokale Aufarbeitung, Anpassung und Rueckfuehrung von Trassen-, Bau- und Werkzeuggut | keine freie Serienfertigung und keine grossen Outputmengen ohne neue Belegkette |
| Betriebsfenster | Netzhoheit und Durchsatzlogik implizieren, dass Reparatur- und Freigabearbeit in B2 priorisiert und getaktet wird | Produktionslogik bleibt an Stationsbetrieb und Engpassarbeit gebunden, nicht an offene Exportwirtschaft |
| Herkunft `produced` | ein Teil des Schienenbund-Guts darf konservativ als lokal aufgearbeitet, instandgesetzt oder kleinseriennah vorbereitet gelesen werden | `produced` allein bleibt kein Beleg fuer konkrete Werkstattmengen oder eigene Fabriklinien |

Rahmenlage (T0)
---------------

- Schienenbund bleibt als logistischer Reparatur- und Baukontext mit aktivem Stationssockel in B2 gerahmt, nicht als quantifiziertes Gesamtlager.
- Dominante Herkunftslabel: `produced`, `scavenged`.
- Stationsscharfe Teilmengen, echte Verbrauchsbilanzen und jede engere Outputlogik bleiben bis zu neuer Belegkette `tbd`.

Bewegungen (Log)
----------------
- 2026-03-31 [RAHMENWERT] Logistik-/Reparaturfokus aus `Warenueberblick-T0.md` und Arbeitsledger fuer die finale Metro-Warenzuteilung bestaetigt; keine Mengensetzung vorgenommen.
- 2026-04-27 01:05 [REVIEW] B2 fuehrt den Schienenbund jetzt auch inventarseitig als aktiven Stationssockel mit Betriebslager, kontrolliertem Transit-/Freigabelager und lokalem Instandsetzungsanker. Mengen bleiben bewusst offen, aber Lager- und Produktionsnahe sind jetzt rollengerecht explizit. Quelle: [B2](../03-locations/B2.md), [Schienenbund](../Schienenbund.md), [rp-startbogen-schienenbund-b2](../../../../../novapolis-dev/docs/process/rp-startbogen-schienenbund-b2.ssot.md).
- Template: YYYY-MM-DD | Bezug: scene-/missionslog-/admin-artefakt | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Schienenbund.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md

