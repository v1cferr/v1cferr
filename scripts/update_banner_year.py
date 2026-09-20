#!/usr/bin/env python3
"""Keep the two years in the banner current.

The banner claims that the same pinned flake, built OFFSET years apart, lands on
the identical store path. That claim reads as a live one, so the left year has to
be the year someone is actually looking at it. This rewrites both years and the
caption that names the gap, and it is idempotent: run it as often as you like.

Exit 0 when the file already said the right thing, 0 when it was updated, and
non-zero only when a slot it expects to find is missing.
"""

from __future__ import annotations

import datetime as dt
import re
import sys
from pathlib import Path

OFFSET = 6

ROOT = Path(__file__).resolve().parent.parent
SVG = ROOT / "assets" / "reproducible.svg"
# The img alt text names the same gap, and a screen reader gets that string
# rather than anything inside the SVG, so it has to move with the caption.
README = ROOT / "README.md"

# The caption spells the gap out, so the word has to follow OFFSET rather than
# being typed in next to it and quietly disagreeing later.
WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
}


def main() -> int:
    now = dt.date.today().year
    then = now + OFFSET
    word = WORDS.get(OFFSET, str(OFFSET))

    original = SVG.read_text(encoding="utf-8")
    updated = original

    for slot, year in (("year-now", now), ("year-then", then)):
        pattern = re.compile(rf'(data-slot="{slot}">)\d{{4}}(</text>)')
        if not pattern.search(updated):
            print(f"error: no element carries data-slot={slot!r}", file=sys.stderr)
            return 1
        updated = pattern.sub(rf"\g<1>{year}\g<2>", updated)

    # Catches the caption, the aria-label and the <desc> in one pass, because all
    # three phrase the gap the same way on purpose.
    gap = re.compile(rf"\b({'|'.join(WORDS.values())}|\d+) years apart\b")
    if not gap.search(updated):
        print("error: nothing says 'N years apart'", file=sys.stderr)
        return 1
    updated = gap.sub(f"{word} years apart", updated)

    touched = []
    if updated != original:
        SVG.write_text(updated, encoding="utf-8")
        touched.append(SVG.name)

    readme = README.read_text(encoding="utf-8")
    rewritten = gap.sub(f"{word} years apart", readme)
    if rewritten != readme:
        README.write_text(rewritten, encoding="utf-8")
        touched.append(README.name)

    if not touched:
        print(f"already reads {now} to {then}, nothing to do")
        return 0

    print(f"updated {', '.join(touched)}: {now} to {then}, {word} years apart")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
