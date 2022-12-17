from __future__ import annotations
import functools
from itertools import chain
from operator import itemgetter
from more_itertools import grouper
import timeit
import json

INPUT_FILEPATH = "./example.txt"
# INPUT_FILEPATH = "./input1.txt"

MAX_HEIGHT = 200
MAX_SIZE = 600

SAND_START = (500, 0)

rocks = set([])
sands = set([])


def print_header():
    print("================")
    print("= AoC - Day 14 =")
    print("================")


def to_point(coord: str):
    values = coord.split(",")
    return (int(values[0]), int(values[1]))


def fill_rock_coords(p_from: tuple(int, int), p_to: tuple(int, int)):
    global rocks

    x_start = min(p_from[0], p_to[0])
    x_end = max(p_from[0], p_to[0])

    for x in range(x_start, x_end + 1):
        rocks.add((x, p_from[1]))

    y_start = min(p_from[1], p_to[1])
    y_end = max(p_from[1], p_to[1])

    for y in range(y_start, y_end):
        rocks.add((p_from[0], y))


def to_rock_coords(points: list(tuple(int, int))):
    for i in range(0, len(points) - 1):
        fill_rock_coords(points[i], points[i + 1])


def pour_sand(min_x, max_x, max_depth):
    for i in range(24):
        print("Sand pouring: " + str(i + 1))
        fall = [SAND_START]
        fall_attempts = []

        while True:
            x, y = fall[-1]
            sand = (x, y + 1)
            # print(sand)

            if sand not in rocks and sand not in sands:
                fall.append(sand)
                fall_attempts.clear()
            else:
                fall_attempts.append(sand)
                fall.pop()
                x, y = fall[-1]
                # print("try diagonaly", fall_attempts)
                if len(fall_attempts) == 1:
                    # print("left")
                    fall.append((x - 1, y + 1))
                elif len(fall_attempts) == 2:
                    # print("right")
                    fall.append((x + 1, y + 1))
                else:
                    # print("in rest")
                    fall.append((x, y + 1))
                    break
        sands.add(fall[-1])
        # print(sands)
        draw(min_x=min_x, max_x=max_x, max_depth=max_depth)


def draw(min_x, max_x, max_depth):
    for y in range(max_depth + 1):
        for x in range(min_x, max_x + 1):
            symb = (
                "#"
                if (x, y) in rocks
                else "+"
                if (x, y) == SAND_START
                else "o"
                if (x, y) in sands
                else "."
            )
            print(symb, end="")
        print("\r")


def round_1(filename: str):
    min_x = 1000
    max_x = 0
    max_depth = 0
    with open(filename) as f:
        [
            to_rock_coords(path)
            for path in [
                list(map(to_point, line.strip().split(" -> ")))
                for line in f.readlines()
            ]
        ]
        min_x = min(min(rocks, key=itemgetter(0))[0], min_x)
        max_x = max(max(rocks, key=itemgetter(0))[0], max_x)
        max_depth = max(max(rocks, key=itemgetter(1))[1], max_depth)

        pour_sand(min_x=min_x, max_x=max_x, max_depth=max_depth)


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
