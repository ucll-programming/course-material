import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("n", range(0, 100))
def test_sum_up_to(n):
    actual = student.sum_up_to(n)
    expected = n * (n + 1) // 2
    assert expected == actual, f'sum_up_to({n}) should return {expected} but instead returned {actual}'
