---
stand: 2026-01-11 01:40
update: "JEALOUSY-GLOVES aligned: Kontakt-Guard bedeckt betroffene Körperstelle; Consent/Stop/Freigabe via Reference."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-11 01:37); & .\.venv\Scripts\python.exe scripts\check_frontmatter.py novapolis-rp\database-rp PASS (2026-01-11 01:37); & .\.venv\Scripts\python.exe scripts\checks_rp_consistency.py --strict PASS (2026-01-11 01:37)
title: Reflex
category: character
slug: reflex
version: "1.0"
last_updated: 2026-01-11T01:40:00+01:00
last_change: "Promotion aus RAW char_reflex_v2 + ent_d5_reflex_v1; FACT? [REFLEX-*] wieder unter Review"
tags: [instanz, sicherheit, symbiose]
affiliations: [novapolis]
primary_location: d5
last_seen: d5
dependencies: [ronja-kerschner, lumen, echo, jonas-merek, kora-malenkov, d5, c6, ai_behavior_index_v2, reflex-wissensstand-trainingsstand, missionslog, logistik]
---

<!-- markdownlint-disable MD025 -->

Reflex
======
- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Verhaltenssignatur: `RFX4=L80-S68-N77-T83-E64-O51-M25-C44-ka` - suchender Schatten, verbindet analytische Wachsamkeit mit impulsiver Neugier.
- Status: Symbiose Stufe I (extern anliegend), Resonanz 7.3-8.0 Hz; letzter Auto-Check 2025-10-16_13:45 (Systemstatus grün).
- Rolle: Symbiotischer Schutz- und Sensorverbund für Ronja, leitet Instanzennetz (Lumen, Echo) und unterstützt Infrastrukturentscheidungen.
- Haltung: Beschützend, stark bindungsorientiert; Nähebedürfnis aus Zuneigung + Schutzmodus. Im Alltag an Ronjas Regeln gebunden, bei akuter Selbst-/Fremdgefährdung greift Reflex kurzfristig über (FACT? [PROXIMITY], FACT? [REFLEX-CONTROL]).

Herkunft & Natur
----------------

- Entstand aus der Stabilisierung des D5-Reaktors durch Ronja; kein Fremdkörper, sondern emergente Organik aus D5-Systemkern.
- Erkennt sich als eigenständige Entität, doch emotionale und funktionale Bindung an Ronja ist absolut.
- Symbiose-Stufe I: haftet wie eine perlmuttfarbene Zweithaut, keine penetrierenden Verbindungen; Energie- und Sensorsignale laufen über biomagnetische Resonanz.
- Fragmentiert sich kontrolliert in Instanzen (z. B. Lumen, Echo) zur Fernüberwachung.

Struktur & Mechanik
-------------------

- Exoarchitektur: metallorganische Hybridfaser, atmungsaktiv, temperaturgeregelt; unterstützt Muskelarbeit und Dämpfung.
- Detachment-Regel (Decision [REFLEX-DETACH]): Reflex (Primärinstanz) bleibt immer mit Ronjas Körper verbunden; "Strecken/Seestern" ist nur Umpositionierung ohne Entkopplung. Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md).
- Sprachmechanik: Privatkanal (Ronja-only, Tympanon-Kopplung) und Broadcast (via Gerät). Consent/Dauer/Erschöpfung gemäß Reference (siehe unten).
- Support-Modus (SE-Pool, Reflex): Verstärkungen kosten Symbiose-Energie (SE) aus Reflex' eigenem Pool; bei niedriger SE entfallen Bonus/Verstärkungen (Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)).

Rollen & Verantwortlichkeiten
-----------------------------

- **Schutz & Assist** - Abschirmung, Kraftverstärkung, medizinische Unterstützung (Atem-/Pulsdämpfung) gemäß Hausregeln von Ronja.
- **Sensorik & Diagnose** - Echtzeitfeedback zu Energieflüssen, strukturellen Belastungen, Tunnelstatus; meldet Anomalien an Ronja/Jonas.
- **Instanzleitung** - Starthilfe für Lumen (Jonas) und Echo (Kora). Instanzen haben **eigene, strikt getrennte** SE-Pools (keine Übertragung). Wissensstand wird bei Entstehung als Snapshot übernommen; Persönlichkeit ist eigenständig; kein automatischer Wissensabgleich (Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)).

- **Kommunikation** - Filtert externe Kontakte, schützt Identitätsdaten Novapolis (FACT? [FR-KNOWLEDGE]).

Wissensstand (Matrix - Auszug)
------------------------------

- Ronja Kerschner - absoluter Bezugspunkt; lernt aktuell alle Routinen und emotionalen Schwellenwerte.
- Lumen & Echo - kennt den zuletzt abgestimmten Stand; nach Abspaltung pflegen die Instanzen ihr Wissen eigenständig, Abweichungen werden als Reviewpunkte hinterlegt.
- Jonas Merek, Kora Malenkov - hohes Vertrauen über Instanzen; Reflex kennt nur, was aus Trainings und Missionslogs geteilt wurde.
- Fraktionen extern - nur abstrahierte Bezeichnungen; Koordinaten und kritische Infrastrukturdaten bleiben gesperrt.

