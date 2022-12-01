import timeit
from itertools import islice

INPUT_FILEPATH = "./input1.txt"


def print_header():
    print("================")
    print("= AoC - Day 01 =")
    print("================")


def insert_sorted_calories(all_calories: list, current_calorie: int):
    i = -1
    if len(all_calories) > 0:
        for i in range(len(all_calories)):
            if current_calorie > all_calories[i]:
                # found
                i -= 1
                break
    all_calories.insert(i + 1, current_calorie)


def read_and_sum_calories(filename: str, head_count: int):
    current_calorie = 0
    all_calories = list()

    with open(filename) as f:
        for line in f:
            calorie = line.strip()
            if calorie == "":
                insert_sorted_calories(
                    all_calories=all_calories, current_calorie=current_calorie
                )
                # reset calorie
                current_calorie = 0
            else:
                current_calorie = current_calorie + int(calorie)

    # get max of 3
    # use islice instead of [:3] to avoid copy
    return sum(islice(all_calories, head_count))


def round_1():
    return read_and_sum_calories(INPUT_FILEPATH, 1)


def round_2():
    return read_and_sum_calories(INPUT_FILEPATH, 3)


def main():
    print_header()
    # max_calories = round_1()
    max_calories = round_2()
    print(f"max calories: {max_calories}")


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
