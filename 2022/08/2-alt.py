#!/usr/bin/env python
"""
    Day 8
"""
import sys
from pathlib import Path
from rich import print
import numpy as np


def main():
    grid = []
    with Path(sys.argv[1]).open() as f:
        for line in f:
            grid.append([int(x) for x in line.strip()])
    grid = np.asarray(grid)

    # need columns, so save some grief by making a transposed one
    gridT = grid.transpose()

    lx = len(grid[0])
    ly = len(grid)

    def checklr(height, l) -> int:
        if not sum(l>=height):
            return len(l)

        return np.argmax(l >= height) + 1

    def check(y: int, x: int) -> int:
        height = grid[y][x]

        tl = checklr(height, grid[y][x - 1 :: -1])
        tr = checklr(height, grid[y][x + 1 :])

        tu = checklr(height, gridT[x][y - 1 :: -1])
        td = checklr(height, gridT[x][y + 1 :])

        #print(f"({x}, {y}) Height: {height} L: {tl} R: {tr} U: {tu} D: {td}")

        return tl * tr * tu * td

    max_view = -1
    for y in range(1, ly - 1):
        for x in range(1, lx - 1):
            c = check(y, x)
            if c > max_view:
                max_view = c
    print(f"Max: {max_view}")


if __name__ == "__main__":
    main()
