"""
Advent of Code 2024
"""

from pathlib import Path

import typer

from . import part1 as p1
from . import part2 as p2

app = typer.Typer()


@app.command()
def part1(filename: Path, width: int, tall: int):
    """Advent of Code: Part 1"""
    p1.main(filename.open("r"), width, tall)


@app.command()
def part2(filename: Path):
    """Advent of Code: Part 2"""
    p2.main(filename.open("r"))
