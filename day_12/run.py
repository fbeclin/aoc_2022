import timeit

INPUT_FILEPATH = "./example.txt"


heightmap = []
start_pos = (0, 0)
end_pos = (0, 0)


def print_header():
    print("================")
    print("= AoC - Day 12 =")
    print("================")


def load_heightmap(line: str):
    global start_pos, end_pos
    row = []
    for i, c in enumerate(line):
        if c == "S":
            start_pos = (len(heightmap), i)
            c = "a"
        elif c == "E":
            end_pos = (len(heightmap), i)
            c = "z"
        row.append(c)
    heightmap.append(row)


def round_1(filename: str):
    with open(filename) as f:
        [load_heightmap(line.strip()) for line in f.readlines()]
        print("start:" + str(start_pos) + " / end:" + str(end_pos))


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
