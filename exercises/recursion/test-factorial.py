import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("n, expected", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
])
def test_factorial(n, expected):
    actual = student.factorial(n)
    assert expected == actual
