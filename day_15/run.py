from __future__ import annotations
from dataclasses import dataclass
from itertools import chain

# from more_itertools import grouper
import timeit
import re


PATTERN = "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)"
INPUT_FILEPATH = "./example.txt"
# INPUT_FILEPATH = "./input1.txt"

sensors_with_closest_beacon = {}
beacon_with_sensors = {}
sensors_coverage = set([])


# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
def load_sensor(line: str):
    search = re.search(PATTERN, line)
    sensor = (int(search.group(1)), int(search.group(2)))
    beacon = (int(search.group(3)), int(search.group(4)))

    # store relationship and their position
    sensors_with_closest_beacon[sensor] = beacon
    beacon_with_sensors[beacon] = sensor


def print_header():
    print("================")
    print("= AoC - Day 15 =")
    print("================")


def get_coverage(sensor: tuple(int, int), x: tuple(int, int), y: tuple(int, int)):
    beacon = sensors_with_closest_beacon[sensor]
    distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

    for dist in range(distance + 1):
        for col in range(distance + 1 - dist):
            c = (sensor[0] - col, sensor[1] - dist)
            if c not in sensors_coverage:
                sensors_coverage.add(c)

        for col in range(distance + 1 - dist):
            c = (sensor[0] + col, sensor[1] - dist)
            if c not in sensors_coverage:
                sensors_coverage.add(c)

        for col in range(distance + 1 - dist):
            c = (sensor[0] + col, sensor[1] + dist)
            if c not in sensors_coverage:
                sensors_coverage.add(c)

        for col in range(distance + 1 - dist):
            c = (sensor[0] - col, sensor[1] + dist)
            if c not in sensors_coverage:
                sensors_coverage.add(c)


def draw(x, y):
    print(x, y)
    for row in range(y[0], y[1] + 1):
        print(f"{row:4} ", end="")
        for col in range(x[0], x[1] + 1):
            symb = (
                "B"
                if beacon_with_sensors.get((col, row))
                else "S"
                if sensors_with_closest_beacon.get((col, row))
                else "#"
                if (col, row) in sensors_coverage
                else "."
            )
            print(symb, end="")
        print("")


def get_number(row: int, x: tuple(int, int)):
    return len(
        [
            x
            for x in range(x[0], x[1] + 1)
            if beacon_with_sensors.get((x, row))
            or sensors_with_closest_beacon.get((x, row))
            or (x, row) in sensors_coverage
        ]
    ) - 1


def round_1(filename: str):
    with open(filename) as f:
        [load_sensor(line.strip()) for line in f.readlines()]

        min_x = min(
            e[0]
            for e in chain(
                beacon_with_sensors.keys(), sensors_with_closest_beacon.keys()
            )
        )
        max_x = max(
            e[0]
            for e in chain(
                beacon_with_sensors.keys(), sensors_with_closest_beacon.keys()
            )
        )

        min_y = min(
            e[1]
            for e in chain(
                beacon_with_sensors.keys(), sensors_with_closest_beacon.keys()
            )
        )
        max_y = max(
            e[1]
            for e in chain(
                beacon_with_sensors.keys(), sensors_with_closest_beacon.keys()
            )
        )
        x = (min_x, max_x)
        y = (min_y, max_y)

        [get_coverage(s, x, y) for s in sensors_with_closest_beacon.keys()]
        print(get_number(10, x))
        # draw(x, y)


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
