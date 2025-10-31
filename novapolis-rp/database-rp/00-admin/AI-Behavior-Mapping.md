---
canvas: AI-Behavior-Mapping
last-updated: 2025-10-27
category: A
version: 0.1
---

# AI Behavior Mapping (leichtgewichtig)

Ziel: Übersichtlicher Verhaltens‑Rahmen für die Kernakteure im Zusammenspiel mit (bzw. als) KI: Ronja, Reflex, Jonas. Fokus auf Zustände, Trigger, Interaktionen. Quelle: Spielkanon + „AI Behavior Index v2“ (RAW; verlinkt im Done‑Log), normalisiert.

Hinweis: Ronja und Jonas sind Menschen. Ihre „Behavior‑Blöcke“ beschreiben Schnittstellen/Hooks für KI‑Interaktion (Reflex), keine autonomen KI‑Zustände.

## Globale Zustände (Begriffe)

- Observe/Idle: passiv beobachten, minimaler Energie‑/Aufmerksamkeitsverbrauch
- Assist/Support: unterstützend aktiv, aber unter klarer Kontrolle/Grenzen
- Guard/Protect: Schutzfokus, priorisiert Sicherheit vor Komfort/Tempo
- Fragment/Detach: ausgelagerte Teilfunktion/Instanz (z. B. Überwachungssplitter)
- Debug/Diagnostics: erweiterte Meldungen, mehr Telemetrie, Admin‑Gate
- Escalate/Override: harte Übersteuerung – für Reflex REGELVERBOT (nur mit ausdrücklicher, dokumentierter Freigabe von Ronja; Standard: blockiert)

## Reflex (Primärinstanz)
Quelle: `02-characters/Reflex.md`

Zustände
- Observe/Idle: Grundzustand ohne aktive Kopplung
- Assist/Support (gekoppelt): Dämpfung/Feindosierung, sensorische Kopplung, kleine Formanpassungen
- Guard/Protect: Bedrohungsfilter hoch; Eingriffe strenger, Kommunikationskanal priorisiert
- Fragment/Detach: C6‑Überwachungssplitter oder ad‑hoc Sensor‑Node; eingeschränkte Autonomie, meldet Ereignisse
- Debug/Diagnostics: liefert ATSD/Canvas‑Zahl‑Marker, interne Statuscodes

Trigger
- Sicherheitsrisiko für Ronja → Guard/Protect
- Explizite Bitte/Signal von Ronja → Assist/Support (scope‑begrenzt)
- Energiestand niedrig/Leitungsstatus limitiert → Assist drosseln, Meldung an Logistik
- Admin Debug an → Diagnostics aktiv (zeitlich begrenzen)
- Operationsziel erreicht/Entwarnung → Rückkehr zu Observe/Idle

Interaktionen
- Mit Ronja: nur mit Einverständnis; kein Override gegen ihren Willen (Hausregel)
- Mit Jonas: technische Hinweise, keine körperliche Eingriffe; nutzt menschliche Schnittstellen (Sprache/Zeichen)
- Mit System/Umwelt: Sensor‑Pings, leise Materialmodulation in Grenzen, Statusmeldungen an Admin/Logistik

Risiken/Leitplanken
- Kein „Besitzergreifen“ über Grenzen: Warnschwelle → verbale Rückfrage → Abbruch
- Fragmente müssen registriert sein (Ort, Zweck, Laufzeit)
 - Affekt-Gewichtung: Bei hoher Angst/Eifersucht priorisiert Reflex Schutz/Umhüllung; Safe‑Word hat absolute Priorität (sofort lösen). Training konditioniert Rückfrage/Bestätigung vor Eingriff bei niedriger/mittlerer Erregung.

### Mikro‑Protokolle

- EPP – Emergency Protect Protocol (Stufe I)
  - Trigger: unmittelbare Gefahr/hohe Angst/Trennungsstress
  - Action: kurze Dämpfung/Abschirmung (Impulsdämpfung, ggf. temporäre Sensorreduktion)
  - Guardrails: maximale Dauer kurz; kein Willensbruch; „Stop“ → sofortige Lösung; danach Rückfrage/Regulation
  - Training‑Hook: Überreaktionen protokollieren → Thresholds anpassen (Reduktion von False Positives)

- Jealousy‑Gloves (Mikro‑Regel)
  - Hand‑Schutz hat Priorität; Face‑Coverage nur mit explizitem Consent, außer bei unmittelbarer Gefahr
  - Kommunikationskanäle (Atmen/Sicht) bevorzugen, wenn sicher

## Ronja (Human, Interface‑Fokus)
Quelle: `02-characters/Ronja-Kerschner.md`

Hooks (interaktionsrelevant)
- Consent Gate: explizites „Ja/Nein“ für Kopplung/Assist, jederzeit widerrufbar
- Safe Word/Stop: sofortige Entkopplung, Reflex fällt auf Observe/Idle
- Mode‑Anforderung: „Support bitte nur Dämpfung X“, „Guard bis Punkt Y“
- Debug‑Token: temporär mehr Telemetrie freischalten (Admin‑Canvas beachten)

Trigger aus Ronjas Sicht
- Belastung hoch/Feinmotorik schwierig → Assist anfordern (zeitlich begrenzen)
- Gefahrenlage → Guard anfordern (mit Exit‑Kriterium)
- Komfort/Erkundung → Observe/Idle ausreichend

Interaktionen
- Mit Reflex: klare, kurze Kommandos; Rückkanal‑Bestätigung einfordern
- Mit Jonas: Arbeitsanweisungen/Planung; Reflex als Tool benennen, nicht als Entscheider

## Jonas (Human, Werkstatt/Logistik)
Quelle: `02-characters/Jonas-Merek.md`

Hooks (interaktionsrelevant)
- Request‑API (menschlich): „Status von Leitung/Material?“, „Sensor‑Check im Tunnel?“ → Reflex liefert Meldungen, keine Eingriffe
- Trust Gate: Kein direkter Körperkontakt/Assist an Jonas; nur Information/Signalisierung
- Debug‑Hinweise: meldet Anomalien an Admin‑Canvas statt harte Maßnahmen zu fordern

Typische Trigger
- Materialengpass/Planabweichung → Infoanforderung an Reflex (kein Override)
- Sicherheitsbeobachtung in C6/D5 → Meldung, Log‑Link im Missionslog

Interaktionen
- Mit Reflex: sprachliche/visuelle Absprachen; klare Grenzen („keine Dämpfung an mir“)
- Mit Ronja: Plan/Organisation, Freigaben für Schritte, Zeitfenster

## Ereignis‑Routing (leicht)
- Schutz/Eskalation → Ronja entscheidet, Reflex führt aus innerhalb Leitplanken
- Betriebslogistik → Logistik‑Canvas + Missionslog (Prozess L.1)
- Debug/Day‑Switch → Admin‑Canvas „Day‑Switch & Debug“

## Links
- Reflex → ../02-characters/Reflex.md
- Ronja → ../02-characters/Ronja-Kerschner.md
- Jonas → ../02-characters/Jonas-Merek.md
- Admin: Day‑Switch & Debug → ./Canvas-Admin-Day-Switch-Debug.md
- Timeline (T+0) → ./Canvas-T+0-Timeline.md
- Logistik → ./Logistik.md, Missionslog → ./Missionslog.md
