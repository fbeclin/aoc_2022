from __future__ import annotations
import functools
from itertools import chain
from more_itertools import grouper
import timeit
import json

# INPUT_FILEPATH = "./example.txt"
INPUT_FILEPATH = "./input1.txt"
dividers = [[[2]], [[6]]]


def compare_v2(left: any, right: any) -> int:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        return 0

    if isinstance(left, int):
        return compare_v2([left], right)
    elif isinstance(right, int):
        return compare_v2(left, [right])

    if isinstance(left, list) and isinstance(right, list):
        for i in range(min(len(left), len(right))):
            c = compare_v2(left[i], right[i])
            if c != 0:
                return c
        if len(left) < len(right):
            return -1
        elif len(left) > len(right):
            return 1
        else:
            return 0


def print_header():
    print("================")
    print("= AoC - Day 13 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        indices = [
            i + 1
            for i, pair in enumerate(
                [
                    json.loads(
                        '{ "left":'
                        + lines[0].strip()
                        + ', "right":'
                        + lines[1].strip()
                        + " }"
                    )
                    for lines in grouper(f, 3, fillvalue="")
                ]
            )
            if compare_v2(pair["left"], pair["right"]) == -1
        ]
        print(indices)
        print(sum(indices))


def get_packet_value(item: dict):
    return item["packet"]


def round_2(filename: str):
    with open(filename) as f:
        packets = sorted(
            map(
                get_packet_value,
                chain(
                    [
                        json.loads('{ "packet":' + line.strip() + " }")
                        for line in f.readlines()
                        if len(line.strip()) > 0
                    ],
                    [json.loads('{ "packet":' + str(dividers[0]) + " }")],
                    [json.loads('{ "packet":' + str(dividers[1]) + " }")],
                ),
            ),
            key=functools.cmp_to_key(compare_v2),
        )
        print((packets.index(dividers[0]) + 1) * (packets.index(dividers[1]) + 1))


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
