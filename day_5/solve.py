def solve_part_1(lines: list) -> int:
    def step(step_map_list, elements):
        total_source_range = []
        total_destination_range = []
        for step_map in step_map_list:
            destination_range = [step_map[0], step_map[0] + step_map[2]]
            source_range = [step_map[1], step_map[1] + step_map[2]]

            total_source_range.append(source_range)
            total_destination_range.append(destination_range)
        next_step_elements = []
        for idx_e, element in enumerate(elements):
            for idx_r, source_range in enumerate(total_source_range):
                if source_range[0] < element <= source_range[1]:
                    start_destination = total_destination_range[idx_r][0]
                    gap = element - source_range[0]
                    next_step_elements.append(start_destination + gap)
                    break
            if len(next_step_elements) != (idx_e + 1):
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
