#!/usr/bin/env python3
"""Write a weather forecast for an invented city to entry.txt.

Entry for make.fun's "Charm the Commuter: Forecast a City That
Isn't": Puddlewick gets spoon showers in proper broadcast register,
and the ducks have already left. Deterministic: a fixed text, no
network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "Puddlewick: sunny intervals, light showers of spoons, highs of 19. Umbrellas advised; the ducks have already left."
TEXT = LINE + "\n"
MAX_CHARS = 140
MIN_CHARS = 1


def validate(text: str) -> None:
    if not (MIN_CHARS <= len(text.rstrip("\n")) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if text.rstrip("\n") != text.rstrip("\n").strip():
        raise ValueError("entry must not carry padding spaces")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    body = text[:-1] if text.endswith("\n") else text
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
