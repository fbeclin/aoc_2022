from dataclasses import dataclass
import timeit


INPUT_FILEPATH = "./input1.txt"


@dataclass
class Slider(object):
    def __init__(self, marker_length: int):
        self.pos = 0
        self.marker_length = marker_length
        self.markers_pos = {}
        self.markers = []

    def slide(self, data_stream: str):
        while len(self.markers) < self.marker_length and self.pos < len(data_stream):
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


def read_datastream(line: str, marker_length: int):
    slider = Slider(marker_length)
    slider.slide(line)
    print(f"markers: {slider.markers} - first marker pos: {slider.get_first_marker()}")


def round_1(filename: str):
    with open(filename) as f:
        [read_datastream(line.strip(), 4) for line in f.readlines()]


def round_2(filename: str):
    with open(filename) as f:
        [read_datastream(line.strip(), 14) for line in f.readlines()]


def main():
    print_header()
    # round_1(INPUT_FILEPATH)
    round_2(INPUT_FILEPATH)


if __name__ == "__main__":
    start_time = timeit.default_timer()
    main()
    print(f"Execution time : {timeit.default_timer() - start_time}")
