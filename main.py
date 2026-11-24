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


def _check_not_empty(text: str) -> None:
    """Gate 1: the excuse must contain more than whitespace."""
    if not text or not text.strip():
        raise ValueError("excuse must not be empty or only whitespace")


def _check_single_line(text: str) -> None:
    """Gate 2: the excuse must be exactly one line."""
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")


def _check_length(text: str) -> None:
    """Gate 3: the excuse must fit the 200-character limit."""
    if len(text) > 200:
        raise ValueError(
            f"excuse is {len(text)} characters, over the 200 limit"
        )


def validate(text: str) -> None:
    """Check the excuse against the competition gate.

    The gate is three separate rules — non-empty, single line, and
    at most 200 characters — each enforced by its own helper so a
    failure names exactly which rule the text broke.
    """
    _check_not_empty(text)
    _check_single_line(text)
    _check_length(text)


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
