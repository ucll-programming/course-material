def can_vote(age):
    return age >= 18


def close_enough(x, y):
    return x - 5 <= y <= x + 5


def free_ticket(age):
    return age < 6 or age >= 65
