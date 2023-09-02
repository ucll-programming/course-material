import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("menu, value", [
    ([], 0),
    ([2], 0),
    *(
        ([1], n)
        for n in range(0, 10)
    ),
    *(
        ([3, 7, 19], 3 * a + 7 * b + c * 19)
        for a in [0, 1, 5]
        for b in [0, 1, 3]
        for c in [0, 1, 4]
    ),
    *(
        ([2, 5, 8, 13], 2 * a + 5 * b + 8 * c + 13 * d)
        for a in [0, 1, 5]
        for b in [0, 1, 3]
        for c in [0, 1, 4]
        for d in [0, 1, 3]
    ),
])
def test_coupon_with_possible_combination(menu, value):
    actual = student.coupon(menu, value)

    assert actual is not None
    assert sum(actual) == value
    assert all(price in menu for price in actual)


@pytest.mark.timeout(1)
@pytest.mark.parametrize("menu, value", [
    ([], 1),
    ([2], 5),
])
def test_coupon_with_impossible_combination(menu, value):
    actual = student.coupon(menu, value)

    assert actual is None
