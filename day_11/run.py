import timeit
import re

INPUT_FILEPATH = "./input1.txt"


class Monkey(object):
    def __init__(
        self,
        items,
        operation: str,
    ) -> None:
        self.items = items


def get_operation(operation: str):
    match = re.match("Operation: new = (\d+|old) (\+|\*\-\/) (\d+|old)", operation)
    if match:

        def handle(old: int) -> int:
            var_1 = int(match[1]) if match[1] == "old" else old
            var_2 = int(match[3]) if match[3] == "old" else old

            match match[2]:
                case "+":
                    return var_1 + var_2
                case "-":
                    return var_1 - var_2
                case "*":
                    return var_1 * var_2
                case "/":
                    return var_1 / var_2

        return handle


def print_header():
    print("================")
    print("= AoC - Day 11 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        pass


def main():
    print_header()
    f_op = get_operation("Operation: new = old + 8")
    print(f_op(10))
    # round_1(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
