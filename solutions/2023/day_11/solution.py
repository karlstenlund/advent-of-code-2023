# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/11

import numpy as np

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2023
    _day = 11

    @answer(9648398)
    def part_1(self) -> int:
        galaxy = []
        for line in self.input:
            galaxy.append(list(line))
            if "#" not in line:
                galaxy.append(list(line))
        galaxy = np.array(galaxy)
        galaxy = np.rot90(galaxy)
        new_galaxy = []
        for line in galaxy:
            new_galaxy.append(list(line))
            if "#" not in line:
                new_galaxy.append(list(line))
        y = 0
        galaxies = []
        for line in new_galaxy:
            x = 0
            for char in line:
                if char == "#":
                    galaxies.append(Galaxy(x, y))
                x += 1
            y += 1
        ack = 0
        while len(galaxies) > 1:
            galaxy_1 = galaxies.pop()
            for galaxy_2 in galaxies:
                ack += abs(galaxy_1.x - galaxy_2.x) + abs(galaxy_1.y - galaxy_2.y)
        return ack

    @answer(618800410814)
    def part_2(self) -> int:
        galaxy = []
        empty_lines_x = []
        empty_lines_y = []
        i = 0
        for line in self.input:
            galaxy.append(list(line))
            if "#" not in line:
                empty_lines_x.append(i)
            i += 1
        galaxy = np.array(galaxy)
        galaxy = np.rot90(galaxy)
        new_galaxy = []
        i = 0
        for line in galaxy:
            new_galaxy.append(list(line))
            if "#" not in line:
                empty_lines_y.append(i)
            i += 1
        y = 0
        galaxies = []
        for line in new_galaxy:
            x = 0
            for char in line:
                if char == "#":
                    galaxies.append(Galaxy(x, y))
                x += 1
            y += 1
        ack = 0
        while len(galaxies) > 1:
            galaxy_1 = galaxies.pop()
            for galaxy_2 in galaxies:
                ack += galaxy_1.manhattan_distance(
                    galaxy_2, empty_lines_x, empty_lines_y
                )
        return ack


class Galaxy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance(self, other, empty_lines_x, empty_lines_y):
        EXPANSION = 1000000 - 1
        lower_x, upper_x = min(self.x, other.x), max(self.x, other.x)
        lower_y, upper_y = min(self.y, other.y), max(self.y, other.y)
        x = sum([1 for line in empty_lines_x if lower_x < line < upper_x]) * EXPANSION
        y = sum([1 for line in empty_lines_y if lower_y < line < upper_y]) * EXPANSION
        return abs(self.x - other.x) + x + abs(self.y - other.y) + y
