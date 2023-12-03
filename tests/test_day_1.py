from utils.reader import read_file
from day_1.solve import solve_part_1, solve_part_2


def test_solve_part_1_with_example_1():
    example_1_lines = read_file("day_1/example_1.txt")
    result = solve_part_1(example_1_lines)
    assert result == 142


def test_solve_part_1_with_input():
    input_lines = read_file("day_1/input.txt")
    result = solve_part_1(input_lines)
    assert result == 54239


def test_solve_part_2_with_example_2():
    example_2_lines = read_file("day_1/example_2.txt")
    result = solve_part_2(example_2_lines)
    assert result == 281


def test_solve_part_2_with_example_2_debug():
    example_2_debug_lines = read_file("day_1/example_2_debug.txt")
    result = solve_part_2(example_2_debug_lines)
    assert result == 363


def test_solve_part_2_with_input():
    input_lines = read_file("day_1/input.txt")
    result = solve_part_2(input_lines)
    assert result == 55343
