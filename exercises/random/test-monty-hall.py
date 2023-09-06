import pytest
import student


@pytest.mark.timeout(1)
def test_monty_hall():
    actual = student.monty_hall(10000)
    expected = 66.6
    assert pytest.approx(expected, abs=2) == actual
