# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2023/day/10

from ...base import StrSplitSolution, answer
import resource, sys

resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**6)


OPENINGS = {
    "above": ["|", "7", "F", "S"],
    "below": ["|", "L", "J", "S"],
    "left": ["-", "F", "L", "S"],
    "right": ["-", "7", "J", "S"],
}


class Solution(StrSplitSolution):
    _year = 2023
    _day = 10

    @answer(6773.0)
    def part_1(self) -> int:
        start, _matrix = self.create_pipes()
        pipe = start.connections[0]
        pipe.connections.remove(start)
        length = 1
        while pipe != start:
            next_pipe = (
                pipe.connections[0]
                if pipe.connections[0] != pipe
                else pipe.connections[1]
            )
            next_pipe.connections.remove(pipe)
            pipe = next_pipe
            length += 1
        return length / 2

    # @answer(1234)
    def part_2(self) -> int:
        start, matrix = self.create_pipes()
        # Find main loop
        pipe = start.connections[1]
        pipe.connections.remove(start)
        loop_outer_border = []
        while pipe != start:
            pipe.main_loop = True
            next_pipe = (
                pipe.connections[0]
                if pipe.connections[0] != pipe
                else pipe.connections[1]
            )
            next_pipe.connections.remove(pipe)
            loop_outer_border.extend(self.get_outer_border(next_pipe, matrix))
            pipe = next_pipe

        start.connections = []
        start.connect(matrix)
        opening_1 = (start.x - start.connections[0].x, start.y - start.connections[0].y)
        opening_2 = (start.x - start.connections[1].x, start.y - start.connections[1].y)
        if set([opening_1, opening_2]) == set([(0, 1), (0, -1)]):
            start.form = "|"
        elif set([opening_1, opening_2]) == set([(1, 0), (-1, 0)]):
            start.form = "-"
        elif set([opening_1, opening_2]) == set([(1, 0), (0, -1)]):
            start.form = "7"
        elif set([opening_1, opening_2]) == set([(0, 1), (1, 0)]):
            start.form = "J"
        elif set([opening_1, opening_2]) == set([(0, 1), (-1, 0)]):
            start.form = "L"
        elif set([opening_1, opening_2]) == set([(0, -1), (-1, 0)]):
            start.form = "F"
        # Convert none main loop pipes to tiles
        for row in matrix:
            for pipe in row:
                if not pipe.main_loop:
                    pipe.form = "."

        # Connect tiles
        ack = 0
        for row in matrix:
            inside = False
            for pipe in row:
                if pipe.form == "." and inside:
                    ack += 1
                elif pipe.form in OPENINGS["below"]:
                    inside = not inside

        for line in matrix:
            print("".join([str(p) for p in line]))
        return ack

    def get_outer_border(self, pipe, matrix):
        direction = pipe.connections[0].x - pipe.x, pipe.connections[0].y - pipe.y
        border = []
        if pipe.form == "|":
            if direction == (0, 1):
                border.append((pipe.x - 1, pipe.y))
            elif direction == (0, -1):
                border.append((pipe.x + 1, pipe.y))
        elif pipe.form == "-":
            if direction == (1, 0):
                border.append((pipe.x, pipe.y + 1))
            elif direction == (-1, 0):
                border.append((pipe.x, pipe.y - 1))
        elif pipe.form == "7":
            if direction == (-1, 0):
                border.append((pipe.x, pipe.y + 1))
                border.append((pipe.x + 1, pipe.y + 1))
                border.append((pipe.x + 1, pipe.y))
        elif pipe.form == "F":
            if direction == (0, -1):
                border.append((pipe.x - 1, pipe.y))
                border.append((pipe.x - 1, pipe.y + 1))
                border.append((pipe.x, pipe.y + 1))
        elif pipe.form == "L":
            if direction == (1, 0):
                border.append((pipe.x, pipe.y - 1))
                border.append((pipe.x - 1, pipe.y - 1))
                border.append((pipe.x - 1, pipe.y))
        elif pipe.form == "J":
            if direction == (0, 1):
                border.append((pipe.x + 1, pipe.y))
                border.append((pipe.x + 1, pipe.y - 1))
                border.append((pipe.x, pipe.y - 1))
        return border

    def get_tile_area(self, tile):
        """
        Returns a list of all tiles in the area of the given tile
        and if the area is inside the main loop
        """
        area = []
        if tile.form == ".":
            area.append(tile)
            tile.form = "X"
            for pipe in tile.connections:
                area.extend(self.get_tile_area(pipe))

        return area

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass

    def create_pipes(self):
        pipe_matrix = []
        y = 0
        start = None
        for line in self.input:
            pipes = [Pipe(pipe, x, y) for x, pipe in enumerate(line)]
            pipe_matrix.append(pipes)
            y += 1
        for row in pipe_matrix:
            for pipe in row:
                pipe.connect(pipe_matrix)
                if pipe.form == "S":
                    start = pipe
                    pipe.main_loop = True

        return start, pipe_matrix


class Pipe:
    def __init__(self, form, x, y):
        self.form = form
        self.x = x
        self.y = y
        self.connections = []
        self.main_loop = False

    def __repr__(self):
        return f"Pipe({self.form})"

    def __str__(self):
        return self.form

    def connect(self, pipes):
        if self.form == ".":
            self.connect_tile(pipes)
        if self.form == "|":
            self.connect_up(pipes)
            self.connect_down(pipes)
        if self.form == "-":
            self.connect_left(pipes)
            self.connect_right(pipes)
        if self.form == "7":
            self.connect_left(pipes)
            self.connect_down(pipes)
        if self.form == "F":
            self.connect_right(pipes)
            self.connect_down(pipes)
        if self.form == "L":
            self.connect_up(pipes)
            self.connect_right(pipes)
        if self.form == "J":
            self.connect_up(pipes)
            self.connect_left(pipes)
        if self.form == "S":
            self.connect_up(pipes)
            self.connect_down(pipes)
            self.connect_left(pipes)
            self.connect_right(pipes)

    def connect_up(self, pipes):
        if not self.y == 0:
            pipe = pipes[self.y - 1][self.x]
            if pipe.form in OPENINGS["above"]:
                self.connections.append(pipe)

    def connect_down(self, pipes):
        if not self.y == len(pipes) - 1:
            pipe = pipes[self.y + 1][self.x]
            if pipe.form in OPENINGS["below"]:
                self.connections.append(pipe)

    def connect_left(self, pipes):
        if not self.x == 0:
            pipe = pipes[self.y][self.x - 1]
            if pipe.form in OPENINGS["left"]:
                self.connections.append(pipe)

    def connect_right(self, pipes):
        if not self.x == len(pipes[self.y]) - 1:
            pipe = pipes[self.y][self.x + 1]
            if pipe.form in OPENINGS["right"]:
                self.connections.append(pipe)

    def connect_tile(self, pipes):
        if not self.y == 0:
            pipe = pipes[self.y - 1][self.x]
            if pipe.form == ".":
                self.connections.append(pipe)
        if not self.y == len(pipes) - 1:
            pipe = pipes[self.y + 1][self.x]
            if pipe.form == ".":
                self.connections.append(pipe)
        if not self.x == 0:
            pipe = pipes[self.y][self.x - 1]
            if pipe.form == ".":
                self.connections.append(pipe)
        if not self.x == len(pipes[self.y]) - 1:
            pipe = pipes[self.y][self.x + 1]
            if pipe.form == ".":
                self.connections.append(pipe)
