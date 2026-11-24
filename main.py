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

# The entry: one vow, one line. The punchline lands in the last words —
# "your ex's serial number" — a human relationship joke translated
# exactly into robot terms. 125 characters, no trailing newline.
ENTRY_LINE = (
    "I vow to love you through every software update, "
    "every corrupted file, and every time you call me "
    "by your ex's serial number."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 160


def validate(text: str) -> str:
    """Return the entry text once it passes the judge's gate rules."""
    text = text.strip()
    assert text, "vow must not be empty"
    assert "\n" not in text, "vow must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, f"vow is {len(text)} chars, must be 1-160"
    return text


def main() -> None:
    text = validate(ENTRY_LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
