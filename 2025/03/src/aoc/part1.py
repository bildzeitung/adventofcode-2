"""
Advent of Code Part 1
"""

from typing import TextIO


def process(line: str) -> int:
    numbers = "9876543210"
    left = -1
    right = -1
    print(f"Processing '{line}' | {len(line)}")
    n: str = ""
    for n in numbers:
        left = line.find(n)
        if left == -1:  # not here
            print(f"Cannot find a '{n}'")
            continue
        if left == len(line) - 1:
            print(f"Found a '{n}' but it's the last character ({left})")
            continue  # can't use last position either
        print(f"Got a '{n}' at position {left}")
        break
    m: str = ""
    for m in numbers:
        right = line.rfind(m)
        if right == len(line):
            print(f"Cannot find a '{m}'")
            continue
        if right <= left:
            print(f"Cannot use same or earlier digit '{m}': {right} <= {left}")
            continue
        print(f"Got a '{m}' at position {right}")
        break
    final = int(n + m)
    print(f"-> {final}")
    return final


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    results = [process(line.strip()) for line in f]
    print(f"Results: {results} | {sum(results)}")
