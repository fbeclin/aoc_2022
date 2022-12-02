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
A / X = Draw
A / Y = Win
A / Z = Lose
B / X = Lose
B / Y = Draw
B / Z = Win
C / X = Win
C / Y = Lose
C / Z = Draw
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


def play_round(line: str) -> int:
    return round_map[line].value + ActionScore[line[2]].value


def round_1(filename: str):
    with open(filename) as f:
        total_score = sum([play_round(line.strip()) for line in f.readlines()])
        print(f"Total_score: {total_score}")


def round_2():
    pass


def main():
    print_header()
    round_1(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
