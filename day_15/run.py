from __future__ import annotations
from itertools import chain

# from more_itertools import grouper
import timeit
import re


PATTERN = "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)"
# INPUT_FILEPATH = "./example.txt"
INPUT_FILEPATH = "./input1.txt"

sensors = {}


# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
def load_sensor(line: str):
    search = re.search(PATTERN, line)
    sensor = (int(search.group(1)), int(search.group(2)))
    beacon = (int(search.group(3)), int(search.group(4)))

    # store relationship and their position
    sensors[sensor] = beacon


def print_header():
    print("================")
    print("= AoC - Day 15 =")
    print("================")


def get_row_coverage(row:int):
    row_range = []
    for sensor in sensors.keys():
        # get beacon
        beacon = sensors[sensor]
        # manatthan dist = |Xb - Xa| + |Yb - Ya|
        # dist between beacon and sensor
        dist = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

        x_range = dist - abs(sensor[1] - row)
        if x_range > 0:
            # both sides
            row_range.append((sensor[0] - x_range, sensor[0] + x_range ))

    # find min and max
    r = sorted(list(chain(*row_range)))
    return r[len(r) -1] - r[0]


def round_1(filename: str):
    with open(filename) as f:
        [load_sensor(line.strip()) for line in f.readlines()]

        min_x = min(e[0] for e in chain(sensors.values(), sensors.keys()))
        max_x = max(e[0] for e in chain(sensors.values(), sensors.keys()))

        min_y = min(e[1] for e in chain(sensors.values(), sensors.keys()))
        max_y = max(e[1] for e in chain(sensors.values(), sensors.keys()))
        x = (min_x, max_x)
        y = (min_y, max_y)
        print(x, y)
        print("row coverage: " + str(get_row_coverage(2000000)))



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
