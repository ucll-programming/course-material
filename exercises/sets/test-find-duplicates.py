import pytest
import student
import itertools


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, expected", [
    (
        [],
        []
    ),
    (
        [1],
        []
    ),
    (
        [1, 1],
        [1]
    ),
    (
        [1, 1, 1],
        [1]
    ),
    *(
        (permutation, [1])
        for permutation in itertools.permutations([1, 1, 2])
    ),
    *(
        (permutation, [1, 2])
        for permutation in itertools.permutations([1, 1, 2, 2])
    ),
    *(
        (permutation, [1, 2])
        for permutation in itertools.permutations([1, 1, 2, 2, 3])
    ),
    *(
        (permutation, [3])
        for permutation in itertools.permutations([1, 2, 3, 3, 3])
    ),
    (
        [1, 2, 3, 1, 2, 3],
        [1, 2, 3]
    ),
    (
        [*"abc"],
        []
    ),
    (
        [*"abcbc"],
        [*"bc"]
    ),
    (
        [0] * 1000000,
        [0]
    )
])
def test_find_duplicates(xs, expected):
    actual = student.find_duplicates(xs)

    assert isinstance(actual, list)
    assert len(expected) == len(actual)
    assert set(expected) == set(actual)
