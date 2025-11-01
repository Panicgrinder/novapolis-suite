# TODO (Novapolis Dev Hub)

Stand: 2025-11-01 – Fokus Canvas-Rettung (Nord-Block, Logistik, Systeme)

- [ ] Charakter-Canvas Nordblock erstellen (`char_varek_solun_v1`, `char_liora_navesh_v1`, `char_marven_v2`, `char_arlen_dross_v2`, `char_pahl_v2`) inkl. JSON-Sidecars, Quellen und Flag-Bereinigung.
- [ ] Bestehende Charakter-Canvas aktualisieren (`Ronja-Kerschner`, `Reflex`, `Jonas-Merek`, `Kora-Malenkov`) gemäß Drift-Overrides (Nachname, Schwesterstatus, Reflex-Frequenzen, Rollenabgleich).
- [ ] Logistik-/Inventar-Daten aus `inventar_c6_v2`, `logistik_c6_v2`, `logistik_novapolis_v2` in `00-admin/Logistik.md` und `04-inventory/` übernehmen; Mixed-Version-Verknüpfungen harmonisieren.
- [ ] Standort-Canvas D5 aktualisieren (Grundfläche, Lastenaufzug, Lager) auf Basis `station_d5_v2.1` + Legacy-Notiz.
- [ ] Admin-/System-Canvas anlegen (`Ereignislog-Weltgeschehen`, `Relationslog Novapolis`, `AI-Behavior-Index v2`, `Cluster-Index`) mit Querverweisen zu Policies.
- [ ] Missionslog prüfen und ggf. verlinkte Rohdaten (`missionslog_novapolis_v1`) einpflegen.
- [ ] Nach Abschluss der Überträge `index.json` und DONELOG aktualisieren, Tests/Validierungen anstoßen (Pytest/Pyright/Mypy bei Agent-Änderungen).
