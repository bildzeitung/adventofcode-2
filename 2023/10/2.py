#!/usr/bin/env python
"""
    Day 9
"""
import sys
from pathlib import Path

maze = {}
dots = set()
maxx = -1
maxy = -1


def ppuzzle(maze):
    SINGLE_RIGHT_TOP = "\u2510"  # 7
    SINGLE_HORIZ_PIPE = "\u2500"  # -
    SINGLE_VERTI_PIPE = "\u2502"  # |
    SINGLE_LEFT_TOP = "\u250c"  # F
    SINGLE_RIGHT_BOTTOM = "\u2518"  # J
    SINGLE_LEFT_BOTTOM = "\u2514"  # L

    """ Pretty printing (because why not) """
    for y in range(maxy):
        o = ""
        for x in range(maxx):
            p = (x, y)
            if p in dots:
                o += "."
                continue
            if not p in maze:
                o += " "
                continue
            c = maze[(x, y)]
            if c == "7":
                o += SINGLE_RIGHT_TOP
            elif c == "-":
                o += SINGLE_HORIZ_PIPE
            elif c == "F":
                o += SINGLE_LEFT_TOP
            elif c == "|":
                o += SINGLE_VERTI_PIPE
            elif c == "J":
                o += SINGLE_RIGHT_BOTTOM
            elif c == "L":
                o += SINGLE_LEFT_BOTTOM
            else:
                o += c
        print(o)


def check_inbound(p):
    x, y = p
    c = list()
    # up |, F, 7
    if (x, y - 1) in maze and maze[(x, y - 1)] in ("|", "F", "7", "S"):
        c.append((x, y - 1))

    # left L, -, F
    if (x - 1, y) in maze and maze[(x - 1, y)] in ("-", "L", "F", "S"):
        c.append((x - 1, y))

    # right J, -, 7
    if (x + 1, y) in maze and maze[(x + 1, y)] in ("-", "J", "7", "S"):
        c.append((x + 1, y))

    # down J, |, L
    if (x, y + 1) in maze and maze[(x, y + 1)] in ("|", "L", "J", "S"):
        c.append((x, y + 1))
    assert len(c) == 2, f"{p} -> {c}"
    return c


def check_connection(p, previous):
    x, y = p
    pipe = maze[p]

    if pipe == "J":
        if (x - 1, y) in maze and (x - 1, y) != previous:  # west
            return (x - 1, y)
        if (x, y - 1) in maze and (x, y - 1) != previous:  # north
            return (x, y - 1)

    if pipe == "|":
        if (x, y - 1) in maze and (x, y - 1) != previous:  # north
            return (x, y - 1)
        if (x, y + 1) in maze and (x, y + 1) != previous:  # south
            return (x, y + 1)

    if pipe == "F":
        if (x, y + 1) in maze and (x, y + 1) != previous:  # south
            return (x, y + 1)
        if (x + 1, y) in maze and (x + 1, y) != previous:  # east
            return (x + 1, y)

    if pipe == "L":
        if (x, y - 1) in maze and (x, y - 1) != previous:  # north
            return (x, y - 1)
        if (x + 1, y) in maze and (x + 1, y) != previous:  # east
            return (x + 1, y)

    if pipe == "7":
        if (x, y + 1) in maze and (x, y + 1) != previous:  # south
            return (x, y + 1)
        if (x - 1, y) in maze and (x - 1, y) != previous:  # west
            return (x - 1, y)

    if pipe == "-":
        if (x - 1, y) in maze and (x - 1, y) != previous:  # west
            return (x - 1, y)
        if (x + 1, y) in maze and (x + 1, y) != previous:  # east
            return (x + 1, y)

    raise NotImplementedError()


def main():
    global maxx
    global maxy
    global dots

    start = None
    y = 0
    with Path(sys.argv[1]).open() as f:
        for line in f:
            x = 0
            for c in line.strip():
                if c == ".":
                    dots.add((x, y))
                    x += 1
                    continue
                if c == "S":
                    start = (x, y)
                maze[(x, y)] = c
                x += 1
            y += 1

    maxy = y
    maxx = len(line)

    assert len(check_inbound(start)) == 2

    # grab the perimeter
    in_maze = [start]
    current = [( check_inbound(start)[0], start)]
    in_maze.append(current[0][0])
    while current:
        item, previous = current.pop(0)
        i = check_connection(item, previous)
        if i == start:
            break
        current.append((i, item))
        in_maze.append(i)

    n = {i: maze[i] for i in in_maze}
    ppuzzle(n)
    print(f"Dots to check: {len(dots)}")

    for d in dots:
        pass


if __name__ == "__main__":
    print(main())
