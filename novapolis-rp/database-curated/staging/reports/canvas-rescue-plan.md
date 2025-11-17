---
stand: 2025-11-16 06:52
update: Guard-Check ersetzt den alten Start-Schritt im Workflow
checks: keine
---

Canvas-Rettung - Plan (Stand 2025-11-01)
========================================

Ausgangslage
------------

- `resolved.md` spiegelt alle ehemaligen `[FACT?]`-Punkte aus `uncertainties.md`; Staging ist bereinigt, Kernfakten liegen vor.
- In `database-rp/` existieren bereits Grund-Canvas (Charaktere, Orte, Admin), viele Felder sind jedoch Platzhalter (`tbd`).
- In `database-raw/99-exports/` liegen kuratierbare Canvas mit Flags (`vorsichtig_behandeln`, teils `korrupt`), die vor Promotion auf Drift geprüft werden müssen.
- Ziel: Roh-Canvas iterativ nach `database-rp/` überführen, dabei FACT-/Policy-Beschlüsse aus `resolved.md` anwenden und Flag-Hinweise abarbeiten.

Priorität A - Charaktere & Führung
----------------------------------

- `RAW-canvas-2025-10-16T03-25-00-000Z.txt` (`char_varek_solun_v1`) → neu `database-rp/02-characters/Varek-Solun.md/json`; Flags: Standortcode H12 vs. Alias `Sektor_H3` harmonisieren, Außenwissen über Novapolis ausblenden (vgl. `[FR-KNOWLEDGE]`).
- `RAW-canvas-2025-10-16T03-25-10-000Z.txt` (`char_liora_navesh_v1`) → neu `database-rp/02-characters/Liora-Navesh.*`; Flag: keine Kenntnis von Novapolis/D5 eintragen, „SÜDFRAGMENT“ ohne H-47-Mapping belassen.
- `RAW-canvas-2025-10-16T14-56-00-000Z.txt` (`char_kora_malenkov_v2`) → bestehendes Canvas aktualisieren (Rollenabgrenzung laut `[CARAVAN-LEADERSHIP]`, Schlaf-/Stressnotizen ergänzen).
- `RAW-canvas-2025-10-16T14-56-10-000Z.txt` (`char_marven_v2`) → neu `Marven-Kael.*`; Flag: Titel klar auf „Konvoi-/Handelsleitung extern“, interne Logistik bei Kora.
- `RAW-canvas-2025-10-16T14-56-20-000Z.txt` (`char_arlen_dross_v2`) → neu `Arlen-Dross.*`; Flag: Rolle auf Händler/Vermittler begrenzen, nicht erneut „Karawanenführer“.
- `RAW-canvas-2025-10-16T14-41-00-000Z.txt` (`char_pahl_v2`) → neu `Pahl.*`; Flag: Gesundheitsstatus (Atembeschwerden) verifizieren, Beziehungen gegen Kanon abgleichen.
- `RAW-canvas-2025-10-16T11-45-00-000Z.txt` (`char_ronja_v2`, `korrupt`) → bestehendes `Ronja-Kerschner`-Canvas revidieren: Nachname korrigieren, Wissensstand gegen `[FR-KNOWLEDGE]`, Stress-/Motivationsblöcke übernehmen, alles mit Review-Hinweis versehen.
- `RAW-canvas-2025-10-16T13-45-00-000Z.txt` (`char_reflex_v2`) & `RAW-canvas-2025-10-16T03-25-20-000Z.txt` (`ent_d5_reflex_v1`) → `Reflex`-Canvas erweitern (Frequenzband 7.3-8.0 Hz, Symbiose-Stufe I, Abgleich mit `[REFLEX-*]` Mechaniken, Notfall-Detachment als Labor-Sonderfall dokumentieren).
- `RAW-canvas-2025-10-16T14-12-00-000Z.txt` (`char_jonas_v2`, `korrupt`) → Jonas-Canvas auffüllen, Schwesterstatus auf „vermisst/unklar“ normalisieren, Makel in Kommentar festhalten.

Priorität B - Logistik, Inventar, Ressourcen
--------------------------------------------

- `RAW-canvas-2025-10-16T12-30-00-000Z.txt` (`inventar_c6_v2`) & `RAW-canvas-2025-10-16T12-55-00-000Z.txt` (`logistik_c6_v2`) → `database-rp/04-inventory/C6-inventar.*` neu anlegen + `00-admin/Logistik.md` erweitern; Flag: Systemverknüpfungen auf v2 anheben oder Abweichung begründen.
- `RAW-canvas-2025-10-16T13-05-00-000Z.txt` (`logistik_novapolis_v2`) → bestehende `Logistik`-Canvas mit aktuellem Lagerstatus/Lieferzyklen füllen; Flag: Mixed-Version-Links prüfen (`inventar_d5_v2` vs. bestehende Strukturen).
- `RAW-canvas-2025-10-16T12-00-00-000Z.txt` (Legacy D5 Versorgung) + `RAW-canvas-2025-10-20T12-05-00-000Z.txt` (`station_d5_v2.1`) → `03-locations/D5` aktualisieren, Grundfläche/Lastenaufzug/Lager auflösen, Legacy als Historie kennzeichnen.
- Inventar-Deltas in `Novapolis-inventar.md`, `D5-inventar.md` ergänzen (Frontmatter bleibt, „tbd“ ersetzen, Links zu Missionslog pflegen).

