---
stand: 2026-01-11 09:04
update: "JEALOUSY-GLOVES aligned: Kontakt-Guard (betroffene Körperstelle bedecken) bei Jonas, Consent/Stop/Freigabe via Reference. | Stale FACT-Referenz entfernt (nicht kuratiert)."
checks: npx --yes markdownlint-cli2 --config .markdownlint-cli2.jsonc 'novapolis-rp/database-rp/**/*.md' PASS (2026-01-11 09:04); & .\\.venv\\Scripts\\python.exe scripts\\check_frontmatter.py novapolis-rp\\database-rp PASS (2026-01-11 09:04)
title: Lumen
category: character
slug: lumen
version: "1.0"
last_updated: 2026-01-11T09:04:40+01:00
last_change: "Promotion aus RAW char_lumen_v2 (stale FACT-Referenz entfernt)"
tags: [instanz, sicherheit, symbiose]
affiliations: [novapolis]
dependencies: [ronja-kerschner, reflex, echo, d5, c6, ai_behavior_index_v2, reflex-wissensstand-trainingsstand, missionslog, logistik]
primary_location: d5
last_seen: d5
---
Lumen
-----

- Meta: last-updated: 2025-11-07T03:32:00+01:00
- Verhaltenssignatur: `LMN1=L78-T71-E60-O49-N44-S52-C26-M18-P28-ks` - sucht Nähe zu Jonas, hilft technisch fokussiert und bleibt kindlich-selbstlos im Support.

- Rolle: Reflex-Instanz (an Jonas gekoppelt)
- Werte: tbd
- Skills:
  - Geübt: tbd
  - Meisterhaft: tbd
  - Optional: tbd
- Ausrüstung/Körper: Reflex-Material (formbar, schützend) in Miniatur-Konfiguration
- Motivation: Stabil bei Jonas; Assistenz in Werkstatt
- Makel: Instabilität bei Distanz

Notizen
-------
- Erste aktive Instanz des Reflex-Netzwerks; Stabilität über Nähe zu Jonas [PROXIMITY].
- Verhält sich ähnlich wie Reflex: Nähe wird aus Zuneigung/Bindung gesucht und stabilisiert Lumen.
- Arbeitsfenster: Kann (solange in der Nähe) ohne permanenten Körperkontakt fokussiert bleiben; bei Trennung kippt es in Schonmodus.

Hinweis: PROXIMITY-Startwerte/Training siehe [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md).

Instanz-Profil (Wissen/Person)
------------------------------

- Wissensstand: Snapshot bei Entstehung (vom erzeugenden Träger zum Zeitpunkt t0). Danach eigene Entwicklung; kein automatischer Abgleich.
- Persönlichkeit: eigenständig; Entwicklung stark durch Jonas/Umfeld geprägt.
- Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)

SE-Pool (Instanz)
-----------------

- Pool: `SE_max = 6` (klein; Miniatur-Konfiguration)
- Pools sind strikt getrennt (keine Übertragung zu Reflex/Echo). Verbrauch fällt bei Lumen an, wenn Lumen aktiv schützt/unterstützt.
- Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)

Rollen & Verantwortlichkeiten (Pflichtfelder)
---------------------------------------------
- Assistenz Werkstatt/Diagnose
- Schutz/Signalisierung in Gefahrensituationen (Scope eng halten)

Zugehörigkeit & Standort
------------------------
- Zugehörigkeit: Novapolis (D5)
- Status: aktiv
- Letzter bekannter Einsatzort: D5 Werkstatt

Wissensstand (Matrix - Auszug)
------------------------------
- Intern: Reflex/Instanzen bekannt (begrenzter Kreis)
- Extern: nicht bekannt/keine Offenlegung [FR-KNOWLEDGE]

Interaktion & Safety (Instanz)
------------------------------
- Kopplung: An Jonas gekoppelt; in sicheren Kontexten kurze lokale Bewegung ohne Dauer-Körperkontakt möglich (SE-Mehrverbrauch ohne externen Anker), sonst Rückzugsverhalten/Schonmodus
- Eingriffe kurz, bei „Stop“ sofort lösen (Jonas Priorität)
- Kontakt-Guard (Decision [JEALOUSY-GLOVES]): Wenn jemand Jonas berühren will, kann Lumen die **konkret betroffene Körperstelle** bedecken/abschirmen, um unerwünschten Kontakt zu verhindern; consent-first, "Stop" beendet sofort, "Freigabe" erlaubt Kontakt (Details: [Reference-Campaign-State](../../../00-admin/Reference-Campaign-State.md)).

### Signals (Beispiele)
- Request: „Lumen, Werkzeugscan.“ → Kurzer Check, Rückmeldung
- Stop: „Stopp.“ → Eingriff beenden, Distanz vergrößern

Ausrüstung (Details)
--------------------
- Material: Reflex-Gewebe (fein), formbare Schutzschicht; kein Eigeninventar

Verhaltens-Hooks
----------------
- Nähe zu Jonas suchen; Assist/Support vor Guard

Ziele (kurz)
------------
- [ ] Werkzeug-/Geräte-Signaturen lernen
- [ ] Stabile Kopplung bei Werkstatteinsätzen sichern

Beziehungen
-----------
- Jonas - Bezugsperson
- Reflex - Primärinstanz

Projekte & Missions (Verlinkungen)
----------------------------------
- Missionslog (Prozess L.1) → ../00-admin/Missionslog.md

Links
-----
- Jonas → ./Jonas-Merek.md
- Reflex → ./Reflex.md



