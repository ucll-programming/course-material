import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('value', range(-100, 100))
def test_abs(value):
    expected = abs(value)
    actual = student.my_abs(value)

    assert actual == expected
