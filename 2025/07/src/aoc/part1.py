"""
Advent of Code Part 1
"""

import re
from typing import TextIO

from rich import print


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    beams: set[int] = set()
    puzzle: list[str] = []
    for line in f:
        line = line.strip()
        if "S" in line:
            beams.add(line.index("S"))
            continue

        if "^" not in line:
            continue

        puzzle.append(line)

    print(puzzle)
    print(f"Start: {beams}")
    splits: int = 0
    for i in puzzle:
        for splitter in re.finditer(r"\^", i):
            pos = splitter.span()[0]
            if pos in beams:
                beams.add(pos - 1)
                beams.add(pos + 1)
                beams.remove(pos)
                splits += 1
        print(f"Beams: {beams} | Splits: {splits}")
