---
stand: 2026-02-09 04:23
update: Arbeitsannahmen fuer realistische Schaetzung ergaenzt.
checks: "not run (content update)"
title: Draisine-/Transportmodul (Prototyp)
category: project
slug: draisine-transportmodul
status: prototyping
version: "0.1"
last_updated: 2026-01-11T02:04:00+01:00
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

Arbeitsannahmen (konservativ)
-----------------------------

- Erstlauf ohne Personentransport (nur Material), bis Tunnel und Not-Aus getestet sind.
- Realistische Schaetzung fuer Materiallast: ca. 200-400 kg pro Lauf (je nach Zustand/Steigung/Abschnitt).
- Fahrweise: langsam/planbar, Fokus auf Sicherheit statt Tempo.

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

Risiken (kurz)
--------------

- Tunnelzustand (Trümmer/Belüftung/Engstellen)
- Energie-/Antriebszuverlässigkeit
- Fraktions-Noise (Beobachtung/Abfangen)

Links
-----

- Projekt Nordlinie-01 → ../05-projects/Nordlinie-01.md
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../../../00-admin/Missionslog.md
- Jonas (Werkstatt) → ../02-characters/Jonas-Merek.md
- Pahl (Abnahme/Hausregeln) → ../02-characters/Pahl.md
- Karawanenbewegungen (Übersicht) → ../../haendlerbund/05-projects/caravan-moves.md
