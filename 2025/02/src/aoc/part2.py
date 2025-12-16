"""
Advent of Code Part 2
"""

from typing import TextIO

from rich.progress import track


def gen_all_possible() -> set[int]:
    """
    Generate all possible bad IDs

    The max length in the input is 10 digits.

    Maybe it's easier to just generate all of the bad IDs and then filter
    for the ones in a given range.
    """
    rv: set[int] = set()
    # repeating single digits
    for i in range(2, 10 + 1):
        for j in range(1, 9 + 1):
            rv.add(int(str(j) * i))
    # repeating pairs
    for i in range(10, 99 + 1):
        rv.add(int(str(i) * 2))  # "aa|aa"
        rv.add(int(str(i) * 3))  # "aa|aa|aa"
        rv.add(int(str(i) * 4))  # "aa|aa|aa|aa"
        rv.add(int(str(i) * 5))  # "aa|aa|aa|aa|aa"
    # repeating triples
    for i in range(100, 999 + 1):
        rv.add(int(str(i) * 2))  # "aaa|aaa"
        rv.add(int(str(i) * 3))  # "aaa|aaa|aaa"
    # repeating quads
    for i in range(1000, 9999 + 1):
        rv.add(int(str(i) * 2))
    # repeating quints
    for i in range(10000, 99999 + 1):
        rv.add(int(str(i) * 2))
    return rv


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    ranges: list[list[int]] = [[int(y) for y in x.split("-")] for x in next(f).strip().split(",")]
    results: list[int] = []

    all_possible = sorted(gen_all_possible())
    print(f"There are {len(all_possible)} invalid IDs")

    for item in track(ranges):
        low, high = item
        results.extend(filter(lambda x: low <= x <= high, all_possible))

    print(f"Results: {results}")
    print(f"Final: {sum(results)}")
