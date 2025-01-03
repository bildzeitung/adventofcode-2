"""
Advent of Code Part 2
"""

from itertools import chain
from typing import List, Set, TextIO, Tuple

from attrs import frozen

DIRECTIONS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


@frozen
class Box:
    front: Tuple[int, int]
    back: Tuple[int, int]

    def has_coord(self, c) -> bool:
        return c == self.front or c == self.back


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    # warehouse
    walls = set()
    boxes: Set[Box] = set()
    y = 0
    robot = None
    for line in f:
        if not line.strip():
            break
        x = 0
        for cell in line.strip():
            if cell == "@":
                robot = (x, y)
            elif cell == "#":
                walls.add((x, y))
                walls.add((x + 1, y))
            elif cell == "O":
                boxes.add(Box((x, y), (x + 1, y)))
            x += 2
        y += 1

    print(f"Boxes: {len(boxes)} | {boxes}")
    initial_number_of_boxes = len(boxes)

    maxx = max(c[0] for c in walls) + 1
    maxy = max(c[1] for c in walls) + 1

    # robot orders
    orders = "".join(line.strip() for line in f)
    print(f"Orders: {orders}")

    def all_box_fronts():
        return set(b.front for b in boxes)

    def get_box_from_coords(coord: Tuple[int, int]) -> Box | None:
        for b in boxes:
            if b.has_coord(coord):
                return b
        return None

    def get_box_from_box(box: Box, old_box: Box) -> List[Box] | None:
        return list(
            filter(
                lambda x: (x.has_coord(box.front) or x.has_coord(box.back)) and x != old_box, boxes
            )
        )

    def display():
        for y in range(maxy):
            line = ""
            x = 0
            while x < maxx:
                coord = (x, y)
                if coord in walls:
                    line += "#"
                elif coord in all_box_fronts():
                    line += "[]"
                    x += 1
                elif coord == robot:
                    line += "@"
                else:
                    line += "."
                x += 1
            print(line)
        print()

    def move_box(box: Box, direction) -> None | List[Tuple[Box, Box]]:
        bx, by = DIRECTIONS[direction]
        new_front = (box.front[0] + bx, box.front[1] + by)
        new_back = (box.back[0] + bx, box.back[1] + by)

        if new_front in walls or new_back in walls:
            return None  # nope, can't do it

        new_box = Box(front=new_front, back=new_back)
        another_box = get_box_from_box(new_box, box)
        assert len(another_box) < 3
        rv = []
        if another_box:
            # maybe, but only if we can also move all of the other boxes too
            rv = [move_box(z, direction) for z in another_box]
            if None in rv:
                for r in filter(lambda x: x is not None, rv):  # rollback
                    # print(f"Rollback .. {rv}")
                    to_remove = set(s[1] for s in r)
                    to_add = set(s[0] for s in r)
                    assert len(to_remove) == len(to_add)
                    for r in to_remove:
                        boxes.remove(r)
                    for r in to_add:
                        boxes.add(r)
                return None

        # move the box
        boxes.remove(box)
        boxes.add(new_box)

        # return a list of everything that would need to rollback
        return list(chain.from_iterable(rv)) + [(box, new_box)]

    display()

    for order in orders:
        dx, dy = DIRECTIONS[order]
        new_coord = (dx + robot[0], dy + robot[1])
        # print(f"Robot is at {robot}; checking {new_coord} | {order}")

        if new_coord in walls:
            continue  # nop; skip
        if new_box := get_box_from_coords(new_coord):
            if not move_box(new_box, order):
                continue

        # empty, so move there
        robot = new_coord
        # display()

    display()
    total = sum(100 * b.front[1] + b.front[0] for b in boxes)
    print(f"Number of boxes: {len(boxes)}")
    assert initial_number_of_boxes == len(boxes)
    print(f"Total -> {total}")
