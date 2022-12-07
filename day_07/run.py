from __future__ import annotations
import timeit
import re

INPUT_FILEPATH = "./input1.txt"

COMMAND_REGEX = "^\$ ([a-z]+) ?(.+)?"
LS_FILE_REGEX = "^([0-9]+) (.+)"
SIZE_THRESHOLD = 100000
MIN_REQUIRED_SIZE = 30000000
TOTAL_SYSTEM_SIZE = 70000000


class Folder(object):
    def __init__(self, name: str, parent_folder: Folder | None) -> None:
        self.name = name
        self.size = 0
        self.parent_folder = parent_folder

    def __str__(self) -> str:
        return self.name


current_folder: Folder = None
sum_size_threshold = 0
folder_sizes = []


def print_header():
    print("================")
    print("= AoC - Day 07 =")
    print("================")


def read_command(command: str):
    match = re.match(COMMAND_REGEX, command)
    if match:
        if match[1] == "cd":
            if match[2] != "..":
                go_into_folder(match[2])
            else:
                go_into_parent_folder()
    else:
        match = re.match(LS_FILE_REGEX, command)
        if match:
            current_folder.size += int(match[1])


def go_into_folder(foldername: str):
    global current_folder
    folder = Folder(foldername, current_folder)
    current_folder = folder


def go_into_parent_folder():
    global current_folder
    global sum_size_threshold

    if current_folder.parent_folder != None:
        folder_sizes.append(current_folder.size)
        if current_folder.size < SIZE_THRESHOLD:
            sum_size_threshold += current_folder.size

        current_folder.parent_folder.size += current_folder.size
        current_folder = current_folder.parent_folder


def go_back_to_root():
    global sum_size_threshold
    while current_folder.parent_folder != None:
        go_into_parent_folder()


def round_1(filename: str):
    with open(filename) as f:
        [read_command(line.strip()) for line in f.readlines()]
    go_back_to_root()
    print(f"sum_size_threshold: {sum_size_threshold}")


def round_2(filename: str):
    round_1(filename)
    for _, v in enumerate(sorted(folder_sizes)):
        if current_folder.size - v <= (TOTAL_SYSTEM_SIZE - MIN_REQUIRED_SIZE):
            print(f"folder_size_to_delete: {v}")
            break


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
