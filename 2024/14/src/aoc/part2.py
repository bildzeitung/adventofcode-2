"""
Advent of Code Part 2
"""

from typing import TextIO

from attrs import asdict, define
from rich.progress import track


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


def display(robots, tall, width, iteration=0) -> None:
    # display the robots
    line = f"Iteration -> {iteration}"
    coords = set((p.x, p.y) for p in robots)
    for y in range(tall):
        for x in range(width):
            if (x, y) in coords:
                line += "X"
            else:
                line += "."
        line += "\n"
    print(line)


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    width = 101
    tall = 103
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

    q1_maxx = width // 2
    q1_maxy = tall // 2

    def score(robots):
        q1 = list(filter(lambda r: r.x < q1_maxx and r.y < q1_maxy, robots))
        q2 = list(filter(lambda r: r.x > q1_maxx and r.y < q1_maxy, robots))
        q3 = list(filter(lambda r: r.x < q1_maxx and r.y > q1_maxy, robots))
        q4 = list(filter(lambda r: r.x > q1_maxx and r.y > q1_maxy, robots))
        return len(q1) * len(q2) * len(q3) * len(q4)

    new_robots = [Robot(**asdict(r)) for r in robots]
    scores = {
        i: score(new_robots := [r.sim(1) for r in new_robots]) for i in track(range(width * tall))
    }
    # print(f"Min: {min(scores.values())}  Max: {max(scores.values())}")
    min_index = sorted(scores, key=lambda x: scores[x])[0]
    max_index = sorted(scores, key=lambda x: scores[x])[-1]
    print(f"{min_index} -> {scores[min_index]}")
    print(f"{max_index} -> {scores[max_index]}")

    # full confession -- this is a WAG based on the minimal scores found
    # in the bit above. Fortunately, manual inspection resulted in finding
    # the required tree picture but .. still ..
    iteration = min_index + 1
    while iteration > 7000:
        maybe_tree = [r.sim(iteration) for r in robots]
        display(maybe_tree, tall, width, iteration)
        # print(score(maybe_tree))
        iteration -= 101
