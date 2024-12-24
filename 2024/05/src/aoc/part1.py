"""
Advent of Code Part 1
"""

from typing import List, TextIO, Tuple


def process(rules: List[Tuple[int, int]], update: List[int]) -> bool:
    """Returns True if the update is correctly ordered"""
    return all(
        update.index(rule[0]) < update.index(rule[1])
        for rule in filter(lambda x: x[0] in update and x[1] in update, rules)
    )


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    rules = []
    for line in f:
        if not line.strip():
            break
        rules.append(tuple(map(int, line.strip().split("|"))))

    to_check = [list(map(int, line.strip().split(","))) for line in f]

    print(sum(check[len(check) // 2] for check in to_check if process(rules, check)))
