"""Validiert die Kamera-Initialisierung ohne echtes Tk-Canvas."""
from __future__ import annotations

from dataclasses import dataclass, field

from ui.camera import CameraView


@dataclass
class FakeCanvas:
    """Minimaler Canvas-Ersatz zum Zählen von Scroll-Operationen."""

    config_calls: list[dict[str, object]] = field(default_factory=list)
    xview_fractions: list[float] = field(default_factory=list)
    yview_fractions: list[float] = field(default_factory=list)
    moveto_calls: list[tuple[tuple[object, ...], dict[str, object]]] = field(
        default_factory=list
    )
    scan_dragto_calls: list[tuple[tuple[object, ...], dict[str, object]]] = field(
        default_factory=list
    )

    def config(self, **kwargs: object) -> None:
        self.config_calls.append(kwargs)

    def xview_moveto(self, fraction: float) -> None:
        self.xview_fractions.append(fraction)

    def yview_moveto(self, fraction: float) -> None:
        self.yview_fractions.append(fraction)

    def moveto(self, *args: object, **kwargs: object) -> None:
        self.moveto_calls.append((args, kwargs))

    def scan_dragto(self, *args: object, **kwargs: object) -> None:
        self.scan_dragto_calls.append((args, kwargs))


def test_camera_does_not_drag_without_movement() -> None:
    """Initialisierung + Tick ohne Bewegung dürfen keine Drag-Calls auslösen."""

    camera = CameraView(cell_size=32, map_size=(10, 10), viewport_size=(128, 128))
    canvas = FakeCanvas()

    # Initiale Zentrierung entspricht dem App-Start.
    changed = camera.center_on((4, 4))
    assert changed is True
    camera.apply(canvas)

    assert canvas.moveto_calls == []
    assert canvas.scan_dragto_calls == []
    assert len(canvas.xview_fractions) == 1
    assert len(canvas.yview_fractions) == 1

    # Erster Tick ohne Bewegung darf keine weiteren Scroll-Befehle auslösen.
    changed = camera.center_on((4, 4))
    assert changed is False
    camera.apply(canvas)

    assert canvas.moveto_calls == []
    assert canvas.scan_dragto_calls == []
    assert len(canvas.xview_fractions) == 1
    assert len(canvas.yview_fractions) == 1
