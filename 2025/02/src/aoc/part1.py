"""
Advent of Code Part 1
"""

from math import ceil, log10
from typing import List, TextIO


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    ranges: List[List[int]] = [[int(y) for y in x.split("-")] for x in next(f).strip().split(",")]
    results = []
    for item in ranges:
        low, high = item
        slow, shigh = str(low), str(high)

        if low < 10:
            print(f"Odd case: {low, high}")
            low = 10
            slow = "10"

        # need even length for start string
        if len(slow) % 2:
            # 123 -> 1000, e.g. lowest next power of 10
            low = 10 ** ceil(log10(low))
            slow = str(low)

        if low > high:
            continue

        # now we can divide the start string into left and right halves
        ll, r = int(slow[0 : len(slow) // 2]), int(slow[len(slow) // 2 :])
        print(f"Processing {slow} --> {ll}, {r}\tmax: {shigh}")

        while True:
            if ll == r:
                print(f"Got invalid ID: {ll, r}")
                results.append(int(str(ll) + str(r)))
                r += 1
                ll += 1

            # eg 9967849351 --> 99678, 49351
            #    so the next possible invalid id is: 9967899678
            if ll > r:
                r = ll
            # eg 117855 --> 117, 855
            #    so the next possible invalid id is: 118118
            elif ll < r:
                ll += 1
                r = ll

            # ok, exhausted the range
            print(f"{ll} | {r} | next: {int(str(ll) + str(r))}")
            if int(str(ll) + str(r)) > high:
                break
    print(f"Results: {results}")
    print(f"Final: {sum(results)}")
