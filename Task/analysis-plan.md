# Analyse-Dossier

Dieses Dossier konsolidiert den Stand der laufenden Untersuchungen aus den [Rendering-Notizen](./rendering-notes.md) und verwandten Arbeitsdokumenten. Es dient als gemeinsame Referenz für Priorisierung, Verantwortlichkeiten und Übergaben.

## Status der Untersuchungen
Die Fortschrittstabelle fasst alle aktiven Spuren zusammen. Zuständigkeiten werden laufend nachgezogen; offene Fragen sind explizit benannt.

| Untersuchung | aktueller Stand | Blocker | Folge-To-dos |
| --- | --- | --- | --- |
| UI-Skalierung auf High-DPI | Unschärfe reproduzierbar, Ursache vermutlich fehlende DPI-Korrektur ([Notizen](./rendering-notes.md#statuslaufend)). Owner noch nicht benannt. | Klärung der Mindestanforderungen für 4k-Displays ausstehend. | [UI-Skalierung: DPI-Anpassung überprüfen](../todo/ui-scaling-dpi.md) |
| Sprite-Offsets bei Fahrzeugen | Versatz bestätigt, Messreihe geplant ([Notizen](./rendering-notes.md#statuslaufend)). Art-Team muss eingebunden werden. | Asset-Korrekturen hängen von externem Export-Workflow ab. | [Sprite-Offsets kalibrieren](../todo/sprite-offset-audit.md) |
| Kamera-Startposition | Start-Viewport durch `CameraView` stabilisiert; Regressionstest deckt Initialisierung und ersten Tick ab (siehe [UI-Doku](../src/ui/README.md#kameraviewport)). | – | [Archiv: Kamera-Initialisierung stabilisieren](../todo/archive/camera-initialization-timing.md) |
| Track-Sprite-Mappings | Randzellen ok, Kreuzungen & T-Junctions fehlen in Mapping + Tests ([Notizen](./rendering-notes.md#weitere-beobachtungen)). | Unklar, ob Asset-Pipeline zusätzliche Varianten liefert. | [Track-Sprite-Mappings für Sonderfälle ergänzen](../todo/track-sprite-mapping.md) |

## Wesentliche Erkenntnisse
- Die Rendering-Probleme konzentrieren sich auf wiederkehrende Layout-Fragen (DPI, Offsets, Kamera). Eine ganzheitliche Review-Session wird empfohlen, bevor isolierte Fixes implementiert werden.
- Testabdeckung für spezielle Gleisformen fehlt weiterhin. Dies blockiert eine belastbare Aussage zur Rendering-Güte dieser Fälle.
- Verantwortlichkeiten sind aktuell überwiegend offen. Die Zuweisung sollte im nächsten Stand-up festgezurrt werden, um die Todo-Verfolgung aus dem [todo/-Verzeichnis](../todo/README.md) zu synchronisieren.

## Empfohlene nächste Tasks
1. **Owner benennen & Briefing aufsetzen** – Klärt Verantwortlichkeiten für UI-, Art- und Gameplay-Teams. Tracking über [UI-Skalierung: DPI-Anpassung überprüfen](../todo/ui-scaling-dpi.md), [Sprite-Offsets kalibrieren](../todo/sprite-offset-audit.md) und [Kamera-Initialisierung stabilisieren](../todo/archive/camera-initialization-timing.md).
2. **Messreihen durchführen** – Sprite-Metriken und Kamera-Profile aufnehmen; Ergebnisse in [Sprite-Offsets kalibrieren](../todo/sprite-offset-audit.md) und [Kamera-Initialisierung stabilisieren](../todo/archive/camera-initialization-timing.md) dokumentieren.
3. **Testabdeckung erweitern** – Sonderformen in den UI-Tests ergänzen und das Mapping dokumentieren, siehe [Track-Sprite-Mappings für Sonderfälle ergänzen](../todo/track-sprite-mapping.md).
