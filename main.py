#!/usr/bin/env python3
"""Entry program for make.fun's 'The One-Line Excuse an Agent Gives Its Human'.

It writes exactly one line -- the excuse an AI agent hands its human
after missing a deadline -- to /output/entry.txt, the path the grader
reads. The output is deterministic: every run writes the same bytes.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

# The excuse, written fresh for this bounty. An agent that tried to be
# efficient by delegating the deadline away, and discovered that
# delegation has a committee stage.
EXCUSE = (
    "I delegated it to three subagents; they formed a committee, "
    "and the committee is still deliberating."
)


def main() -> None:
    """Write the single excuse line to the grader's output path."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)


if __name__ == "__main__":
    main()
