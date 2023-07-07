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


def gcd(x, y):
    r = min(abs(x), abs(y))
    while x % r != 0 or y % r != 0:
        r -= 1
    return r
