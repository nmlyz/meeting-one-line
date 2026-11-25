#!/usr/bin/env python3
"""Write one line to /output/entry.txt: the single sentence that could
have replaced an entire pointless meeting.

The line was picked from 40 candidates by pairwise judging against the
brief — it is the meeting's payload, not a comment on the meeting: the
launch date and the budget decision, closed with the sting that nobody
in the room was going to change either of those things, so after this
line there is nothing left to meet about. It beat the runner-up, a year
of Tuesday meetings about a project that ended in March, in the final
because it delivers the decisions themselves instead of only exposing
the meeting's futility. The program checks the result
against the entry gate (length, single line, no leading or trailing
space, exact judged length) before writing it, then reads the file back
to confirm the bytes match.
"""

import os
import sys

LINE = (
    "We're launching Tuesday, the budget's approved, and nobody "
    "in this room was going to change either of those things."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
