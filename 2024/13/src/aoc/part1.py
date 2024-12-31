"""
Advent of Code Part 1
"""

from typing import TextIO

from pulp import PULP_CBC_CMD, LpProblem, LpVariable, value
from pulp.constants import LpInteger, LpMinimize, LpStatusOptimal
from rich.progress import track


def solve(x1: int, y1: int, x2: int, y2: int, goal_x: int, goal_y: int) -> int:
    a = LpVariable("a", 0, 100, cat=LpInteger)
    b = LpVariable("b", 0, 100, cat=LpInteger)
    prob: LpProblem = LpProblem("tosolve", LpMinimize)
    prob += x1 * a + x2 * b == goal_x  # constraint
    prob += y1 * a + y2 * b == goal_y  # constraint
    prob += a + b  # objective function

    status = prob.solve(PULP_CBC_CMD(msg=False))
    if status == LpStatusOptimal:
        return 3 * value(a) + value(b)

    return 0


def main(f: TextIO) -> None:
    """
    Solution to part 1
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

        problems.append([x1, y1, x2, y2, goal_x, goal_y])

        try:
            next(f)  # blank
        except StopIteration:
            break

    total = sum(solve(*p) for p in track(problems))
    print(f"Final total -> {total}")
