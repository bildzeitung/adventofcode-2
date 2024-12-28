"""
Advent of Code Part 1
"""

from typing import TextIO


def mix(x: int, y: int) -> int:
    return x ^ y


def prune(x: int) -> int:
    return x % 16777216


def process_secret(secret: int) -> int:
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret


def main(f: TextIO, rounds: int) -> None:
    """
    Solution to part 1
    """
    rv = []
    for line in f:
        secret = int(line.strip())
        initial_secret = secret
        for _ in range(rounds):
            secret = process_secret(secret)
        rv.append(secret)
        print(f"{initial_secret}: {secret}")
    print(f"Total: {sum(rv)}")
