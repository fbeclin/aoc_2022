from __future__ import annotations
from io import TextIOWrapper
import timeit
import re

INPUT_FILEPATH = "./example.txt"
PRINT = True


class Monkey(object):
    def __init__(
        self,
        items: list[int],
        operation_fct: any,
    ) -> None:
        self.items = items
        self.operation_fct = operation_fct

    def inspect_and_throw(self, monkeys: list[Monkey]):
        while self.items:
            result = self.operation_fct(self.items[0])
            monkeys[result[0]].items.append(result[1])
            del self.items[0]

def get_operation(
    operation: str, divisible_by: int, to_monkey_if_true: int, to_monkey_if_false: int
):
    match = re.match("(\d+|old) (\+|\*|\-|\/) (\d+|old)", operation)
    if not match:
        raise ValueError("Invalid operation")

    def handle(current_worry: int) -> int:
        var_1 = int(match[1]) if match[1] != "old" else current_worry
        var_2 = int(match[3]) if match[3] != "old" else current_worry

        new_worry = 0
        match match[2]:
            case "+":
                new_worry = var_1 + var_2
            case "-":
                new_worry = var_1 - var_2
            case "*":
                new_worry = var_1 * var_2
            case "/":
                new_worry = var_1 / var_2

        new_worry = int(new_worry / 3)

        return (
            (to_monkey_if_true, new_worry)
            if new_worry % divisible_by == 0
            else (to_monkey_if_false, new_worry)
        )

    return handle


def read(f: TextIOWrapper, prefix: str):
    return f.readline().removeprefix(prefix).strip()


def get_monkey(line: str, f: TextIOWrapper):
    if line.startswith("Monkey"):
        starting_items = list(map(int, read(f, "  Starting items: ").split(",")))
        operation = get_operation(
            read(f, "  Operation: new = "),
            int(read(f, "  Test: divisible by ")),
            int(read(f, "    If true: throw to monkey ")),
            int(read(f, "    If false: throw to monkey ")),
        )

        return Monkey(items=starting_items, operation_fct=operation)
    else:
        raise ValueError("Invalid line")


def print_header():
    print("================")
    print("= AoC - Day 11 =")
    print("================")


def round_1(filename: str):
    with open(filename) as f:
        monkeys: list[Monkey] = []
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if line is not "":
                monkeys.append(get_monkey(line, f))

        for r in range(20):
            print(f"Round: {r} ---------------------------------")
            for i, m in enumerate(monkeys):
                m.inspect_and_throw(monkeys=monkeys)

            for i, m in enumerate(monkeys):
                print(f"Monkey {i}: {m.items}")
            

def main():
    print_header()
    round_1(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
