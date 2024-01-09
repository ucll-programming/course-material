import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("k", [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 179424673
])
def test_is_prime(k):
    assert student.is_prime(k), f"is_prime({k}) should return True"


@pytest.mark.timeout(1)
@pytest.mark.parametrize("k", [
    0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20
])
def test_is_not_prime(k):
    assert not student.is_prime(k), f"is_prime({k}) should return False"
