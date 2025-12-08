"""
Advent of Code Part 2
"""

from itertools import combinations
from typing import TextIO

import networkx as nx
from rich import print
from rich.progress import track


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    points: list[tuple[int, ...]] = [tuple(int(x) for x in line.strip().split(",")) for line in f]

    G = nx.Graph()
    G.add_nodes_from(points)

    # now we want the Euclidean distance between all points
    reverse_index: dict[int, tuple[tuple, tuple]] = {}
    for a, b in track(combinations(points, 2)):
        d = (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2
        reverse_index[d] = (a, b)

    # sort by smallest -> largest
    idx = sorted(reverse_index)

    # compose the graph!
    counter = 0
    lastOne = []
    while not nx.is_connected(G):
        a, b = reverse_index[idx[counter]]
        G.add_edge(a, b)
        counter += 1
        lastOne = [a, b]

    print(f"Connected after {counter}; {lastOne}; {lastOne[0][0] * lastOne[1][0]}")
