"""
Advent of Code Part 2
"""

import re
from math import prod
from typing import Generator, TextIO

# need to find: mul(2,4) | do() | don't()
FINDER = re.compile(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))")


def process(x: str) -> int:
    return prod(map(int, x.replace("mul(", "").replace(")", "").split(",")))


def tokenize(f: TextIO) -> Generator[str]:
    """Generate match tokens from the file"""
    for line in f:
        for m in FINDER.findall(line.strip()):
            yield m


def main(f: TextIO) -> None:
    """
    Solution to part 2

    """
    total = 0
    enabled = True
    for x in tokenize(f):
        if x[0] and enabled:
            total += process(x[0])
        elif x[1]:
            enabled = True
        else:
            enabled = False
    print(total)
