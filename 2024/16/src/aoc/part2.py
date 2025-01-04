"""
Advent of Code Part 2
"""

import heapq
from typing import TextIO, Tuple, Set

from attrs import define, field

DIRECTIONS = [
    (1, 0),  # East
    (0, 1),  # South
    (-1, 0),  # West
    (0, -1),  # North
]


@define(frozen=True)
class Node:
    """For the sake of equality, only position and
    direction are considered
    """

    position: Tuple[int, int]
    direction: int
    g: int = field(eq=False)
    h: int = field(eq=False)
    parent : "Node" = field(eq=False, default=None)

    @property
    def f(self) -> int:
        """Total score; used as priority in the queue"""
        return self.g + self.h

    def __lt__(self, a: "Node"):
        return self.f < a.f

    @property
    def next_position(self) -> Tuple[int, int]:
        x, y = self.position
        dx, dy = DIRECTIONS[self.direction]
        return (x + dx, y + dy)


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    y = 0
    walls = set()
    start = None
    finish = None
    for line in f:
        for x, c in enumerate(line.strip()):
            if c == "#":
                walls.add((x, y))
            elif c == "S":
                start = (x, y)
            elif c == "E":
                finish = (x, y)
        y += 1

    print(f"Maze is {start} -> {finish}")

    def h(pos: Tuple[int, int]) -> int:
        """Manhattan distance to end
        This is admissible b/c this function is either the
        exact number of future steps (in the linear case), or
        less than that (because turns are expensive)
        """
        return abs(finish[0] - pos[0]) + abs(finish[1] - pos[1])

    score_of_best_path = 0
    pqueue = []  # priority queue
    closed = set()
    heapq.heappush(pqueue, Node(start, 0, 0, 0, 0))
    parts_of_best_path : Set[Tuple[int,int]]= set()
    while pqueue:
        current: Node = heapq.heappop(pqueue)
        # print(f"Considering: {current}")
        if current in closed:
            continue

        closed.add(current)

        if current.position == finish:
            #print(f"We have a winner: {current}")
            print("We have a winner")
            if not score_of_best_path:
                score_of_best_path = current.g
            else:
                if current.g > score_of_best_path:
                    print(f"No more best paths ({current.g} > {score_of_best_path})")
                    break
            tracer = current
            while tracer:
                parts_of_best_path.add(tracer.position)
                tracer = tracer.parent
            print(f"So far {len(parts_of_best_path)} tiles are recorded")
            continue

        # child: move along current direction
        new_pos = current.next_position
        if new_pos not in walls:
            heapq.heappush(pqueue, Node(new_pos, current.direction, current.g + 1, h(new_pos), current))

        # child: turn clockwise
        heapq.heappush(
            pqueue,
            Node(
                current.position,
                (current.direction + 1) % len(DIRECTIONS),
                current.g + 1000,
                h(current.position),
                current,
            ),
        )

        # child: turn counter-clockwise
        heapq.heappush(
            pqueue,
            Node(
                current.position,
                (current.direction + len(DIRECTIONS) - 1) % len(DIRECTIONS),
                current.g + 1000,
                h(current.position),
                current,
            ),
        )

    print(f"There are {len(parts_of_best_path)} tiles")