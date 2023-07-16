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


def compact(xs):
    result = []
    for x in xs:
        if x is not None:
            result.append(x)
    return result


def compact_in_place(xs):
    for i in range(len(xs) - 1, -1, -1):
        if xs[i] is None:
            del xs[i]


def remove_runs(ns):
    result = []
    for n in ns:
        if not result or result[-1] != n:
            result.append(n)
    return result
