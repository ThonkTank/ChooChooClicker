# Modulübersicht `src/`

```text
src/
├── README.md
├── main.py         # Einstiegspunkt & Komposition
├── assets/         # Sprite-Lade- und Cachelogik
├── game/           # Spiellogik & Momentum
├── ui/             # Tkinter-Anwendung
└── world/          # Karten- und Weltmodell
```

## Zweck des Ordners
`src/` bündelt alle Python-Module der Anwendung. Die Pakete sind so geschnitten, dass Spiellogik und UI strikt getrennt bleiben und über `src/main.py` zusammengesetzt werden.

## Komponenten
- **`main.py`** – erstellt `GameEngine`, initialisiert die Standardkarte und verdrahtet UI und Assets.
- **`assets/`** – siehe [assets/README.md](assets/README.md) für Sprite-Handling-Konventionen.
- **`game/`** – siehe [game/README.md](game/README.md) für Momentum- und Tick-Regeln.
- **`ui/`** – siehe [ui/README.md](ui/README.md) für Tkinter-spezifische Komponenten.
- **`world/`** – siehe [world/README.md](world/README.md) für das Weltmodell.

## Standards & Konventionen
- Querschnittsthemen (Logging, Tick-Kommunikation) werden in den Paket-Readmes dokumentiert und hier verlinkt.
- Neue Pakete benötigen eine eigene README mit Strukturdiagramm, Zweck und Verweisen auf Tests.
- Änderungen am Einstiegspunkt müssen gleichzeitig die Startskripte und die Haupt-README aktualisieren.

## Weiterführende Dokumentation
- [Projekt-README](../README.md)
- [Struktur-Review](../docs/structure-review.md)
- [Testübersicht](../tests/README.md)
