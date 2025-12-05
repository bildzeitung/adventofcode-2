"""
Advent of Code Part 2
"""

from typing import Set, TextIO, Tuple

type Point = Tuple[int, int]


def evaluate(points: Set[Point], point: Point) -> bool:
    x, y = point
    return sum((xx, yy) in points for yy in range(y - 1, y + 2) for xx in range(x - 1, x + 2)) < 5


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    points = set()
    y: int = 0
    for line in f:
        for x, c in enumerate(line.strip()):
            if c == "@":
                points.add((x, y))
        y += 1

    def func(p: Point) -> bool:  # gotta love a partial
        return evaluate(points, p)

    grand_total: int = 0
    while True:
        results = [i for i in filter(func, points)]

        if not results:  # no more to do
            break
        grand_total += len(results)
        points -= set(results)
    print(f"Grand total: {grand_total}")
