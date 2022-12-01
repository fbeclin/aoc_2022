import timeit
from itertools import islice


def print_header():
    print("================")
    print("= AoC - Day 01 =")
    print("================")


def read_calories(filename: str):
    # The function readlines() reads the file.
    i = 0
    all_calories = dict()

    with open(filename) as f:
        for line in f:
            calorie = line.strip()
            if calorie == "":
                i += 1
            else:
                current_calory = all_calories.get(i, 0)
                all_calories[i] = current_calory + int(calorie)

    # get max of 3
    # use islice instead of [:3] to avoid copy
    return sum(islice(sorted(all_calories.values(), reverse=True), 3))


def main():
    print_header()
    max_calories = read_calories("./input1.txt")
    print(f"max calories: {max_calories}")


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
