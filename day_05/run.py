import timeit

INPUT_FILEPATH = "./input1.txt"


def print_header():
    print("================")
    print("= AoC - Day 05 =")
    print("================")


def round_1(filename: str):
    pass
    # with open(filename) as f:
    #     sum_fully_countained = sum(
    #         [is_fully_contained(line.strip().split(",")) for line in f.readlines()]
    #     )
    #     print(f"sum_fully_countained: {sum_fully_countained}")


def round_2(filename: str):
    pass


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
