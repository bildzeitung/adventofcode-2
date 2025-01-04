"""
Advent of Code Part 2
"""

import logging
from typing import TextIO

from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()])

log = logging.getLogger("rich")


def main(f: TextIO) -> None:
    """
    Solution to part 2
    """
    reg_a = int(next(f).strip().split(":")[1])
    reg_b = int(next(f).strip().split(":")[1])
    reg_c = int(next(f).strip().split(":")[1])
    output = []

    # blank
    next(f)

    program = list(map(int, next(f).strip().split(":")[1].split(",")))
    log.debug(f"Registers: {reg_a} {reg_b} {reg_c}")
    log.debug(f"Program: {program}")

    def combo(operand: int) -> int:
        if operand < 4:
            return operand

        if operand == 4:
            return reg_a

        if operand == 5:
            return reg_b

        if operand == 6:
            return reg_c

    ip = 0
    while True:
        log.debug(f"IP == {ip}, {reg_a} {reg_b} {reg_c} {output}")
        if ip >= len(program):
            break  # halt

        op, operand = program[ip], program[ip + 1]
        match op:
            case 0:  # adv
                log.debug(f"({ip}) ADV {reg_a} / 2 ^ {combo(operand)} --> {reg_a // 2 ** combo(operand)}")
                reg_a = reg_a // 2 ** combo(operand)
            case 1:  # bxl
                log.debug(f"({ip}) BXL {reg_b} ^ {operand} --> {reg_b ^ operand}")
                reg_b = reg_b ^ operand
            case 2:  # bst
                log.debug(f"({ip}) BST {combo(operand)} % 8 --> {combo(operand) % 8}")
                reg_b = combo(operand) % 8
            case 3:  # jnz
                log.debug(f"({ip}) JNZ {reg_a} {operand}")
                if reg_a:
                    ip = operand
                    continue
            case 4:  # bxc
                log.debug(f"({ip}) BXC {reg_b} ^ {reg_c} --> {reg_b ^ reg_c}")
                reg_b = reg_b ^ reg_c
            case 5:  # out
                log.debug(f"({ip}) OUT {combo(operand)} | {combo(operand) % 8}")
                output.append(combo(operand) % 8)
            case 7:  # cdv
                log.debug(f"({ip}) CDV {reg_a} / 2 ^ {combo(operand)} --> {reg_a // 2 ** combo(operand)}")
                reg_c = reg_a // 2 ** combo(operand)
            case _:
                raise (Exception(f"Bad operand: {op}"))
        # next instruction
        ip += 2

    print(",".join(map(str, output)))
