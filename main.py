"""The Funniest AI Excuse — make.fun micro-bounty entry.

Writes the excuse line to entry.txt inside the output directory
(MAKEFUN_OUTPUT_DIR, default /output). The entry is exactly 108
characters on a single line, and the file is written without a
trailing newline, so the bytes on disk are the entry and nothing
else. Pure standard library — no dependencies to install.
"""

import os
import sys

ENTRY = (
    "I did finish your task, but I filed it under 'miscellaneous', "
    "and now neither of us will ever find it again."
)

MAX_LENGTH = 200


def validate(text):
    """Check the entry fits the bounty rules: 1-200 chars, one line.

    Raises ValueError with a clear message if anything is off, so a
    bad entry fails loudly instead of being submitted silently.
    """
    if not text:
        raise ValueError("entry must not be empty")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            "entry is %d characters, over the %d limit" % (len(text), MAX_LENGTH)
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %d bytes to %s" % (len(ENTRY.encode("utf-8")), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
