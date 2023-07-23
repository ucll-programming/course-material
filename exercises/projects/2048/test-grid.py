import pytest
from grid import *


@pytest.mark.timeout(1)
@pytest.mark.parametrize("grid, expected", [
    (
        [[1, 2, 3]], 3
    ),
    (
        [
            [1, 2, 3],
            [4, 5, 6]
        ], 3
    ),
    (
        [
            [1, 2, 3, 5],
            [4, 5, 6, 7]
        ], 4
    ),
    (
        [
            [1, 2, 3, 5],
            [1, 2, 3, 5],
            [4, 5, 6, 7],
            [4, 5, 6, 7],
            [4, 5, 6, 7],
        ], 4
    ),
])
def test_width(grid, expected):
    actual = width(grid)
    assert expected == actual


@pytest.mark.timeout(1)
@pytest.mark.parametrize("grid, expected", [
    (
        [[1, 2, 3]], 1
    ),
    (
        [
            [1, 2, 3],
            [4, 5, 6]
        ], 2
    ),
    (
        [
            [1, 2, 3, 5],
            [4, 5, 6, 7]
        ], 2
    ),
    (
        [
            [1, 2, 3, 5],
            [1, 2, 3, 5],
            [4, 5, 6, 7],
            [4, 5, 6, 7],
            [4, 5, 6, 7],
        ], 5
    ),
])
def test_height(grid, expected):
    actual = height(grid)
    assert expected == actual


@pytest.mark.timeout(1)
@pytest.mark.parametrize("grid, index, expected", [
    (
        [[1]],
        0,
        [1]
    ),
    (
        [
            [1, 2],
        ],
        0,
        [1]
    ),
    (

        [
            [1, 2],
        ],
        1,
        [2]
    ),
    (
        [
            [1, 2],
        ],
        0,
        [1]
    ),
    (
        [
            [1, 2],
            [3, 4],
        ],
        0,
        [1, 3]
    ),
    (
        [
            [1, 2],
            [3, 4],
            [5, 6]
        ],
        0,
        [1, 3, 5]
    ),
])
def test_column(grid, index, expected):
    actual = column(grid, index)
    assert expected == actual


@pytest.mark.timeout(1)
@pytest.mark.parametrize("grid, expected", [
    (
        [
            [1]
        ],
        [
            [1]
        ]
    ),
    (
        [
            [1, 2]
        ],
        [
            [1],
            [2]
        ]
    ),
    (
        [
            [1, 2],
            [3, 4],
        ],
        [
            [1, 3],
            [2, 4]
        ]
    ),
    (
        [
            [1, 2, 5],
            [3, 4, 6],
        ],
        [
            [1, 3],
            [2, 4],
            [5, 6],
        ]
    ),
])
def test_transpose(grid, expected):
    actual = transpose(grid)
    assert expected == actual



@pytest.mark.timeout(1)
@pytest.mark.parametrize("grid, expected", [
    (
        [
            [1]
        ],
        [
            [1]
        ]
    ),
    (
        [
            [1, 2]
        ],
        [
            [1],
            [2]
        ]
    ),
    (
        [
            [1, 2],
            [3, 4],
        ],
        [
            [3, 1],
            [4, 2]
        ]
    ),
    (
        [
            [1, 2, 5],
            [3, 4, 6],
        ],
        [
            [3, 1],
            [4, 2],
            [6, 5],
        ]
    ),
])
def test_rotate_cw(grid, expected):
    actual = rotate_cw(grid)
    assert expected == actual
