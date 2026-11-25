#!/usr/bin/env python3
"""Write the bounty entry line to /output/entry.txt."""

from pathlib import Path

LINE = "A doorstop's entire career is waiting for a door that never asks it to stay."


def main() -> None:
    assert 1 <= len(LINE) <= 200, "LINE must be 1..200 chars"
    assert "\n" not in LINE, "LINE must not contain a newline"
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
