"""
Advent of Code Part 2
"""

from typing import Dict, TextIO

"""
These are all the possible cases:

    M.S
    .A.
    M.S

    S.S
    .A.
    M.M

    M.M
    .A.
    S.S

    S.M
    .A.
    S.M
"""
EXES = (
    "MSMS",
    "SSMM",
    "MMSS",
    "SMSM",
)


def check_deltas(puzzle: Dict[tuple, str], i: tuple) -> bool:
    """Look for diagonals"""
    x, y = i
    to_check = (
        puzzle[(x - 1, y - 1)]
        + puzzle[(x + 1, y - 1)]
        + puzzle[(x - 1, y + 1)]
        + puzzle[(x + 1, y + 1)]
    )
    return to_check in EXES


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    puzzle = {}
    y = 0
    for line in f:
        line = line.strip()
        for x, c in enumerate(line):
            puzzle[(x, y)] = c
        y += 1

    y -= 1  # adjust for last increment

    total = 0
    for i, j in filter(
        # look for center "A" and exclude edges
        lambda z: z[1] == "A" and z[0][0] > 0 and z[0][1] > 0 and z[0][1] < y and z[0][0] < x,
        puzzle.items(),
    ):
        r = check_deltas(puzzle, i)
        print(i, j, r)
        total += r
    print(f"Total: {total}")
