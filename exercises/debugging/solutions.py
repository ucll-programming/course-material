def reverse(lst):
    for i in range(len(lst) // 2):
        j = len(lst) - i - 1
        temp = lst[i]
        lst[i] = lst[j]
        lst[j] = temp


def is_prime(n):
    k = 2
    while k * k <= n:
        if n % k == 0:
            return False
        k += 1

    return n >= 2


def contains_equal_neighbors(xs):
    for i in range(len(xs) - 1):
        if xs[i] == xs[i+1]:
            return True
    return False


def capitalize_words(string):
    words = string.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)


def merge(xs, ys):
    result = []
    i = 0
    j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1
    result.extend(xs[i:])
    result.extend(ys[j:])
    return result


def move_elements(xs, new_positions):
    ys = xs[:]
    for i in range(len(new_positions)):
        j = new_positions[i]
        ys[j] = xs[i]
    xs.clear()
    xs += ys
