from __future__ import annotations
import timeit

INPUT_FILEPATH = "./example.txt"


def print_header():
    print("================")
    print("= AoC - Day 08 =")
    print("================")


def to_np_array(line: str):
    return map(int, list(line.strip()))


def round_1(filename: str):
    array = None
    with open(filename) as f:
        grid = [list(to_np_array(line)) for line in f.readlines()]
        print(grid)
        


def round_2(filename: str):
    pass


def main():
    print_header()
    round_1(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
