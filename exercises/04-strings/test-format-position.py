import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("x, y, expected", [
    (0, 0, "(0, 0)"),
    (1, 0, "(1, 0)"),
    (0, 1, "(0, 1)"),
    (-87, 545, "(-87, 545)"),
])
def test_format_position(x, y, expected):
    actual = student.format_position(x, y)
    assert expected == actual
