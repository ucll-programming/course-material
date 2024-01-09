import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("grades, expected", [
    ((20,), 100),
    ((20, 20), 100),
    ((10, 10, 10), 100),
    ((0,), 0),
    ((0, 0), 0),
    ((9, 9), 0),
    ((9, 10), 50),
    ((5, 10, 15, 20), 75),
    ((5, 5, 5, 10), 25),
    ((8, 13, 11, 5, 18), 60),
])
def test_passing_percentage(grades, expected):
    actual = student.passing_percentage(grades)
    assert pytest.approx(expected) == actual
