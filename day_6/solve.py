import math
import re


def solve_part_1(lines: list) -> int:
    def get_options(time, record_distance):
        options = []
        for speed in range(1, time):
            distance = speed * (time - speed)
            if distance > record_distance:
                options.append(distance)
        return options

    time_list = re.findall(r"\d+", lines[0].split(":", 1)[1])
    distance_list = re.findall(r"\d+", lines[1].split(":", 1)[1])
    number_possibilities = []
    for time, distance in zip(time_list, distance_list):
        number_possibilities.append(len(get_options(int(time), int(distance))))
    return math.prod(number_possibilities)


def solve_part_2(lines: list) -> int:
    def get_options(time, record_distance):  # 8s
        options = []
        for speed in range(1, time):
            distance = speed * (time - speed)
            if distance > record_distance:
                options.append(distance)
        return options

    def get_options_opti(time, record_distance):  # 1.36 s
        n_options = time
        for speed in range(1, time):
            distance = speed * (time - speed)
            if distance < record_distance:
                n_options -= 1
            else:
                break
        for speed in range(time, 1, -1):
            distance = speed * (time - speed)
            if distance < record_distance:
                n_options -= 1
            else:
                break
        return n_options

    time = "".join(re.findall(r"\d+", lines[0].split(":", 1)[1]))
    distance = "".join(re.findall(r"\d+", lines[1].split(":", 1)[1]))
    return get_options_opti(int(time), int(distance))
