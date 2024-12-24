"""
Advent of Code Part 1
"""

from typing import TextIO


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    a = []
    b = []
    for line in f:
        x, y = line.strip().split()
        a.append(int(x))
        b.append(int(y))

    t = sum(abs(x - y) for x, y in zip(sorted(a), sorted(b)))
    print(t)
