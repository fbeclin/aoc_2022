from __future__ import annotations
from dataclasses import dataclass

# from more_itertools import grouper
import timeit
import re


PATTERN = "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)"
INPUT_FILEPATH = "./example.txt"
# INPUT_FILEPATH = "./input1.txt"


@dataclass
class Sensor(object):
    x: int
    y: int
    beacon: Beacon


@dataclass
class Beacon(object):
    x: int
    y: int


# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
def load_sensor(line: str):
    print(line)
    search = re.search(PATTERN, line)
    return Sensor(
        x=search.group(1),
        y=search.group(2),
        beacon=Beacon(x=search.group(3), y=search.group(4)),
    )


def print_header():
    print("================")
    print("= AoC - Day 15 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        [print(load_sensor(line.strip())) for line in f.readlines()]
        pass


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
