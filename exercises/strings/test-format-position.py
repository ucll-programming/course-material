import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("x, y, expected", [
    (0, 0, "(0.000, 0.000)"),
    (2, 3, "(2.000, 3.000)"),
    (-87.1, 545.78462, "(-87.100, 545.785)"),
    (5.31, 1.086213, "(5.310, 1.086)"),
])
def test_format_position(x, y, expected):
    actual = student.format_position(x, y)
    assert expected == actual
