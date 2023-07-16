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


def increasing(ns):
    for i in range(1, len(ns)):
        if ns[i-1] > ns[i]:
            return False
    return True


def empty_seats(used_seats):
    if len(used_seats) == 0:
        return 0
    total_seats = max(used_seats) - min(used_seats) + 1
    return total_seats - len(used_seats)


def all_equal(xs):
    for i in range(1, len(xs)):
        if xs[i-1] != xs[i]:
            return False
    return True


def all_different(xs):
    for i in range(len(xs)):
        for j in range(i + 1, len(xs)):
            if xs[i] == xs[j]:
                return False
    return True


def add_points(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return (x1 + x2, y1 + y2)
