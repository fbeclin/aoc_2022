from __future__ import annotations
import timeit

INPUT_FILEPATH = "./example.txt"
MAX_HEIGHT = 1000

heightmap = []
start: Height
end: Height


def get_letter_int(pos: tuple[int, int]):
    x, y = pos
    if x >= 0 and x < len(heightmap) and y >= 0 and y < len(heightmap[0]):
        return ord(heightmap[x][y])
    return MAX_HEIGHT


class Height(object):
    def __init__(self, pos: tuple[int, int]) -> None:
        self.pos = pos
        self.neighbors: list[Height] = []
        self.visited = {}

    def _add_neighbor(self, n_pos: tuple[int, int], pos: tuple[int, int]):
        print(n_pos, pos)
        print(get_letter_int(n_pos), get_letter_int(pos))
        if (
            get_letter_int(n_pos) - get_letter_int(pos) <= 1
        ) and n_pos not in self.visited:
            self.neighbors.append(Height(n_pos))
            self.visited[n_pos] = 1

    def climb(self):
        x_pos, y_pos = self.pos
        # left
        self._add_neighbor((x_pos - 1, y_pos), self.pos)
        # right
        self._add_neighbor((x_pos + 1, y_pos), self.pos)
        # top
        self._add_neighbor((x_pos, y_pos - 1), self.pos)
        # bottom
        self._add_neighbor((x_pos, y_pos + 1), self.pos)

    def __str__(self) -> str:
        return str(self.pos)

    def __repr__(self) -> str:
        return self.__str__()

def print_header():
    print("================")
    print("= AoC - Day 12 =")
    print("================")


def load_heightmap(line: str):
    global start, end
    row = []
    for i, c in enumerate(line):
        if c == "S":
            start = Height((len(heightmap), i))

            c = "a"
        elif c == "E":
            end = Height((len(heightmap), i))

            c = "z"
        row.append(c)
    heightmap.append(row)


def find_path():
    start.climb()


def round_1(filename: str):
    with open(filename) as f:
        [load_heightmap(line.strip()) for line in f.readlines()]
        print("start:" + str(start) + " / end:" + str(end))
        find_path()
        print(start.neighbors)


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
