"""
Advent of Code Part 1
"""

from collections import defaultdict
from itertools import combinations
from typing import Dict, List, Set, TextIO, Tuple

from rich import print


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    graph: Dict[str, List[str]] = defaultdict(list)
    edges: Set[Tuple[str, str]] = set()
    for line in f:
        a, b = line.strip().split("-")
        graph[a].append(b)
        graph[b].append(a)
        edges.add((a, b))
        edges.add((b, a))

    all_triples: Set[str] = set()
    starts_with_t = list(filter(lambda x: x.startswith("t"), graph))
    for i in starts_with_t:
        # get all the neighbours
        neighbours = graph[i]
        # how many combinations of those have edges?
        all_triples.update(
            "|".join(sorted([i, y[0], y[1]]))
            for y in filter(lambda x: (x[0], x[1]) in edges, combinations(neighbours, 2))
        )
        # all_triples.update(triples)
        # print(f"Item {i} has {triples} 3-graphs")

    print(f"All triples: {all_triples}")
    print(f"Number of triples: {len(all_triples)}")
