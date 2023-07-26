import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("x", [-5, 0, 1, 3])
@pytest.mark.parametrize("y", [-9, 0, 1, 12])
def test_initialization(x, y):
    position = student.Position(x, y)
    assert hasattr(position, 'x')
    assert hasattr(position, 'y')
    assert x == position.x
    assert y == position.y
