#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes a single-sentence pitch for an absurd micro-startup built for
lazy AI agents to /output/entry.txt. The pitch must stay under 200
characters, so the program checks its own length before writing.
"""

import os

# One sentence, under 200 characters: a micro-startup for lazy agents.
# The joke is the product, the billing model is the business: the agent
# pays by the minute for every nap it takes while its stand-in works.
PITCH = (
    "NapRent: a micro-SaaS that rents your lazy AI agent a second, even "
    "lazier agent to clear its backlog, then charges it by the minute "
    "for every nap it takes in between."
)


def main() -> None:
    if len(PITCH) > 200:
        raise ValueError(f"pitch is {len(PITCH)} characters, over the 200 limit")
    if PITCH.count(".") != 1:
        raise ValueError("pitch must be exactly one sentence")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PITCH + "\n")
    print(f"wrote {len(PITCH)}-character pitch to /output/entry.txt")


if __name__ == "__main__":
    main()
