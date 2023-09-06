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
