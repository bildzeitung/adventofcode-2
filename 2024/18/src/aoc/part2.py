"""
Advent of Code Part 2
"""

import heapq
from typing import Dict, Set, TextIO, Tuple, TypeAlias

from attrs import define, field

COORD: TypeAlias = Tuple[int, int]

DIRECTIONS = [
    (1, 0),  # East
    (0, 1),  # South
    (-1, 0),  # West
    (0, -1),  # North
]

MAZE_LIMIT = (70, 70)


@define()
class Node:
    """For the sake of equality, only position is considered"""

    position: COORD
    g: int = field(eq=False)
    h: int = field(eq=False)
    valid: bool = field(eq=False, default=True)

    @property
    def f(self) -> int:
        """Total score; used as priority in the queue"""
        return self.g + self.h

    def __lt__(self, a: "Node"):
        return self.f < a.f


def h(pos: COORD) -> int:
    """Manhattan distance"""
    return abs(MAZE_LIMIT[0] - pos[0]) + abs(MAZE_LIMIT[1] - pos[1])


def solve(puzzle: Set[COORD]) -> bool:
    """Returns True if the maze has a solution, False otherwise"""
    start = (0, 0)

    # A*
    pqueue = []  # priority queue
    closed: Set[COORD] = set()
    all_open_pos: Dict[COORD, Node] = {}

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

        if current.position == MAZE_LIMIT:
            return True

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

            new_node = Node(new_pos, current.g + 1, h(new_pos))
            try:
                existing_node = all_open_pos[new_node.position]
                if existing_node.valid and new_node.g < existing_node.g:
                    existing_node.valid = False
            except KeyError:
                pass

            heapq.heappush(pqueue, new_node)
            all_open_pos[new_node.position] = new_node

    return False  # no solution


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    blocks = [(x, y) for x, y in [map(int, line.strip().split(",")) for line in f]]
    print(f"Have {len(blocks)} blocks")

    # 1024 has a solution; need to find max number with a valid solution
    # a binary search will do nicely
    rhs = len(blocks)
    delta = len(blocks) // 2
    while delta > 0:  # while both markers haven't met
        puzzle = set(blocks[0:rhs])
        rv = solve(puzzle)
        print(f"RHS == {rhs}  DELTA == {delta} --> {rv}")
        if rv:
            # True, so need a bigger value
            rhs += delta
        else:
            # False, so need to bring in the value
            rhs -= delta
        delta //= 2

    # ok, so see how this works
    print("Ok .. search complete ..")
    print(f"RHS == {rhs-1} --> {solve(blocks[0:rhs-1])}")
    print(f"RHS == {rhs} --> {solve(blocks[0:rhs])} --> {blocks[rhs-1]}")
    print(f"RHS == {rhs+1} --> {solve(blocks[0:rhs+1])}")
