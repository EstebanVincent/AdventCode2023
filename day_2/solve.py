import pandas as pd


def convert_to_df(lines: list) -> pd.DataFrame:
    rows_dict = {
        "game_id": [],
        "draw_id": [],
        "red": [],
        "green": [],
        "blue": [],
    }
    for game_id, line in enumerate(lines, 1):
        _, game = line.split(":", 1)
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
    df = pd.DataFrame.from_dict(rows_dict).astype(int)
    return df


def solve_part_1(lines: list, red: int, green: int, blue: int):
    df = convert_to_df(lines)
    impossible_df = df[(df["red"] > red) | (df["green"] > green) | (df["blue"] > blue)]
    possible_games = set(df["game_id"]) - set(impossible_df["game_id"])
    return sum(possible_games)


def solve_part_2(lines: list) -> int:
    df = convert_to_df(lines)
    df_min = df.groupby(
        by=["game_id"],
    ).max()
    df_min["power"] = df_min["red"] * df_min["green"] * df_min["blue"]
    return df_min["power"].sum()
