import timeit

INPUT_FILEPATH = "./example.txt"


class Movement(object):
    def __init__(self, line: str) -> None:
        values = line.split(" ")
        self.direction = values[0]
        self.step = int(values[1])

    def __str__(self) -> str:
        return f"direction: {self.direction} , step: {self.step}"


class Rope(object):
    def __init__(self) -> None:
        self.head = Head()
        self.tail = Tail()
        print(f"H:{self.head}")

    def move_head_to(self, movement: Movement):
        print(f"{movement}")
        for _ in range(movement.step):
            self.head.move_to(movement.direction)

        print(f"H:{self.head}")
        return self

    def _move_tail_to(self):
        pass


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
        pass


class Grid(object):
    def __init__(self):
        self.max_x = 0
        self.max_y = 0
        self.min_x = 0
        self.min_y = 0

    def _update_coord(self, x_pos: int, y_pos: int):
        if x_pos < self.min_x:
            self.min_x = x_pos
        elif x_pos > self.max_x:
            self.max_x = x_pos

        if y_pos < self.min_y:
            self.min_y = y_pos
        elif y_pos > self.max_y:
            self.max_y = y_pos

    def draw(self, rope: Rope):
        self._update_coord(rope.head.x_pos, rope.head.y_pos)

        for row in range(self.min_y, self.max_y + 1):
            drawing_row = ""
            for col in range(self.min_x, self.max_x + 1):
                if col == rope.head.x_pos and row == rope.head.y_pos:
                    drawing_row += "H"
                elif col == rope.tail.x_pos and row == rope.tail.y_pos:
                    drawing_row += "T"
                else:
                    drawing_row += "."
            
            print(drawing_row)

        print("\r")


visited_positions = {}


def print_header():
    print("================")
    print("= AoC - Day 09 =")
    print("================")


def round_1(filename: str):
    
    with open(filename) as f:
        grid = Grid()
        rope = Rope()
        [grid.draw(rope.move_head_to(Movement(line.strip()))) for line in f.readlines()]


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
