import timeit

INPUT_FILEPATH = "./example.txt"


def print_header():
    print("================")
    print("= AoC - Day 04 =")
    print("================")


def get_range_as_set(range_from_file: str) -> set:
    range_values = range_from_file.split("-")
    return range(int(range_values[0]), int(range_values[1]))


def is_fully_contained(ranges: list):
    first_range_set = set(get_range_as_set(ranges[0]))
    second_range_set = set(get_range_as_set(ranges[1]))
    first_set_len = len(first_range_set)
    second_set_len = len(second_range_set)

    first_range_set.intersection_update(second_range_set)
    return (
        len(first_range_set) == first_set_len or len(first_range_set) == second_set_len
    )


def round_1(filename: str):
    with open(filename) as f:
        sum_fully_countained = sum(
            [is_fully_contained(line.strip().split(",")) for line in f.readlines()]
        )
        print(f"sum_fully_countained: {sum_fully_countained}")


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
