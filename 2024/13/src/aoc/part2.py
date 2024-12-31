"""
Advent of Code Part 2

nb. z3 is more able to cope with the massive 10 billion scaling, avoiding
    any sort of closed form analytical solution that is probably more
    appropriate for this problem.

"""

from typing import TextIO

from rich.progress import track
from z3 import Z3_L_TRUE, Int, Optimize


def dmk_solve(x1: int, y1: int, x2: int, y2: int, goal_x: int, goal_y: int) -> int:
    a = Int("a")
    b = Int("b")
    opt = Optimize()
    opt.add(x1 * a + x2 * b == goal_x)
    opt.add(y1 * a + y2 * b == goal_y)
    opt.minimize(3 * a + b)
    if opt.check().r == Z3_L_TRUE:
        m = opt.model()
        return m.eval(3 * a + b).as_long()

    return 0


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    problems = []
    while True:
        # button A
        x1, y1 = map(
            int,
            next(f)
            .strip()
            .split(":")[1]
            .replace("X", "")
            .replace("Y", "")
            .replace("+", "")
            .replace(" ", "")
            .split(","),
        )
        # button B
        x2, y2 = map(
            int,
            next(f)
            .strip()
            .split(":")[1]
            .replace("X", "")
            .replace("Y", "")
            .replace("+", "")
            .replace(" ", "")
            .split(","),
        )
        # prize
        goal_x, goal_y = map(
            int,
            next(f)
            .strip()
            .split(":")[1]
            .replace("X", "")
            .replace("Y", "")
            .replace("=", "")
            .replace(" ", "")
            .split(","),
        )

        problems.append([x1, y1, x2, y2, goal_x + 10_000_000_000_000, goal_y + 10_000_000_000_000])

        try:
            next(f)  # blank
        except StopIteration:
            break

    total = sum(dmk_solve(*p) for p in track(problems))
    print(f"Final total -> {total}")
