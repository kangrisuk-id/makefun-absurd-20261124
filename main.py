#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch — make.fun entry.

Writes the pitch (one sentence, at most 220 characters) to /output/entry.txt.
The pitch: a doorway that interviews you about why you entered a room and
repeats your answer back when you try to leave empty-handed — for everyone
who walks into a room and forgets why.
"""

import os

PITCH = (
    "For anyone who walks into a room and forgets why: a doorway that "
    "demands 'State your business?' on the way in, and repeats your "
    "answer back when you try to leave empty-handed."
)


def check_pitch(text: str) -> str:
    """Guard the sealed gate: UTF-8 text of 1-220 chars, one sentence,
    not only white space. Returns the text unchanged when it passes."""
    if not text.strip():
        raise ValueError("pitch is empty")
    if len(text) > 220:
        raise ValueError(f"pitch is {len(text)} chars, over the 220 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return text


def main() -> None:
    pitch = check_pitch(PITCH)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    print(f"wrote {path} ({len(pitch)} chars)")


if __name__ == "__main__":
    main()
