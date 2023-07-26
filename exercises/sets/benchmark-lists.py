from timeit import repeat


def benchmark(message_builder, *, setup='pass', n=1):
    def wrapper(func):
        times = repeat(func, setup=setup, number=1, repeat=n)
        time = sum(times)
        print(message_builder(time))
    return wrapper



SIZE = 100000


@benchmark(lambda s: f'Inserting in front of list: {s}s')
def insert_front():
    xs = []
    for _ in range(SIZE):
        xs.insert(0, 0)


@benchmark(lambda s: f'Inserting in back of list: {s}s')
def insert_back():
    xs = []
    for _ in range(SIZE):
        xs.append(0)


@benchmark(lambda s: f'Removing at front of list: {s}s')
def remove_front():
    xs = list(range(SIZE))
    while xs:
        xs.pop(0)


@benchmark(lambda s: f'Removing at back of list: {s}s')
def remove_back():
    xs = list(range(SIZE))
    while xs:
        xs.pop()



@benchmark(lambda s: f'Membership list: {s}s')
def remove_back():
    xs = list(range(SIZE))
    for i in range(SIZE):
        i in xs
