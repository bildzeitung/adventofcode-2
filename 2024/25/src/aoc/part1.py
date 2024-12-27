"""
Advent of Code Part 1
"""

from typing import TextIO


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    all_keys = []
    all_locks = []

    for line in f:
        lock_or_key = ""
        line = line.strip()
        # find out which mode to use
        if line.count("#") == len(line):
            # ok, it's a lock
            lock_or_key = "LOCK"
        else:
            # ok, it's a key
            lock_or_key = "KEY"

        sums = [0] * len(line)
        line = next(f).strip()
        while line:
            for idx, val in enumerate(line):
                if val == "#":
                    sums[idx] += 1
            try:
                line = next(f).strip()
            except StopIteration:
                break
        if lock_or_key == "KEY":
            for i in range(len(sums)):
                sums[i] -= 1

        if lock_or_key == "LOCK":
            all_locks.append(sums)
        else:
            all_keys.append(sums)

    print(f"Locks: {all_locks}")
    print(f"Keys : {all_keys}")
    ml = max(max(x) for x in all_locks)
    mk = max(max(x) for x in all_keys)
    assert ml == mk

    total = 0
    for l in all_locks:
        for k in all_keys:
            sums = [x + y for x, y in zip(k, l)]
            if any(x > ml for x in sums):
                continue
            total += 1
    print(f"Grand total: {total}")