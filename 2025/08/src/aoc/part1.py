"""
Advent of Code Part 1
"""

from itertools import combinations
from math import prod
from typing import TextIO

import networkx as nx
from rich import print
from rich.progress import track


def main(f: TextIO) -> None:
    """
    Solution to part 1
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
    for i in range(1000):
        a, b = reverse_index[idx[i]]
        G.add_edge(a, b)

    # grab the 3 largest connected components
    i = sorted(nx.connected_components(G), key=len, reverse=True)[0:3]
    print(f"Total: {prod(len(x) for x in i)}")
