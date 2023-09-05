import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, expected", [
    (
        [],
        []
    ),
    (
        [1],
        [1]
    ),
    (
        [1, 1],
        [1]
    ),
    (
        [1, 2],
        [1, 2]
    ),
    (
        [4, 2, 3, 1],
        [4, 2, 3, 1]
    ),
    (
        [4, 2, 3, 3, 4, 1, 1, 2],
        [4, 2, 3, 1]
    ),
    (
        [1, 4, 2, 3, 3, 4, 1, 1, 2],
        [1, 4, 2, 3]
    ),
    (
        list(range(1, 10000)) * 100,
        list(range(1, 10000))
    )
])
def test_remove_duplicates(xs, expected):
    actual = student.remove_duplicates(xs)
    assert expected == actual
