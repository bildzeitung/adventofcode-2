"""
Advent of Code Part 2
"""

from itertools import combinations
from typing import TextIO


def process(line: str) -> int:
    r =  max(int(''.join(r)) for r in combinations(line, 12))
    print(f"Got: {r}")
    return r

def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    results = [process(x.strip()) for x in f]
    print(f"Results: {results} | {sum(results)}")
