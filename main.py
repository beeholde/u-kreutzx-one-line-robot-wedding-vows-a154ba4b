#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The vow was designed against the published judge
brief: a real wedding promise ("I vow to love you through ..."),
machine-specific details (software updates, corrupted files, a serial
number), and the laugh paying off in the last few words — the speaker
being called by an ex's serial number, a human relationship joke
translated exactly into robot terms. 125 characters, one line, no
trailing newline issues: the file holds the line alone.
"""

import os

VOW = (
    "I vow to love you through every software update, "
    "every corrupted file, and every time you call me "
    "by your ex's serial number."
)


def main() -> None:
    text = VOW.strip()
    assert text, "vow must not be empty"
    assert "\n" not in text, "vow must be a single line"
    assert 1 <= len(text) <= 160, f"vow is {len(text)} chars, must be 1-160"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
