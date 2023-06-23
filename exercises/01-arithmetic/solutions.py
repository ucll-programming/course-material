import math


def five():
    return 5


def double(x):
    return x * 2


def average(x, y):
    return (x + y) / 2


def candy_per_child(candy_count, child_count):
    return candy_count // child_count


def buses_needed(people_count, bus_capacity):
    return math.ceil(people_count / bus_capacity)


def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5


def cake(eggs):
    return eggs // 5


def cake2(eggs, flour):
    limited_by_eggs = eggs // 5
    limited_by_flour = flour // 250
    return min(limited_by_eggs, limited_by_flour)


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
