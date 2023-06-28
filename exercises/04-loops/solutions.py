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
