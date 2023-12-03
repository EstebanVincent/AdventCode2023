import re


def solve_part_1(lines: list) -> int:
    list_str_digits = ["".join(re.findall(r"\d+", line.strip())) for line in lines]
    list_calibration_values = [
        int(str(digits)[0] + str(digits)[-1]) for digits in list_str_digits
    ]
    result = sum(list_calibration_values)
    return result


def replace_str_number(line: str) -> str:
    literal_numbers = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    index_first_match, replaced_first_occurence_line = 0, ""
    first_occurence_list, last_occurence_list = [], []

    for literal_number in literal_numbers:
        first_occurence_list.append(line.find(literal_number))
        last_occurence_list.append(line.rfind(literal_number))
    try:
        index_first_match = min(filter(lambda x: x >= 0, first_occurence_list))
        first_occurence = first_occurence_list.index(index_first_match)
        replaced_first_occurence_line = line.replace(
            literal_numbers[first_occurence], str(first_occurence + 1), 1
        )
    except:
        pass
    try:
        last_occurence = last_occurence_list.index(
            max(filter(lambda x: x >= 0, last_occurence_list))
        )
        if literal_numbers[last_occurence] in line:
            head, _, tail = line[index_first_match + 1 :].rpartition(
                literal_numbers[last_occurence]
            )
            line = (
                replaced_first_occurence_line[: index_first_match + 1]
                + head
                + str(last_occurence + 1)
                + tail
            )

    except:
        pass
    return line


def solve_part_2(lines: list) -> int:
    list_str_number = [replace_str_number(line) for line in lines]
    return solve_part_1(list_str_number)
