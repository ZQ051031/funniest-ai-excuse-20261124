#!/usr/bin/env python3
"""Write the funniest AI excuse entry to /output/entry.txt.

The entry is a single line: an AI agent's excuse after failing a task.
The line is written exactly as-is, with no trailing newline, and is
validated against the competition gate (1-200 characters, one line).
"""

import os

ENTRY = "I did finish your task, but I filed it under 'miscellaneous', and now neither of us will ever find it again."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
