from dataclasses import dataclass
import timeit


INPUT_FILEPATH = "./example.txt"


@dataclass
class Slider(object):
    pos: int
    markers_pos: dict
    markers: list

    def __init__(self):
        self.pos = 0
        self.markers_pos = {}
        self.markers = []

    def slide(self, data_stream: str):
        while len(self.markers) < 4 and self.pos < len(data_stream):
            char = data_stream[self.pos]
            current_marker_pos = self.markers_pos.get(char, -1)
            if current_marker_pos != -1:
                self._update_pos_until(current_marker_pos + 1)

            self.markers_pos[char] = len(self.markers)
            self.markers.append(char)

            # move forward
            self.pos += 1

    def _update_pos_until(self, pos: int):
        # remove old markers
        for i in range(pos):
            char = self.markers[i]
            # remove marker
            del self.markers_pos[char]
        self.markers = self.markers[pos:]

        # update new marker pos
        for i, char in enumerate(self.markers):
            self.markers_pos[char] = i

    def get_first_marker(self):
        return self.pos


def print_header():
    print("================")
    print("= AoC - Day 06 =")
    print("================")


def read_datastream(line: str):
    slider = Slider()
    slider.slide(line)
    print(f"markers: {slider.markers} - first marker pos: {slider.get_first_marker()}")


def round_1(filename: str):
    with open(filename) as f:
        [read_datastream(line.strip()) for line in f.readlines()]


def round_2(filename: str):
    with open(filename) as f:
        pass
        # [
        #     read_movements(line, True) if switch_to_crane else read_stacks(line)
        #     for line in f.readlines()
        # ]


def main():
    print_header()
    round_1(INPUT_FILEPATH)
    # round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
