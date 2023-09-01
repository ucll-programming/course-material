import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("x1, y1, x2, y2, expected", [
    (0, 0, 0, 0, 0),
    (0, 0, 1, 0, 1),
    (0, 0, 0, 1, 1),
    (0, 0, 2, 0, 2),
    (0, 0, 0, 2, 2),
    (1, 0, 0, 0, 1),
    (0, 2, 0, 0, 2),
    (5, 7, 5, 7, 0),
    (5, 7, 5, 7, 0),
    (1, 1, 8, 1, 7),
    (1, 4, 4, 8, 5),
    (4, 4, 1, 8, 5),
    (0, 0, 1, 1, 2**0.5),
    (5, 3, 8, 4, 10**0.5),
])
def test_distance(x1, y1, x2, y2, expected):
    actual = student.distance(x1, y1, x2, y2)

    assert expected == pytest.approx(actual, abs=0.1)
