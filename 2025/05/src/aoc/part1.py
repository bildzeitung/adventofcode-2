"""
Advent of Code Part 1
"""

from typing import TextIO

from rich import print


def check(ranges, item) -> bool:
    for r in ranges:
        if r[0] <= item <= r[1]:
            return True
    return False


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    all_ranges = []
    for line in f:
        if not line.strip():
            break
        start, stop = [int(x) for x in line.strip().split("-")]
        all_ranges.append((start, stop))

    # to check
    def check_item(item: int) -> bool:
        return check(all_ranges, item)

    to_check = [int(line.strip()) for line in f]
    results = [x for x in filter(check_item, to_check)]
    print(f"{results} | {len(results)}")
