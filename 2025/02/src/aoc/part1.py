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
        # catch some easy cases
        if len(slow) % 2 and len(shigh) == len(slow):
            print(f"[{low, high}] have no invalid IDs (both odd lengths)")
            continue

        if len(slow) == 1 and len(shigh) > 1:
            print(f"Odd case: {low, high}")
            low = 10
            slow = str(low)

        # need even length for start string
        if len(slow) % 2:
            # 123 -> 1000, e.g. lowest next power of 10
            low = 10 ** ceil(log10(low))
            slow = str(low)
            assert low <= high

        # now we can divide the start string into left and right halves
        l, r = int(slow[0 : len(slow) // 2]), int(slow[len(slow) // 2 :])
        print(f"Processing {slow} --> {l}, {r}\tmax: {shigh}")

        while True:
            if l == r:
                print(f"Got invalid ID: {l, r}")
                results.append(int(str(l) + str(r)))
                r += 1
                l += 1

            # eg 9967849351 --> 99678, 49351
            #    so the next possible invalid id is: 9967899678
            if l > r:
                r = l
            # eg 117855 --> 117, 855
            #    so the next possible invalid id is: 118118
            elif l < r:
                l += 1
                r = l

            # ok, exhausted the range
            print(f"{l} | {r} | next: {int(str(l) + str(r))}")
            if int(str(l) + str(r)) > high:
                break
    print(f"Results: {results}")
    print(f"Final: {sum(results)}")
