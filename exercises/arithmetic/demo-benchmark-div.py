from timeit import timeit
from math import floor


def floor_division():
    for x in range(1, 1000):
        for y in range(1, 1000):
            x // y


def floor_of_true_division():
    for x in range(1, 1000):
        for y in range(1, 1000):
            floor(x / y)


print('Benchmarking floor division (should take less than 10s)...')
floor_division_time = timeit(floor_division, number=100)
print(f"Floor division took {floor_division_time:.2f}s")

print('Benchmarking floor of true division (should take less than 20s)...')
true_division_time = timeit(floor_of_true_division, number=100)
print(f"Ceiling of true division took {true_division_time:.2f}s")

print(f"Floor division is {true_division_time / floor_division_time:.2f} times faster")
