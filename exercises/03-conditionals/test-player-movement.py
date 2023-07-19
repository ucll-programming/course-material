import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("position, left_arrow_pressed, right_arrow_pressed, shift_pressed, expected", [
    (position, left_arrow_pressed, right_arrow_pressed, shift_pressed, position + delta)
    for position in [-5, 0, 10, 29]
    for left_arrow_pressed, right_arrow_pressed, shift_pressed, delta in [
        (False, False, False, 0),
        (True, False, False, -1),
        (False, True, False, 1),
        (True, True, False, 0),
        (False, False, True, 0),
        (True, False, True, -2),
        (False, True, True, 2),
        (True, True, True, 0),
    ]
])
def test_player_movement(position, left_arrow_pressed, right_arrow_pressed, shift_pressed, expected):
    actual = student.player_movement(position, left_arrow_pressed, right_arrow_pressed, shift_pressed)
    assert expected == actual
