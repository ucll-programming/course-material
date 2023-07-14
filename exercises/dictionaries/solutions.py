def group_by_first_letter(strings):
    result = {}
    for string in strings:
        key = string[0].upper()
        result.setdefault(key, []).append(string)
    return result


def counts(xs):
    result = {}
    for x in xs:
        result[x] = result.get(x, 0) + 1
    return result


def inverse_lookup(dictionary, value):
    result = []
    for k, v in dictionary.items():
        if v == value:
            result.append(k)
    return result


def combine(d1, d2):
    result = {}
    for key, value in d1.items():
        if value in d2:
            result[key] = d2[value]
    return result
