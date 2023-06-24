import pytest
import student


@pytest.mark.parametrize('x, y', [
    (x, x + dx)
    for x in range(-20, 20)
    for dx in range(-5, 6)
])
def test_close_enough(x, y):
    assert student.close_enough(x, y)


@pytest.mark.parametrize('x, y', [
    (x + dxf * dx, x)
    for x in range(-20, 20)
    for dx in range(6, 10)
    for dxf in [-1, 1]
])
def test_not_close_enough(x, y):
    assert not student.close_enough(x, y)
