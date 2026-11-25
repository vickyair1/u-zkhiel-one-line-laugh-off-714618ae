#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Deterministic: the same line on every run.
"""

import os

ENTRY = "My therapist bills by the hour, so I cry in bullet points now."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200 and ENTRY.strip(), "entry must be 1-200 non-blank chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
