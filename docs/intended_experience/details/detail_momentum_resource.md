---
id: detail_momentum_resource
title: Momentum-Ressource
date: 2025-09-28
status: draft
tags: [detail, momentum, mechanics]
---

# Detail: Momentum-Ressource

## Beschreibung
Das Momentum repräsentiert die Bewegungsenergie des Zuges und fungiert als primäre Ressource im Gameplay-Loop. Es wird durch die Kurbelinteraktion aufgebaut und schrittweise verbraucht, wenn der Zug über das Schienennetz fährt.

## Visualisierung
- **Ressourcenanzeige:** Eine horizontale Leiste oder ein kreisförmiger Zähler zeigt den aktuellen Wert (0–10).
- **Zug-Feedback:** Der Zug vibriert oder erzeugt Dampffahnen, wenn Momentum hoch ist; bei niedrigem Momentum verlangsamt sich die Animation.
- **Warnhinweise:** Bei Momentum ≤ 2 erscheint ein Hinweis im Panel, der zur Kurbelinteraktion auffordert.

## Interaktionsregeln
- Minimum 0, Maximum 10.
- Momentum generiert sich ausschließlich durch aktive Spielerinteraktion (kein Autorefill).
- Verbrauch pro Kachel: 1 Momentum.
- Momentum pausiert, wenn die Strecke unterbrochen oder ungültig ist; Fehlermeldungen erklären die Ursache.

## Offen Punkte
- Skalierung des Maximums durch Upgrades? (Backlog-Eintrag)
- Zusätzliche Quellen für Momentum (Events, Boni)?

## Verknüpfte Seiten
- [Feature: Momentum-basierte Zugbewegung](../features/feature_momentum_train.md)
