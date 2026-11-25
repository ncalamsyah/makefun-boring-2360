#!/usr/bin/env python3
"""make.fun bounty entry: write the one-line review to /output/entry.txt."""

from pathlib import Path

LINE = "A doorstop's entire career is waiting for a door that never asks it to stay."


def main() -> None:
    """Validate LINE and write it (and only it) to /output/entry.txt."""
    assert 1 <= len(LINE) <= 200, "LINE must be 1..200 chars"
    assert "\n" not in LINE, "LINE must not contain a newline"
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
