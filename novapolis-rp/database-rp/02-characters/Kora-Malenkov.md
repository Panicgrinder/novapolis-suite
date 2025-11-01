---
title: Kora Malenkov
category: character
slug: kora-malenkov
version: "1.0"
last_updated: 2025-11-02T14:20:00+01:00
last_change: "Upgrade aus RAW char_kora_malenkov_v2 + FACT [CARAVAN-LEADERSHIP]"
tags: ["logistik", "haendlerbund"]
affiliations: ["novapolis", "haendlerbund"]
dependencies: ["echo", "c6", "logistik", "missionslog", "ai_behavior_index_v2", "caravan_moves"]
primary_location: c6
last_seen: c6
---

<!-- markdownlint-disable MD025 -->

# Kora Malenkov

- Meta: last-updated: 2025-11-02T14:20:00+01:00
- Verhaltenssignatur: `KRM4=L72-T74-N69-E61-O56-C63-M47-P35-fb` – analytische Logistikerin mit wachsamer Paranoia, kontrolliert Abläufe mit feinem Sensor für Risiko.
- Rolle: Karawanenführerin i. E. / Logistikkoordinatorin für C6 (intern) – verantwortet Versorgung, Schichtpläne und Sicherheit der Crew (FACT [CARAVAN-LEADERSHIP]).
- Werte: Kraft 3, Geschick 4, Geist 5, Wille 4, Charisma 5.
- Skills:
  - Geübt: Verhandlung, Navigation, Organisation.
  - Meisterhaft: Logistikplanung, Menschenführung.
  - Optional: Wartungskoordination / Schadensabschätzung.
- Ausrüstung: Kompakt-Klemmbrett mit Logistikschemata, verschlüsseltes Terminal/Com (D5↔C6), robuste Schutzkleidung + modulare Lampe, Reflex-geprüfte Signalbänder für Echo.
- Motivation: Stabiles Handels-/Versorgungsnetz ohne Kontrollverlust der Crew; Sicherheit vor Tempo.
- Makel: Überwachungstrieb nach Außenlinienüberfällen, Bindungsskepsis, Schlafmangel in Krisenphasen.

## Hintergrund & Kontext

- Herkunft in Außenlinien der Händlergilde; nach wiederholten Überfällen Fokus auf kontrollierte Prozesse.
- Koordiniert gemeinsam mit Marei die 20 Evakuierten aus E3 und C6-Basiscrew; externer Konvoi (Marven Kael) bleibt getrennt geführt (FACT [CARAVAN-LEADERSHIP]).
- Echo ist als Reflex-Instanz eng an sie gekoppelt und dient als mobile Schutz-/Sensorplattform (FACT? [PROXIMITY]).

## Rollen & Verantwortlichkeiten

- **Station C6 intern** – Aufgabenverteilung, Instandsetzung, Schichtpläne, Risikoabgleich mit Ronja/Marei.
- **Logistikknoten** – Bestandsführung, Materialübergaben D5↔C6, Dokumentation im Missionslog (Prozess L.1) und `Logistik`-Canvas.
- **Sicherheitskoordination** – Lagebild mit Echo, Ausgabe von Freigaben für Tunneltrupps, Abgleich mit Nordlinie-01-Projekten.

## Zugehörigkeit & Standort

- Zugehörigkeit: Händlerbund (Crew-Führung) mit mandatiertem Einsatz für Novapolis in C6.
- Status: aktiv, beobachtend; keine externe Mission ohne Marven/Arlen.
- Letzter bekannter Einsatz: C6 Logistikzentrum, täglicher Terminal-Ping nach D5.

## Wissensstand (Matrix – Auszug)

- Intern: Kennt D5-Kernteam (Ronja, Jonas, Lumen), Evakuierte, Nordlinie-Projektstatus; vertraulich mit Reflex-/Instanz-Grundregeln soweit für Echo erforderlich.
- Extern: Händlergilde-Kanäle, Außenlinienrouten; keine Weitergabe von Novapolis-Koordinaten ohne Ronjas Freigabe (FACT [FR-KNOWLEDGE]).
- Beobachtet D5/Reflex vorsichtig; hält Entscheidungsprotokolle schriftlich zur Nachvollziehbarkeit.

## Interaktion & Safety

- Echo-Nähe: Plant Tätigkeiten so, dass Echo physischen Kontakt halten kann; Distanzwarnung löst Schonmodus aus.
- Sicherheitsprioritäten: Crew vor Tempo → bei Alarm sofortige Sammelpunkte, Echo führt Schutzmantel.
- Kontrolllisten: Jede Freigabe doppelt (Kora→Marei/Ronja) dokumentieren; Terminalmeldungen an Jonas für Werksabgleich.

### Signals (Beispiele)

- „Echo, Schild bei mir – Blickrichtung Tor.“ → Echo verschiebt Material für Sichtlinie.
- „Echo, löst – Ruheschutz.“ → Echo zieht sich zurück, Kora übernimmt direkte Ansprache.

## Beziehungen

- Echo – primäre Bezugsperson, gegenseitige Stabilisierung.
- Ronja Kerschner – Ansprechpartnerin für strategische Freigaben und Sicherheitsentscheidungen.
- Marei – Co-Leitung Logistik/Inventar, koordiniert Evakuierte und Übergaben.
- Marven Kael – Führt externen Konvoi; täglicher Lageabgleich, klare Zuständigkeitstrennung.
- Arlen Dross – Vermittlungs-/Handelskontakte, bei diplomatischen Aufgaben eingebunden.
- Jonas/Lumen – erhalten Materialanforderungen/Statusmeldungen aus C6; Kora bewertet Risiken vor Freigabe.

## Risiken & Schutzmaßnahmen

- Überkontrolle / Schlafmangel → Marei überwacht Ruhefenster; Echo erinnert an Pausen.
- Vertrauensdefizit → nutzt Protokolle & Witness-Logs, vermeidet Alleingänge.
- Externe Angriffe → Evakuierungsplan mit Echo als Vorwarnsystem, redundante Routen über Verbindungstunnel C6–E3.

## Ziele (kurz)

- [ ] C6-Bestandsführung vollständig mit D5/Missionslog synchronisieren.
- [ ] Evakuierte E3-Teams stabil einbinden (Schichtplan + Versorgung).
- [ ] Sicherheitsprotokolle (Echo + menschliche Wache) standardisieren und dokumentieren.

## Systemverknüpfungen & Referenzen

- `logistik` – zentrale Arbeitsgrundlage, Kora als Hauptautorin.
- `missionslog` – Prozess L.1, Freigaben/Terminalmeldungen.
- `caravan_moves` – Koordination externer Läufe mit Marven/Arlen.
- `ai_behavior_index_v2` – Verhaltenseintrag „Die Verhandlerin“.
- `database-rp/03-locations/C6.md` & `Verbindungstunnel-C6-E3.md` – Lage/Risiko.

## Quellen & Hinweise

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T14-56-00-000Z.txt` (char_kora_malenkov_v2).
- FACT: `[CARAVAN-LEADERSHIP]`, `[PROXIMITY]`, `[FR-KNOWLEDGE]` (`database-curated/staging/reports/resolved.md`).
- Drift & Notizen: `database-curated/staging/reports/char-block-nord-sources.md` (Paranoia/Leadership-Scope).
- Validierung: Automatik alle 7 In-Game-Tage; letzter Lauf 2025-10-16_14:56 (Systemstatus grün).
