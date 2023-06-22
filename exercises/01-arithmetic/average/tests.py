import pytest
import student


@pytest.mark.parametrize('x', range(-10, 10))
@pytest.mark.parametrize('y', range(-10, 10))
def test_average(x, y):
    actual = student.average(x, y)

    assert 2 * actual == x + y
