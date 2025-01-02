"""
Advent of Code Part 1
"""

from typing import TextIO

DIRECTIONS = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    # warehouse
    walls = set()
    boxes = set()
    y = 0
    robot = None
    for line in f:
        if not line.strip():
            break
        for x, cell in enumerate(line.strip()):
            if cell == "@":
                robot = (x, y)
            elif cell == "#":
                walls.add((x, y))
            elif cell == "O":
                boxes.add((x, y))
        y += 1

    print(f"Walls: {walls}")
    print(f"Boxes: {boxes}")
    print(f"Robot: {robot}")

    maxx = max(c[0] for c in walls) + 1
    maxy = max(c[1] for c in walls) + 1

    # robot orders
    orders = "".join(line.strip() for line in f)
    print(f"Orders: {orders}")

    def display():
        for y in range(maxy):
            line = ""
            for x in range(maxx):
                coord = (x, y)
                if coord in walls:
                    line += "#"
                elif coord in boxes:
                    line += "O"
                elif coord == robot:
                    line += "@"
                else:
                    line += "."
            print(line)

    def move_box(box_coord, direction) -> bool:
        bx, by = DIRECTIONS[direction]
        new_box_coord = (bx + box_coord[0], by + box_coord[1])
        if new_box_coord in walls:
            return False  # nope, can't do it
        if new_box_coord in boxes:
            # maybe, but only if we can also move that other box too
            if not move_box(new_box_coord, direction):
                return False

        # remove the box
        boxes.remove(box_coord)
        boxes.add(new_box_coord)
        return True

    for order in orders:
        dx, dy = DIRECTIONS[order]
        new_coord = (dx + robot[0], dy + robot[1])
        # print(f"Robot is at {robot}; checking {new_coord} | {order}")

        if new_coord in walls:
            # print(f"Wall at {new_coord}")
            continue  # nop; skip
        if new_coord in boxes:
            if move_box(new_coord, order):
                robot = new_coord
            continue

        # empty, so move there
        # print(f"Move to -> {new_coord}")
        robot = new_coord

    display()
    total = sum(b[0] + 100 * b[1] for b in boxes)
    print(f"Total -> {total}")
