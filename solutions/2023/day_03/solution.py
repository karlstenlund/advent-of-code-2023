# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/3

import re
from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 3
    REG = r"\d+"

    # @answer(550891)
    def part_1(self) -> int:
        ack = 0
        index = 0
        for line in self.input:
            ack += self.find_numbers(line, index)
            index += 1

        return ack

    def find_numbers(self, line, index):
        nums = self.get_numbers_and_positions(line)
        ack = 0
        for num, place in nums:
            if self.symbols_in_line_above_or_below(num, place, index):
                ack += int(num)
        return ack

    def get_numbers_and_positions(self, line):
        """
        Returns list och tuples with number and position in line
        e.g.
        >>> get_numbers_and_positions("123 456")
        [(123, 0), (456, 4)]
        """
        matches = re.finditer(self.REG, line)
        return [(match.group(), match.start()) for match in matches]

    def symbols_in_line_above_or_below(self, num, place, line_index):
        above_index = line_index - 1 if line_index > 0 else 0
        below_index = (
            line_index + 1 if line_index < len(self.input) - 1 else len(self.input) - 1
        )
        before_index = place - 1 if place > 0 else 0
        after_index = (
            place + len(num) + 1
            if place < len(self.input[0]) - 1
            else len(self.input[0]) - 1
        )
        above = self.input[above_index][before_index:after_index]
        middle = self.input[line_index][before_index:after_index]
        below = self.input[below_index][before_index:after_index]

        # if any char is not number or period, return true
        for char in above:
            if not char.isdigit() and char != ".":
                return True
        for char in middle:
            if not char.isdigit() and char != ".":
                return True
        for char in below:
            if not char.isdigit() and char != ".":
                return True
        return False

    # @answer(1234)
    def part_2(self) -> int:
        line_number = 0
        gears = {}
        for line in self.input:
            gears = self.find_gears(line, line_number, gears)
            line_number += 1

        return sum(
            [
                int(value[0]) * int(value[1])
                for value in gears.values()
                if len(value) == 2
            ]
        )

    def find_gears(self, line, line_number, gears):
        """
        Returns list with position of gear and number
        e.g.
        >>> find_gears("123*456")
        [((0,3), 123), ((0,3), 456)]
        """
        nums = self.get_numbers_and_positions(line)
        for num, place in nums:
            if poistion := self.asterisk_around_number(num, place, line_number):
                if poistion in gears:
                    gears[poistion].append(num)
                else:
                    gears[poistion] = [num]

        return gears

    def asterisk_around_number(self, num, place, line_number):
        above_number = line_number - 1 if line_number > 0 else 0
        below_number = (
            line_number + 1
            if line_number < len(self.input) - 1
            else len(self.input) - 1
        )
        before_number = place - 1 if place > 0 else 0
        after_number = (
            place + len(num) + 1
            if place < len(self.input[0]) - 1
            else len(self.input[0]) - 1
        )
        above = self.input[above_number][before_number:after_number]
        middle = self.input[line_number][before_number:after_number]
        below = self.input[below_number][before_number:after_number]

        # if any char is not number or period, return true
        for char in above:
            if char == "*":
                return (
                    above_number,
                    self.input[above_number].find("*", before_number, after_number),
                )
        for char in middle:
            if char == "*":
                return (
                    line_number,
                    self.input[line_number].find("*", before_number, after_number),
                )
        for char in below:
            if char == "*":
                return (
                    below_number,
                    self.input[below_number].find("*", before_number, after_number),
                )
        return None

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
