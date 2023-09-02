import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("a, b, expected", [
    (a, b, sum(range(min(a, b), max(a, b) + 1)))
    for a in range(10)
    for b in range(10)
])
def test_sum_range(a, b, expected):
    actual = student.sum_range(a, b)
    assert expected == actual, f'Expected sum_range({a}, {b}) to be equal to {expected}, got {actual} instead'
