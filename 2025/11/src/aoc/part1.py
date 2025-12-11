"""
Advent of Code Part 1
"""

from collections import deque
from typing import TextIO

from rich import print


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    puzzle: dict[str, list[str]] = {}
    for line in f:
        a, b = line.strip().split(":")
        puzzle[a] = b.strip().split(" ")

    # start at 'you'
    q = deque(puzzle["you"])
    totalPaths = 0
    while q:
        # print(q)
        node = q.popleft()
        if node == "out":
            totalPaths += 1
            continue
        q.extend(puzzle[node])

    print(totalPaths)
