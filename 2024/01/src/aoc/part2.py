"""
Advent of Code Part 2
"""

from typing import TextIO


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    a = []
    b = []
    for line in f:
        x, y = line.strip().split()
        a.append(int(x))
        b.append(int(y))

    t = sum(b.count(x) * x for x in a)
    print(t)
