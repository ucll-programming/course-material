import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("string, expected_x, expected_y", [
    (
        f"({x}, {y})",
        x,
        y
    )
    for x in [-416, -1, 0, 1, 5, 19]
    for y in [-57, -1, 0, 1, 5, 254]
])
def test_parse_position(string, expected_x, expected_y):
    actual_x = student.parse_position_x(string)
    actual_y = student.parse_position_y(string)

    assert expected_x == actual_x
    assert expected_y == actual_y
