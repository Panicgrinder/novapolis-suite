---
stand: 2026-04-02 06:27
update: Fluesterkollektiv fuehrt jetzt den belegten Minimalrahmen aus unbekanntem Novapolis-Kontakt und interner Kanal-/Sicherheitskette; Mengen bleiben offen.
checks: scripts/run_checks_and_report.py overall=PASS; markdownlint=PASS; frontmatter=PASS; path-portability=PASS; namingpolicy=PASS; todo-index-sync=PASS; doc-freshness=PASS; logs-policy=PASS; ruff=PASS; black=PASS; pytest=PASS; pyright=PASS; mypy=PASS; report=.tmp\results\reports\checks_report_20260402_062604.md
canvas: Inventar Fluesterkollektiv
last_updated: 2026-04-01T00:53:51+02:00
category: inventory
slug: fluesterkollektiv-inventar
owner: fluesterkollektiv
scope: faction
version: "0.1"
tags: []
---

Inventar - Fluesterkollektiv (Fraktion)
======================================

Bestände (Auszug)
-----------------
- Kugeln (neu): hochwertig (1 neu ≈ 10 gebraucht; Bestand nicht quantifiziert)
- Kugeln (gebraucht): Alltagswährung/Hauptmunition (Qualität streut; Bestand nicht quantifiziert)
- Informationsgüter: variabel (Gerüchte, Kontakte, Zugangscodes; Abrechnung nach Trust)
- Tarn-/Signaltechnik: variabel (keine Stückzahlen; abhängig von Lage)
- Verbrauchsmaterial: variabel (Batterien/Filter/Verbrauch; keine Stückzahlen)

Rahmenlage (T0)
---------------

- Fluesterkollektiv bleibt als Informations- und Spezialgüterraum gerahmt, nicht als harter Sachgutbestand.
- Dominante Herkunftslabel: `unknown`, `scavenged`.
- Konkrete Verbrauchsmengen, Technikposten und tauschbare Spezialgüter bleiben bis zu neuer Belegkette `tbd`.

Aussenlage (belegt)
-------------------

- Gegen Novapolis ist derzeit nur `unbekannt` belastbar; dort sind mehrere Funksignale registriert, aber Quelle und Absicht bleiben offen.
- Corin Mael fuehrt indirekte Tausch- und Informationskanaele ueber risikoarme Uebergaben.
- Sera Kaal sichert Freigaben, Zutrittszonen und Gegenaufklaerung ab; Iris Vey priorisiert Einflusslinien und Eskalationen.
- Benannte Gegenparteien, konkrete Spezialguterlisten, Routen und Mengen bleiben ohne eigenen Dealbeleg `tbd`.

Bewegungen (Log)
----------------
- 2026-01-14: Baseline angelegt; keine Buchungen dokumentiert.
- 2026-03-31 [RAHMENWERT] Informations- und Spezialgüterraum aus `Warenueberblick-T0.md` und Arbeitsledger fuer die finale Metro-Warenzuteilung bestaetigt; keine Mengensetzung vorgenommen.
- 2026-04-01 [FACT?] Das aktive Novapolis-Relationslog fuehrt das Fluesterkollektiv als `unbekannt`; belegt sind nur mehrere Funksignale bei unklarer Quelle und Absicht. Quelle: [Relationslog-Novapolis](../../novapolis/06-handel-diplomatie/Relationslog-Novapolis.md), [Relationslog-Fluesterkollektiv](../06-handel-diplomatie/Relationslog-Fluesterkollektiv.md).
- 2026-04-01 [FACT?] Kontakt-, Handels- und Sicherheitskette laufen ueber `Corin Mael -> Sera Kaal -> Iris Vey`: Corin fuehrt indirekte Kanaele, Sera schirmt sensible Uebergaben ab, Iris setzt Prioritaeten und Einflusslinien. Quelle: [Corin-Mael](../02-characters/Corin-Mael.md), [Sera-Kaal](../02-characters/Sera-Kaal.md), [Iris-Vey](../02-characters/Iris-Vey.md), [Handelslog-Fluesterkollektiv](../06-handel-diplomatie/Handelslog-Fluesterkollektiv.md).
- Template: YYYY-MM-DD | Bezug: scene-... | Delta: +/− | Gegenpartei: ... | Abrechnung: Kugeln/Tausch | Notiz: ...

Links
-----
- Logistik (Admin) → ../../../00-admin/Logistik.md
- Missionslog → ../05-projects/Missionslog-Fluesterkollektiv.md
- Handelslog → ../06-handel-diplomatie/Handelslog-Fluesterkollektiv.md
- Relationslog → ../06-handel-diplomatie/Relationslog-Fluesterkollektiv.md
- Währung "Kugeln" (Reference) → ../../../00-admin/Reference-Campaign-State.md
