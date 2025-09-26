# Choo Choo Clicker – Projektleitfaden

Choo Choo Clicker ist ein minimalistisches Pixelart-Clicker-Spiel rund um einen kleinen Zug. Die Anwendung läuft lokal als eigenständiges Tkinter-Programm und dient als spielerischer Prototyp für eine ressourcenbasierte Idle-Mechanik.

## Inhaltsverzeichnis
- [Projektüberblick](#projektüberblick)
- [Verzeichnisstruktur](#verzeichnisstruktur)
- [Soll-Workflows](#soll-workflows)
- [Weiterführende Dokumentation](#weiterführende-dokumentation)

## Projektüberblick
- **Spielfeld**: Ein 12×12-Raster wird über 32×32-Pixel-Sprites aus `Ground-Rails.png` gerendert. Für jede Zelle wählt das Spiel automatisch den passenden Schienen- oder Bodentile.
- **Zuglogik**: Ein einzelner Zug bewegt sich entlang des platzierten Streckennetzes. Momentum entscheidet, ob der Zug sich im nächsten Tick um ein Feld weiter bewegt.
- **Architektur**: Spiellogik (`src/game/`) und Weltmodell (`src/world/`) sind von der Tkinter-Oberfläche (`src/ui/`) getrennt und werden in [`src/main.py`](src/main.py) zusammengeführt.

## Verzeichnisstruktur
| Pfad | Inhalt & Zweck |
| --- | --- |
| `Ground-Rails.png` | Sprite-Sheet mit Boden- und Schienentiles für das gesamte Spielfeld. |
| `README.md` | Diese Übersicht mit Projektzielen, Workflows und Verweisen auf Detaildokumente. |
| `src/` | Python-Quellcode der Anwendung. Enthält Einstiegspunkt, Assets-, Gameplay-, UI- und Welt-Pakete (siehe [src/README.md](src/README.md)). |
| `tests/` | Pytest-Suite für Spiel- und Weltlogik (siehe [tests/README.md](tests/README.md)). |
| `docs/` | Hintergrunddokumentation und Architektur-Reviews. |
| `start_game.sh` / `start_game.bat` | Startskripte für Linux/macOS bzw. Windows. |
| `todo/` | Verzeichnis für offene Aufgaben (siehe [todo/README.md](todo/README.md)). |

## Soll-Workflows
1. **Spiel starten (Linux/macOS)**
   ```bash
   ./start_game.sh
   ```
   Das Skript nutzt `python3`, fällt aber bei Bedarf auf `python` zurück und startet `src/main.py`.
2. **Spiel starten (Windows)**
   ```powershell
   .\start_game.bat
   ```
   Das Batch-Skript versucht zuerst `py`, anschließend `python`, jeweils mit `src\main.py`.
3. **Direkter Programmstart**
   ```bash
   python src/main.py
   ```
   Öffnet das Tkinter-Fenster, zeigt das Raster und blendet rechts den Momentum-Button ein. Der Zug fährt automatisch, sobald Momentum verfügbar ist.

Während des Spielens füllt der Button **Schieben** den Momentum-Speicher, bis zehn Einheiten erreicht sind. Jede Tick-Iteration (600 ms) verbraucht eine Einheit. Ist die aktuelle Richtung blockiert, sucht die Spiel-Logik passende Alternativen anhand der bestehenden Schienenverbindungen.

## Weiterführende Dokumentation
- [src/README.md](src/README.md) – Details zur Code-Struktur, Komponenten und Render-Pipeline.
- [docs/index.md](docs/index.md) – Projektweite Analysen und Entscheidungsgrundlagen (z. B. aktuelle Struktur-Review).
- [tests/README.md](tests/README.md) – Überblick über die automatisierten Tests.

Offene Architektur- oder Feature-Fragen werden nicht hier, sondern im `todo/`-Verzeichnis mit direktem Kontext dokumentiert.
