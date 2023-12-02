import re
import pandas as pd


def read_file(file_path: str) -> pd.DataFrame:
    with open(file_path, "r") as file:
        lines = file.readlines()
    rows_dict = {
        "game_id": [],
        "draw_id": [],
        "red": [],
        "green": [],
        "blue": [],
    }
    for game_id, line in enumerate(lines, 1):
        _, game = line.split(":", 1)
        game = game.replace("\n", "")
        draws = game.split(";")
        for draw_id, draw in enumerate(draws, 1):
            sets = draw.split(",")
            row = {
                "game_id": game_id,
                "draw_id": draw_id,
                "red": 0,
                "green": 0,
                "blue": 0,
            }
            for set in sets:
                _, value, key = set.split(" ")
                row[key] = value
            for key in row:
                rows_dict[key].append(row[key])
    df = pd.DataFrame.from_dict(rows_dict, dtype=int)
    return df


def solve_part_1(df: pd.DataFrame, red: int, green: int, blue: int):
    impossible_df = df[(df["red"] > red) | (df["green"] > green) | (df["blue"] > blue)]
    possible_games = set(df["game_id"]) - set(impossible_df["game_id"])
    return sum(possible_games)


def solve_part_2(df: pd.DataFrame) -> int:
    df_min = df.groupby(
        by=["game_id"],
    ).max()
    df_min["power"] = df_min["red"] * df_min["green"] * df_min["blue"]
    return df_min["power"].sum()
