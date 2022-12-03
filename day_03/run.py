import timeit

INPUT_FILEPATH = "./example.txt"


priority_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQSRTUVWXYZ"


def print_header():
    print("================")
    print("= AoC - Day 03 =")
    print("================")


def get_priority(item_type: str):
    return priority_map.index(item_type) + 1


def find_share_item_type(line: str):
    first_visited_item_type: set = set()
    second_visited_item_type: set = set()
    middle_index = int(len(line) / 2)
    first = line[:middle_index]
    second = line[middle_index + 1 :]

    for _, first_item_type in enumerate(first):
        first_visited_item_type.add(first_item_type)

        # first iteration
        if len(second_visited_item_type) != len(second):
            for _, second_item_type in enumerate(second):
                second_visited_item_type.add(first_item_type)
                if first_item_type == second_item_type:
                    return get_priority(first_item_type)

        else:
            # find by index
            if first_item_type in second_visited_item_type:
                return get_priority(first_item_type)

    for _, second_item_type in enumerate(second_visited_item_type):
        if second_item_type in first_visited_item_type:
            return get_priority(second_item_type)

    # not found
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
