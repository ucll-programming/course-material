import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("temperatures, expected", [
    ([40, 40, 40, 40], False),
    ([40, 40, 40, 40, 40], True),
    ([40, 40, 20, 40, 40, 40], False),
    ([24, 28, 31, 35, 36, 32, 20], True),
    ([24, 26, 28, 31, 29, 27, 32, 25, 27, 26, 30, 23], True),
    ([25, 20, 24, 29, 23, 24, 28, 24], False),
    ([24, 28, 30, 33, 31, 24], False),
    ([24, 28, 30, 33, 31, 24, 22, 25, 29, 26, 30, 29, 31, 30, 26, 24], True),
    ([24, 28, 30, 33, 31, 26, 24, 22, 25, 29, 26, 30, 29, 31, 26, 24], True),
    ([24, 28, 30, 31, 26, 24, 22, 25, 29, 26, 30, 29, 26, 24], False),
])
def test_heatwave(temperatures, expected):
    actual = student.heatwave(temperatures)
    assert expected == actual, f'heatwave({temperatures!r}) should return {expected}'
