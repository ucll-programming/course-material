def sum_up_to(n):
    result = 0
    for k in range(1, n+1):
        result += k
    return result


def sum_range(a, b):
    result = 0
    for k in range(a, b+1):
        result += k
    return result


def factorial(n):
    result = 1
    for k in range(2, n+1):
        result *= k
    return result


def thanos(queue_size, target_size):
    snap_count = 0
    while queue_size >= target_size:
        queue_size = queue_size // 2
        snap_count += 1
    return snap_count


def rpg2(n_sides, goal):
    count = 0
    for a in range(1, n_sides + 1):
        for b in range(1, n_sides + 1):
            if a + b >= goal:
                count += 1
    return count / n_sides**2 * 100


def rpg3(n_sides, goal):
    count = 0
    for a in range(1, n_sides + 1):
        for b in range(1, n_sides + 1):
            for c in range(1, n_sides + 1):
                if a + b + c >= goal:
                    count += 1
    return count / n_sides**3 * 100


def sum_of_input():
    total = 0
    number = int(input())
    while number != 0:
        total += number
        number = int(input())
    print(total)


def to_roman(number):
    table = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    result = ""
    for value, representation in table:
        while value <= number:
            number -= value
            result += representation
    return result


def from_roman(numeral):
    table = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
    ]

    result = 0
    for value, representation in table:
        while numeral.startswith(representation):
            result += value
            numeral = numeral[len(representation):]
    return result
