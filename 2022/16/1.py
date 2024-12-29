#!/usr/bin/env python
"""
    Day 11
"""
import sys
from pathlib import Path
from rich import print


def main():
    maze = {}
    valves = {}
    rejects = set()
    with Path(sys.argv[1]).open() as f:
        for line in f:
            tunnel, connections = (
                line.replace("Valve ", "")
                .replace("has flow rate=", "")
                .replace(" tunnels lead to valves ", "")
                .replace(" tunnel leads to valve ", "")
                .strip()
                .split(";")
            )
            valve, fr = tunnel.split(" ")

            # if you don't contribute, you don't play
            #if not int(fr) and valve != "AA":
            #    rejects.add(valve)
            #    continue

            valves[valve] = int(fr)
            maze[valve] = [x.strip() for x in connections.split(",")]

    # now, finish pruning
    """
    to_del = set()
    for k, v in maze.items():
        maze[k] = [x for x in v if x not in rejects]
        if not maze[k]:
            to_del.add(k)

    for i in to_del:
        del maze[i]
    """
    print(valves)
    print(maze)
    #print(rejects)

    pos = "AA"
    total_flow = 0
    for _ in range(30):
        pass
    print(f"Total: {total_flow}")


if __name__ == "__main__":
    main()
