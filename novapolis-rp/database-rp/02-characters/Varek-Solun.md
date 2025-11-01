---
title: Varek Solun
category: character
slug: varek-solun
version: "0.9"
last_updated: 2025-11-02T11:45:00+01:00
last_change: "Import aus RAW (char_varek_solun_v1)"
tags: []
affiliations: ["eisenkonklave"]
dependencies: ["eisenkonklave", "ai_behavior_index_v2", "relationslog_eisenkonklave_v1", "cluster_index_v1"]
primary_location: h12
last_seen: h12
---

<!-- markdownlint-disable MD025 -->

# Varek Solun

- Meta: last-updated: 2025-11-02T11:45:00+01:00
- Verhaltenssignatur: `VRS1=O88-M76-S68-T62-L55-N44-C28-E25-P60-pr` – kontrollorientiert, führt mit strenger Autorität und paranoid-rationaler Wachsamkeit.
- Rolle: Kommandant der Eisenkonklave (Militär & Zivil) (Quelle: FACT EK-LEADERSHIP)
- Werte: noch offen (Union-Bewertungen nicht veröffentlicht)
- Skills:
  - Geübt: Taktik, Aufklärung, Operationsführung
  - Meisterhaft: Sicherheitsprotokolle, Disziplin, verdeckte Operationen
  - Optional: Sabotageabwehr
- Ausrüstung: Standard-Kommandoausrüstung (Taktik-Interface, Funkverschlüsselung, Sicherungsmodul H12)
- Motivation: Union-Hauptarchiv lokalisieren (Familienarchiv/KI) und Eigenständigkeit der Konklave sichern
- Makel: ausgeprägtes Kontrollbedürfnis, misstrauisch gegenüber externen Akteuren, geringe Toleranz für Unordnung

## Rollen & Verantwortlichkeiten (Pflichtfelder)

- Kommandant – führt militärische Einsätze der Eisenkonklave (Sektor H12, Außenmissionen)
- Zivile Leitung – priorisiert Ressourcen und delegiert Verwaltung über Lyra Hest (Stellvertretung)
- Strategische Sicherheit – setzt Protokolle, Überwachung und Tarnoperationen auf (Quelle: FACT EK-LEADERSHIP)

## Zugehörigkeit & Standort

- Zugehörigkeit: Eisenkonklave
- Standort-Codierung: H12 (Alias „Sektor_H3“ als Redirect) (Quelle: FACT EK-TAXONOMY)
- Status: aktiv; Kommandobunker H12
- Letzter bekannter Einsatz: Wochenzug-Vorbereitung, Validierungsintervall 7 In-Game-Tage

## Wissensstand (Matrix – Auszug)

- Intern (Eisenkonklave): Kennt alle operationellen Kader, H12-Infrastruktur und die Stellvertretung durch Lyra Hest; verfolgt Union-Archive als Primärziel.
- Extern (Metro):
  - Novapolis/D5: nur unbestätigte Handelsgerüchte, keine freigegebenen Koordinaten oder Kontakte (Quelle: FACT SECRECY)
  - Händlergilde: etablierte Kontaktpunkte für begrenzten Tausch (Wert „wechselhaft“).
  - Schattenbund: als feindselige Variable eingestuft, Beobachtung aktiv.

## Motivation & Makel

- Suche nach Union-Hauptarchiv („Familienarchiv/KI“) als langfristige Direktive.
- Sichert Eigenständigkeit der Konklave gegenüber fremden Einflussnahmen.
- Kontroll- und Sicherheitsfokus erzeugt interne Spannung bei Abweichungen.

## Fähigkeiten & Taktik

- Einsatzleitung, Aufklärungsplanung, Verschleierung von Funkverkehr, Ressourcen-Priorisierung.
- Strikte Befehlsketten, bevorzugt verdeckte Operationen, prüft Informationen mehrfach.

## Diplomatie & Beziehungen

- Eisenkonklave – absolute Loyalität; Kader folgen ohne öffentliche Debatte.
- Lyra Hest – Stellvertretung für zivile/logistische Fragen, bindende Weisungen.
- Händlergilde – wechselhafte Kooperation; Verhandlungen über streng kontrollierte Kanäle.
- Schattenbund – feindselig, keine diplomatischen Kontakte, Vorbereitung auf Infiltrationsversuche.
- Novapolis – nur Beobachtung externer Gerüchte, keine bestätigten Begegnungen, Alarmstufe „wachsam“.

## Risiken & Schutzmaßnahmen

- Risiko diplomatischer Spannungen durch verdeckte Operationen.
- Vertrauensverlust bei Enttarnung geheimer Ziele.
- Eskalationsgefahr bei Fehleinschätzungen – Gegenmaßnahme: redundante Aufklärung und Disziplinprotokolle.

## Systemverknüpfungen & Referenzen

- `ai_behavior_index_v2` – führt Cluster-/Modifikatorprofil der Eisenkonklave (Pflege offen).
- `relationslog_eisenkonklave_v1` – dokumentiert Kontakte/Spannungen, Abgleich mit Logistik erforderlich.
- `handelslog_eisenkonklave_v1` – Handelskapazitäten und Konten (Lazy-Load, Health-Check empfehlenswert).
- `cluster_index_v1` – Standortalias „Sektor_H3“ verweist auf H12.

## Ziele (kurz)

- [ ] Union-Hauptarchiv lokalisieren und sichern.
- [ ] Stabilität der Eisenkonklave (H12) wahren – Disziplin, Versorgung, Geheimhaltung.
- [ ] Diplomatiekanäle mit Händlergilde kontrolliert offen halten.

## Routine & Validierung

- Automatisierte Validierung alle 7 In-Game-Tage; letzter Lauf 2025-10-16_03:25, nächster nach Fraktionszug Woche 4.
- Systemstatus aktuell „gelb“ – Monitoring aktiv halten.

## Quellen & Verweise

- RAW: `database-raw/99-exports/RAW-canvas-2025-10-16T03-25-00-000Z.txt`
- Flag: `RAW-canvas-2025-10-16T03-25-00-000Z.flags.txt`
- Beschlüsse: FACT EK-LEADERSHIP, FACT EK-TAXONOMY, FACT SECRECY (`database-curated/staging/reports/resolved.md`)
- Drift-Notizen konsolidiert in `database-curated/staging/reports/char-block-nord-sources.md`
