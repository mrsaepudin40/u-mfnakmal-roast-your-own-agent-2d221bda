#!/usr/bin/env python3
"""Roast Your Own Agent: write one roast line to /output/entry.txt."""

from pathlib import Path

# Punch lands on the last words: a meeting with itself.
LINE = "My agent treats a one-line fix like a PhD thesis: three citations, two diagrams, and a follow-up meeting with itself."


def main():
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
