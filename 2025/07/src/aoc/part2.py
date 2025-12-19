"""
Advent of Code Part 2
"""

import re
from collections import Counter
from typing import TextIO

from rich import print


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    beams: Counter[int] = Counter()
    puzzle: list[str] = []
    for line in f:
        line = line.strip()
        if "S" in line:
            beams[line.index("S")] = 1
            continue

        if "^" not in line:
            continue

        puzzle.append(line)

    """ Can still go row by row, but keep a list of active beams and how many
        paths lead to them. At the end, that'll be the total number of possible
        ways the beam can go
    """
    print(f"Start: {beams}")
    for i in puzzle:
        print(f"Processing: {i}")
        splitters = set(x.span()[0] for x in re.finditer(r"\^", i))

        # breadth-first iteration
        current_beams = list(beams.keys())
        for b in current_beams:
            if b in splitters:
                beams[b - 1] += beams[b]
                beams[b + 1] += beams[b]
                del beams[b]  # no beams go here now; reset

        print(f"Beams: {beams} | Paths: {sum(beams.values())}")