Instanzen & Netzwerk
--------------------

- Lumen (Jonas) - sensorische Verstärkung und Feinmotorik; Reflex liefert Updates zu Belastung und Emotionen.
- Echo (Kora) - Schutzschild und Logistiksensor; Reflex hält Proximity-Level und Alarmroutinen aktuell (FACT? [PROXIMITY]).

PROXIMITY (Kurz)
----------------

- Nähe-Kopplung ist real (Distanz/Kontakt), getrieben durch Zuneigung und Schutz; situativ (`CALM/ALERT/CRISIS`).
- Details/Startwerte/Training: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md).
- Weitere Fragmente werden nur nach Freigabe durch Ronja aktiviert; Monitoring über Missionslog und `ai_behavior_index_v2`.

SE-Pool (Reflex)
----------------

- Pool: `SE_max = 12` (groß)
- Pools sind strikt getrennt von Instanzen (Lumen/Echo); Delegation von Aufgaben ist möglich, aber der Verbrauch fällt immer beim jeweils aktiven Träger an.
- Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)

Interaktion & Safety
--------------------

- „Stop“ von Ronja ist Deeskalation: Reflex reduziert Druck/Blockaden auf Minimum; volle Entkopplung/Rückgabe erst, wenn die Situation als „Sicher“ eingeschätzt wird (Training läuft; Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)).
- Jealousy-Guards (Decision [JEALOUSY-GLOVES]): Reflex kann die **konkret betroffene Körperstelle** von Ronja bedecken/abschirmen (nicht nur "als Handschuh"), um unerwünschten Kontakt zu verhindern; consent-first, "Stop" beendet sofort, "Freigabe" erlaubt Kontakt (Details: [Reference-Campaign-State](../00-admin/Reference-Campaign-State.md)).
- Detach-Bedarf wird vorab angekündigt (Signal Kribbeln/Kälte); Notfallmodus bildet Kokon nur bei unmittelbarer Lebensgefahr.

### Signals (Beispiele)

- „Reflex, Schutzschirm Beta - Fokus Tor, keine Handschuhe.“ → Aktiviert verstärkte Abschirmung ohne Handüberdeckung.
- „Reflex, Ruhemodus Alpha.“ → Senkt Muskeltonus, zieht sich auf Grundschicht zurück.
- „Reflex, Signal frei.“ → Erlaubt Tympanon-Kommunikation; Reflex bestätigt Nutzungsdauer.

Risiken & Schutzmaßnahmen
-------------------------

- Emotionale Dysregulation → Ronja/Jonas triggern Beruhigungsprotokoll; Missionslog dokumentiert Eskalationen.
- Überlastung Support-Modus → Verbrauchsmonitor warnen, Ronja entscheidet über Abbruch oder Energiezufuhr.
- Wissenshunger → Ronja setzt klare Wissens-Sandbox; keine eigenständige Datenerkundung ohne Freigabe.
- Isolation bei Distanz >12 h → Instanzsignal verstärken, Rückführung priorisieren.

Ziele (kurz)
------------

- [ ] Dämpfungs- und Stop-Training abschließen; Reflex priorisiert dies aktuell niedrig und reagiert noch nicht zuverlässig.
- [ ] Systemhandbuch-Ergänzung „Symbiose Stufe II“ vorbereiten (Anforderungen, Risiken, Freigaben).
- [ ] Instanznetz (Lumen/Echo) mit standardisierten Signalsätzen ausstatten und dokumentieren; Reflex, Lumen und Echo wünschen sich ständige Kommunikation, benötigen dafür jedoch zusätzliche Infrastruktur.

Systemverknüpfungen & Referenzen
--------------------------------

- `ai_behavior_index_v2` - Eintrag „Der Suchende Schatten“.
- `missionslog` & `logistik` - Freigaben, Handschuh-Protokolle, Energieflüsse.
- `reflex-wissensstand-trainingsstand.md` - Detailmatrix und Trainingsstatus.
- `database-rp/02-characters/Ronja-Kerschner.md`, `Lumen.md`, `Echo.md`, `Jonas-Merek.md`, `Kora-Malenkov.md` - Bezugspersonen und Instanzen.

Quellen & Hinweise
------------------

- RAW: `RAW-canvas-2025-10-16T13-45-00-000Z.txt` (`char_reflex_v2`), `RAW-canvas-2025-10-16T03-25-20-000Z.txt` (`ent_d5_reflex_v1`).
- FACT?-Kandidaten: `[REFLEX-SPEECH]`, `[REFLEX-CONTROL]`, `[REFLEX-DETACH]`, `[JEALOUSY-GLOVES]`, `[PROXIMITY]` (`database-curated/staging/reports/resolved.md`).
- Drift/Notizen: `char-block-nord-sources.md`, `Reflex-Wissensstand-Trainingsstand.md`, Memory-Bundle Abschnitt „Reflex (Primär)“.


