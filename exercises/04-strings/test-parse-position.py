import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected_x, expected_y", [
    (
        f"({x:.3f}, {y:.3f})",
        x,
        y
    )
    for x in [-416, -1.12, 0, 1.78, 5.878, 19.112]
    for y in [-57.453, -1.541, 0, 1.998, 5.245, 254.2]
])
def test_parse_position(string, expected_x, expected_y):
    actual_x = student.parse_position_x(string)
    actual_y = student.parse_position_y(string)

    assert pytest.approx(expected_x) == actual_x
    assert pytest.approx(expected_y) == actual_y
