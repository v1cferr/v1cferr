#!/usr/bin/env python3
"""Keep meta.lastModified honest.

A hand-typed "last updated" line is the clearest possible signal that a profile
was abandoned: it is right for a week and wrong for a year. So this derives the
date from git instead, and specifically from the last commit that a person made.

Commits by the bot are skipped on purpose. If they counted, the date would
report when the automation last ran rather than when anything actually changed,
and every monthly firing would claim the profile was freshly updated.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

README = Path(__file__).resolve().parent.parent / "README.md"

BOT_NAME = "github-actions[bot]"
BOT_EMAIL = "41898282+github-actions[bot]@users.noreply.github.com"

# meta.lastModified = "2026-09-20";
FIELD = re.compile(r'(lastModified\s*=\s*")(\d{4}-\d{2}-\d{2})(")')


def last_human_commit_date() -> str | None:
    """The committer date of the most recent commit not made by the bot."""
    try:
        out = subprocess.run(
            ["git", "log", "-50", "--format=%cs%x1f%an%x1f%ae"],
            capture_output=True, text=True, check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        print(f"error: cannot read git history: {exc}", file=sys.stderr)
        return None

    for line in out.splitlines():
        date, _, rest = line.partition("\x1f")
        name, _, email = rest.partition("\x1f")
        if name == BOT_NAME or email == BOT_EMAIL:
            continue
        return date

    # Every commit in the window was the bot's. Better to leave the file alone
    # than to stamp it with a date no human earned.
    print("error: no human commit in the last 50", file=sys.stderr)
    return None


def main() -> int:
    date = last_human_commit_date()
    if date is None:
        return 1

    original = README.read_text(encoding="utf-8")
    if not FIELD.search(original):
        print("error: README has no lastModified field", file=sys.stderr)
        return 1

    updated = FIELD.sub(rf"\g<1>{date}\g<3>", original)
    if updated == original:
        print(f"lastModified already reads {date}")
        return 0

    README.write_text(updated, encoding="utf-8")
    print(f"lastModified updated to {date}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
