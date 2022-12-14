from __future__ import annotations
from more_itertools import grouper
import timeit
import json

INPUT_FILEPATH = "./example.txt"
# INPUT_FILEPATH = "./input1.txt"


def compare(left: list, right: list, depth: int = 0):
    i = 0
    while i < len(left) and i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True
        elif isinstance(left[i], list) and isinstance(right[i], list):
            return compare(left[i], right[i], depth + 1)
        else:
            if isinstance(left[i], int):
                return compare([left[i]], right[i], depth + 1)
            else:
                return compare(left[i], [right[i]], depth + 1)
        i += 1

    if i != len(left) and i >= len(right):
        return False
    return True


def print_header():
    print("================")
    print("= AoC - Day 13 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        i = 1
        for pair in [
            json.loads(
                '{ "left":' + lines[0].strip() + ', "right":' + lines[1].strip() + " }"
            )
            for lines in grouper(f, 3, fillvalue="")
        ]:
            print(f"== Pair {i} ==")
            compare(pair["left"], pair["right"])
            print("")
            i += 1


def round_1_without_print(filename: str):
    with open(filename) as f:
        print(
            sum(
                i+1
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
                if compare(pair["left"], pair["right"])
            )
        )


def round_2(filename: str):
    with open(filename) as f:
        pass


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_1_without_print(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
