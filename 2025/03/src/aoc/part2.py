"""
Advent of Code Part 2
"""

from typing import TextIO


def get_highest_leftmost(line: str, need_right: int) -> tuple[str, str]:
    """Get the highest, leftmost digit

    The largest digit in [0, 9] is always going to be the largest number.
    So, find the biggest one that leaves enough string so that all the rest
    can be found.

    Return the digit, but also return the remaining part of the string after
    that digit.
    """
    for i in [str(i) for i in range(9, 0, -1)]:
        if i in line and len(line) - line.index(i) >= need_right:
            return i, line[line.index(i) + 1 :]

    return "0", line[line.index("0") + 1 :]


def process(line: str) -> int:
    rv = ""
    to_place: int = 12
    while to_place:
        digit, line = get_highest_leftmost(line, to_place)
        rv += digit
        to_place -= 1
    return int(rv)


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    results: list[int] = [process(x.strip()) for x in f]
    print(f"Results: {results} | {sum(results)}")
