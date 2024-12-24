"""
Advent of Code Part 1
"""

import re
from math import prod
from typing import TextIO


def process(x: str) -> int:
    print(x)
    return prod(map(int, x.replace("mul(", "").replace(")", "").split(",")))


def main(f: TextIO) -> None:
    """
    Solution to part 1

    need to find: mul(2,4)
    """
    exp = r"mul\(\d+,\d+\)"
    total = sum(sum(process(x) for x in re.findall(exp, line.strip())) for line in f)
    print(total)
