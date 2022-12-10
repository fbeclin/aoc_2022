from __future__ import annotations
import timeit

INPUT_FILEPATH = "./input1.txt"


def print_header():
    print("================")
    print("= AoC - Day 10 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        pass


def main():
    print_header()
    round_1(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")