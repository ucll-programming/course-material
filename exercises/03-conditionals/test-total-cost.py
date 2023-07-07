import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("amount, expected", [
    *(
        (amount, amount + 10)
        for amount in range(1, 100, 7)
    ),
    *(
        (amount, amount)
        for amount in range(100, 200, 4)
    ),
    *(
        (amount, amount * 0.95)
        for amount in range(200, 500, 5)
    )
])
def test_total_cost(amount, expected):
    actual = student.total_cost(amount)

    assert expected == pytest.approx(actual, abs=1), f"total_cost({amount}) should return {expected} but instead got {actual}"
