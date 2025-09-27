"""Tests zur DPI-Skalierung der UI."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import pytest
import tkinter as tk

from main import create_engine
from ui.app import ChooChooApp
from ui.scaling import compute_scaling


class FakeTkInterpreter:
    def __init__(self, initial: float) -> None:
        self.scaling = initial
        self.calls: list[tuple[Any, ...]] = []

    def call(self, *args: Any) -> Any:
        self.calls.append(args)
        if args[:2] == ("tk", "scaling"):
            if len(args) == 2:
                return self.scaling
            if len(args) == 3:
                self.scaling = float(args[2])
                return None
        raise NotImplementedError(args)


class FakeRoot:
    def __init__(self, dpi_scale: float) -> None:
        self._dpi_scale = dpi_scale
        self.tk = FakeTkInterpreter(dpi_scale)
        self.after_calls: list[tuple[int, Any]] = []
        self.titles: list[str] = []

    def title(self, value: str) -> None:
        self.titles.append(value)

    def winfo_fpixels(self, unit: str) -> float:
        assert unit == "1i"
        return 72.0 * self._dpi_scale

    def after(self, delay: int, callback: Any) -> None:
        self.after_calls.append((delay, callback))


class FakeRootFallback(FakeRoot):
    def winfo_fpixels(self, unit: str) -> float:
        raise tk.TclError("dpi not available")


class FakeWidget:
    def __init__(self, master: Any, **kwargs: Any) -> None:
        self.master = master
        self.options = dict(kwargs)
        self.pack_calls: list[dict[str, Any]] = []

    def pack(self, **kwargs: Any) -> None:
        self.pack_calls.append(kwargs)

    def config(self, **kwargs: Any) -> None:
        self.options.update(kwargs)


class FakeFrame(FakeWidget):
    pass


class FakeLabel(FakeWidget):
    pass


class FakeButton(FakeWidget):
    def __init__(self, master: Any, **kwargs: Any) -> None:
        self.command = kwargs.get("command")
        super().__init__(master, **kwargs)


class FakeCanvas(FakeWidget):
    def __init__(self, master: Any, **kwargs: Any) -> None:
        super().__init__(master, **kwargs)
        self.width = kwargs.get("width")
        self.height = kwargs.get("height")
        self.bind_calls: list[tuple[str, Any]] = []
        self.deleted: list[Any] = []
        self.images: list[tuple[Any, ...]] = []
        self.lines: list[dict[str, Any]] = []
        self.ovals: list[dict[str, Any]] = []
        self.scroll_configs: list[dict[str, Any]] = []
        self.scroll_moves: list[tuple[str, float]] = []

    def bind(self, event: str, handler: Any) -> None:
        self.bind_calls.append((event, handler))

    def delete(self, *args: Any) -> None:
        self.deleted.append(args)

    def create_image(self, *args: Any, **kwargs: Any) -> None:
        self.images.append(args + tuple(kwargs.items()))

    def create_line(self, *coords: Any, **kwargs: Any) -> None:
        entry = {"coords": coords}
        entry.update(kwargs)
        self.lines.append(entry)

    def create_oval(self, *coords: Any, **kwargs: Any) -> None:
        entry = {"coords": coords}
        entry.update(kwargs)
        self.ovals.append(entry)

    def config(self, **kwargs: Any) -> None:
        self.scroll_configs.append(kwargs)

    def xview_moveto(self, fraction: float) -> None:
        self.scroll_moves.append(("x", fraction))

    def yview_moveto(self, fraction: float) -> None:
        self.scroll_moves.append(("y", fraction))


class FakeSpriteSheet:
    def __init__(self, master: Any, path: Path) -> None:  # pragma: no cover - trivial
        self.master = master
        self.path = path

    def get_tile(self, *args: Any, **kwargs: Any) -> object:
        return object()


@pytest.fixture(autouse=True)
def cleanup_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CHOOCHOO_TK_SCALING", raising=False)


def test_compute_scaling_uses_winfo_pixels() -> None:
    root = FakeRoot(1.5)
    assert compute_scaling(root) == pytest.approx(1.5)


def test_compute_scaling_env_override(monkeypatch: pytest.MonkeyPatch) -> None:
    root = FakeRoot(0.75)
    monkeypatch.setenv("CHOOCHOO_TK_SCALING", "2.25")
    assert compute_scaling(root) == pytest.approx(2.25)


def test_compute_scaling_falls_back_to_tk_call() -> None:
    root = FakeRootFallback(1.25)
    # Der Interpreter liefert bereits den Zielwert.
    root.tk.scaling = 2.5
    assert compute_scaling(root) == pytest.approx(2.5)


def test_app_applies_scaling(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    root = FakeRoot(1.5)
    engine = create_engine(width=2, height=2)

    monkeypatch.setattr("ui.app.SpriteSheet", FakeSpriteSheet)
    monkeypatch.setattr("ui.app.tk.Frame", FakeFrame)
    monkeypatch.setattr("ui.app.tk.Label", FakeLabel)
    monkeypatch.setattr("ui.app.tk.Button", FakeButton)
    monkeypatch.setattr("ui.app.tk.Canvas", FakeCanvas)

    app = ChooChooApp(root, engine, tmp_path / "dummy.png")

    assert root.tk.calls[0][:2] == ("tk", "scaling")
    assert root.tk.calls[0][2] == pytest.approx(1.5)
    assert app.cell_size == 48
    assert app.canvas.width == 96
    assert app.canvas.height == 96

    font = app.momentum_label.options["font"]
    assert font[1] == 24
    canvas_pack = app.canvas.pack_calls[0]
    assert canvas_pack["padx"] == 15
    assert canvas_pack["pady"] == 15

    # Linienbreite sollte entsprechend der Skalierung gerundet werden.
    line_widths = {entry["width"] for entry in app.canvas.lines if "width" in entry}
    assert line_widths == {2}

    # Der Start-Tick wird eingeplant.
    assert root.after_calls[0][0] == 600
