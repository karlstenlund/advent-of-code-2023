# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/4

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 4

    @answer(27059)
    def part_1(self) -> int:
        ack = 0
        for line in self.input:
            power = -1
            wining_numbers, your_numbers = line.split(":")[1].split("|")
            wining_numbers = wining_numbers.split()
            for number in your_numbers.split():
                if number in wining_numbers:
                    power += 1

            ack += 2**power if power > -1 else 0

        return ack

    # @answer(1234)
    def part_2(self) -> int:
        cards = []
        for line in self.input:
            cards.append(ScratchCard(line))

        while any([card.copies > 0 for card in cards]):
            for card in cards:
                price = card.scratch()
                for c in range(price):
                    if card.card + c < len(cards):
                        cards[card.card + c].add_copy()

        return sum([card.scratched for card in cards])


class ScratchCard:
    def __init__(self, line):
        self.line = line
        self.card, numbers = line.split(":")
        self.card = int(self.card.split()[1])
        self.wining_numbers, self.your_numbers = numbers.split("|")
        self.wining_numbers = self.wining_numbers.split()
        self.your_numbers = self.your_numbers.split()
        self.copies = 1
        self.scratched = 0

    def scratch(self):
        if self.copies == 0:
            return 0
        ack = 0
        for number in self.your_numbers:
            if number in self.wining_numbers:
                ack += 1

        self.copies -= 1
        self.scratched += 1
        return ack

    def add_copy(self):
        self.copies += 1

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
