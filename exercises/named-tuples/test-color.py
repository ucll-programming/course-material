import pytest
import student


def does_function_exist(function_name):
    return function_name in dir(student)


def if_function_exists(function_name):
    return pytest.mark.skipif(not does_function_exist(function_name), reason=f'{function_name} not found in student module')


def test_color_exists():
    assert 'Color' in dir(student)


@if_function_exists('Color')
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


@if_function_exists('valid_color')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("color, expected", [
    *(
        (student.Color(r, g, b), True)
        for r in [0, 64, 192, 255]
        for g in [0, 64, 192, 255]
        for b in [0, 64, 192, 255]
    ),
    (student.Color(256, 0, 0), False),
    (student.Color(0, 256, 0), False),
    (student.Color(0, 0, 256), False),
    (student.Color(-1, 0, 0), False),
    (student.Color(0, -1, 0), False),
    (student.Color(0, 0, -1), False),
])
def test_valid_color(color, expected):
    actual = student.valid_color(color)
    assert expected == actual
