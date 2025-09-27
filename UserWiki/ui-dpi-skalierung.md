# DPI-Konfiguration für die Benutzeroberfläche

Diese Anleitung beschreibt den Soll-Workflow, um Schriftgrößen und Spielfeldraster an hochauflösende Displays anzupassen.

## Ausgangslage
- `ChooChooApp` ermittelt beim Start automatisch den DPI-Faktor über [`compute_scaling`](../src/ui/scaling.py) und setzt ihn auf das Tkinter-Toolkit.
- Standardmäßig resultiert ein Faktor von `1.0` (72 dpi). Auf 150 %-Displays liegt der Faktor typischerweise bei `1.5`.
- Alle relevanten Abstände, Schriftgrößen und die Zellgröße (`BASE_CELL_SIZE = 32`) werden intern mit diesem Faktor multipliziert.

## Automatischer Ablauf
1. Spiel über `./start_game.sh` oder `python src/main.py` starten.
2. Beim Fensteraufbau liest die Anwendung `root.winfo_fpixels("1i")` aus. Der resultierende Skalierungsfaktor (begrenzt auf 0.75–3.0) wird auf Fonts, Canvas und Kamera übertragen.
3. Nach erfolgreicher Initialisierung wirkt der Faktor auf alle Widgets; kein weiterer Eingriff ist nötig.

## Manuelle Anpassung
Falls Tk die DPI-Information nicht bereitstellt oder ein individueller Wert bevorzugt wird:

1. Umgebungsvariable `CHOOCHOO_TK_SCALING` auf den gewünschten Faktor setzen.
   - **Linux/macOS (bash):**
     ```bash
     export CHOOCHOO_TK_SCALING=1.75
     python src/main.py
     ```
   - **Windows (PowerShell):**
     ```powershell
     $Env:CHOOCHOO_TK_SCALING = "1.75"
     python src/main.py
     ```
2. Werte außerhalb des gültigen Bereichs (0.75–3.0) werden automatisch auf diese Grenzen gekappt.
3. Nach Tests die Variable wieder entfernen, um zur automatischen Erkennung zurückzukehren.

## Prüfung & Fehlersuche
- Der Faktor lässt sich über den automatisierten Test `pytest tests/ui/test_scaling.py` verifizieren. Dieser simuliert unterschiedliche DPI-Werte und kontrolliert Fonts und Canvas-Dimensionen.
- Bleiben Schriften unverändert, prüfen, ob ein Terminal-/Desktop-Logout notwendig ist, damit die neue Umgebungsvariable greift.
- Für langfristige Verbesserungen oder Auffälligkeiten existiert das To-do [todo/ui-scaling-dpi.md](../todo/ui-scaling-dpi.md).

## Querverweise
- Implementierungsdetails in [`src/ui/app.py`](../src/ui/app.py) und [`src/ui/scaling.py`](../src/ui/scaling.py).
- Hintergrundnotizen: [Task/rendering-notes.md](../Task/rendering-notes.md).
