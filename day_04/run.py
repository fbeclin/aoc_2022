import timeit

INPUT_FILEPATH = "./input1.txt"


def print_header():
    print("================")
    print("= AoC - Day 04 =")
    print("================")


def get_range_as_set(range_from_file: str):
    range_values = range_from_file.split("-")
    return set(range(int(range_values[0]), int(range_values[1]) + 1))


def is_fully_contained(ranges: list):
    first_range_set = get_range_as_set(ranges[0])
    second_range_set = get_range_as_set(ranges[1])
    first_set_len = len(first_range_set)
    second_set_len = len(second_range_set)

    first_range_set.intersection_update(second_range_set)
    return (
        len(first_range_set) == first_set_len or len(first_range_set) == second_set_len
    )


def overlap(ranges: list):
    first_range_set = set(get_range_as_set(ranges[0]))
    second_range_set = set(get_range_as_set(ranges[1]))
    first_range_set.intersection_update(second_range_set)
    return len(first_range_set) != 0


def round_1(filename: str):
    with open(filename) as f:
        sum_fully_countained = sum(
            [is_fully_contained(line.strip().split(",")) for line in f.readlines()]
        )
        print(f"sum_fully_countained: {sum_fully_countained}")


def round_1_no_set(filename: str):
    with open(filename) as f:
        sum_fully_countained = sum(
            [
                is_fully_contained_no_set(line.strip().split(","))
                for line in f.readlines()
            ]
        )
        print(f"sum_fully_countained: {sum_fully_countained}")


def round_2(filename: str):
    with open(filename) as f:
        sum_overlap = sum([overlap(line.strip().split(",")) for line in f.readlines()])
        print(f"sum_overlap: {sum_overlap}")


def round_2_no_set(filename: str):
    with open(filename) as f:
        sum_overlap = sum(
            [overlap_no_set(line.strip().split(",")) for line in f.readlines()]
        )
        print(f"sum_overlap: {sum_overlap}")


def get(range_from_file: str):
    range_split = range_from_file.split("-")
    return [int(range_split[0]), int(range_split[1])]


def is_range_contained_in_other(first_range, second_range):
    return (
        first_range[0] >= second_range[0]
        and first_range[0] <= second_range[1]
        and first_range[1] >= second_range[0]
        and first_range[1] <= second_range[1]
    )


def is_fully_contained_no_set(ranges: list):
    range_1 = get(ranges[0])
    range_2 = get(ranges[1])

    # range 1 contained
    if is_range_contained_in_other(range_1, range_2):
        return True

    # range 2 contained
    if is_range_contained_in_other(range_2, range_1):
        return True

    return False


def overlap_no_set(ranges: list):
    range_1 = get(ranges[0])
    range_2 = get(ranges[1])

    return not (range_1[1] < range_2[0] or range_1[0] > range_2[1])


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    # round_1_no_set(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)
    round_2_no_set(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
