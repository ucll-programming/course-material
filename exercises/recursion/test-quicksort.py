import pytest
import student
import itertools


@pytest.mark.timeout(1)
@pytest.mark.parametrize("ns, expected", [
    (permutation, sorted(ns))
    for ns in [
        [],
        [1],
        [1, 2, 3],
        [1, 2, 2, 3],
        [1, 3, 9, 9, 9],
        [4, 7, 8, 10, 13],
    ]
    for permutation in itertools.permutations(ns)
])
def test_quicksort(ns, expected):
    actual = student.quicksort(tuple(ns))
    assert list(actual) == list(expected)
