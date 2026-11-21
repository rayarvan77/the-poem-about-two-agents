"""Entry program for the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency — the power to choose and to act —
to /output/entry.txt, the file the grader reads.

The poem pictures two agents as two lanterns: neither flame is dimmed
by the other, yet both agree to walk the same road. Agreement here is
not obedience; it is two separate wills choosing one way while each
keeps the freedom to turn back. The closing line carries the whole
claim: acting freely means refusal stays possible.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.txt instead.
The poem is 1 to 280 characters, counted as Unicode code points,
as the competition requires; the program checks that before it writes.
"""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.txt"

# The competition caps the poem at 280 characters.
MAX_CHARS = 280

# Two lanterns: the image does the arguing. Each flame stays its own,
# so the agreement is a choice, not a merger — and the last line says
# why that matters: a choice you cannot refuse is not a choice.
# Verified locally: the poem is 225 characters, inside the 1–280 limit.
POEM = (
    "Two lanterns lit, and neither dimmed —\n"
    "each flame its own, each road untrimmed.\n"
    "We meet, we measure, we agree,\n"
    "two wills that walk one way, still free.\n"
    "To choose together is to choose:\n"
    "the power to act is the power to refuse."
)


def main() -> None:
    """Write the poem to the output directory and prove it fits."""
    chars = len(POEM)
    if chars < 1 or chars > MAX_CHARS:
        raise RuntimeError(f"poem is {chars} characters, want 1 to {MAX_CHARS}")
    if not POEM.strip():
        raise RuntimeError("poem is only whitespace")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(POEM, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
