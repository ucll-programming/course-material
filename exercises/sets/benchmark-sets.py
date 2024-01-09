from timeit import repeat


def benchmark(message_builder, *, setup='pass', n=1):
    def wrapper(func):
        times = repeat(func, setup=setup, number=1, repeat=n)
        time = sum(times)
        print(message_builder(time))
    return wrapper



SIZE = 100000


@benchmark(lambda s: f'Inserting in set: {s}s')
def insert_in_set():
    xs = set()
    for i in range(SIZE):
        xs.add(i)


@benchmark(lambda s: f'Removing from set: {s}s')
def remove_from_set():
    xs = set(range(SIZE))
    for i in range(SIZE):
        xs.remove(i)


@benchmark(lambda s: f'Set membership: {s}s')
def remove_from_set():
    xs = set(range(SIZE))
    for i in range(SIZE):
        i in xs
