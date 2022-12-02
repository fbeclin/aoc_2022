from enum import Enum
import timeit

INPUT_FILEPATH = "./input.txt"


class RoundScore(Enum):
    LOSE = 0
    DRAW = 3
    WIN = 6


class ActionScore(Enum):
    X = 1
    Y = 2
    Z = 3


def print_header():
    print("================")
    print("= AoC - Day 02 =")
    print("================")


"""
Opponent: A = Rock, B = Paper, C = Scissors
You: X = Rock, Y = Paper, Z = Scissors
A / X = Draw = 0
A / Y = Win = -1
A / Z = Lose = -2
B / X = Lose = 1
B / Y = Draw = 0
B / Z = Win = 1
C / X = Win = 2
C / Y = Lose = 1
C / Z = Draw = 0
"""

round_map = {
    "A X": RoundScore.DRAW,
    "A Y": RoundScore.WIN,
    "A Z": RoundScore.LOSE,
    "B X": RoundScore.LOSE,
    "B Y": RoundScore.DRAW,
    "B Z": RoundScore.WIN,
    "C X": RoundScore.WIN,
    "C Y": RoundScore.LOSE,
    "C Z": RoundScore.DRAW,
}


"""
Opponent: A = Rock, B = Paper, C = Scissors
You: X = Rock, Y = Paper, Z = Scissors
X = Lose
Y = Draw
Z = Win
"""

round_map_action = {
    "A X": "Z",
    "A Y": "X",
    "A Z": "Y",
    "B X": "X",
    "B Y": "Y",
    "B Z": "Z",
    "C X": "Y",
    "C Y": "Z",
    "C Z": "X",
}


def play_round(line: str) -> int:
    return round_map[line].value + ActionScore[line[2]].value


def round_1(filename: str):
    with open(filename) as f:
        total_score = sum([play_round(line.strip()) for line in f.readlines()])
        print(f"Total_score: {total_score}")


def play_round_2(line: str) -> int:
    shape = round_map_action[line]
    return round_map[f"{line[0]} {shape}"].value + ActionScore[shape].value


def round_2(filename: str):
    with open(filename) as f:
        total_score = sum([play_round_2(line.strip()) for line in f.readlines()])
        print(f"Total_score: {total_score}")


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
