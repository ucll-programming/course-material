import random


def lottery(k, n, simulation_count):
    win_count = 0
    numbers = list(range(n))
    picked_numbers = set(range(k))
    for _ in range(simulation_count):
        if set(random.sample(numbers, k)) == picked_numbers:
            win_count += 1
    return win_count / simulation_count * 100
