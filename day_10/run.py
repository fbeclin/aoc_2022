from __future__ import annotations
import timeit

INPUT_FILEPATH = "./example2.txt"

x_register = [1]


def noop():
    global cycle
    x_register.append(x_register[len(x_register) - 1])


def run(command: str):
    global cycle
    global x_register
    match command:
        case "noop":
            noop()
        case _:
            noop()
            value = int(command.split(" ")[1])
            x_register.append(x_register[len(x_register) - 1] + value)


def print_header():
    print("================")
    print("= AoC - Day 10 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        [run(line.strip()) for line in f.readlines()]
        print(sum([x_register[c - 1] * c for c in range(20, 221, 40)]))


def main():
    print_header()
    round_1(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
