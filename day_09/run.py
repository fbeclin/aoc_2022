import timeit
from typing import Iterable

INPUT_FILEPATH = "./example.txt"


def print_header():
    print("================")
    print("= AoC - Day 09 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
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
