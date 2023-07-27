import pytest
import student


def if_method_exists(method_name):
    return pytest.mark.skipif(method_name not in dir(student.Interval), reason=f'{method_name} not found in Interval class')



@pytest.mark.timeout(1)
@pytest.mark.parametrize("lower", [-4, 0, 9])
@pytest.mark.parametrize("upper", [-2, 0, 5])
def test_initialization(lower, upper):
    interval = student.Interval(lower, upper)

    assert interval.lower == lower
    assert interval.upper == upper


@if_method_exists('contains')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("interval, value, expected", [
    *(
        (student.Interval(lower, upper), value, True)
        for lower in [-5, 0, 10]
        for upper in [-5, 0, 10]
        for value in range(lower, upper + 1)
    ),
    (student.Interval(5, 10), 4, False),
    (student.Interval(5, 10), 11, False),
    (student.Interval(8, 8), 8, True),
    *(
        (student.Interval(2, 1), value, False)
        for value in range(-5, 6)
    )
])
def test_contains(interval, value, expected):
    actual = interval.contains(value)
    assert expected == actual


@if_method_exists('is_empty')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("interval, expected", [
    (student.Interval(a, b), a > b)
    for a in [-5, 3, 20]
    for b in [-5, 3, 20]
])
def test_contains(interval, expected):
    actual = interval.is_empty()
    assert expected == actual


@if_method_exists('overlaps_with')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("i1, i2, expected", [
    *(
        (student.Interval(a, b), student.Interval(x, y), any(a <= k <= b and x <= k <= y for k in range(min(a, x), max(b, y) + 1)))
        for a in [-5, -1, 3, 8, 12]
        for b in [-5, -1, 3, 8, 12]
        for x in [-5, -1, 3, 8, 12]
        for y in [-5, -1, 3, 8, 12]
    )
])
def test_overlaps_with(i1, i2, expected):
    actual = i1.overlaps_with(i2)
    assert expected == actual, f'Interval({i1.lower}, {i1.upper}).overlaps_with({i2.lower}, {i2.upper}) should return {expected}'