Priorität C - Systeme, Indizes, Ereignisse
------------------------------------------

- `RAW-canvas-2025-10-16T05-34-00-000Z.txt` (`ereignislog_weltgeschehen_v1`) → neues Admin-Canvas `00-admin/Ereignislog-Weltgeschehen.*`; Flag: Begriff „Allianz“ vs. `[SECRECY]` prüfen, H-47 als ehemalige Karawane kennzeichnen.
- `RAW-canvas-2025-10-16T08-07-00-000Z.txt` (`relationslog_novapolis_v1`) → neues Canvas unter `05-projects/relations/` oder `00-admin/`; IDs auf Schema `logistik_novapolis_v2`, Händlerkontakt „Senn Daru“ als eigener Charakter (bereits angelegt) verlinken.
- `RAW-canvas-2025-10-16T11-05-00-000Z.txt` (`ai_behavior_index_v2`) → `AI-Behavior-Mapping.md` ergänzen (Cluster, Modifikatoren, Beispielcode), JSON-Fassung anlegen.
- `RAW-canvas-2025-10-16T16-55-00-000Z.txt` (`meta_cluster_index_v1`) → neues Admin-Canvas (`Cluster-Index.md`), Flag: Spannungen/PsyLinks gegen Kanon validieren.
- Prüfen, ob `missionslog_novapolis_v1` relevante Daten trägt → bei Bedarf Querverweis in `Missionslog.md` ergänzen (keine direkte RAW-Datei, aber referenzierte Inhalte).

Übertragungs-Workflow (pro Canvas)
----------------------------------

- Guard-Check: Flag-Notizen lesen, relevante FACT-Beschlüsse (`resolved.md`) notieren, Drift-Markierungen (Alias, Geheimhaltung) abgleichen.
- Normalisieren: Namen (z. B. „Ronja Vallin“ → „Ronja Kerschner“), System-IDs (CamelCase vs. snake_case) angleichen; externe Kenntnisse entfernen oder als „unbekannt“ markieren.
- Strukturieren: Frontmatter nach bestehendem Schema (`title`, `category`, `version`, `last_updated`, Tags/Affiliations) pflegen; Pflichtfelder laut Policy ausfüllen (z. B. Rollenmatrix, Wissensstand, ATSD).
- Quellenblock: In jedem Canvas RAW-Datei + relevante Beschlüsse verlinken (`Quelle: database-raw/... + resolved.md #[FACT]`).
- Prüfpfad: Nach Migration `resolved.md`/`uncertainties.md` querlesen → keine neuen offenen Punkte erzeugen. Änderungen anschließend im passenden DONELOG (`novapolis-dev/docs/donelog.md`) eintragen.
- Tests: Bei größeren Admin-/Policy-Änderungen `novapolis_agent/tests/test_content_policy_profiles.py` (Agent-Repo) berücksichtigen, falls Verhaltenstexte betroffen (nur Hinweis für späteren Apply-Schritt).

Kurzfristige Nächste Schritte (Sprint 1)
----------------------------------------

1. Charakter-Block Nord (Varek Solun, Liora Navesh, Marven Kael, Arlen Dross, Pahl) aus RAW übernehmen und in `02-characters/` konsolidieren; dabei Rollen gemäß `[CARAVAN-LEADERSHIP]`, `[EK-LEADERSHIP]`, `[ARKO-RESEARCH]` anwenden.
2. Logistik-/Inventar-Daten (`inventar_c6_v2`, `logistik_c6_v2`, `logistik_novapolis_v2`) in `00-admin/Logistik.md` und `04-inventory/` einpflegen, Mixed-Version-Verknüpfungen bereinigen, Tages-/Wochenzyklen dokumentieren.
3. Ereignis- und System-Canvas (`ereignislog_weltgeschehen_v1`, `ai_behavior_index_v2`, `meta_cluster_index_v1`) aufbereiten, neue Admin-Dateien erstellen und mit bestehenden Policies (`AI-Behavior-Mapping`, `Canvas-T+0-Timeline`) verknüpfen.

Abhängigkeiten & Prüfhinweise
-----------------------------

- Ronja/Jonas/Reflex-Rohdaten besitzen `korrupt`-Flags → nur Ausschnitte übernehmen, drifthafte Aussagen kommentieren (z. B. Schuldflag als „non-canon, siehe resolved #[JONAS-SIS]“).
- Systemverknüpfungen (logistik_novapolis_v1/v2) konsistent halten; wenn Migrationspfad noch nicht existiert, `Placeholder` mit TODO notieren.
- Bei neuen Canvas JSON-Sidecar nicht vergessen (Schema wie bei bestehenden Dateien); Einträge in `database-rp/index.json` erweitern.
- Vor finaler Promotion prüfen, ob zusätzliche Redirects/Alias (z. B. `Sektor_H3`) in Admin-Docs dokumentiert werden müssen.

