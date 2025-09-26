"""Analyse script for the Ground-Rails sprite sheet.

The tool prints heuristic orientation hints for every 32x32 tile in the
image using only Python's standard library. It is useful for headless
verification during reviews.
"""
from __future__ import annotations

import argparse
import struct
import zlib
from pathlib import Path
from typing import Iterable, Sequence

BYTES_PER_PIXEL = 4  # RGBA
TILE_SIZE = 32


class PngDecodeError(RuntimeError):
    """Raised when the PNG stream uses unsupported features."""


def _read_png(path: Path) -> tuple[int, int, list[bytearray]]:
    data = path.read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise PngDecodeError("File does not start with PNG signature")

    pos = 8
    width = height = None
    compressed = bytearray()

    while pos < len(data):
        if pos + 8 > len(data):
            raise PngDecodeError("Unexpected end of file while reading chunk header")
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        pos += 4
        chunk_type = data[pos : pos + 4]
        pos += 4
        chunk_data = data[pos : pos + length]
        pos += length
        pos += 4  # skip CRC

        if chunk_type == b"IHDR":
            width, height, bit_depth, color_type, compression, filter_method, interlace = struct.unpack(
                ">IIBBBBB", chunk_data
            )
            if bit_depth != 8 or color_type != 6:
                raise PngDecodeError(
                    f"Unsupported pixel format (bit_depth={bit_depth}, color_type={color_type})"
                )
            if compression != 0 or filter_method != 0 or interlace != 0:
                raise PngDecodeError("Unsupported PNG features in IHDR")
        elif chunk_type == b"IDAT":
            compressed.extend(chunk_data)
        elif chunk_type == b"IEND":
            break

    if width is None or height is None:
        raise PngDecodeError("Missing IHDR chunk")

    raw = zlib.decompress(bytes(compressed))
    row_stride = width * BYTES_PER_PIXEL

    pixels: list[bytearray] = []
    pos = 0
    for _ in range(height):
        filter_type = raw[pos]
        pos += 1
        row = bytearray(raw[pos : pos + row_stride])
        pos += row_stride

        if filter_type == 0:  # None
            pass
        elif filter_type == 1:  # Sub
            for i in range(BYTES_PER_PIXEL, len(row)):
                row[i] = (row[i] + row[i - BYTES_PER_PIXEL]) % 256
        elif filter_type == 2:  # Up
            prev = pixels[-1] if pixels else bytearray(len(row))
            for i in range(len(row)):
                row[i] = (row[i] + prev[i]) % 256
        elif filter_type == 3:  # Average
            prev = pixels[-1] if pixels else bytearray(len(row))
            for i in range(len(row)):
                left = row[i - BYTES_PER_PIXEL] if i >= BYTES_PER_PIXEL else 0
                up = prev[i]
                row[i] = (row[i] + ((left + up) // 2)) % 256
        elif filter_type == 4:  # Paeth
            prev = pixels[-1] if pixels else bytearray(len(row))
            for i in range(len(row)):
                a = row[i - BYTES_PER_PIXEL] if i >= BYTES_PER_PIXEL else 0
                b = prev[i]
                c = prev[i - BYTES_PER_PIXEL] if i >= BYTES_PER_PIXEL else 0
                p = a + b - c
                pa = abs(p - a)
                pb = abs(p - b)
                pc = abs(p - c)
                if pa <= pb and pa <= pc:
                    predictor = a
                elif pb <= pc:
                    predictor = b
                else:
                    predictor = c
                row[i] = (row[i] + predictor) % 256
        else:
            raise PngDecodeError(f"Unhandled filter type {filter_type}")
        pixels.append(row)

    return width, height, pixels


def _summaries(width: int, height: int, pixels: Sequence[bytearray]) -> Iterable[tuple[int, int, dict[str, int]]]:
    cols = width // TILE_SIZE
    rows = height // TILE_SIZE

    for row in range(rows):
        for col in range(cols):
            start_x = col * TILE_SIZE
            start_y = row * TILE_SIZE
            stats = {
                "alpha_pixels": 0,
                "bright_top": 0,
                "bright_bottom": 0,
                "bright_left": 0,
                "bright_right": 0,
            }
            for y in range(start_y, start_y + TILE_SIZE):
                row_data = pixels[y]
                for x in range(start_x, start_x + TILE_SIZE):
                    offset = x * BYTES_PER_PIXEL
                    r, g, b, a = row_data[offset : offset + BYTES_PER_PIXEL]
                    if a < 10:
                        continue
                    stats["alpha_pixels"] += 1
                    gray = (r + g + b) / 3
                    if gray > 120:  # heuristically treat as rail highlight
                        if y - start_y < TILE_SIZE // 2:
                            stats["bright_top"] += 1
                        else:
                            stats["bright_bottom"] += 1
                        if x - start_x < TILE_SIZE // 2:
                            stats["bright_left"] += 1
                        else:
                            stats["bright_right"] += 1
            yield col, row, stats


def _format_summary(col: int, row: int, stats: dict[str, int]) -> str:
    def orientation() -> str:
        if stats["alpha_pixels"] == 0:
            return "leer"
        vertical_bias = stats["bright_top"] + stats["bright_bottom"]
        horizontal_bias = stats["bright_left"] + stats["bright_right"]
        if vertical_bias == 0 and horizontal_bias == 0:
            return "boden"
        if stats["bright_right"] and not stats["bright_left"]:
            return "vertical (east offset)"
        if stats["bright_left"] and not stats["bright_right"]:
            return "vertical (west offset)"
        if stats["bright_top"] and not stats["bright_bottom"]:
            return "horizontal (top)"
        if stats["bright_bottom"] and not stats["bright_top"]:
            return "horizontal (bottom)"
        return "curve or mixed"

    return f"({col},{row}) -> {orientation():<24} rail_px={stats['alpha_pixels']}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("png", type=Path, help="Path to Ground-Rails.png")
    args = parser.parse_args()

    width, height, pixels = _read_png(args.png)
    for col, row, stats in _summaries(width, height, pixels):
        print(_format_summary(col, row, stats))


if __name__ == "__main__":
    main()
