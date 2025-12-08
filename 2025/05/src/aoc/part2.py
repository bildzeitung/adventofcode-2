"""
Advent of Code Part 2
"""

from typing import TextIO, Set


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    all_ranges = []
    for line in f:
        if not line.strip():
            break
        start, stop = [int(x) for x in line.strip().split("-")]
        all_ranges.append((start, stop))
    
    '''
    The naive approach:

    all_numbers : set[int] = set()
    for r in all_ranges:
        all_numbers |= set(x for x in range(r[0], r[1]+1))

    print(f"Total: {len(all_numbers)}")
    '''
    
    ''' 
        Cases:

    1)  |----|
          |----|

    2)    |----|
        |----|
        
    3)    |-|
        |----|

    4)  |----|
          |-|
    '''