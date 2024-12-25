"""
Advent of Code Part 1
"""

import operator
from collections import deque
from typing import Dict, TextIO

from rich import print

OPS = {
    "AND": operator.__and__,
    "OR": operator.__or__,
    "XOR": operator.__xor__,
}


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    values: Dict[str, int] = {}
    # pick up the values
    for line in f:
        if not line.strip():
            break
        k, v = line.strip().split(":")
        values[k] = int(v)

    # equations
    equations = deque()
    for line in f:
        a, op, b, produces = line.strip().replace("->", "").split()
        equations.append((a, op, b, produces))

    print(equations)
    while equations:
        a, op, b, gets = equations.popleft()
        if a in values and b in values:
            # ok, can solve for a var
            values[gets] = OPS[op](values[a], values[b])
            print(f"{gets} => {values[a]} {op} {values[b]} => {values[gets]}")
            continue
        equations.append((a, op, b, gets))

    print("Ok, solved for all.")
    print(values)

    to_convert = sorted(filter(lambda x: x.startswith("z"), values))
    print(f"To convert:{to_convert}")
    p = 1
    total = 0
    for v in to_convert:
        total += p * values[v]
        p *= 2
    print(f"Final: {total}")
