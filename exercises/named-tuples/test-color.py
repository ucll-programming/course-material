import pytest
import student


def is_defined(function_name):
    return function_name in dir(student)


def if_defined(*identifiers):
    condition = all(is_defined(identifier) for identifier in identifiers)
    return pytest.mark.skipif(not condition, reason=f'One of {identifiers!r} not found in student module')


def c(*args, **kwargs):
    if 'Color' in dir(student):
        return student.Color(*args, **kwargs)
    else:
        return None


def test_color_exists():
    assert 'Color' in dir(student)


@if_defined('Color')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("r, g, b", [
    (r, g, b)
    for r in [0, 20, 255]
    for g in [0, 50, 255]
    for b in [0, 100, 255]
])
def test_color(r, g, b):
    actual = student.Color(r, g, b)

    assert r == actual.r
    assert g == actual.g
    assert b == actual.b


@if_defined('Color', 'valid_color')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("color, expected", [
    *(
        (c(r, g, b), True)
        for r in [0, 64, 192, 255]
        for g in [0, 64, 192, 255]
        for b in [0, 64, 192, 255]
    ),
    (c(256, 0, 0), False),
    (c(0, 256, 0), False),
    (c(0, 0, 256), False),
    (c(-1, 0, 0), False),
    (c(0, -1, 0), False),
    (c(0, 0, -1), False),
])
def test_valid_color(color, expected):
    actual = student.valid_color(color)
    assert expected == actual


@if_defined('valid_color')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("color, expected", [
    (
        c(0, 0, 0),
        c(0, 0, 0),
    ),
    (
        c(-1, 0, 0),
        c(0, 0, 0),
    ),
    (
        c(0, -1, 0),
        c(0, 0, 0),
    ),
    (
        c(0, 0, -1),
        c(0, 0, 0),
    ),
    (
        c(10, 20, -1),
        c(10, 20, 0),
    ),
    (
        c(256, 40, 120),
        c(255, 40, 120),
    ),
    (
        c(60, 256, 120),
        c(60, 255, 120),
    ),
    (
        c(60, 192, 256),
        c(60, 192, 255),
    ),
])
def test_clamp_color(color, expected):
    actual = student.clamp_color(color)
    assert expected == actual