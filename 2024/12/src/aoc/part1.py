"""
Advent of Code Part 1
"""

from collections import deque
from typing import TextIO

from rich import print


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    # puzzle = defaultdict(list)
    all_coords = {}
    y = 0
    for line in f:
        for x, i in enumerate(line.strip()):
            # puzzle[i].append((x, y))
            all_coords[(x, y)] = i
        y += 1

    # need to identify contigous areas
    seen = set()
    to_check = deque(all_coords.keys())
    all_groups = []
    while to_check:
        start = to_check.popleft()
        if start in seen:
            continue
        # ok, so this is new, so trace it
        group_name = all_coords[start]
        check = deque()
        check.append(start)
        group_members = set()
        while check:
            x, y = check.popleft()
            if (x, y) in seen:
                continue
            seen.add((x, y))
            group_members.add((x, y))
            if (
                (x - 1, y) in all_coords
                and (x - 1, y) not in seen
                and all_coords[(x - 1, y)] == group_name
            ):
                check.append((x - 1, y))
            if (
                (x + 1, y) in all_coords
                and (x + 1, y) not in seen
                and all_coords[(x + 1, y)] == group_name
            ):
                check.append((x + 1, y))
            if (
                (x, y - 1) in all_coords
                and (x, y - 1) not in seen
                and all_coords[(x, y - 1)] == group_name
            ):
                check.append((x, y - 1))
            if (
                (x, y + 1) in all_coords
                and (x, y + 1) not in seen
                and all_coords[(x, y + 1)] == group_name
            ):
                check.append((x, y + 1))
        # print(f"Total for {group_name} -> {group_members}")
        all_groups.append((group_name, group_members))

    # ok, now calc area and perimeter for all the groups
    # print(all_groups)
    total = 0
    for group in all_groups:
        perimeter = 0
        name, members = group
        area = len(members)
        for member in members:
            x, y = member
            lper = (
                (
                    ((x - 1, y) not in all_coords)
                    or ((x - 1, y) in all_coords and all_coords[(x - 1, y)] != name)
                )
                + (
                    ((x + 1, y) not in all_coords)
                    or ((x + 1, y) in all_coords and all_coords[(x + 1, y)] != name)
                )
                + (
                    ((x, y - 1) not in all_coords)
                    or ((x, y - 1) in all_coords and all_coords[(x, y - 1)] != name)
                )
                + (
                    ((x, y + 1) not in all_coords)
                    or ((x, y + 1) in all_coords and all_coords[(x, y + 1)] != name)
                )
            )
            perimeter += lper
            # print(f"** {member} | {name} -> {lper}")

        # print(f"For {name} => {perimeter} * {area} == {perimeter*area}")
        total += perimeter * area

    print(f"Total --> {total}")
