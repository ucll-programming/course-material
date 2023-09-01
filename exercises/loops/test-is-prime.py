import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("n", [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    97,
    101
])
def test_is_prime(n):
    assert student.is_prime(n) == True, f"is_prime({n}) should return True"


@pytest.mark.timeout(1)
@pytest.mark.parametrize("n", [
    1,
    4,
    6,
    8,
    9,
    10,
    12,
    14,
    15,
    16,
    18,
    20,
    21,
    22,
    24,
])
def test_is_not_prime(n):
    assert student.is_prime(n) == False, f"is_prime({n}) should return False"

