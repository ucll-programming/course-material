import math


def buses_needed(people_count, bus_capacity):
    return math.ceil(people_count / bus_capacity)
