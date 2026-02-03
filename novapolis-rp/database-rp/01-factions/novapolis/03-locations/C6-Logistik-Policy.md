---
stand: 2026-02-02 12:45
update: Aus 00-admin verschoben (stationsbezogene Policies liegen bei Locations); Links/Ops-Pfad angepasst.
checks: manuell (2026-02-02 12:45)
slug: c6-logistik-policy
status: v0.1 (Entwurf, aktiv)
category: Location
---
C6 - Logistik-Policy (Novapolis)
================================

Bezug: [MERCHANT-HQ] S.3 in `database-curated/staging/reports/uncertainties.md`

Zweck
-----
C6 ist Teil von Novapolis und dient der Logistikabteilung als Stützpunkt. Diese Policy definiert Zonen, Zugriffsrechte, Betriebsregeln
und Verlinkungen.

Zonen
-----
- Öffentlich/Handel (Z1)
  - Zweck: Warenumschlag, diplomatische Kontakte, Gästeempfang (kontrolliert)
  - Zugang: Begleitet; Besucher-Log verpflichtend
- Betrieb/Logistik (Z2)
  - Zweck: Lager, Umladung, Wartung, Materialfluss
  - Zugang: Logistikrolle erforderlich; PSA nach Aushang
- Kernsektor Novapolis (Z3)
  - Zweck: interne Arbeits- und Ruhezonen (Novapolis-Kern)
  - Zugang: Nur Novapolis-Kernrollen; Besucher verboten
- Technik/Generator (Z4)
  - Zweck: Energie/Schalt- und Leitungszustände; Prüf-/Wartungsbereich
  - Zugang: Technik/Leitung; Freigabeprotokoll vor Eingriffen
- Med/Quarantäne (Z5)
  - Zweck: Behandlung/Isolation; temporär aktivierbar
  - Zugang: Med/Leitung; Protokolle priorisiert

Hinweis: Zonen sind schematisch („nicht als Referenz“). Genaue Lage siehe [C6](./C6.md) (schematisch) und Stations-Canvas.

Zugriffs- und Rollenregeln
--------------------------
- Rollen-Pflichtfelder (vgl. Charakter-Canvas): Wächter, Technik, Leitung, Logistik, Med
- Rollen-Split Karawane H-47 (SSOT):
  - Kora: Betrieb/Logistik (Z2) und interne Leitung; führt Echo-Protokolle
  - Marven: Konvoi/Handel (Z1) und Außenkoordination; schützt vertrauliche Koordinaten/Absprachen
  - Arlen: Vermittlung/Außenkontakte (Z1); keine Doppelrolle als interne Leitung
- Zutritt Zonen:
  - Z1: Begleitet; Besucher-Log
  - Z2: Logistikrolle
  - Z3: Kernrollen
  - Z4: Technik/Leitung + Freigabe
  - Z5: Med/Leitung
- Hausregeln (H.1): Unautorisierte Nachschau („Schnüffeln“) → Verwarnung → Entzug Zugriffe; Meldung an Leitung

Betriebslogistik
----------------
- Inventare strikt getrennt (Y.1): pro Fraktion; Fraktionshändler separat
- Missionsfluss (L.1): Status → Inventarabschluss → Verlinkungen (Logistik/Missionen) → Archiv
- Energie/Versorgung: Teilversorgung durch D5; Leitungs-/Schaltzustand limitiert
- Wöchentliche Abrechnung (U.2): Sim/Abrechnung im Wochenzyklus (Gesamtabrechnung)

Kommunikation & Systemmeldungen
-------------------------------
- Betriebslog: Statusmeldungen/Abweichungen werden protokolliert (Details/Marker siehe [C6 - Logistik-Policy (Ops)](../../../00-ops/C6-Logistik-Policy.ops.md))
- Funk: D5↔C6 schwach, boosterabhängig (linienbasiertes Modell)

Sicherheit
----------
- Wächter priorisieren Z3/Z4, Besucherführung in Z1
- Anomalien (W.1): Im Lokations-Canvas; Auswirkungen in betroffenen Charakter-Canvas

Verlinkungen
------------
- Locations: [C6](./C6.md)
- Logistik-Canvas: [Logistik](../../../00-admin/Logistik.md)
- Missionslog: [Missionslog](../../../00-admin/Missionslog.md)
- Neutralgruppen: (geplant) `database-rp/00-admin/Neutralgruppen.md`
- Karawanenbewegungen: (geplant) [caravan_moves](../01-factions/haendlerbund/05-projects/caravan_moves.md)

Änderungen/Versionierung
------------------------
- Änderungen per 3-Schritt-Prozess; kleine Commits; Verweise auf IDs (S.3, L.1, Y.1, U.2, H.1)


