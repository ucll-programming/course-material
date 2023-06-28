import pytest
import student


def if_function_exists(function_name):
    return pytest.mark.skipif(function_name not in dir(student), reason=f'{function_name} not found in student module')


@if_function_exists('increase_version')
@pytest.mark.parametrize("version, breaking_change, new_features, expected", [
    testcase
    for major in [0, 1, 4]
    for minor in [0, 2, 5, 9]
    for patch in [0, 3, 15]
    for testcase in [
        (
            (major, minor, patch),
            True,
            False,
            (major + 1, 0, 0),
        ),
        (
            (major, minor, patch),
            True,
            True,
            (major + 1, 0, 0),
        ),
        (
            (major, minor, patch),
            False,
            True,
            (major, minor + 1, 0),
        ),
        (
            (major, minor, patch),
            False,
            False,
            (major, minor, patch + 1),
        )
    ]
])
def test_increase_version(version, breaking_change, new_features, expected):
    actual = student.increase_version(
        version=version,
        breaking_change=breaking_change,
        new_features=new_features
    )

    assert expected == actual, f"increase_version({version}, {breaking_change}, {new_features}) should return {expected} but returned {actual}"


@if_function_exists('is_more_recent')
@pytest.mark.parametrize("v1, v2", [
    (
        (a, b, c),
        (x, y, z),
    )
    for a in range(0, 3)
    for b in range(0, 3)
    for c in range(0, 3)
    for x in range(0, 3)
    for y in range(0, 3)
    for z in range(0, 3)
])
def test_is_more_recent(v1, v2):
    actual = student.is_more_recent(v1, v2)
    expected = v1 > v2
    assert expected == actual, f'is_more_recent({v1}, {v2}) should return {expected}'


@if_function_exists('is_older')
@pytest.mark.parametrize("v1, v2", [
    (
        (a, b, c),
        (x, y, z),
    )
    for a in range(0, 3)
    for b in range(0, 3)
    for c in range(0, 3)
    for x in range(0, 3)
    for y in range(0, 3)
    for z in range(0, 3)
])
def test_is_older(v1, v2):
    actual = student.is_older(v1, v2)
    expected = v1 < v2
    assert expected == actual, f'is_older({v1}, {v2}) should return {expected}'
