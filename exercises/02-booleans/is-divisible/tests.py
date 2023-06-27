import pytest
import student


@pytest.mark.parametrize('a, b', [
    [k * b, b]
    for k in [1, 2, 4, 9, 14]
    for b in [1, 2, 3, 10, 19, 501]
])
def test_is_divisible(a, b):
    assert student.is_divisible(a, b), f'{a} should be divisible by {b}'


@pytest.mark.parametrize('a, b', [
    [k * b + c, b]
    for k in [1, 2, 13]
    for b in [1, 2, 10, 501]
    for c in range(1, b)
])
def test_is_not_divisible(a, b):
    assert not student.is_divisible(a, b), f'{a} should not be divisible by {b}'
