import random


def lottery(k, n, simulation_count):
    win_count = 0
    numbers = list(range(n))
    picked_numbers = set(range(k))
    for _ in range(simulation_count):
        if set(random.sample(numbers, k)) == picked_numbers:
            win_count += 1
    return win_count / simulation_count * 100


def birthday_paradox(n, simulation_count):
    count = 0
    for _ in range(simulation_count):
        birthdays = {random.randint(1, 365) for _ in range(n)}
        if len(birthdays) != n:
            count += 1
    return count / simulation_count


def monty_hall(simulation_count):
    count = 0
    for _ in range(simulation_count):
        door_with_car = random.randint(1, 3)
        first_choice = 1
        if first_choice == door_with_car:
            host_choice = random.randint(2, 3)
        elif door_with_car == 2:
            host_choice = 3
        else:
            host_choice = 2
        second_choice = 6 - first_choice - host_choice
        if second_choice == door_with_car:
            count += 1
    return count / simulation_count * 100



def wins_game(my_pattern, opponent_pattern):
    current = ""
    current += random.choice('HT')
    current += random.choice('HT')
    current += random.choice('HT')
    while True:
        if current == opponent_pattern:
            return False
        if current == my_pattern:
            return True
        current += random.choice('HT')
        current = current[1:]


def winning_percentage(my_pattern, opponent_pattern, simulation_count):
    count = 0
    for _ in range(simulation_count):
        if wins_game(my_pattern, opponent_pattern):
            count += 1
    return count / simulation_count * 100


def find_best_pattern(opponent_pattern):
    choices = [
        f'{a}{b}{c}'
        for a in 'TH'
        for b in 'TH'
        for c in 'TH'
    ]
    choices.remove(opponent_pattern)
    return max(choices, key=lambda p: winning_percentage(p, opponent_pattern, 1000))


choices = [
        f'{a}{b}{c}'
        for a in 'TH'
        for b in 'TH'
        for c in 'TH'
    ]
for choice in choices:
    winner = find_best_pattern(choice)
    print(f'("{choice}", "{winner}")')
