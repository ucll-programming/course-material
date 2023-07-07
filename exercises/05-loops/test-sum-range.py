import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("a, b", [
    (a, b)
    for a in range(0, 20)
    for b in range(a, 20)
])
def test_sum_range(a, b):
    actual = student.sum_range(a, b)
    expected = ((b - a + 1) * (a + b)) // 2.
    assert expected == actual, f'sum_range({a}, {b}) should return {expected} but instead returned {actual}'
