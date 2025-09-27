# Hilfspaket `tests_support/`

```text
tests_support/
├── README.md
└── asset_fakes.py
```

## Zweck
Bündelt gemeinsam genutzte Test-Hilfen, die nicht an einen einzelnen Testordner gebunden sind. Dadurch lassen sich Fakes und Fixtures wiederverwenden, ohne die Namensräume der Produktivmodule zu beeinflussen.

## Module & Hauptfunktionen
- **`asset_fakes.py`** – stellt `FakePhotoImage`, `FakeInterpreter` und `make_sheet` zur Verfügung, damit SpriteSheet-Tests ohne echte Tk-Instanz ausgeführt werden können.

## Standards & Konventionen
- Hilfsfunktionen aus diesem Paket dürfen ausschließlich Testcode importieren.
- Neue Helfer müssen in diesem README dokumentiert und mit Verwendungsstellen verlinkt werden.

## Weiterführende Dokumentation
- [Testsuite-Übersicht](../../tests/README.md)
- [Asset-Dokumentation](../assets/README.md)
