import pytest
import student


@pytest.mark.timeout(1)
def test_five():
    expected = 5
    actual = student.five()
    assert expected == actual, f'Expected {expected}, got {actual} instead'
