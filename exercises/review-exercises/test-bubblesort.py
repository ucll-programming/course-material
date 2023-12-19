import pytest
import student
import random


def get_rand_floats(count: int):
    random.seed(0)
    return [random.uniform(-1, 1) * 100 for _ in range(count)]


def get_rand_ints(count: int):
    return list(map(lambda x: int(x), get_rand_floats(count)))


@pytest.mark.timeout(1)
@pytest.mark.parametrize(
    "ns",
    [get_rand_floats(i) for i in range(20)] + [get_rand_ints(i) for i in range(20)],
)
def test_bubblesort(ns):
    actual = student.bubblesort(ns=ns)
    assert actual == sorted(ns), f"{actual} is not sorted"
