# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/1

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 1

    @answer(53386)
    def part_1(self) -> int:
        ack = 0
        for line in self.input:
            ints = [x for x in line if x.isdigit()]
            ack += int(f"{ints[0]}{ints[-1]}")
        return ack

       
    @answer(53312)
    def part_2(self) -> int:
        ack = 0
        for line in self.input:
            line = self.convert_str_num_to_int(line)
            self.debug(line)
            ints = [x for x in line if x.isdigit()]
            self.debug(f"{ints[0]}{ints[-1]}")
            ack += int(f"{ints[0]}{ints[-1]}")
        return ack
    

    @staticmethod
    def convert_str_num_to_int(num: str) -> str:
        numbers = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        for key, value in numbers.items():
            num = num.replace(key, f"{key}{value}{key}")
        return num
    