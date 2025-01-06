"""
Advent of Code Part 1
"""

from typing import TextIO
from rich.progress import track

def solve(available : list[str], to_find: str) -> bool:
    """ Return True if to_find can be made of available; False otherwise """
    # if nothing to match, then yay!
    if not to_find:
        return True
    
    # recursive search
    return any(solve(available, to_find[len(i):]) for i in available if to_find.startswith(i))


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    available_towels = next(f).strip().replace(' ', '').split(',')
    
    next(f)  # blank

    all_lines = [line.strip() for line in f]
    for line in all_lines:
        print(f"{line} -> {solve(available_towels, line)}")
    #total = sum(solve(available_towels, line) for line in track(all_lines))
    #print(f"Total: {total}")