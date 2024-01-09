import pytest
import student
import math


@pytest.mark.timeout(1)
@pytest.mark.parametrize("amount, rate, goal", [
    (amount, rate, goal)
    for amount in [100, 500, 12785]
    for rate in [2, 5, 100]
    for goal in [amount, amount * 2, amount * 10, amount * 100]
])
def test_invest(amount, rate, goal):
    expected = math.ceil(math.log(goal / amount, 1 + rate / 100)) if amount < goal else 0
    actual = student.invest(amount=amount, rate=rate, goal=goal)

    assert expected == actual, f"invest(amount={amount}, rate={rate}, goal={goal}) should return {expected} but instead returned {actual}"
