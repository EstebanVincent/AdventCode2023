from utils.reader import read_file
from day_6.solve import solve_part_1, solve_part_2


def test_solve_part_1_with_example_1():
    example_1_lines = read_file("day_6/example_1.txt")
    result = solve_part_1(example_1_lines)
    assert result == 288


def test_solve_part_1_with_input():
    input_lines = read_file("day_6/input.txt")
    result = solve_part_1(input_lines)
    assert result == 2374848


def test_solve_part_2_with_example_2():
    example_2_lines = read_file("day_6/example_2.txt")
    result = solve_part_2(example_2_lines)
    assert result == 71503


def test_solve_part_2_with_input():
    input_lines = read_file("day_6/input.txt")
    result = solve_part_2(input_lines)
    assert result == 39132886
