from utils.reader import read_file
from day_2.solve import solve_part_1, solve_part_2


def test_solve_part_1_with_example_1():
    example_1_lines = read_file("day_2/example_1.txt")
    result = solve_part_1(example_1_lines, red=12, green=13, blue=14)
    assert result == 8


def test_solve_part_1_with_input():
    input_lines = read_file("day_2/input.txt")
    result = solve_part_1(input_lines, red=12, green=13, blue=14)
    assert result == 2076


def test_solve_part_2_with_example_2():
    example_2_lines = read_file("day_2/example_2.txt")
    result = solve_part_2(example_2_lines)
    assert result == 2286


def test_solve_part_2_with_input():
    input_lines = read_file("day_2/input.txt")
    result = solve_part_2(input_lines)
    assert result == 70950
