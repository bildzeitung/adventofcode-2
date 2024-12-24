"""
Advent of Code Part 2
"""

from collections import defaultdict
from typing import Dict, Set, TextIO, Tuple

from rich import print


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    graph: Dict[str, Set[str]] = defaultdict(set)
    edges: Set[Tuple[str, str]] = set()
    for line in f:
        a, b = line.strip().split("-")
        graph[a].add(b)
        graph[b].add(a)
        edges.add((a, b))
        edges.add((b, a))

    # about the data ..
    # - each node has the same number of neighbours
    # - can likely build up from 3-connected upwards
    #

    # loop through working set
    # grab the set intersection of neighbours of all members
    # add (a, b, x) where x is a member of the intersection set
    # repeat until it's an empty intersection set
    next_connected_set = set()
    connected_set = edges
    print(f"Starting number of edges: {len(connected_set)}")

    while True:
        for s in connected_set:
            common = set.intersection(*[graph[x] for x in s])
            for x in common:
                next_connected_set.add(tuple(sorted((*s, x))))

        if not next_connected_set:
            break
        connected_set = set(next_connected_set)
        next_connected_set = set()
        print(f"Connected set has {len(connected_set)} members")

    assert len(connected_set) == 1
    print(",".join(connected_set.pop()))
