import timeit


def print_header():
    print("================")
    print("= AoC - Day 06 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        pass
        # [
        #     read_movements(line, True) if switch_to_crane else read_stacks(line)
        #     for line in f.readlines()
        # ]


def round_2(filename: str):
    with open(filename) as f:
        pass
        # [
        #     read_movements(line, True) if switch_to_crane else read_stacks(line)
        #     for line in f.readlines()
        # ]


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
