import math


def five():
    return 5


def triple(x):
    return x * 3


def average(x, y):
    return (x + y) / 2


def candy_per_child(candy_count, child_count):
    return candy_count // child_count


def leftover_candy(candy_count, child_count):
    return candy_count % child_count


def buses_needed(people_count, bus_capacity):
    return math.ceil(people_count / bus_capacity)


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def cake(eggs):
    return eggs // 5


def cake2(eggs, flour):
    return min(eggs // 5, flour // 250)


def cake3(eggs, flour, butter, sugar):
    limited_by_eggs = eggs // 5
    limited_by_flour = flour // 250
    limited_by_butter = butter // 200
    limited_by_sugar = sugar // 250
    return min(limited_by_eggs, limited_by_flour, limited_by_butter, limited_by_sugar)


def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    limited_by_eggs = eggs // eggs_per_cake
    limited_by_flour = flour // flour_per_cake
    limited_by_butter = butter // butter_per_cake
    limited_by_sugar = sugar // sugar_per_cake
    return min(limited_by_eggs, limited_by_flour, limited_by_butter, limited_by_sugar)


def internet_costs(duration_in_seconds, cost_per_block):
    return math.ceil(duration_in_seconds / 360) * cost_per_block


def middle(a, b, c):
    return (a + b + c) - min(a, b, c) - max(a, b, c)


def last_digit(n):
    return n % 10


def drop_last_digit(n):
    return n // 10


def next_player(player, player_count):
    return (player + 1) % player_count


def next_player2(player, player_count):
    return player % player_count + 1


def coins(amount):
    five_coins = amount // 5
    amount_after_five = amount - 5 * five_coins
    two_coins = amount_after_five // 2
    one_coins = amount_after_five - 2 * two_coins
    return five_coins + two_coins + one_coins


def hours(duration):
    return duration // 3600


def minutes(duration):
    return (duration - hours(duration) * 3600) // 60


def seconds(duration):
    return duration - hours(duration) * 3600 - minutes(duration) * 60
