import pytest
import student


def does_function_exist(function_name):
    return function_name in dir(student)


def if_function_exists(function_name):
    return pytest.mark.skipif(not does_function_exist(function_name), reason=f'{function_name} not found in student module')


test_data = [
    ([], []),
    ([None], []),
    ([0], [0]),
    ([''], ['']),
    ([False], [False]),
    ([1, 2, 3], [1, 2, 3]),
    ([1, None, 9, False], [1, 9, False]),
    ([None, None, None, None], []),
    ([None, 1, 'x'], [1, 'x']),
    ([1, None, 'x'], [1, 'x']),
    ([1, 'x', None], [1, 'x']),
    ([1, None,'x', None], [1, 'x']),
    ([None, 1, None,'x', None], [1, 'x']),
    ([None, 1, None,'x', None, False], [1, 'x', False]),
    ([None, 1, None,'x', None, None, False], [1, 'x', False]),
]


@if_function_exists('compact')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, expected", test_data)
def test_compact(xs, expected):
    copy = xs[:]
    actual = student.compact(copy)

    assert copy == xs
    assert expected == actual


@if_function_exists('compact')
@pytest.mark.timeout(1)
@pytest.mark.parametrize("xs, expected", test_data)
def test_compact_in_place(xs, expected):
    copy = xs[:]
    student.compact_in_place(copy)
    assert expected == copy
