import re
import pandas as pd


def read_file(file_path: str) -> list:
    with open(file_path, "r") as file:
        lines = file.readlines()
    return lines


def convert_to_df(lines: list, part_2: bool = False) -> pd.DataFrame:
    clean_lines = [line.replace("\n", "") for line in lines]
    if part_2:
        array_2d = [list(line) for line in clean_lines]
        df = pd.DataFrame(array_2d)
        return df
    changed_symbols_lines = [re.sub(r"[^.\d]+", "*", line) for line in clean_lines]
    array_2d = [list(line) for line in changed_symbols_lines]
    df = pd.DataFrame(array_2d)
    return df


def solve_part_1(lines: list) -> int:
    def valid_part_number() -> bool:
        if not number_index:
            return False
        row = number_index[0][0]
        rows = {row - 1, row, row + 1}
        columns = {number_index[0][1] - 1, number_index[-1][1] + 1}
        for cell in number_index:
            columns.add(cell[1])
        valid_rows = allowed_rows_index & rows
        valid_columns = allowed_columns_index & columns
        cells_to_check = {(x, y) for x in valid_rows for y in valid_columns}
        contains_asterisk = any(
            df.loc[cell[0], cell[1]] == "*" for cell in cells_to_check
        )
        return contains_asterisk

    df = convert_to_df(lines)
    part_numbers = []
    allowed_rows_index = set(range(df.shape[0]))
    allowed_columns_index = set(range(df.shape[1]))
    treated_cells = set()
    for row_index in range(df.shape[0]):
        for column_index in range(df.shape[1]):
            cell_index = (row_index, column_index)
            if cell_index in treated_cells:
                continue
            treated_cells.add(cell_index)
            cell_value = df.loc[row_index, column_index]
            number = ""
            number_index = list()
            i = 0
            while cell_value.isdigit() and (column_index + i) in allowed_columns_index:
                number_index.append((row_index, column_index + i))
                number += cell_value
                i += 1
                if column_index + i == df.shape[1]:
                    break
                cell_value = df.loc[row_index, column_index + i]
                treated_cells.add((row_index, column_index + i))
            if valid_part_number():
                part_numbers.append(int(number))
    return sum(part_numbers)


def solve_part_2(lines: list) -> int:
    def get_asterixs() -> list:
        if not number_index:
            return None
        row = number_index[0][0]
        rows = {row - 1, row, row + 1}
        columns = {number_index[0][1] - 1, number_index[-1][1] + 1}
        for cell in number_index:
            columns.add(cell[1])
        valid_rows = allowed_rows_index & rows
        valid_columns = allowed_columns_index & columns
        cells_to_check = {(x, y) for x in valid_rows for y in valid_columns}
        asterix_cells = [
            cell for cell in cells_to_check if df.loc[cell[0], cell[1]] == "*"
        ]
        return asterix_cells

    def get_gears_df() -> pd.DataFrame:
        potential_gears_df = pd.DataFrame.from_dict(
            {
                "potential_gears": potential_gears,
                "adjacent_number": potential_gears_adjacent_number,
                "count": 1,
            }
        )
        grp_potential_gears_df = potential_gears_df.groupby(["potential_gears"]).sum()
        # Assuming you have a groupby result DataFrame named `grouped_df`
        gears_df = potential_gears_df[
            potential_gears_df["potential_gears"].map(grp_potential_gears_df["count"])
            == 2
        ]
        return gears_df[["potential_gears", "adjacent_number"]]

    df = convert_to_df(lines, part_2=True)

    potential_gears = []
    potential_gears_adjacent_number = []
    allowed_rows_index = set(range(df.shape[0]))
    allowed_columns_index = set(range(df.shape[1]))
    treated_cells = set()
    for row_index in range(df.shape[0]):
        for column_index in range(df.shape[1]):
            cell_index = (row_index, column_index)
            if cell_index in treated_cells:
                continue
            treated_cells.add(cell_index)
            cell_value = df.loc[row_index, column_index]
            number = ""
            number_index = list()
            i = 0
            while cell_value.isdigit() and (column_index + i) in allowed_columns_index:
                number_index.append((row_index, column_index + i))
                number += cell_value
                i += 1
                if column_index + i == df.shape[1]:
                    break
                cell_value = df.loc[row_index, column_index + i]
                treated_cells.add((row_index, column_index + i))
            asterix_cells = get_asterixs()
            if not asterix_cells:
                continue
            for cell in asterix_cells:
                potential_gears.append(cell)
                potential_gears_adjacent_number.append(int(number))
    gears_df = get_gears_df()
    result_df = gears_df.groupby(["potential_gears"]).agg("prod")
    return result_df["adjacent_number"].sum()


lines = read_file("day_3/example_2.txt")
print(solve_part_2(lines))
