"""
Advent of Code Part 2
"""


from typing import TextIO

type Pair = tuple[int, int]
type PairList = list[Pair]


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    all_ranges: PairList = []
    for line in f:
        if not line.strip():
            break

        start, stop = [int(x) for x in line.strip().split("-")]
        all_ranges.append((start, stop))

    all_ranges = sorted(all_ranges)
    print(all_ranges)

    finalRanges: PairList = []
    current: Pair = all_ranges[0]
    for item in all_ranges[1:]:
        if current[0] <= item[0] <= current[1]:
            current = (current[0], max(current[1], item[1]))
        else:
            finalRanges.append(current)
            current = item
    finalRanges.append(current)
    print(finalRanges)
    print(f"Original: {len(all_ranges)} Reduced: {len(finalRanges)}")
    print(f"Total: {sum(i[1] - i[0] + 1 for i in finalRanges)}")
