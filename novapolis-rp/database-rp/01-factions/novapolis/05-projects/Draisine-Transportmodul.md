---
stand: 2026-04-27 01:53
update: Arbeitsstand fuehrt jetzt zusaetzlich die aktuelle kleine Werkstattbindung aus D5 als konkrete Materialbuchung.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260427_015145.md
title: Draisine-/Transportmodul (Prototyp)
category: project
slug: draisine-transportmodul
status: prototyping
version: "0.1"
last_updated: 2026-04-27T00:44:00+02:00
tags: [transport, nordlinie, werkstatt]
owners: [jonas-merek, pahl]
locations: [d5]
dependencies: [logistik, missionslog, nordlinie-01]
---

Draisine-/Transportmodul (Prototyp)
----------------------------------

Ziel
----

Ein kleines, robustes Transportmodul (Draisine/Schienenfahrzeug-Ansatz), das Material und Personen entlang der Nordlinie (D5↔C6) sicherer und effizienter bewegt.

Scope (was ist es)
------------------

- Prototyp aus Werkstattbestand (D5), mit Fokus auf **Sicherheit** und **Wartbarkeit**.
- Primärer Nutzen: Materiallauf-Unterstützung (Werkzeug, Adapter, Filter, Zellen), sekundär: Personen-/Rettungstransport.

Nicht-Scope (was es nicht ist)
------------------------------

- Kein "schneller Zug" und kein verlässlicher Dauerdienst ohne Tunnel-Freigaben.
- Kein Ersatz für Konvoi-Planung/Handelsrouten (siehe [caravan-moves](../../haendlerbund/05-projects/caravan-moves.md)).

Status (aktueller Arbeitsstand)
-------------------------------

- Status: **prototyping** (angefangen vor RP-Abbruch; noch kein abgesicherter Feldtest).
- Nächster Meilenstein: **sicherer Testlauf** unter konservativen Bedingungen.

Canonical Constraints (Reference)
---------------------------------

- Träger/Owner: Jonas (Bau/Integration), mit Sicherheits-/Systemreview durch Pahl.
- Ziel bleibt ein konservativer Material-/Transport-Usecase für Nordlinie (D5↔C6), nicht „schnell“ und nicht als Dauerdienst.
- Erstlauf ohne Personentransport, bis Tunnel + Not-Aus validiert sind.
- Logpflicht: Missionslog + Logistik (Materialverbrauch, Schäden, Lessons Learned).

Arbeitsannahmen (konservativ)
-----------------------------

- Erstlauf ohne Personentransport (nur Material), bis Tunnel und Not-Aus getestet sind.
- Realistische Schaetzung fuer Materiallast: ca. 200-400 kg pro Lauf (je nach Zustand/Steigung/Abschnitt).
- Fahrweise: langsam/planbar, Fokus auf Sicherheit statt Tempo.

Materialbuchung Werkstatt (konservativ, 2026-04-27)
---------------------------------------------------

| Posten | Aus D5 gebunden | Rest in D5 | Lesart |
| --- | --- | --- | --- |
| Schmieroel | `1` | `3` | fuer aktuellen Prototyp-/Montagezustand gebunden |
| Lagerfett (Technik) | `1` | `2` | fuer Lauf- und Lagerpunkte gebunden |
| Sicherungssatz | `1 Set` | `3 Sets` | kleiner Elektro-/Sicherungsbedarf im Werkstattaufbau |
| Dichtungsmanschette | `1` | `5` | fuer Abdichtung/Passung im Prototyp gebunden |

Hinweise

- Diese Buchung meint gebundenen Werkstattbestand, nicht bereits verfahrenen Feldverbrauch.
- Solange kein freigegebener Testlauf stattfindet, bleiben weitere Verbraeuche und Schaeden offen.

Rollen
------

- Jonas: Bau/Integration, Werkstattlog, Materialliste, Erst-Checks.
- Pahl: Sicherheits- und Systemreview, Freigaben (Hausregeln), Abnahme von Risiko-/Notfallprotokollen.

Gates für den ersten Testlauf
-----------------------------

- **Tunnel-Status**: Abschnitt freigegeben (Sicherung/Belüftung/Statik ok) → Link: `Nordlinie-01`.
- **Brems-/Stop-Protokoll**: definierte Stopp-Punkte, Not-Aus, Rückzug.
- **Lastgrenzen**: konservativ; kein Personentransport im Erstlauf, wenn nicht explizit freigegeben.
- **Logpflicht**: Missionslog-Eintrag + Logistik-Abgleich (Materialverbrauch, Schäden, Lessons Learned).
- Die aktuelle kleine Werkstattbindung ist nun konkret gebucht; weitere Teile bleiben bewusst offen, bis sie wirklich im Prototyp verschwinden oder als Ersatzlauf belegt sind.

Risiken (kurz)
--------------

- Tunnelzustand (Trümmer/Belüftung/Engstellen)
- Energie-/Antriebszuverlässigkeit
- Fraktions-Noise (Beobachtung/Abfangen)

Links
-----

- Projekt Nordlinie-01 → ../05-projects/Nordlinie-01.md
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ./Missionslog-Novapolis.md
- Jonas (Werkstatt) → ../02-characters/Jonas-Merek.md
- Pahl (Abnahme/Hausregeln) → ../02-characters/Pahl-Brenner.md
- Karawanenbewegungen (Übersicht) → ../../haendlerbund/05-projects/caravan-moves.md
