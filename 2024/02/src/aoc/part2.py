"""
Advent of Code Part 2
"""

from typing import TextIO


def process(items: list[int]) -> bool:
    deltas = [x[0] - x[1] for x in zip(items, items[1:])]
    # if any of the deltas are > 3 or 0
    if sum(x for x in map(lambda x: not (0 < abs(x) < 4), deltas)):
        return False
    # now check for monotonicity
    return abs(sum(x for x in map(lambda x: x // abs(x), deltas))) == len(deltas)


def redo(items: list[int]) -> bool:
    """drop items one at a time to see if it gets better"""

    for i in range(len(items)):
        if process(items[0 : i] + items[i + 1 : len(items)]):
            return True

    return False


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    r = []
    for line in f:
        items = [x for x in map(int, line.strip().split())]
        r.append(process(items) or redo(items))

    print(sum(r))
