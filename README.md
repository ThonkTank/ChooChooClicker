# Choo Choo Clicker – Projektleitfaden

Choo Choo Clicker ist ein Clicker-Spiel rund um einen kleinen Zug. Die Anwendung soll lokal laufen.
Der grundlegende Gameplay Loop besteht darin, den zug über eine aus einem Grid bestehende Karte fahren zu lassen. Der user kann eine Kurbel betätigen, um dem Zug Momentum zu geben. Momentum wird pro Schritt zur nächsten Kachel verbraucht. Es kann bis zu 10 Momentum gespeichert werden. Mit Rechtsklick kann der Spieler schienen entfernen oder hinzufügen. Dabei gibt es grade schienen, kurven und kreuzungen. An Kreuzungen hat jeder ausgang eine Weiche, welche bestimmt wie der Zug abbiegt. Die Weiche kann mit linksklick gestellt werden.

Die UI besteht aus drei Komponenten. Einem Karten Fenster links, einer Menü Leiste mit resourcen trackern oben und einem Ui Panel rechts. Die Karte enthält die graphische Darstellung der Welt, das Ui panel die Klicker-menü elemente.

## Entwicklung

```bash
npm install
npm run dev
```

## Tests

```bash
npm test
```
