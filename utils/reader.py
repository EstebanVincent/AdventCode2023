def read_file(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return [line.strip("\n") for line in lines]
