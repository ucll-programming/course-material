def split_name(full_name):
    space_index = full_name.find(' ')
    first_name = full_name[:space_index]
    last_name = full_name[space_index+1:]
    return (first_name, last_name)


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


def split_in_two(xs):
    index = (len(xs) + 1) // 2
    return (xs[:index], xs[index:])


def count(xs, elt):
    result = 0
    for x in xs:
        if x == elt:
            result += 1
    return result


def election_winner(votes):
    votes = sorted(votes)
    winner = None
    winner_vote_count = 0
    i = 0
    while i < len(votes):
        j = i
        while j < len(votes) and votes[i] == votes[j]:
            j += 1
        vote_count = j - i + 1
        if vote_count > winner_vote_count:
            winner = votes[i]
            winner_vote_count = vote_count
        i = j
    return winner


def average(ns):
    return sum(ns) / len(ns)


def passing_percentage(grades):
    passing = 0
    for grade in grades:
        if grade >= 10:
            passing += 1
    return passing / len(grades) * 100


def heatwave(temperatures):
    above_25_count = 0
    above_30_count = 0
    for temperature in temperatures:
        if temperature < 25:
            above_25_count = 0
            above_30_count = 0
        else:
            above_25_count += 1
            if temperature >= 30:
                above_30_count += 1
            if above_25_count >= 5 and above_30_count >= 3:
                return True
    return False


def domino_chain(dominos):
    for i in range(1, len(dominos)):
        _, a = dominos[i-1]
        b, _ = dominos[i]
        if a != b:
            return False
    return True


def subtuple(xs, ys):
    for i in range(len(xs)-len(ys)+1):
        if xs[i:i+len(ys)] == ys:
            return True
    return False
