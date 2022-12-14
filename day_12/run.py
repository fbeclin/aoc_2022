from __future__ import annotations
from collections import deque
import timeit

# INPUT_FILEPATH = "./example.txt"
INPUT_FILEPATH = "./input1.txt"
MAX_HEIGHT = 1000

heightmap = []

start: tuple[int, int]
end: tuple[int, int]


def print_header():
    print("================")
    print("= AoC - Day 12 =")
    print("================")


def get_letter_int(pos: tuple[int, int]):
    x, y = pos
    if x >= 0 and x < len(heightmap) and y >= 0 and y < len(heightmap[0]):
        return ord(heightmap[x][y])
    return MAX_HEIGHT


def load_heightmap(line: str):
    global start, end
    row = []
    for i, c in enumerate(line):
        if c == "S":
            start = (len(heightmap), i)
            c = "a"
        elif c == "E":
            end = (len(heightmap), i)
            c = "z"
        row.append(c)
    heightmap.append(row)


def add_neighbors(current: tuple[int, int, int], queue: list, visited: set):
    x, y, depth = current
    for delta in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        dx, dy = delta
        n_pos = (x + dx, y + dy)
        if (
            get_letter_int(n_pos) - get_letter_int((x, y)) <= 1
        ) and n_pos not in visited:
            queue.append((n_pos[0], n_pos[1], depth + 1))
            visited.add(n_pos)


def bfs(start_pos, end_pos):
    visited = set([start_pos])
    x, y = start_pos
    queue = deque([(x, y, 0)])
    while len(queue) > 0:
        current = queue.popleft()
        x, y, depth = current
        if (x, y) == end_pos:
            return depth
        else:
            add_neighbors(current=current, queue=queue, visited=visited)

    return 0


def round_1(filename: str):
    with open(filename) as f:
        [load_heightmap(line.strip()) for line in f.readlines()]
        print(bfs(start_pos=start, end_pos=end))


def round_2(filename: str):
    with open(filename) as f:
        [load_heightmap(line.strip()) for line in f.readlines()]
        paths = []
        for row in range(len(heightmap)):
            for col in range(len(heightmap[0])):
                if heightmap[row][col] == "a":
                    steps = bfs(start_pos=(row, col), end_pos=end)
                    if steps > 0:
                        paths.append(steps)

        print(min(paths))


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
