import timeit

INPUT_FILEPATH = "./input1.txt"
DRAW_GRID = False


class Movement(object):
    def __init__(self, line: str) -> None:
        values = line.split(" ")
        self.direction = values[0]
        self.step = int(values[1])

    def __str__(self) -> str:
        return f"direction: {self.direction} , step: {self.step}"


class Head(object):
    def __init__(self) -> None:
        self.x_pos = 0
        self.y_pos = 0

    def move_to(self, direction: str):
        match direction:
            case "R":
                self.x_pos += 1
            case "L":
                self.x_pos -= 1
            case "U":
                self.y_pos -= 1
            case "D":
                self.y_pos += 1

    def __str__(self) -> str:
        return f"x: {self.x_pos} , y: {self.y_pos}"


class Tail(object):
    def __init__(self) -> None:
        self.x_pos = 0
        self.y_pos = 0

    def move_to(self, head: Head):
        if abs(self.x_pos - head.x_pos) >= 2:
            self.x_pos += 1 if self.x_pos < head.x_pos else -1

            if self.y_pos != head.y_pos:
                self.y_pos += 1 if self.y_pos < head.y_pos else -1

        if abs(self.y_pos - head.y_pos) >= 2:
            self.y_pos += 1 if self.y_pos < head.y_pos else -1

            if self.x_pos != head.x_pos:
                self.x_pos += 1 if self.x_pos < head.x_pos else -1


class Grid(object):
    def __init__(self):
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0
        self.min_y = 0
        self.tail_visited_positions = {}

    def _update_coord(self, x_pos: int, y_pos: int):
        if x_pos < self.min_x:
            self.min_x = x_pos
        elif x_pos > self.max_x:
            self.max_x = x_pos

        if y_pos < self.min_y:
            self.min_y = y_pos
        elif y_pos > self.max_y:
            self.max_y = y_pos

    def update(self, head: Head, tail: Tail):
        self._update_coord(head.x_pos, head.y_pos)
        self.tail_visited_positions[(tail.x_pos, tail.y_pos)] = 1

        if DRAW_GRID:
            for row in range(self.min_y, self.max_y + 1):
                drawing_row = ""
                for col in range(self.min_x, self.max_x + 1):
                    if col == head.x_pos and row == head.y_pos:
                        drawing_row += "H"
                    elif col == tail.x_pos and row == tail.y_pos:
                        drawing_row += "T"
                    else:
                        drawing_row += "."

                print(drawing_row)

            print("\r")

    @property
    def number_of_tail_visited_positions(self):
        return len(self.tail_visited_positions)


class Rope(object):
    def __init__(self) -> None:
        self.head = Head()
        self.tail = Tail()
        print(f"H:{self.head}")

    def move_head_to(self, movement: Movement, grid: Grid):
        if DRAW_GRID:
            print(f"{movement}")
        for _ in range(movement.step):
            self.head.move_to(movement.direction)
            self._move_tail_to_head()
            grid.update(self.head, self.tail)

        return self

    def _move_tail_to_head(self):
        self.tail.move_to(self.head)


def print_header():
    print("================")
    print("= AoC - Day 09 =")
    print("================")


def round_1(filename: str):

    with open(filename) as f:
        grid = Grid()
        rope = Rope()
        [rope.move_head_to(Movement(line.strip()), grid) for line in f.readlines()]
        print(f"number_of_visited_positions: {grid.number_of_tail_visited_positions}")


def round_2(filename: str):
    with open(filename) as f:
        pass


def main():
    print_header()
    round_1(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
