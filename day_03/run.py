import timeit
from string import ascii_letters

INPUT_FILEPATH = "./input1.txt"


def print_header():
    print("================")
    print("= AoC - Day 03 =")
    print("================")


def get_priority(item_type: str):
    return ascii_letters.index(item_type) + 1


def find_share_item_type(line: str):
    middle_index = int(len(line) / 2)
    first_compartiment = set(line[:middle_index])
    second_compartiment = set(line[middle_index:])
    # intersection
    intersect = first_compartiment.intersection(second_compartiment)
    return get_priority(intersect.pop()) if intersect else 0


def find_share_item_type_2(group: list):
    # intersection
    intersect = (group[0] & (group[1])) & group[2]
    priority = get_priority(intersect.pop()) if intersect else 0
    return priority


def round_1(filename: str):
    with open(filename) as f:
        sum_priorities = sum(
            [find_share_item_type(line.strip()) for line in f.readlines()]
        )
        print(f"sum_priorities: {sum_priorities}")


def round_2(filename: str):
    with open(filename) as f:
        sum_priorities = sum(
            [
                find_share_item_type_2(group)
                for group in zip(
                    *[iter([set(line.strip()) for line in f.readlines()])] * 3
                )
            ]
        )
        print(f"sum_priorities: {sum_priorities}")


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
