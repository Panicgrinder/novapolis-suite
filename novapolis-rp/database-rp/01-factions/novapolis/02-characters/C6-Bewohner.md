---
stand: 2026-01-14 14:08
update: "E3-Evakuierte: Einzel-SSOTs verlinkt (inkl. neuer Dateien); Checks werden neu receipted."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-14 14:08); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-14 14:08); & .\\.venv\\Scripts\\python.exe scripts\\checks_rp_consistency.py --strict PASS (2026-01-14 14:08); npm validate:rp PASS (2026-01-14 14:08); npm validate:crossrefs PASS (2026-01-14 14:08)

title: C6 Bewohner (Gruppe)
category: character
slug: c6-bewohner
version: "0.1"
last_updated: 2026-01-14T14:06:00+01:00
tags: ["gruppe", "c6", "e3", "evakuierte"]
affiliations: ["novapolis", "e3", "c6"]
dependencies: ["marei", "verbindungstunnel-c6-e3", "c6", "e3", "logistik"]
primary_location: c6
last_seen: c6
---

<!-- markdownlint-disable MD025 -->

C6 Bewohner (Gruppe)
===================

- Meta: last-updated: 2026-01-14T14:06:00+01:00
- Zweck: Maschinenlesbarer Roster für die C6-integrierten Evakuierten aus E3.
- Hinweis: Nur Name + Persönlichkeit + nutzbare Rollenanker; keine tiefen Backstories vorab.

E3-Evakuierte (20, inkl. Marei)
------------------------------

| ID | Name | Rolle/Fokus | Persönlichkeit (kurz) | Notiz/Hook |
| --- | --- | --- | --- | --- |
| E3-01 | Marei | Stellvertretung C6 (Koordination) | strukturiert, ruhig, schützend | Separates Canvas: [Marei](Marei-Falk.md) |
| E3-02 | [Iva Kern](Iva-Kern.md) | Sanität (Basis) | direkt, pragmatisch, warmherzig | erkennt Stress früh; will klare Zuständigkeiten |
| E3-03 | [Bastian Rühl](Bastian-Ruehl.md) | Instandhaltung (Leitungen) | vorsichtig, detailfixiert, loyal | hat Angst vor erneutem Blackout; checkt alles doppelt |
| E3-04 | [Selma Varga](Selma-Varga.md) | Verpflegung/Planung | humorarm, effizient, konsequent | will Vorräte zählen dürfen, nicht „gefühlt“ verteilen |
| E3-05 | [Nino Jaspers](Nino-Jaspers.md) | Botengänge/Runner | neugierig, schnell, leichtsinnig | kennt Abkürzungen; muss gebremst werden |
| E3-06 | [Anouk Seidel](Anouk-Seidel.md) | Wasser/Filter | geduldig, methodisch, skeptisch | fragt nach Messwerten, bevor sie zusagt |
| E3-07 | [Farid Qamar](Farid-Qamar.md) | Strom/Ladefenster | gelassen, lösungsorientiert, stur | verteidigt „seine“ Ladezeiten gegen Eingriffe |
| E3-08 | [Rika Malm](Rika-Malm.md) | Küche/Improvisation | kreativ, empfindsam, energiegeladen | macht aus Resten „Gerichte“; Trigger bei Gerüchen |
| E3-09 | [Hagen Dittmar](Hagen-Dittmar.md) | Lager/Transport | wortkarg, kräftig, zuverlässig | arbeitet am liebsten nachts; meidet Menschenmengen |
| E3-10 | [Leena Roos](Leena-Roos.md) | Kinder-/Ruhezone | sanft, beharrlich, aufmerksam | kann Konflikte deeskalieren; fordert Rückzugsorte |
| E3-11 | [Milan Tarek](Milan-Tarek.md) | Funk/Notizen | nervös, klug, misstrauisch | dokumentiert alles; braucht Freigabe-Rituale |
| E3-12 | [Jule Benning](Jule-Benning.md) | Reparatur (klein) | pfiffig, stolz, ungeduldig | will ernst genommen werden; hasst „Schonung“ |
| E3-13 | [Orhan Velik](Orhan-Velik.md) | Sicherheit (Wache) | wachsam, höflich, kompromisslos | reagiert schlecht auf unklare Regeln |
| E3-14 | [Pia Lentz](Pia-Lentz.md) | Hygiene/Quarantäne | streng, fürsorglich, prinzipientreu | setzt Standards durch; wird bei Schlamperei kalt |
| E3-15 | [Sora Min](Sora-Min.md) | Daten/Inventar | still, analytisch, loyal | baut Listen; möchte Zugriff auf Logistik-Policy |
| E3-16 | [Viktor Lahn](Viktor-Lahn.md) | Schichtkoordination (unter Marei) | dominant, zuverlässig, reizbar | Konfliktpotenzial: will „klare Ansagen“ |
| E3-17 | [Elif Nader](Elif-Nader.md) | Reparatur (Feinmechanik) | ruhig, konzentriert, stolz | arbeitet an Ventilen/Fittings; mag keine Hektik |
| E3-18 | [Timo Bracht](Timo-Bracht.md) | Entsorgung/Filterwechsel | zäh, freundlich, abergläubisch | glaubt an „Tunnelzeichen“; kann Unruhe auslösen |
| E3-19 | [Amira Halden](Amira-Halden.md) | Betreuung/Versorgung | empathisch, erschöpft, mutig | setzt sich für Schwache ein; braucht Pausen |
| E3-20 | [Kian Rohde](Kian-Rohde.md) | Materialkunde | offen, lernbegierig, respektvoll | will von Kora/Ronja „wie es läuft“ lernen |

Rollen & Verantwortlichkeiten (Pflichtfelder)
--------------------------------------------

- C6: Evakuierte sind in Schichten (Versorgung, Instandhaltung, Hygiene) eingebunden.
- E3-Nachlauf: Wissen über E3 bleibt bei Bedarf abrufbar (Marei koordiniert).

Zugehörigkeit & Standort
------------------------

- Zugehörigkeit: Novapolis (provisorisch aufgenommen; E3-Herkunft)
- Status: aktiv, C6-integriert (Quarantäne aufgehoben)
- Letzter bekannter Einsatzort: C6

Kanonische Zählung (Abgleich)
-----------------------------

- Quelle „20 Evakuierte aus E3“ ist in [C6](../03-locations/C6.md) und [E3](../03-locations/E3.md) dokumentiert.
- Dieser Roster dient als eindeutiger Abgleich, ohne Einzel-Canvases für alle 20 anlegen zu müssen.

Links
-----

- C6 → ../03-locations/C6.md
- E3 → ../03-locations/E3.md
- Verbindungstunnel C6-E3 → ../03-locations/Verbindungstunnel-C6-E3.md
- Logistik → ../../00-admin/Logistik.md
