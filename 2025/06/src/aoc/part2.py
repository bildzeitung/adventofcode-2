"""
Advent of Code Part 2
"""

import re
from collections import defaultdict
from math import prod
from typing import TextIO


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    operators = []
    operandStrings = defaultdict(str)
    for line in f:
        line = line.rstrip("\n")
        if "+" in line or "*" in line:
            operators = re.split(r"\s+", line.strip())
            break
        for idx, c in enumerate(line):
            operandStrings[idx] += c

    row = []
    operands = []
    for k, v in operandStrings.items():
        v = v.strip()
        # print(f"-> {k,v}")
        if v == "":
            operands.append(row)
            row = []
        else:
            row.append(int(v))
    operands.append(row)
    print(f"Operators: {operators}")
    print(f"Operands: {operands}")

    accumulator = []
    for idx, op in enumerate(operators):
        if op == "+":
            accumulator.append(sum(operands[idx]))
        else:
            accumulator.append(prod(operands[idx]))

    print(f"Accumulator: {accumulator}")
    print(f"Total: {sum(accumulator)}")
