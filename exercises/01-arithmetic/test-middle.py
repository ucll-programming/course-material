import pytest
import student
import itertools


@pytest.mark.parametrize("a", [-4, 0, 1, 4])
@pytest.mark.parametrize("b", [-2, 0, 2, 8])
@pytest.mark.parametrize("c", [-9, 0, 3, 6])
def test_double(a, b, c):
    expected = sorted([a, b, c])[1]
    actual = student.middle(a, b, c)

    assert actual == expected
