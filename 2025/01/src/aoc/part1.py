"""
Advent of Code Part 1
"""

from typing import TextIO

DIALSTART: int = 50


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    dial: int = DIALSTART
    zeros: int = 0
    for line in f:
        d = -1 if line[0] == "L" else 1
        q = d * int(line[1:].strip())
        dial = (100 + dial + q) % 100
        if dial == 0:
            zeros += 1
    print(f"Zeros: {zeros}")
