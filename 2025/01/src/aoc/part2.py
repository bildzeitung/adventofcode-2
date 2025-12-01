"""
Advent of Code Part 2
"""

from typing import TextIO

DIALSTART: int = 50


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    dial: int = DIALSTART
    zeros: int = 0
    for line in f:
        d = -1 if line[0] == "L" else 1
        q = d * int(line[1:].strip())
        # spinning the dial
        while q > 100:
            q -= 100
            zeros += 1
        while q < -100:
            q += 100
            zeros += 1

        old = dial
        dial = (100 + dial + q) % 100
        print(f"Old: {old}\tQ: {q} Dial: {dial}")

        # now there are cases for going past 0 during a move
        if old + q > 100:
            zeros += 1
        if old + q < 0 and old != 0:
            zeros += 1

        # .. and our base case
        if dial == 0:
            zeros += 1
    print(f"Zeros: {zeros}")
