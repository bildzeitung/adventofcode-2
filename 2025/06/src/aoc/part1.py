"""
Advent of Code Part 1
"""

import re
from typing import TextIO


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    operands = []
    operators = []
    for line in f:
        items = re.split(r"\s+", line.strip())
        if items[0] in "+*":
            operators = items
            break
        else:
            items = [int(x) for x in items]
            operands.append(items)
    print(f"Operators: {operators}")
    print(f"Operands: {operands}")

    accumulator = operands[0]
    for items in operands[1:]:
        for idx, op in enumerate(operators):
            if op == "+":
                accumulator[idx] += items[idx]
            else:
                accumulator[idx] *= items[idx]
    print(f"Accumulator: {accumulator}")
    print(f"Total: {sum(accumulator)}")
