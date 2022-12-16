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
        min_x = min(min(rocks,key=itemgetter(0))[0], min_x)
        max_x = max(max(rocks,key=itemgetter(0))[0], max_x)
        max_depth = max(max(rocks,key=itemgetter(1))[1], max_depth)

        for y in range(max_depth + 1):
            for x in range(min_x, max_x + 1):
                symb = "#" if (x, y) in rocks else "."
                print(symb, end="")
            print("\r")


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
