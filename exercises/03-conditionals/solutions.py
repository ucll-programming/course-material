def my_abs(x):
    if x < 0:
        return -x
    else:
        return x


def sign(x):
    if x < 0:
        return -1
    elif x == 0:
        return 0
    else:
        return 1


def total_cost(amount):
    if amount < 100:
        amount += 10
    if amount >= 200:
        amount *= 0.95
    return amount
