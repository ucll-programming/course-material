import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, expected", [
    ([], False),
    ([1], False),
    ([1, 1], True),
    ([1, 2], False),
    ([1, 2, 1], True),
    (list(range(1000000)), False),
    ([*range(1000000), 99999], True),
    ([5] * 1000000, True),
])
def test_contains_duplicates(xs, expected):
    actual = student.contains_duplicates(xs)
    assert expected == actual
