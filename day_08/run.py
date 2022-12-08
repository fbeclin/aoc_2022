import timeit
from typing import Iterable

INPUT_FILEPATH = "./input1.txt"


def print_header():
    print("================")
    print("= AoC - Day 08 =")
    print("================")


def find_tallest(grid: list[list], col: int, row: int):
    current_tree_height = grid[row][col]
    left = grid[row][:col]
    right = grid[row][col + 1 :]
    top = [grid[i][col] for i in range(row)]
    bottom = [grid[i][col] for i in range(row + 1, len(grid))]

    return (
        (left and max(left) < current_tree_height)
        or (right and max(right) < current_tree_height)
        or (top and max(top) < current_tree_height)
        or (bottom and max(bottom) < current_tree_height)
    )


def sum_until(iter: Iterable, ref_value: int):
    nb_tree = 0
    for _, v in iter:
        if v < ref_value:
            nb_tree += 1
        else:
            if v == ref_value:
                nb_tree += 1
            break
    return nb_tree


def calc_viewing_score(grid: list[list], col: int, row: int):
    current_tree_height = grid[row][col]
    left = sum_until(enumerate(reversed(grid[row][:col])), current_tree_height)
    right = sum_until(enumerate(grid[row][col + 1 :]), current_tree_height)
    top = sum_until(
        enumerate(reversed([grid[i][col] for i in range(row)])), current_tree_height
    )
    bottom = sum_until(
        enumerate([grid[i][col] for i in range(row + 1, len(grid))]),
        current_tree_height,
    )
    return left * right * top * bottom


def round_1(filename: str):
    with open(filename) as f:
        grid = [list(map(int, list(line.strip()))) for line in f.readlines()]

        nb_visible_trees = 0
        for col in range(1, len(grid) - 1):
            for row in range(1, len(grid) - 1):
                nb_visible_trees += 1 if find_tallest(grid, col=col, row=row) else 0

        nb_visible_trees += (len(grid) - 1) * 4
        print(f"nb_visible_trees: {nb_visible_trees}")


def round_2(filename: str):
    highest_scenic_score = 0
    with open(filename) as f:
        grid = [list(map(int, list(line.strip()))) for line in f.readlines()]
        for col in range(len(grid)):
            for row in range(len(grid)):
                current_scenic_score = calc_viewing_score(grid, col=col, row=row)
                if current_scenic_score > highest_scenic_score:
                    highest_scenic_score = current_scenic_score
    print(f"highest_scenic_score: {highest_scenic_score}")


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
