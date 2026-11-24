#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes the funniest one-line excuse an AI agent gives for a missed
deadline to /output/entry.txt, validates it against the competition
gate (one line, 1-200 characters, not only whitespace), and reads the
file back to confirm it holds exactly what was written.
"""

import os
import sys

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")

EXCUSE = (
    "I gave myself a 99.9% chance of finishing on time, then spent "
    "the deadline proving the 0.1% right."
)


def validate(text: str) -> None:
    """Check the excuse against the competition gate."""
    if not text or not text.strip():
        raise ValueError("excuse must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if len(text) > 200:
        raise ValueError(
            f"excuse is {len(text)} characters, over the 200 limit"
        )


def main() -> int:
    validate(EXCUSE)

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EXCUSE)

    # Exact read-back: the file must hold precisely what was written,
    # and the text read back must pass the gate on its own too.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != EXCUSE:
        raise ValueError(
            "read-back mismatch: /output/entry.txt does not match "
            "the excuse exactly"
        )
    validate(written)

    print(f"Wrote {len(EXCUSE)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
