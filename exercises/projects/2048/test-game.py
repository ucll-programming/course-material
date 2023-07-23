import pytest
from game import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("tiles, expected_tiles, expected_has_changed", [
    (
        [None, None, None, None],
        [None, None, None, None],
        False
    ),
    (
        [2, None, None, None],
        [2, None, None, None],
        False,
    ),
    (
        [None, 2, None, None],
        [2, None, None, None],
        True,
    ),
    (
        [None, None, 8, None],
        [8, None, None, None],
        True,
    ),
    (
        [None, None, None, 32],
        [32, None, None, None],
        True,
    ),
    (
        [2, 2, None, None],
        [4, None, None, None],
        True,
    ),
    (
        [2, None, 2, None],
        [4, None, None, None],
        True,
    ),
    (
        [2, None, None, 2],
        [4, None, None, None],
        True,
    ),
    (
        [4, None, None, 2],
        [4, 2, None, None],
        True,
    ),
    (
        [2, 2, None, 4],
        [4, 4, None, None],
        True,
    ),
    (
        [2, 2, 4, 4],
        [4, 8, None, None],
        True,
    ),
    (
        [2, 2, 2, None],
        [4, 2, None, None],
        True,
    ),
])
def test_row_shift_left(tiles, expected_tiles, expected_has_changed):
    has_changed = shift_row_left(tiles)
    assert expected_tiles == tiles
    assert expected_has_changed == has_changed


@pytest.mark.timeout(1)
@pytest.mark.parametrize("tiles, expected_tiles, expected_has_changed", [
    (
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        False
    ),
    (
        [
            [None, None, None, None],
            [2, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [None, None, None, None],
            [2, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        False
    ),
    (
        [
            [None, None, None, None],
            [None, 2, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [None, None, None, None],
            [2, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        True
    ),
])
def test_shift_grid_left(tiles, expected_tiles, expected_has_changed):
    actual_tiles, actual_has_changed = shift_grid_left(tiles)
    assert expected_tiles == actual_tiles
    assert expected_has_changed == actual_has_changed



@pytest.mark.timeout(1)
@pytest.mark.parametrize("tiles, expected_tiles, expected_has_changed", [
    (
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        False
    ),
    (
        [
            [None, None, None, None],
            [2, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        [
            [2, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        True
    ),
    (
        [
            [None, 8, 2, None],
            [2, 8, 4, None],
            [None, None, 4, None],
            [2, None, None, None],
        ],
        [
            [4, 16, 2, None],
            [None, None, 8, None],
            [None, None, None, None],
            [None, None, None, None],
        ],
        True
    ),
])
def test_shift_grid_up(tiles, expected_tiles, expected_has_changed):
    actual_tiles, actual_has_changed = shift_grid_up(tiles)
    assert expected_tiles == actual_tiles
    assert expected_has_changed == actual_has_changed
