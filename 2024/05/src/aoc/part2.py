"""
Advent of Code Part 2
"""

from functools import cmp_to_key
from typing import List, TextIO, Tuple


def process(rules: List[Tuple[int, int]], update: List[int]) -> bool:
    """Returns True if the update is incorrectly ordered"""
    return not all(
        update.index(rule[0]) < update.index(rule[1])
        for rule in filter(lambda x: x[0] in update and x[1] in update, rules)
    )


def fix(rules: List[Tuple[int, int]], update: List[int]) -> int:
    applicable_rules = list(filter(lambda x: x[0] in update and x[1] in update, rules))

    def cmp(x, y):
        if (x, y) in applicable_rules:
            return -1

        if (y, x) in applicable_rules:
            return 1

        return 0

    s = sorted(update, key=cmp_to_key(cmp))
    return s[len(s) // 2]


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    rules = []
    for line in f:
        if not line.strip():
            break
        rules.append(tuple(map(int, line.strip().split("|"))))

    to_check = [list(map(int, line.strip().split(","))) for line in f]
    to_fix = filter(lambda x: process(rules, x), to_check)

    print(sum(fix(rules, f) for f in to_fix))
