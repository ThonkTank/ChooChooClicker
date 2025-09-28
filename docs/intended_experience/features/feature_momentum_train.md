---
id: feature_momentum_train
title: Momentum-basierte Zugbewegung
date: 2025-09-28
status: draft
tags: [gameplay, momentum, train]
---

# Feature: Momentum-basierte Zugbewegung

## Nutzenversprechen
Spieler:innen erleben eine unmittelbare, physikalisch nachvollziehbare Steuerung des Zuges. Das Aufladen und Verbrauch von Momentum vermittelt Fortschritt und Kontrolle innerhalb des Clicker-Loops.

## Nutzerfluss
1. Spieler:in betätigt die Kurbel (z. B. per wiederholtem Klick oder gedrücktem Button), um Momentum aufzubauen.
2. Der Momentum-Speicher füllt sich bis zu einem Maximum von 10 Einheiten; UI-Feedback zeigt den aktuellen Stand.
3. Der Zug fährt automatisch die nächste Kachel entlang der verlegten Strecke und verbraucht pro Schritt eine Momentum-Einheit.
4. Sinkt das Momentum auf 0, stoppt der Zug. Die UI fordert zur erneuten Kurbelinteraktion auf.
5. Während der Fahrt können Spieler:innen Schienenumbauten planen oder ausführen, ohne den Bewegungsfluss zu verlieren.

## Akzeptanzkriterien
- Momentum-Aufbau ist nur über die Kurbelaktion möglich und respektiert das Maximal-Limit von 10.
- Jede Bewegung zur nächsten Kachel reduziert das Momentum um genau 1.
- Der aktuelle Momentum-Wert wird sowohl im Ressourcenpanel als auch durch visuelle Effekte am Zug dargestellt.
- Der Zug pausiert automatisch bei Momentum = 0 und startet wieder, sobald Momentum > 0 wird.
- Fehlbedienungen (z. B. Kurbeln ohne Strecke) liefern klares Feedback.

## Verknüpfte Details
- [Detail: Momentum-Ressource](../details/detail_momentum_resource.md)
