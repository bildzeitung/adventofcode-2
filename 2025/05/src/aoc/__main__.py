"""
Advent of Code 2025
"""

from pathlib import Path

import typer

from . import part1 as p1
from . import part2 as p2

app = typer.Typer()


@app.command()
def part1(filename: Path):
    """Advent of Code: Part 1"""
    p1.main((Path("data") / filename).open("r"))


@app.command()
def part2(filename: Path):
    """Advent of Code: Part 2"""
    p2.main((Path("data") / filename).open("r"))
