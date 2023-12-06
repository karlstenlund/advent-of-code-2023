# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/6

import math

from sympy import Eq, solve, symbols
from sympy.abc import x, y

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 6

    @answer(1731600)
    def part_1(self) -> int:
        times, distances = [line.split()[1:] for line in self.input]
        ack = 1
        for time, distance in zip(times, distances):
            possible = 0
            time = int(time)
            for i in range(0, time):
                if i * (time - i) > int(distance):
                    possible += 1
            if possible > 0:
                ack = ack * possible

        return ack

    @answer(40087680)
    def part_2(self) -> int:
        time, distance = [int("".join(line.split()[1:])) for line in self.input]
        eq = Eq(y**2 - time * y + distance, y)
        solution = solve(eq, y)
        return math.floor(solution[1]) - math.ceil(solution[0]) - 2
