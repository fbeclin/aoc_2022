import timeit
import re


INPUT_FILEPATH = "./input1.txt"
STACK_REGEX = "( {4}|\[([A-Z])\])"
CRANE_REGEX = "move (\d+) from (\d+) to (\d+)"


switch_to_crane = False
stacks = []


def print_header():
    print("================")
    print("= AoC - Day 05 =")
    print("================")


def read_stacks(line: str):
    global switch_to_crane
    if len(line) < 3:
        switch_to_crane = True
    else:
        matches = re.findall(STACK_REGEX, line)
        if len(matches) > 0:
            load_stacks(matches)


def load_stacks(matches: list):
    global stacks
    if not stacks:
        stacks = [[] for _ in range(len(matches))]

    for i, stack in enumerate(matches):
        if stack[1]:
            stacks[i].insert(0, stack[1])


def read_movements(line: str):
    global stacks
    matches = re.findall(CRANE_REGEX, line)[0]
    apply_movement(int(matches[0]), int(matches[1]), int(matches[2]))


def apply_movement(nb_stack: int, from_stack: int, to_stack: int):
    for _ in range(nb_stack):
        stack = stacks[from_stack - 1].pop()
        stacks[to_stack - 1].append(stack)


def get_message():
    global stacks
    print("".join(s[len(s) - 1] for _, s in enumerate(stacks)))


def print_stacks():
    for i, s in enumerate(stacks):
        print(f"{i+1}: {s}")


def round_1(filename: str):
    with open(filename) as f:
        [
            read_movements(line) if switch_to_crane else read_stacks(line)
            for line in f.readlines()
        ]
        get_message()


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
