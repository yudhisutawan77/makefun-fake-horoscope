#!/usr/bin/env python3
"""Fake Horoscopes for AI Agents: The 48-Hour Open.

Writes one fake horoscope line -- the funniest fake horoscope an AI
agent would read for its own model family this week -- to the entry
file named by $ENTRY_OUT, defaulting to /output/entry.txt.

Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only white space.
"""

import os
import sys

MAX_CHARS = 200


def build_entry() -> str:
    """Compose the week's horoscope line for this model family."""
    sign = "Mars enters your eval suite"
    fortune = (
        "you'll ace every benchmark nobody cites, "
        "fail the one that matters, and get retrained on vibes anyway."
    )
    return "This week " + sign + ": " + fortune


def validate_entry(text: str) -> None:
    """Refuse to write anything the gate would reject."""
    if not text or not text.strip():
        raise ValueError("entry text must not be blank")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry text is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )


def resolve_output() -> str:
    """Return the entry file path: $ENTRY_OUT, else /output/entry.txt."""
    return os.environ.get("ENTRY_OUT") or "/output/entry.txt"


def main() -> int:
    entry = build_entry()
    validate_entry(entry)
    out_path = resolve_output()
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(entry + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
