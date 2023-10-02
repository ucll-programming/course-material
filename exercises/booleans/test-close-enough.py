import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('x, y', [
    (x, x + sign * dx)
    for x in [-51, -0.2, 0, 0.6, 1, 4.9, 2431.1]
    for dx in [0, 0.09, 0.099]
    for sign in [-1, 1]
])
def test_close_enough(x, y):
    assert student.close_enough(x, y), f'{x} and {y} should be considered close enough'


@pytest.mark.timeout(1)
@pytest.mark.parametrize('x, y', [
    (x + sign * dx, x)
    for x in [-51, -0.2, 0, 0.6, 1, 4.9, 2431.1]
    for dx in [0.11, 0.15, 0.8, 1, 12, 19, 500]
    for sign in [-1, 1]
])
def test_not_close_enough(x, y):
    assert not student.close_enough(x, y), f'{x} and {y} should be considered not close enough'
