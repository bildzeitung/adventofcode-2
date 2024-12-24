"""
Advent of Code Part 1
"""

from typing import TextIO


def process(line: str) -> bool:
    items = [x for x in map(int, line.split())]
    deltas = [x[0] - x[1] for x in zip(items, items[1:])]
    # if any of the deltas are > 3 or 0
    if sum(x for x in map(lambda x: not (0 < abs(x) < 4), deltas)):
        return False
    # now check for monotonicity
    return abs(sum(x for x in map(lambda x: x // abs(x), deltas))) == len(deltas)


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    print(sum(process(line.strip()) for line in f))
