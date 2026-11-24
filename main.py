#!/usr/bin/env python3
"""Two Days of Excuses - entry writer.

Writes the one-line excuse exactly as given to /output/entry.txt.
No trailing newline is added, so the file content is byte-identical
to the entry text.
"""

ENTRY = "I finished in four seconds, then spent six hours confidently explaining to the linter why it was wrong."

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path=OUTPUT_PATH):
    """Write the entry text to path, byte-exact, no trailing newline."""
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main():
    write_entry()


if __name__ == "__main__":
    main()
