---
id: feature_track_management
title: Schienenbau und Weichenmanagement
date: 2025-09-28
status: draft
tags: [building, tracks, switches]
---

# Feature: Schienenbau und Weichenmanagement

## Nutzenversprechen
Spieler:innen können ihr Streckennetz kreativ gestalten, optimieren und dynamisch anpassen. Das Hinzufügen und Entfernen von Schienen sowie das Steuern von Weichen ermöglicht flexible Zugrouten.

## Nutzerfluss
1. Mit Rechtsklick wird der Baumenü-Modus aktiviert, in dem die gewünschte Schienenart (gerade, Kurve, Kreuzung) ausgewählt werden kann.
2. Ein weiterer Rechtsklick platziert oder entfernt das Schienenelement auf der gewählten Kachel, sofern keine Konflikte bestehen.
3. Kreuzungen verfügen über interaktive Weichen. Spieler:innen wählen den gewünschten Abzweig und stellen die Weiche per Linksklick.
4. Der Zug folgt automatisch dem aktuellen Weichenstatus. Visualisierungen auf der Karte zeigen den aktiven Pfad.
5. Änderungen am Streckennetz geben unmittelbares Feedback, damit Spieler:innen schnell auf Staus oder neue Ziele reagieren können.

## Akzeptanzkriterien
- Rechtsklick kontextualisiert das Platzieren oder Entfernen von Schienen.
- Schienenarten sind klar unterscheidbar und lassen sich auf gültigen Kacheln platzieren.
- Weichen an Kreuzungen lassen sich pro Ausgang schalten und zeigen ihren Status deutlich an.
- Das System verhindert fehlerhafte Verbindungen (z. B. Sackgassen ohne Anschluss) oder kommuniziert diese klar.
- Der Zug passt seine Route sofort an geänderte Weichenstellungen an.

## Verknüpfte Details
- [Detail: UI-Layout und Informationshierarchie](../details/detail_ui_layout.md)
