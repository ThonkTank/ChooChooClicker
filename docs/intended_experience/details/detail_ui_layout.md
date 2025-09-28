---
id: detail_ui_layout
title: UI-Layout und Informationshierarchie
date: 2025-09-28
status: draft
tags: [detail, ui, layout]
---

# Detail: UI-Layout und Informationshierarchie

## Beschreibung
Die Benutzeroberfläche gliedert sich in drei Hauptbereiche: Kartenfenster links, Menüleiste oben und Aktionspanel rechts. Jeder Bereich übernimmt eine klar definierte Rolle, um Informationsüberlastung zu vermeiden.

## Layout-Struktur
- **Kartenfenster (links):** Zeigt das Schienennetz in einer isometrischen oder top-down Ansicht. Fokus auf Zugbewegung, Schienenarten und Weichenstatus.
- **Menüleiste (oben):** Enthält globale Ressourcenanzeigen (z. B. Gesamtgeld, Fortschritt, Events) sowie Schnellzugriffe auf Einstellungen.
- **Aktionspanel (rechts):** Bündelt Clicker-Aktionen, Upgrades und Kontextinformationen.

## Interaktionsprinzipien
- Mauszeigeränderungen signalisieren Moduswechsel (Bau vs. Navigation).
- Tooltips folgen einem konsistenten Stil und bieten bei Hover kurze Erklärungen.
- Wichtige Warnungen (z. B. Momentum leer, Strecke blockiert) erscheinen als Overlays im Panel und auf der Karte.

## Responsivität
- Mindestauflösung definiert; Layout skaliert bis zu einer großzügigen Desktop-Breite.
- Panel-Bereiche lassen sich ggf. ein-/ausklappen, ohne wichtige Informationen zu verstecken.

## Verknüpfte Seiten
- [Feature: Schienenbau und Weichenmanagement](../features/feature_track_management.md)
- [Feature: Ressourcen- und Aktionspanel](../features/feature_ui_panel.md)
