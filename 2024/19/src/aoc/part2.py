"""
Advent of Code Part 2
"""

from functools import cache
from typing import TextIO

from rich.progress import track

max_lookup_size: int
lookup_towels: dict[int, set[str]] = {}


@cache
def solve(to_find: str) -> int:
    """Return True if to_find can be made of available; False otherwise

    Use a recursive depth-first search by longest prefix
    """
    global max_lookup_size
    global lookup_towels

    # if nothing to match, then yay!
    if not to_find:
        return 1

    total = 0
    for i in reversed(range(1, min(max_lookup_size, len(to_find)) + 1)):
        if to_find[:i] in lookup_towels[i]:
            total += solve(to_find[i:])

    return total


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    global max_lookup_size
    global lookup_towels
    available_towels = next(f).strip().replace(" ", "").split(",")

    # let's order them by length
    for towel in available_towels:
        towel_length = len(towel)
        if towel_length not in lookup_towels:
            lookup_towels[towel_length] = set()
        lookup_towels[towel_length].add(towel)
    # print(lookup_towels)
    max_lookup_size = max(lookup_towels)
    # print(f"Largest match: {max_lookup_size}")

    next(f)  # blank

    all_lines = [line.strip() for line in f]
    # for line in all_lines:
    #    print(f"{line} -> {solve(line)}")
    total = sum(solve(line) for line in track(all_lines))
    print(f"Total: {total}")
