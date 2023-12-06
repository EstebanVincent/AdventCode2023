def solve_part_1(lines: list) -> int:
    def step(step_map_list, elements):
        total_source_range = []
        total_destination_range = []
        for step_map in step_map_list:
            destination_range = list(range(step_map[0], step_map[0] + step_map[2]))
            source_range = list(range(step_map[1], step_map[1] + step_map[2]))

            total_source_range += source_range
            total_destination_range += destination_range
        next_step_elements = []
        for element in elements:
            try:
                index = total_source_range.index(element)
                next_step_elements.append(total_destination_range[index])
            except ValueError:
                next_step_elements.append(element)
        return next_step_elements

    seeds = [int(x) for x in lines[0].split(": ", 1)[1].split(" ")]

    parts = []
    for idx, line in enumerate(lines):
        if "map" in line:
            parts.append(idx)
    parts.append(len(lines))
    elements = seeds
    for i in range(len(parts) - 1):
        step_map_list = []
        for line in lines[parts[i] + 1 : parts[i + 1] - 1]:
            step_map_list.append([int(x) for x in line.split(" ")])
        elements = step(step_map_list, elements)

    return min(elements)


def solve_part_2(lines: list) -> int:
    return 2
