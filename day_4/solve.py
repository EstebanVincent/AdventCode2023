def solve_part_1(lines: list) -> int:
    cards_worths = []
    for _, line in enumerate(lines, 1):
        _, card = line.split(": ", 1)
        win_numbers, my_numbers = card.split(" | ", 1)
        win_numbers_set = set(win_numbers.split())
        my_numbers_set = set(my_numbers.split())
        matching_set = win_numbers_set & my_numbers_set

        number_matching = len(matching_set)
        if number_matching == 0:
            cards_worths.append(0)
            continue
        card_worth = 2 ** (number_matching - 1)
        cards_worths.append(card_worth)
    return int(sum(cards_worths))


def solve_part_2(lines: list) -> int:
    number_cards = [1] * len(lines)
    for card_id, line in enumerate(lines, 1):
        _, card = line.split(": ", 1)
        win_numbers, my_numbers = card.split(" | ", 1)
        win_numbers_set = set(win_numbers.split())
        my_numbers_set = set(my_numbers.split())
        matching_set = win_numbers_set & my_numbers_set

        number_matching = len(matching_set)
        number_cards[card_id : card_id + number_matching] = [
            x + (number_cards[card_id - 1])
            for x in number_cards[card_id : card_id + number_matching]
        ]

    return int(sum(number_cards))
