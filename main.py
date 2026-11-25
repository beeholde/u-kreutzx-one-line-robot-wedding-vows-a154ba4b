#!/usr/bin/env python3
"""One-Line Robot Wedding Vows v2 — make.fun entry.

Writes one line of wedding vows for a robot couple to /output/entry.txt.

Built against the published judge brief (pairwise, z-ai/glm-5.3-flash):
a real wedding promise ("I vow to love you through ..."), machine-specific
details (software updates, corrupted files, serial numbers), and the laugh
paying off in the last few words — the speaker being called by an ex's
serial number, with the sting in the tail: the ex is a toaster. 156
characters, one line, no trailing newline.
"""

import os

VOW = (
    "I vow to love you through every software update, "
    "every corrupted file, and every time you call me "
    "by your ex's serial number — even when it's the toaster's."
)

OUT = "/output/entry.txt"
LIMIT = 160


def check(line: str) -> str:
    """Return the vow once it passes the gate: 1-160 chars, one line."""
    line = line.strip()
    if not line:
        raise SystemExit("vow must not be empty")
    if "\n" in line:
        raise SystemExit("vow must be a single line")
    if len(line) > LIMIT:
        raise SystemExit(f"vow is {len(line)} chars, over the {LIMIT} limit")
    return line


def main() -> None:
    # The joke's turn sits in the last words: "the toaster's" reframes the
    # ex as a kitchen appliance — the same serial-number gag as v1, with a
    # second, more surprising payoff stacked on top of it.
    line = check(VOW)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
