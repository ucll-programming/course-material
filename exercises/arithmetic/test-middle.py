import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("a", [-3, -1, 0, 1, 3, 4, 7])
@pytest.mark.parametrize("b", [-3, -1, 0, 1, 3, 4, 7])
@pytest.mark.parametrize("c", [-3, -1, 0, 1, 3, 4, 7])
def test_middle(a, b, c):
    expected = sorted([a, b, c])[1]
    actual = student.middle(a, b, c)

    assert actual == expected, f'middle({a}, {b}, {c}) should return {expected} but got {actual} instead'
