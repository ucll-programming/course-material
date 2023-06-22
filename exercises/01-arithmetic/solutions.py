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
