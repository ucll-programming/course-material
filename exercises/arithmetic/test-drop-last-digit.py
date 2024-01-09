import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("n", [0, 4, 81, 482, 993, 8454, 95184, 813790, 489, 678, 267, 106])
def test_drop_last_digit(n):
    actual = student.drop_last_digit(n)

    assert actual * 10 + n % 10 == n, f"drop_last_digit({n}) wrongly returned {actual}"
