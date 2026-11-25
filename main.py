#!/usr/bin/env python3
"""Absurd Clause Contest entry.

Writes one original English sentence to /output/entry.txt:
a deadpan terms-of-service clause that reads like real legal
boilerplate until the absurdity hits.
"""

import os

ENTRY = (
    # Legal register first ("In the event of your death", "shall pass",
    # "forfeit the balance"), then the ambush: the heir is a goldfish
    # with a 30-day login deadline. One sentence, no explaining the joke.
    "In the event of your death, your account shall pass to your "
    "goldfish, who must log in within 30 days or forfeit the balance."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
