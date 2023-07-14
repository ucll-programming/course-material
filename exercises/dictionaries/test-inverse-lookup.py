import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('dictionary, value, expected', [
    (
        {},
        1,
        []
    ),
    (
        {'a': 1},
        1,
        ['a']
    ),
    (
        {'a': 1, 'b': 1},
        1,
        ['a', 'b']
    ),
    (
        {'a': 1, 'b': 1, 'c': 2},
        1,
        ['a', 'b']
    ),
    (
        {'a': 1, 'b': 1, 'c': 2},
        2,
        ['c']
    ),
    (
        {'a': 1, 'b': 1, 'c': 2},
        3,
        []
    ),
    (
        {'x': 0, 'y': 1},
        'x',
        []
    ),
    (
        {'x': 0, 'y': 1},
        'y',
        []
    ),
    (
        {'x': 0, 'y': 1},
        0,
        ['x']
    ),
    (
        {'x': 0, 'y': 1},
        1,
        ['y']
    ),
    (
        {'x': 0, 'y': 0},
        0,
        ['x', 'y']
    ),
    (
        {'x': 0, 'y': 0},
        1,
        []
    ),
])
def test_inverse_lookup(dictionary, value, expected):
    actual = student.inverse_lookup(dictionary, value)
    assert sorted(expected) == sorted(actual), f'inverse_lookup({dictionary}, {value}) should return {expected} but got {actual}'
