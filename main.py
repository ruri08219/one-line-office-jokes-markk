#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes one single-line joke about office life to /output/entry.txt.
Stdlib only: os.
"""
import os

ENTRY = "The printer jammed on the one page I needed, so I printed my resignation \u2014 it jammed on that too."
MAX_CHARS = 199


def check_entry(text):
    """Gate mirror: 1-199 chars, one line, not only whitespace."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError("entry must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    return text


def main():
    check_entry(ENTRY)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (path, len(ENTRY)))


if __name__ == "__main__":
    main()
