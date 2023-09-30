import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("amount, expected", [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 2),
    (5, 1),
    (6, 2),
    (7, 2),
    (8, 3),
    (9, 3),
    (10, 2),
    (11, 3),
    (12, 3),
    (13, 4),
    (19, 5),
])
def test_coins(amount, expected):
    actual = student.coins(amount=amount)

    assert expected == actual, f"coins({amount}) should return {actual}, but returned {expected} instead"
