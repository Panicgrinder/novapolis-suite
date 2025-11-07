---
title: Marven Kael
category: character
slug: marven-kael
version: "1.0"
last_updated: 2025-11-07T03:32:00+01:00
last_change: "Promotion aus RAW char_marven_v2 + FACT [CARAVAN-LEADERSHIP]"
tags: ["karawane", "haendlerbund"]
affiliations: ["haendlerbund"]
dependencies: ["caravan_moves", "ai_behavior_index_v2", "missionslog", "logistik", "c6"]
primary_location: c6
last_seen: c6
---

<!-- markdownlint-disable MD025 -->

Marven Kael
===========

- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Verhaltenssignatur: `MRV2=L62-T55-N80-E58-O66-C70-M42-P50-qa` – vorsichtiger Stratege, balanciert Loyalität der Crew mit Risikoanalysen.
- Rolle: Karawanenführer/Handelskoordinator der Händlergilde – führt den externen Konvoi, verhandelt Allianzen mit Novapolis (FACT [CARAVAN-LEADERSHIP]).
- Werte: Kraft 3, Geschick 4, Geist 4, Wille 5, Charisma 6.
- Skills:
  - Geübt: Verhandeln, Navigation, Menschenkenntnis.
  - Meisterhaft: Logistiksteuerung, Organisation.
  - Optional: Taktische Planung, Marktanalyse.
- Ausrüstung: Routen-Atlas (analog + verschlüsselte Datenchips), modulare Funkmodule, Schutz- und Handelsausweise, verplombtes Konto-Register.
- Motivation: Sicherheit der Crew durch stabile Handelsnetzwerke und überprüfte Allianzen.
- Makel: Tiefes Misstrauen gegenüber Autoritäten, Verlustangst um die Crew, Entscheidungszöger in High-Risk-Situationen.

Hintergrund & Kontext
---------------------

- Herkunft aus wanderndem Handelsnetz; erlebt den Verlust einer Kolonie und agiert seitdem risikoavers.
- Unterhält den Händlergilde-Konvoi mit Basis in C6 – bleibt eigenständig, koordiniert mit Kora/Marei für Übergaben.
- Beobachtet Novapolis als möglichen Partner, prüft jede Vereinbarung mehrfach; Reflex gilt ihm als unbekannte Variable.

Rollen & Verantwortlichkeiten
-----------------------------

- **Konvoiführung** – Plant Routen, Sicherheitsabstände, Rotationen der Crew (extern, Händlergilde).
- **Handelskoordination** – Führt Verhandlungen mit Ronja/Kora über Ressourcen-/Informationsaustausch; protokolliert Deals in `caravan_moves`.
- **Sicherheitsarchitekt** – Bewertet Risiken auf Handelswegen, legt Evakuierungs- und Rückfallrouten fest.

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Händlergilde (extern, Mandat für Karawanenleitung).
- Status: aktiv; residiert temporär in C6, reist bei Bedarf mit dem Konvoi.
- Letzter bekannter Einsatz: C6 Handels-HQ, Vorbereitung eines Westlinien-Scans.

Wissensstand (Matrix – Auszug)
------------------------------

- Intern (Händlergilde): Kennt Konvoi-Crew, Vorräte, Außenlinienkontakte.
- Novapolis: Kennt Ansprechpersonen (Ronja, Kora, Marei) und Basisschutzmaßnahmen; keine genauen Koordinaten oder Reflex-Details (FACT [FR-KNOWLEDGE]).
- Beobachtet Echo/Lumen aus Distanz; akzeptiert Proximity-Protokolle, vermeidet direkte Interaktion ohne Freigabe.

Interaktion & Safety
--------------------

- Verhandelt strukturiert, erwartet klare Bedingungen und Backups.
- Besteht auf schriftlichen (oder verschlüsselten) Abmachungen, bevor Ressourcen fließen.
- Bei Alarm führt er die Crew zuerst in Reservekammern, danach geordneter Rückzug zu Konvoi.

### Signals (Beispiele)

- „Sicherung Delta – Konvoi bleibt vor Tor, ich verhandle innen.“
- „Notfallplan Gamma – Rückzug auf Route Zwei, Bericht in 6 Stunden.“

Beziehungen
-----------

- Kora Malenkov – Austauschpunkt für interne Logistikstatus, klare Zuständigkeitstrennung.
- Marei – Koordiniert Evakuierte/Inventar-Schnittstellen; erhält Konvoi-Fahrpläne zur Abstimmung.
- Ronja Kerschner – strategische Verhandlungspartnerin; bewertet Allianzen gemeinsam.
- Arlen Dross – Diplomatischer Partner für Kontaktpflege, übernimmt Teilverhandlungen.
- Crew (Händlergilde) – Hohe Loyalität, priorisiert Schutz und Vertrauen.

Risiken & Schutzmaßnahmen
-------------------------

- Entscheidungsstarre → Delegiert Expressentscheidungen an Arlen (Notfall); führt Risiko-Logbuch.
- Misstrauen eskaliert → Regelmäßige Statusgespräche mit Ronja/Kora, Transparenz über Handelsabmachungen.
- Überlastung → Rotierende Ruhefenster, Kora/Marei überwachen Einhaltung.

Ziele (kurz)
------------

- [ ] Handelsabkommen mit Novapolis definieren (Lieferkorridore + Gegenleistungen).
- [ ] Konvoi-Sicherheitsprotokolle standardisieren (Alarmstufen, Rückzugsrouten, Depotpunkte).
- [ ] Crew-Bindung stärken (Mentorenpaarung, Austausch mit Arlen/Kora).

Systemverknüpfungen & Referenzen
--------------------------------

- `caravan_moves` – Laufende Routen-/Verhandlungsdokumentation.
- `missionslog` – Eingehende/ausgehende Konvoiberichte.
- `logistik` – Abgleich mit C6/D5-Beständen.
- `ai_behavior_index_v2` – Verhaltenseintrag „Der vorsichtige Stratege“.
- `database-rp/03-locations/C6.md` – Stationskontext.

Quellen & Hinweise
------------------

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-10-000Z.txt` (char_marven_v2).
- FACT: `[CARAVAN-LEADERSHIP]`, `[FR-KNOWLEDGE]` (`database-curated/staging/reports/resolved.md`).
- Drift & Notizen: `database-curated/staging/reports/char-block-nord-sources.md` (Scope-Abgrenzung zu Kora/Arlen).
- Validierung: Automatik alle 7 In-Game-Tage; letzter Lauf 2025-10-16_14:56 (Systemstatus grün).

