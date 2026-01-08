---
stand: 2026-01-08 09:15
update: ATSD-Referenz als Link ergänzt; Verlinkungen auf relative Pfade vereinheitlicht.
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' 'DONELOG.md' PASS (2026-01-08 09:15); python scripts/check_frontmatter.py novapolis-rp/database-rp DONELOG.md PASS (2026-01-08 09:15); python scripts/checks_rp_consistency.py --strict PASS (2026-01-08 09:15)
slug: c6-logistik-policy
status: v0.1 (Entwurf, aktiv)
category: Admin
---

C6 - Logistik-Policy (Novapolis)
================================

Bezug: [MERCHANT-HQ] S.3 in `database-curated/staging/reports/uncertainties.md`

Zweck
-----
C6 ist Teil von Novapolis und dient der Logistikabteilung als Stützpunkt. Diese Policy definiert Zonen, Zugriffsrechte, Betriebsregeln und Verlinkungen.

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

Hinweis: Zonen sind schematisch („nicht als Referenz“). Genaue Lage siehe `03-locations/C6.md` (schematisch) und Stations-Canvas.

Zugriffs- und Rollenregeln
--------------------------
- Rollen-Pflichtfelder (vgl. Charakter-Canvas): Wächter, Technik, Leitung, Logistik, Med
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
- System-/Debug: Persistenz aktiv; ATSD-String + Canvas-Zahl (Definition: [Admin: Day-Switch & Debug](./Canvas-Admin-Day-Switch-Debug.md))
- Debug-Mode: zuschaltbar für erweiterte Ausgaben
- Funk: D5↔C6 schwach, boosterabhängig (linienbasiertes Modell)

Sicherheit
----------
- Wächter priorisieren Z3/Z4, Besucherführung in Z1
- Anomalien (W.1): Im Lokations-Canvas; Debuffs in betroffenen Charakter-Canvas

Verlinkungen
------------
- Locations: [C6](../03-locations/C6.md)
- Logistik-Canvas: [Logistik](./Logistik.md)
- Missionslog: [Missionslog](./Missionslog.md)
- Neutralgruppen: (geplant) `database-rp/00-admin/Neutralgruppen.md`
- Karawanenbewegungen: (geplant) [caravan_moves](../05-projects/caravan_moves.md)

Änderungen/Versionierung
------------------------
- Änderungen per 3-Schritt-Prozess; kleine Commits; Verweise auf IDs (S.3, L.1, Y.1, U.2, H.1)


