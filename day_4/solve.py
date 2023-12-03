import re
import pandas as pd


def read_file(file_path: str) -> list:
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def convert_to_df(lines: list) -> pd.DataFrame:
    pass


def solve_part_1(lines: list) -> int:
    pass


def solve_part_2(lines: list) -> int:
    pass


lines = read_file("day_3/example_2.txt")
print(solve_part_2(lines))
