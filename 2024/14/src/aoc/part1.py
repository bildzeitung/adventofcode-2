"""
Advent of Code Part 1
"""

from typing import TextIO

from attrs import define
from rich import print


@define
class Robot:
    x: int
    y: int
    dx: int
    dy: int
    width: int
    tall: int

    def sim(self, rounds: int) -> "Robot":
        x = (self.x + self.dx * rounds) % self.width
        y = (self.y + self.dy * rounds) % self.tall
        return Robot(x, y, self.dx, self.dy, width=self.width, tall=self.tall)


def main(f: TextIO, width: int, tall: int) -> None:
    """
    Solution to part 1
    """
    robots = [
        Robot(
            *map(
                int,
                line.strip()
                .replace("=", "")
                .replace("p", "")
                .replace("v", "")
                .replace(" ", ",")
                .split(","),
            ),
            width=width,
            tall=tall,
        )
        for line in f
    ]
    # print(robots)

    """
     +----+----+
     | Q1 | Q2 |
     +----+----+
     | Q3 | Q4 |
     +----+----+
    """
    new_robots = [r.sim(100) for r in robots]
    q1_maxx = width // 2
    q1_maxy = tall // 2

    q1 = list(filter(lambda r: r.x < q1_maxx and r.y < q1_maxy, new_robots))
    print(f"Q1: {q1}")
    q2 = list(filter(lambda r: r.x > q1_maxx and r.y < q1_maxy, new_robots))
    print(f"Q2: {q2}")
    q3 = list(filter(lambda r: r.x < q1_maxx and r.y > q1_maxy, new_robots))
    print(f"Q3: {q3}")
    q4 = list(filter(lambda r: r.x > q1_maxx and r.y > q1_maxy, new_robots))
    print(f"Q4: {q4}")

    print(f"Total --> {len(q1) * len(q2) * len(q3) * len(q4)}")
