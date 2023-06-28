def increase_version(version, breaking_change, new_features):
    x, y, z = version
    if breaking_change:
        return (x + 1, 0, 0)
    elif new_features:
        return (x, y + 1, 0)
    else:
        return (x, y, z + 1)


def is_more_recent(v1, v2):
    a, b, c = v1
    x, y, z = v2
    return a > x or (a == x and b > y) or (a == x and b == y and c > z)


def is_older(v1, v2):
    return is_more_recent(v2, v1)
