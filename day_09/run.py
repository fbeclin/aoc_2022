from __future__ import annotations
import timeit

INPUT_FILEPATH = "./input1.txt"
DRAW_GRID = False
NB_OF_KNOTS = 10


class Movement(object):
    def __init__(self, line: str) -> None:
        values = line.split(" ")
        self.direction = values[0]
        self.step = int(values[1])

    def __str__(self) -> str:
        return f"direction: {self.direction} , step: {self.step}"


class Knot(object):
    def __init__(self, is_head: bool) -> None:
        self.x_pos = 0
        self.y_pos = 0
        self.is_head = is_head

    def move_to_direction(self, direction: str):
        if self.is_head:
            match direction:
                case "R":
                    self.x_pos += 1
                case "L":
                    self.x_pos -= 1
                case "U":
                    self.y_pos -= 1
                case "D":
                    self.y_pos += 1

    def move_to_knot(self, knot: Knot):
        if abs(self.x_pos - knot.x_pos) >= 2:
            self.x_pos += 1 if self.x_pos < knot.x_pos else -1

            if self.y_pos != knot.y_pos:
                self.y_pos += 1 if self.y_pos < knot.y_pos else -1

        if abs(self.y_pos - knot.y_pos) >= 2:
            self.y_pos += 1 if self.y_pos < knot.y_pos else -1

            if self.x_pos != knot.x_pos:
                self.x_pos += 1 if self.x_pos < knot.x_pos else -1

    def __str__(self) -> str:
        return f"x:{self.x_pos},y:{self.y_pos}"


class Grid(object):
    def __init__(self):
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0
        self.min_y = 0
        self.tail_visited_positions = {}

    def _update_grid_size(self, x_pos: int, y_pos: int):
        if x_pos < self.min_x:
            self.min_x = x_pos
        elif x_pos > self.max_x:
            self.max_x = x_pos

        if y_pos < self.min_y:
            self.min_y = y_pos
        elif y_pos > self.max_y:
            self.max_y = y_pos

    def update(self, knots: list[Knot]):
        self._update_grid_size(knots[0].x_pos, knots[0].y_pos)
        self.tail_visited_positions[
            (knots[NB_OF_KNOTS - 1].x_pos, knots[NB_OF_KNOTS - 1].y_pos)
        ] = 1

        if DRAW_GRID:
            for row in range(self.min_y, self.max_y + 1):
                drawing_row = ""
                for col in range(self.min_x, self.max_x + 1):
                    found = False
                    for i, k in enumerate(knots):
                        if col == k.x_pos and row == k.y_pos:
                            if i == 0:
                                drawing_row += "H"
                            else:
                                drawing_row += str(i)
                            found = True
                            break
                    if not found:
                        drawing_row += "."

                print(drawing_row)

            print("\r")

    @property
    def number_of_tail_visited_positions(self):
        return len(self.tail_visited_positions)


class Rope(object):
    def __init__(self) -> None:
        self.knots = [Knot(i == 0) for i in range(NB_OF_KNOTS)]

    def move_to(self, movement: Movement, grid: Grid):
        if DRAW_GRID:
            print(f"{movement}")
        for _ in range(movement.step):
            self.knots[0].move_to_direction(movement.direction)
            for i in range(1, len(self.knots)):
                self.knots[i].move_to_knot(self.knots[i - 1])
                grid.update(self.knots)

        return self


def print_header():
    print("================")
    print("= AoC - Day 09 =")
    print("================")


def round_1(filename: str):

    with open(filename) as f:
        grid = Grid()
        rope = Rope()
        [rope.move_to(Movement(line.strip()), grid) for line in f.readlines()]
        print(f"number_of_visited_positions: {grid.number_of_tail_visited_positions}")


def main():
    print_header()
    round_1(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
