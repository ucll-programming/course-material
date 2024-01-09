import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("used_seats, expected", [
    ((), 0),
    ((1,), 0),
    ((1, 2), 0),
    ((1, 3), 1),
    ((1, 4), 2),
    ((1, 5), 3),
    ((2, 5), 2),
    ((1, 2, 5), 2),
    ((1, 2, 5, 6), 2),
    ((1, 2, 5, 7), 3),
    ((1, 2, 5, 7, 10), 5),
    ((1, 2, 6, 7, 10), 5),
    ((1, 2, 6, 9, 10), 5),
    ((1, 2, 6, 9, 10, 21), 15),
])
def test_empty_seats(used_seats, expected):
    actual = student.empty_seats(used_seats)
    assert expected == actual
