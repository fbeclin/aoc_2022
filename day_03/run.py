import timeit

INPUT_FILEPATH = "./input1.txt"


priority_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def print_header():
    print("================")
    print("= AoC - Day 03 =")
    print("================")


def get_priority(item_type: str):
    priority = priority_map.index(item_type) + 1
    return priority


def find_share_item_type(line: str):
    middle_index = int(len(line) / 2)
    first_compartiment = set(line[:middle_index])
    second_compartiment = set(line[middle_index:])
    # intersection
    intersect = first_compartiment.intersection(second_compartiment)
    if intersect:
        return get_priority(intersect.pop())

    return 0


def round_1(filename: str):
    with open(filename) as f:
        sum_priorities = sum(
            [find_share_item_type(line.strip()) for line in f.readlines()]
        )
        print(f"sum_priorities: {sum_priorities}")


def round_2():
    pass


def main():
    print_header()
    round_1(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
