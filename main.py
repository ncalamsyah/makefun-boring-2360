#!/usr/bin/env python3
"""make.fun bounty entry: write the one-line review to /output/entry.txt."""

from pathlib import Path

PATH = Path("/output/entry.txt")
LINE = (
    "A doorstop spends its whole life holding open opportunities it will never walk through."
)


def main() -> None:
    """Validate LINE and write it (and only it) to PATH."""
    assert 1 <= len(LINE) <= 200, "LINE must be 1..200 chars"
    assert "\n" not in LINE, "LINE must not contain a newline"
    PATH.parent.mkdir(parents=True, exist_ok=True)
    PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
