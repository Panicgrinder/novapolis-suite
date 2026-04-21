---
stand: 2026-04-21 01:59
update: Der RP-Laufzeitbereich fuehrt jetzt zusaetzlich eine feste Routing-Matrix, damit der RP-Agent Mischfaelle nach Datentyp getrennt statt unscharf in einen Sammelpfad schreibt.
checks: snapshot-lock PASS (2026-04-21 01:59); markdownlint=PASS; frontmatter=PASS (touched md)
---

RP Runtime Staging
==================

Zweck
-----

Dieser Pfad ist die kontrollierte Laufzeit- und Arbeitsflaeche fuer RP im Chat.

- Hier landen neue oder veraenderte Fakten zuerst als Arbeitsstand.
- Nichts unter `rp-runtime/` ist automatisch RP-SSOT.
- Promotion in `novapolis-rp/database-rp/**` erfolgt erst nach Review oder expliziter User-Freigabe.

Geeignete Inhalte
-----------------

- laufende Szenen- und Sitzungsprotokolle
- neue Figuren in Arbeitsform
- Beziehungs- und Fraktionsaenderungen auf Probe
- Inventar- und Ressourcenverschiebungen waehrend eines RP-Laufs
- Welt- oder Standortstatus zwischen zwei Promotionsschritten

Empfohlene Struktur
-------------------

- `sessions/<session-id>/scene-log.md`
- `characters/<slug>.md`
- `relationships/<slug>.md`
- `inventories/<slug>.md`
- `state/<slug>.md`

Vorhandene Startstruktur
------------------------

- `sessions/README.md` und `sessions/session-template.md`
- `characters/README.md` und `characters/character-template.md`
- `relationships/README.md` und `relationships/relationship-template.md`
- `inventories/README.md` und `inventories/inventory-template.md`
- `state/README.md` und `state/state-template.md`

Automatische Routing-Matrix
---------------------------

- Szenenzuege, Turn-Protokolle und laufender Dialog: `sessions/<session-id>/scene-log.md`
- Figurenanlage oder Figurenupdate: `characters/<slug>.md`
- Beziehungs- oder Loyalitaetsverschiebung: `relationships/<slug>.md`
- Inventar-, Transfer- oder Ressourcenupdate: `inventories/<slug>.md`
- Welt-, Orts-, Fraktions- oder Projektstatus: `state/<slug>.md`

Regel fuer Mischfaelle
----------------------

- Ein RP-Zug mit mehreren Folgen landet nicht nur in einer Datei.
- Der Ablauf geht immer nach `sessions/<session-id>/scene-log.md`.
- Jede zusaetzliche belastbare Folge wird parallel in die passende Typdatei geschrieben.
- Sekundaerdateien bleiben knapp, referenzieren aber nach Moeglichkeit Session und Turn.

Vertragsregeln
--------------

- RP-SSOT bleibt `novapolis-rp/database-rp/**`.
- `rp-runtime/` ist absichtlich fluechtiger, aber nachvollziehbarer als freie Chat-Improvisation.
- Jeder Eintrag soll kenntlich machen, ob er `Probe`, `Arbeitsstand`, `review_required` oder `promotion_ready` ist.
- Wenn Faktenlage unsicher ist, bleibt der Eintrag hier und wandert nicht direkt in den Kanon.

Promotion-Pfad
--------------

1. Szene oder Verwaltungsakt im Chat erzeugt ein Arbeitsartefakt unter `rp-runtime/`
2. Review auf Kanontreue, Belastbarkeit und Stil
3. Erst danach gezielte Uebernahme nach `database-rp/**` oder in andere kuratierte Artefakte