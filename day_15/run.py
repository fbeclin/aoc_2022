from __future__ import annotations
from itertools import chain
from multiprocessing import Pool

# from more_itertools import grouper
import timeit
import re


PATTERN = "Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)"
# INPUT_FILEPATH = "./example.txt"
INPUT_FILEPATH = "./input1.txt"

sensors = {}
beacons = {}
distances = {}

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
def load_sensor(line: str):
    search = re.search(PATTERN, line)
    sensor = (int(search.group(1)), int(search.group(2)))
    beacon = (int(search.group(3)), int(search.group(4)))

    # store relationship and their position
    sensors[sensor] = beacon
    # store manathan distance
    distance = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
    distances[sensor] = distance


def find_excluded_beacon(max_row: int):
    for s, sensor in enumerate(sensors.keys()):
        x,y = sensor
        distance = distances[sensor] + 1
        print(s, " sensor:", sensor)

        for i in range(distance + 1):
            if (x - distance + i >= 0):
                if (y - i >= 0) :
                    # left-top
                    point_to_check = (x - distance + i, y - i )
                    # print("# left-top:" + str(point_to_check))
                    if not is_covered_by_another_sensor(point_to_check, sensor):
                        return point_to_check
                if (y + i <= max_row) :
                    # left-bottom
                    point_to_check = (x - distance + i, y + i )
                    # print("# left-bottom:" + str(point_to_check))
                    if not is_covered_by_another_sensor(point_to_check, sensor):
                        return point_to_check
            
            if (x + distance - i <= max_row):
                if (y - i >= 0) :
                    # right-top
                    point_to_check = (x + distance - i, y - i )
                    # print("# right-top:" + str(point_to_check))
                    if not is_covered_by_another_sensor(point_to_check, sensor):
                        return point_to_check
                if (y + i <= max_row) :
                    # right-bottom
                    point_to_check = (x + distance - i, y + i )
                    # print("# right-bottom:" + str(point_to_check))
                    if not is_covered_by_another_sensor(point_to_check, sensor):
                        return point_to_check


def is_covered_by_another_sensor(point_to_check: tuple(int,int), current_sensor: tuple(int, int)):
    for sensor in sensors.keys():
        if sensor != current_sensor:
            # get distance of current sensor
            dist = distances[sensor]
            # get distance from point_to_check to current sensor
            distance = abs(point_to_check[0] - sensor[0]) + abs(point_to_check[1] - sensor[1])
            if distance <= dist:
                # covered
                return True

    return False

def print_header():
    print("================")
    print("= AoC - Day 15 =")
    print("================")


def get_row_coverage(row: int, max_range: int, range_set: set):
    range_list = []
    for sensor in sensors.keys():
        # get beacon
        beacon = sensors[sensor]
        # manatthan dist = |Xb - Xa| + |Yb - Ya|
        # dist between beacon and sensor
        dist = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])

        x_range = dist - abs(sensor[1] - row)
        if x_range > 0:
            start_time = timeit.default_timer()
            # both sides but with boundaries
            new_left_x = sensor[0] - x_range
            new_right_x = sensor[0] + x_range
            [
                range_list.append(i)
                for i in range(
                    new_left_x if new_left_x > 0 else 0,
                    new_right_x + 1 if new_right_x < max_range else max_range + 1,
                )
            ]
            print(f"Execution time : {timeit.default_timer() - start_time}")

    return range_set.difference(range_list)





def round_1(filename: str):
    with open(filename) as f:
        [load_sensor(line.strip()) for line in f.readlines()]
        print("row coverage: " + str(get_row_coverage(2000000)))


def round_2(filename: str):
    max_range = 4000000
    with open(filename) as f:
        [load_sensor(line.strip()) for line in f.readlines()]
        beacon = find_excluded_beacon(max_range)
        print("distress_beacon: ", beacon[0]*max_range + beacon[1])

def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
