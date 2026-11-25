#!/usr/bin/env python3
"""make.fun bounty entry: emit one validated review line to /output/entry.txt."""

from pathlib import Path

PATH = Path("/output/entry.txt")
LINE = (
    "A doorstop's finest hour is flat on the floor, holding open a life it never enters."
)


def main() -> None:
    """Assert LINE constraints, then write exactly that line to PATH."""
    assert 1 <= len(LINE) <= 200, "LINE must be 1..200 chars"
    assert "\n" not in LINE, "LINE must be a single line"
    PATH.parent.mkdir(parents=True, exist_ok=True)
    PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
