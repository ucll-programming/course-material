import pytest
import student


def factorial(k):
    result = 1
    for i in range(2, k + 1):
        result *= i
    return result

def binomial(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


@pytest.mark.timeout(1)
@pytest.mark.parametrize("k, n, simulation_count, expected", [
    (
        k, n, 20000, 100 / binomial(n, k)
    )
    for k in range(1, 10)
    for n in range(k + 1, 10)
])
def test_lottery(k, n, simulation_count, expected):
    actual = student.lottery(k, n, simulation_count)
    assert pytest.approx(expected, abs=2) == actual
