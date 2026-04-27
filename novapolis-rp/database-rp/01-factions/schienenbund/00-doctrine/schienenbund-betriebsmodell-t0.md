---
stand: 2026-04-27 02:30
update: Schienenbund fuehrt jetzt ein konservatives Betriebsmodell T0 fuer B2, Freigabekette und innere Konfliktlinien.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_022916.md
slug: schienenbund-betriebsmodell-t0
category: canon
version: "0.1"
---

Schienenbund - Betriebsmodell T0
================================

Zweck
-----

- Dieser SSOT zieht fuer den Schienenbund ein konservatives Betriebsmodell T0 nach.
- Er verdichtet den belegten Kernknoten `B2` und den Funktionskorridor `B1 -> B2 -> C3`, ohne daraus ein frei verteiltes Mehrstationsreich zu machen.

Guardrails
----------

- Der Schienenbund bleibt ein enger Infrastruktur- und Reparaturblock, kein flaechiger Stationsverbund.
- `B2` ist der aktive Fraktionskern; `B1` und `C3` bleiben funktionale Nachbarraeume, aber keine voll kontrollierten Kernstationen.
- Mengen, Personalstaerken und freie Produktionsleistungen bleiben weiter offen, solange keine neue Belegkette vorliegt.

Kernlesart T0
-------------

| Bereich | Status | Funktionsprofil | Lesart |
| --- | --- | --- | --- |
| [B2](../03-locations/B2.md) | aktiv | Netzhoheit, Reparaturpriorisierung, Transitfreigabe, Sperrlogik | aktiver Schienenbund-Kern |
| [B1](../../../03-locations/B1.md) | neutral, aktiv | Vorpuffer, Sichtung, Timing vor dem partiellen Zulauf | vorgeschalteter Filterraum |
| [C3](../../../03-locations/C3.md) | neutral, teilaktiv | Zwischenhalt, Anschluss unter Hazard- und Verschleissdruck | verletzlicher Nachpuffer |

Freigabekette und Rollen
------------------------

- Helia Vorn fuehrt den Kommandoknoten und priorisiert Netzhoheit, Eskalation und Betriebsfenster.
- Rian Kord steuert Transit- und Handelsfenster nur innerhalb tragbarer Sicherheits- und Reparaturgrenzen.
- Tera Solm haelt Zugangskontrolle, Sperrprotokolle und die Absicherung des partiellen `B1`-Zulaufs.

Betriebsprioritaeten
--------------------

| Prioritaet | Lesart | Guardrail |
| --- | --- | --- |
| Netzbetrieb | Trassen muessen funktionsfaehig und kontrollierbar bleiben | kein Wachstumspfad gegen die Korridorlage |
| Reparatur | der partielle Zulauf `B1 -> B2` erzeugt dauernden Instandsetzungsdruck | kein stilles Wegdefinieren des Engpasses |
| Durchsatz | Transit ist wichtig, aber nur unter Freigabe | keine offene Marktlogik |
| Sicherheit | Sperrlogik schuetzt den Kern vor Ueberlastung oder Kontrollverlust | Sicherheit bleibt Mittel des Betriebs, nicht Selbstzweck ohne Kontext |

Spielbare Konfliktlinien
------------------------

- Reparatur gegen Durchsatz: Was gerade laufen soll, blockiert oft das, was erst instandgesetzt werden muesste.
- Handel gegen Sperre: Rian braucht verwertbare Fenster, Tera zieht dieselben Fenster aus Sicherheitsgruenden enger.
- Kern gegen Korridor: Helia fuehrt aus `B2`, aber der Zustand von `B1` und `C3` bestimmt, wie weit diese Kontrolle real traegt.
- Halten gegen Expandieren: Der Schienenbund wirkt stark, solange er den Korridor hart priorisiert; jeder uebereilte Ausbau ueberdehnt denselben Kern.

Alltagslesart fuer Spiel und Szenen
----------------------------------

- `B2` wirkt nach innen diszipliniert, taktend und zweckgebunden.
- `B1` ist aus Schienenbund-Sicht ein Vorraum voller Timing-, Sichtungs- und Zugriffsspannung.
- `C3` ist kein sicherer Ruecken, sondern ein nutzbarer, aber ermuedeter Nachlauf mit Anschlussrisiko.

Verknuepfte Quellen
-------------------

- [Schienenbund](../Schienenbund.md)
- [B2](../03-locations/B2.md)
- [Schienenbund-inventar](../04-inventory/Schienenbund-inventar.md)
- [schienenbund-nahraum-t0](./schienenbund-nahraum-t0.md)
- [rp-startbogen-schienenbund-b2](../../../../../novapolis-dev/docs/process/rp-startbogen-schienenbund-b2.ssot.md)
