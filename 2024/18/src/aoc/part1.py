"""
Advent of Code Part 1
"""

import heapq
from typing import Dict, Set, TextIO, Tuple

from attrs import define, field

DIRECTIONS = [
    (1, 0),  # East
    (0, 1),  # South
    (-1, 0),  # West
    (0, -1),  # North
]

MAZE_LIMIT = (70, 70)


@define()
class Node:
    """For the sake of equality, only position and
    direction are considered
    """

    position: Tuple[int, int]
    g: int = field(eq=False)
    h: int = field(eq=False)
    parent: "Node" = field(eq=False, default=None)
    valid: bool = field(eq=False, default=True)

    @property
    def f(self) -> int:
        """Total score; used as priority in the queue"""
        return self.g + self.h

    def __lt__(self, a: "Node"):
        return self.f < a.f


def printWinner(n: Node):
    count = 0
    while n.parent:
        count += 1
        n = n.parent
    print(f"Path length: {count}")


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    blocks = [(x, y) for x, y in [map(int, line.strip().split(",")) for line in f]]
    print(f"Have {len(blocks)} blocks")

    # apply 1024 blocks only
    puzzle = set(blocks[0:1024])
    print(f"Puzzle has {len(puzzle)} blocks")

    # solve maze
    start = (0, 0)
    finish = MAZE_LIMIT

    # A*
    def h(pos: Tuple[int, int]) -> int:
        return abs(finish[0] - pos[0]) + abs(finish[1] - pos[1])

    pqueue = []  # priority queue
    closed: Set[Tuple[int, int]] = set()
    all_open_pos: Dict[Tuple[int, int], Node] = {}

    # init
    start_node = Node(start, 0, 0)
    heapq.heappush(pqueue, start_node)
    all_open_pos[start_node.position] = start_node
    while pqueue:
        current: Node = heapq.heappop(pqueue)

        if not current.valid:
            continue  # skip invalidated nodes

        if current.position in closed:
            continue

        if current.position == finish:
            # print(f"We have a winner: {current}")
            printWinner(current)
            break

        del all_open_pos[current.position]
        closed.add(current.position)

        # child: move in any direction
        for d in DIRECTIONS:
            x, y = current.position
            new_pos = (x + d[0], y + d[1])
            # roll off left and top
            if new_pos[0] < 0 or new_pos[1] < 0:
                continue
            # roll off left and bottom
            if new_pos[0] > MAZE_LIMIT[0] or new_pos[1] > MAZE_LIMIT[1]:
                continue
            # hit wall
            if new_pos in puzzle:
                continue

            new_node = Node(new_pos, current.g + 1, h(new_pos), current)
            try:
                existing_node = all_open_pos[new_node.position]
                if existing_node.valid and new_node.g < existing_node.g:
                    existing_node.valid = False
            except KeyError:
                pass

            heapq.heappush(pqueue, new_node)
            all_open_pos[new_node.position] = new_node
