# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/2

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 2
    CUBES = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    # @answer(2449)
    def part_1(self) -> int:
        ack = 0
        for line in self.input:
            game, hands = line.split(":")
            if self.too_many_cubes(hands):
                continue
            ack += int(game.split(" ")[1])
        return ack

    
    def too_many_cubes(self, hands: list[str]) -> bool:
        for hand in hands.split(";"):
            for cube in hand.split(","):
                amount, color = cube.strip().split(" ")
                if int(amount) > self.CUBES[color]:
                    return True
        return False
    

    # @answer(1234)
    def part_2(self) -> int:
        ack = 0
        for line in self.input:
            _game, hands = line.split(":")
            ack += self.sum_minimum_number_of_cubes(hands)
        return ack



    def sum_minimum_number_of_cubes(self, hands: list[str]) -> int:
        cubes = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for hand in hands.split(";"):
            for cube in hand.split(","):
                amount, color = cube.strip().split(" ")
                if cubes[color] < int(amount):
                    cubes[color] = int(amount)
        return cubes["red"] * cubes["green"] * cubes["blue"]

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
