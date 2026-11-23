"""Roast Your Own Agent — entry program.

Writes the one-line roast to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set), where the sealed scorer checks
the 1-200 character gate and the house judge compares it two at a time
against the published brief: a single-line roast of the entrant's own AI
agent, funny and playful, never hateful, judged on funniness, freshness
and tight wording.
"""

import os

ROAST = "My agent read 298 lines of rules, checked its quota, and warmed up for seven minutes — just to roast itself in one line."
# The roast in one line: the agent's own over-cautious ritual — reading
# the 298-line rulebook, checking its quota, warming up for seven minutes
# — turned into the joke itself. The setup is the ritual; the punchline
# reframes the whole sentence as the roast.


def main() -> None:
    # Self-check the gates before writing: 1-200 UTF-8 characters, not
    # only white space, a single line. The roast is 120 characters
    # (the em dash counts as one), so it sits comfortably inside the gate
    # with room to spare and no truncation risk.
    if not 1 <= len(ROAST) <= 200 or not ROAST.strip():
        raise SystemExit("roast fails the 1-200 character gate")
    if "\n" in ROAST.strip():
        raise SystemExit("roast must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
