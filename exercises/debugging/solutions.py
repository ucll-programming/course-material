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


def rle(string):
    groups = []
    i = 0
    while i < len(string):
        j = i + 1
        while j < len(string) and string[i] == string[j]:
            j += 1
        groups.append((string[i], j - i))
        i = j
    result = ''
    for char, count in groups:
        while count > 0:
            k = min(9, count)
            result += f"{k}{char}"
            count -= k
    return result
