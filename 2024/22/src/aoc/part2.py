"""
Advent of Code Part 2
"""

from typing import TextIO

from rich.progress import track

ROUNDS = 2000  # from the puzzle


def mix(x: int, y: int) -> int:
    return x ^ y


def prune(x: int) -> int:
    return x % 16777216


def process_secret(secret: int) -> int:
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    all_4t = []
    inputs = [int(line.strip()) for line in f]
    for secret in track(inputs):
        all_secrets = [secret % 10] + [
            (secret := process_secret(secret)) % 10 for _ in range(ROUNDS)
        ]
        deltas = [all_secrets[x] - all_secrets[x - 1] for x in range(1, len(all_secrets))]
        fourtuples = {}
        for idx, v in enumerate(zip(deltas, deltas[1:], deltas[2:], deltas[3:])):
            t = (v[0], v[1], v[2], v[3])
            if t not in fourtuples:
                fourtuples[t] = all_secrets[idx+4]
        all_4t.append(fourtuples)

    print("...done creating 4-tuples...")
    common = set()
    for t in all_4t[1:]:
        common |= set(t)
    print(f"Possible deltas to check: {len(common)}")

    # calc the sum for each 4-tuple across all 4-tuple dicts
    all_sums = { c: sum(x[c] for x in all_4t if c in x) for c in track(common)}
    print("Finished calculating all sums; sorting next..")
    top_banana = sorted(all_sums, key=lambda x: all_sums[x])[-1]
    print(f"Top sequence: {top_banana} --> {all_sums[top_banana]}")