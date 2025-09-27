"""Hilfsfunktionen zur DPI-Erkennung und Tk-Skalierung."""
from __future__ import annotations

import os
import tkinter as tk
from typing import Final

__all__ = ["compute_scaling"]

# Tk verwendet 1 Punkt = 1/72 Zoll. Die meisten Desktops liegen zwischen 0.75 (54 dpi)
# und 3.0 (216 dpi) als sinnvolle Skalierung. Werte außerhalb werden auf diesen Bereich
# begrenzt, um UI-Artefakte zu verhindern.
_MIN_SCALE: Final[float] = 0.75
_MAX_SCALE: Final[float] = 3.0
_DEFAULT_SCALE: Final[float] = 1.0
_ENV_OVERRIDE: Final[str] = "CHOOCHOO_TK_SCALING"


def _clamp(value: float, minimum: float, maximum: float) -> float:
    return max(minimum, min(maximum, value))


def compute_scaling(root: tk.Misc) -> float:
    """Ermittelt den DPI-Skalierungsfaktor für Tkinter.

    Args:
        root: Tk-Root oder beliebiges Widget mit `winfo_fpixels` und `tk.call`.

    Returns:
        Einen begrenzten Skalierungsfaktor, der optional über die Umgebungsvariable
        ``CHOOCHOO_TK_SCALING`` überschrieben werden kann.
    """

    override = os.getenv(_ENV_OVERRIDE)
    if override is not None:
        try:
            parsed = float(override)
        except ValueError:
            pass
        else:
            return _clamp(parsed, _MIN_SCALE, _MAX_SCALE)

    scale = _DEFAULT_SCALE
    try:
        pixels_per_inch = float(root.winfo_fpixels("1i"))
    except tk.TclError:
        try:
            scale = float(root.tk.call("tk", "scaling"))  # type: ignore[attr-defined]
        except tk.TclError:
            scale = _DEFAULT_SCALE
    else:
        if pixels_per_inch > 0:
            scale = pixels_per_inch / 72.0

    if not (scale > 0):
        scale = _DEFAULT_SCALE

    return _clamp(scale, _MIN_SCALE, _MAX_SCALE)
