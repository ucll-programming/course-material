import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("width, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (5, 8),
    (6, 13)
])
def test_tilings(width, expected):
    actual = student.tilings(width)
    assert expected == actual
