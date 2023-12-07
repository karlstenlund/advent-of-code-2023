# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/7

from ...base import StrSplitSolution, answer

VALUES = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}
VALUES_JOKER = VALUES.copy()
VALUES_JOKER["J"] = 1


class Solution(StrSplitSolution):
    _year = 2023
    _day = 7

    @answer(246912307)
    def part_1(self) -> int:
        poker_hands = []
        for line in self.input:
            hand, value = line.split()
            poker_hand = PokerHand(hand, value)
            poker_hands.append(poker_hand)
        rank = 1
        ack = 0
        for h in sorted(poker_hands):
            ack += rank * int(h.value)
            rank += 1

        return ack

    @answer(246894760)
    def part_2(self) -> int:
        poker_hands = []
        for line in self.input:
            hand, value = line.split()
            poker_hand = JokerHand(hand, value)
            poker_hands.append(poker_hand)
        rank = 1
        ack = 0
        for h in sorted(poker_hands):
            ack += rank * int(h.value)
            rank += 1

        return ack

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass


class PokerHand:
    def __init__(self, hand: str, value: int) -> None:
        self.hand = hand
        self.value = value
        self.hand_value = self._hand_value()
        self.hand_count = self._concat_hand()

    def __repr__(self) -> str:
        return f"{self.hand}"

    def __lt__(self, other) -> bool:
        if self.hand_value == other.hand_value:
            return self.hand_count < other.hand_count
        else:
            return self.hand_value < other.hand_value

    def __gt__(self, other) -> bool:
        if self.hand_value == other.hand_value:
            return self.hand_count > other.hand_count
        else:
            return self.hand_value > other.hand_value

    def _hand_value(self) -> int:
        hand_types = self._group()
        if len(hand_types) == 1:
            return 7
        elif len(hand_types) == 2:
            if 1 in hand_types.values():
                return 6
            else:
                return 5
        elif len(hand_types) == 3:
            if 3 in hand_types.values():
                return 4
            else:
                return 3
        elif len(hand_types) == 4:
            return 2
        else:
            return 1

    def _group(self) -> dict[str, int]:
        groups = {}
        for card in self.hand:
            if card[0] in groups:
                groups[card[0]] += 1
            else:
                groups[card[0]] = 1
        return groups

    def _concat_hand(self) -> int:
        hand = ""
        for card in self.hand:
            hand += f"{VALUES[card[0]]:02d}"
        return int(hand)


class JokerHand(PokerHand):
    def __repr__(self) -> str:
        return super().__repr__() + f" ({self.hand_value})" + f" ({self.hand_count})"

    def _hand_value(self) -> int:
        hand_types, jokers = self._group()
        if len(hand_types) == 1:
            return 7
        elif len(hand_types) == 2:
            if 1 in hand_types.values():
                if jokers:
                    return 7
                return 6
            else:
                if jokers:
                    return 7
                return 5
        elif len(hand_types) == 3:
            if 3 in hand_types.values():
                if jokers:
                    return 6
                return 4
            else:
                if jokers == 1:
                    return 5
                if jokers == 2:
                    return 6
                return 3
        elif len(hand_types) == 4:
            if jokers:
                return 4
            return 2
        else:
            if jokers:
                return 2
            return 1

    def _group(self) -> dict[str, int]:
        groups = {}
        jokers = 0
        for card in self.hand:
            if card[0] == "J":
                jokers += 1
            if card[0] in groups:
                groups[card[0]] += 1
            else:
                groups[card[0]] = 1
        return groups, jokers

    def _concat_hand(self) -> int:
        hand = ""
        for card in self.hand:
            hand += f"{VALUES_JOKER[card[0]]:02d}"
        return int(hand)
