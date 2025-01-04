"""
Advent of Code Part 1
"""

from typing import TextIO


def main(f: TextIO) -> None:
    """
    Solution to part 1
    """
    reg_a = int(next(f).strip().split(":")[1])
    reg_b = int(next(f).strip().split(":")[1])
    reg_c = int(next(f).strip().split(":")[1])
    output = []

    # blank
    next(f)

    program = list(map(int, next(f).strip().split(":")[1].split(",")))
    print(f"Registers: {reg_a} {reg_b} {reg_c}")
    print(f"Program: {program}")

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
    while (True):
        #print(f"IP == {ip}, {reg_a} {reg_b} {reg_c} {output}")
        if ip >= len(program):
            break  # halt
        
        op, operand = program[ip], program[ip+1]
        match op:
            case 0:  # adv
                reg_a = reg_a // 2 ** combo(operand)
            case 1:  # bxl
                reg_b = reg_b ^ operand
            case 2:  # bst
                reg_b = combo(operand) % 8
            case 3:  # jnz
                if reg_a:
                    ip = operand
                    continue
            case 4:  # bxc
                reg_b = reg_b ^ reg_c
            case 5:  # out
                output.append(combo(operand) % 8)
            case 7:  # cdv
                reg_c = reg_a // 2 ** combo(operand)
            case _:
                raise(Exception(f"Bad operand: {op}"))
        # next instruction
        ip += 2

    print(",".join(map(str,output)))