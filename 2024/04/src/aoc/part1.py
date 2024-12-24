"""
Advent of Code Part 1
"""

from typing import Dict, TextIO

DELTAS = [
    (0, 1),  # down
    (0, -1),  # up
    (1, 0),  # right
    (-1, 0),  # left
    (1, 1),  # down right
    (-1, 1),  # down left
    (1, -1),  # up right
    (-1, -1),  # up left
]


def check_deltas(puzzle: Dict[tuple, str], i: tuple) -> bool:
    """Look for XMAS"""
    total = 0
    ix, iy = i
    for d in DELTAS:
        dx, dy = d
        s = ""
        for i in range(4):
            try:
                s += puzzle[dx * i + ix, dy * i + iy]
            except KeyError:
                pass
        total += s == "XMAS"
    return total


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    puzzle = {}
    y = 0
    for line in f:
        line = line.strip()
        for x, c in enumerate(line):
            puzzle[(x, y)] = c
        y += 1

    total = sum(check_deltas(puzzle, i) for i, j in filter(lambda x: x[1] == "X", puzzle.items()))
    print(f"Total: {total}")
