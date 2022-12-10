from __future__ import annotations
import timeit

INPUT_FILEPATH = "./input1.txt"

CRT_WIDTH = 40
CRT_HEIGHT = 6
MAX_CYCLE = 220
CYCLE_STEP = 40

x_register = [1]
crt_screen = [["."] * CRT_WIDTH for _ in range(CRT_HEIGHT)]


def draw():
    global x_register
    x = x_register[len(x_register) - 2]
    pos = (len(x_register) - 2) % CYCLE_STEP
    if pos == 0:
        print("\r")
        
    print("#" if pos >= x - 1 and pos <= x + 1 else ".", end="", flush=True)




def noop():
    x_register.append(x_register[len(x_register) - 1])
    draw()

def add_x(command: str):
    value = int(command.split(" ")[1])
    x_register.append(x_register[len(x_register) - 1] + value)
    draw()


def run(command: str):
    global x_register
    match command:
        case "noop":
            noop()
        case _:
            noop()
            add_x(command=command)


def print_header():
    print("================")
    print("= AoC - Day 10 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        [run(line.strip()) for line in f.readlines()]
        print("\r")
        print(
            sum([x_register[c - 1] * c for c in range(20, MAX_CYCLE + 1, CYCLE_STEP)])
        )


def main():
    print_header()
    round_1(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
