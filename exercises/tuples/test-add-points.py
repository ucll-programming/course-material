import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("p1, p2, expected", [
    ((0, 0), (0, 0), (0, 0)),
    ((1, 0), (0, 0), (1, 0)),
    ((0, 1), (0, 0), (0, 1)),
    ((0, 0), (1, 0), (1, 0)),
    ((0, 0), (0, 1), (0, 1)),
    ((1, 2), (3, 4), (4, 6)),
    ((-1, 2), (1, -2), (0, 0)),
    ((9, 4), (-3, 2), (6, 6)),
])
def test_add_points(p1, p2, expected):
    actual = student.add_points(p1, p2)
    assert expected == actual
