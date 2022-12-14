from __future__ import annotations
from more_itertools import grouper
import timeit
import json

INPUT_FILEPATH = "./example.txt"
# INPUT_FILEPATH = "./input1.txt"


def compare(left: list, right: list, depth: int = 0):
    left_padding = " "*depth
    print(f"{left_padding}- Compare {left} vs {right}")
    i = 0
    while i < len(left) and i < len(right):
        if isinstance(left[i], int) and isinstance(right[i], int):
            left_padding = " "*(depth+1)
            print(f"{left_padding}- Compare {left[i]} vs {right[i]}")

            if left[i] > right[i]:
                left_padding = " "*(depth+2)
                print(f"{left_padding}- Right side is smaller, so inputs are NOT in the right order")
                return False
            elif left[i] < right[i]:
                left_padding = " "*(depth+2)
                print(f"{left_padding}- Left side is smaller, so inputs are in the right order")
                return True
        elif isinstance(left[i], list) and isinstance(right[i], list):
            left_padding = " "*(depth+1)
            return compare(left[i], right[i], depth+1)
        else:
            left_padding = " "*(depth+1)
            if isinstance(left[i], int):
                print(f"{left_padding}- Mixed types; convert left to [{left[i]}] and retry comparison")
                return compare([left[i]], right[i], depth+1)
            else:
                print(f"{left_padding}- Mixed types; convert right to [{right[i]}] and retry comparison")
                return compare(left[i], [right[i]], depth+1)
        i+=1

    if i != len(left) and i >= len(right):
        left_padding = " "*(depth+1)
        print(f"{left_padding}- Right side ran out of items, so inputs are NOT in the right order")
        return False
    left_padding = " "*(depth+1)
    print(f"{left_padding}- Left side ran out of items, so inputs are in the right order")
    return True


def print_header():
    print("================")
    print("= AoC - Day 13 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:

        i = 1
        for pair in [
            json.loads("{ \"left\":" + lines[0].strip() +  ", \"right\":" + lines[1].strip() + " }")
            for lines in grouper(f, 3, fillvalue="")
        ]:
            print(f"== Pair {i} ==")
            compare(pair["left"],pair["right"])
            print("")
            i+=1
        pass


def round_2(filename: str):
    with open(filename) as f:
        pass


def main():
    print_header()
    round_1(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
