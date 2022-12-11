from __future__ import annotations
from io import TextIOWrapper
import timeit
import re

INPUT_FILEPATH = "./example.txt"

class Monkey(object):
    def __init__(
        self,
        items: list[int],
        operation_fct: any,
    ) -> None:
        self.items = items
        self.operation_fct = operation_fct
        self.number_of_inspection = 0

    def inspect_and_throw(self, monkeys: list[Monkey]):
        while self.items:
            result = self.operation_fct(self.items[0])
            monkeys[result[0]].items.append(result[1])
            del self.items[0]
            self.number_of_inspection += 1


def get_operation(
    operation: str, divisible_by: int, to_monkey_if_true: int, to_monkey_if_false: int, divide_by_3: bool = False
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

        if divide_by_3:
            new_worry = int(new_worry / 3)

        return (
            (to_monkey_if_true, new_worry)
            if new_worry % divisible_by == 0
            else (to_monkey_if_false, new_worry)
        )

    return handle


def read(f: TextIOWrapper, prefix: str):
    return f.readline().removeprefix(prefix).strip()


def get_monkey(line: str, f: TextIOWrapper, divide_by_3: bool = False):
    if line.startswith("Monkey"):
        starting_items = list(map(int, read(f, "  Starting items: ").split(",")))
        operation = get_operation(
            read(f, "  Operation: new = "),
            int(read(f, "  Test: divisible by ")),
            int(read(f, "    If true: throw to monkey ")),
            int(read(f, "    If false: throw to monkey ")),
            divide_by_3
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
            if line != "":
                monkeys.append(get_monkey(line, f, True))

        for _ in range(20):
            for _, m in enumerate(monkeys):
                m.inspect_and_throw(monkeys=monkeys)

        monkeys = sorted(monkeys, key=lambda x: x.number_of_inspection, reverse=True)
        print(monkeys[0].number_of_inspection * monkeys[1].number_of_inspection)


def round_2(filename: str):
    with open(filename) as f:
        monkeys: list[Monkey] = []
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            if line != "":
                monkeys.append(get_monkey(line, f))

        for i in range(10000):
            print(f"round: {i}")
            for _, m in enumerate(monkeys):
                m.inspect_and_throw(monkeys=monkeys)

        monkeys = sorted(monkeys, key=lambda x: x.number_of_inspection, reverse=True)
        print(monkeys[0].number_of_inspection * monkeys[1].number_of_inspection)

def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)

if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
