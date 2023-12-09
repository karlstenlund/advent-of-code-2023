# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/9

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 9

    @answer(1938800261)
    def part_1(self) -> int:
        seqs = [extrapolate([int(x) for x in line.split()]) for line in self.input]
        return sum(x[0][-1] for x in seqs)

    @answer(1112)
    def part_2(self) -> int:
        seqs = [
            extrapolate_backwards([int(x) for x in line.split()]) for line in self.input
        ]
        return sum(x[0][0] for x in seqs)


def extrapolate(seq, ack=0):
    if any(seq):
        der, ack = extrapolate(derivative(seq), ack)
        extra = seq[-1] + der[-1]
        seq.append(extra)
        return seq, ack + extra
    seq.append(0)
    return seq, 0


def extrapolate_backwards(seq, ack=0):
    if any(seq):
        der, ack = extrapolate_backwards(derivative(seq), ack)
        extra = seq[0] - der[0]
        seq.insert(0, extra)
        return seq, ack + extra
    seq.insert(0, 0)
    return seq, 0


def derivative(seq):
    return [y - x for x, y in zip(seq, seq[1:])]
