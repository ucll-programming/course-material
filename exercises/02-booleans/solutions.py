def can_vote(age):
    return age >= 18


def close_enough(x, y):
    return x - 0.1 <= y <= x + 0.1


def free_ticket(age):
    return age < 6 or age >= 65


def is_divisible(a, b):
    return a % b == 0
