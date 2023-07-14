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
