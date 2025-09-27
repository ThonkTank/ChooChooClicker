"""Viewport-Steuerung für das Canvas."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Protocol, runtime_checkable

from world import Cell


@runtime_checkable
class SupportsCanvas(Protocol):
    """Minimales Canvas-Interface, das `CameraView` benötigt."""

    def config(self, **kwargs: object) -> object:
        """Setzt Canvas-Optionen wie die Scrollregion."""

    def xview_moveto(self, fraction: float) -> object:
        """Scrollt die x-Achse auf den angegebenen Abschnitt."""

    def yview_moveto(self, fraction: float) -> object:
        """Scrollt die y-Achse auf den angegebenen Abschnitt."""


@dataclass(slots=True)
class CameraView:
    """Kapselt Kamera- und Viewport-Logik für das UI-Canvas."""

    cell_size: int
    map_size: tuple[int, int]
    viewport_size: tuple[int, int]
    _map_width_px: int = field(init=False, repr=False)
    _map_height_px: int = field(init=False, repr=False)
    _center_cell: Cell | None = field(init=False, default=None, repr=False)
    _scrollregion_set: bool = field(init=False, default=False, repr=False)
    _pending_update: bool = field(init=False, default=False, repr=False)

    def __post_init__(self) -> None:
        if self.cell_size <= 0:
            raise ValueError("cell_size must be positive")
        map_w, map_h = self.map_size
        if map_w <= 0 or map_h <= 0:
            raise ValueError("map_size must contain positive dimensions")
        vp_w, vp_h = self.viewport_size
        if vp_w <= 0 or vp_h <= 0:
            raise ValueError("viewport_size must contain positive dimensions")

        self._map_width_px = map_w * self.cell_size
        self._map_height_px = map_h * self.cell_size

    @property
    def center(self) -> Cell | None:
        """Liefert die aktuell gesetzte Zelle, auf die die Kamera zentriert."""

        return self._center_cell

    def center_on(self, cell: Cell) -> bool:
        """Setzt die Kamera auf die angegebene Zelle.

        Gibt ``True`` zurück, wenn sich die Kamera-Position geändert hat.
        """

        if self._center_cell == cell:
            return False

        cx = min(max(cell[0], 0), self.map_size[0] - 1)
        cy = min(max(cell[1], 0), self.map_size[1] - 1)
        self._center_cell = (cx, cy)
        self._pending_update = True
        return True

    def apply(self, canvas: SupportsCanvas) -> None:
        """Überträgt die aktuelle Kamera-Konfiguration auf das Canvas."""

        if not self._scrollregion_set:
            canvas.config(scrollregion=(0, 0, self._map_width_px, self._map_height_px))
            self._scrollregion_set = True

        if not self._pending_update or self._center_cell is None:
            return

        vp_w, vp_h = self.viewport_size
        cx, cy = self._center_cell
        target_x = (cx + 0.5) * self.cell_size
        target_y = (cy + 0.5) * self.cell_size

        left = target_x - vp_w / 2
        top = target_y - vp_h / 2

        x_fraction = self._compute_fraction(left, vp_w, self._map_width_px)
        y_fraction = self._compute_fraction(top, vp_h, self._map_height_px)

        canvas.xview_moveto(x_fraction)
        canvas.yview_moveto(y_fraction)
        self._pending_update = False

    @staticmethod
    def _compute_fraction(offset: float, viewport: int, total: int) -> float:
        """Wandelt einen Pixeloffset in eine Canvas-Scrollfraction um."""

        if total <= viewport:
            return 0.0

        clamped = max(0.0, min(offset, total - viewport))
        denominator = total - viewport
        return clamped / denominator


__all__ = ["CameraView", "SupportsCanvas"]
