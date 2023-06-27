import pytest
import student


@pytest.mark.parametrize("n", [0, 4, 81, 482, 993, 8454, 95184, 813790, 489, 678, 267, 106])
def test_last_digit(n):
    actual = student.last_digit(n)
    expected = int(str(n)[-1])

    assert expected == actual
