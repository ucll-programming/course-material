def is_prime(n):
    k = 2
    while k * k < n:
        if n % k == 0:
            return False
        k += 1

    return k >= 2
