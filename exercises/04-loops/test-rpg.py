import pytest
import student


def if_function_exists(function_name):
    return pytest.mark.skipif(function_name not in dir(student), reason=f'{function_name} not found in student module')


@if_function_exists('test_rpg2')
@pytest.mark.parametrize("n_sides, goal, expected", [
    (4, 8, 100/16),
    (5, 10, 100/25),
    (4, 2, 100),
    (4, 3, 1500/16),
    (6, 7, 175/3),
    (6, 8, 125/3),
    (10, 8, 79),
    (10, 10, 64),
    (10, 11, 55),
    (20, 18, 66),
    (5, 20, 0),
    (6, 20, 0),
])
def test_rpg2(n_sides, goal, expected):
    actual = student.rpg2(n_sides=n_sides, goal=goal)
    assert pytest.approx(expected) == actual, f'rpg2(n_sides, goal) should return approximately {expected}'


@if_function_exists('test_rpg3')
@pytest.mark.parametrize("n_sides, goal, expected", [
    (4, 4, 1575/16),
    (4, 5, 375/4),
    (5, 5, 484/5),
    (6, 5, 2650/27),
    (6, 7, 2450/27),
    (7, 3, 100),
    (7, 4, 34200/343),
    (7, 21, 100/343),
    (7, 22, 0),
])
def test_rpg3(n_sides, goal, expected):
    actual = student.rpg3(n_sides=n_sides, goal=goal)
    assert pytest.approx(expected) == actual, f'rpg3(n_sides, goal) should return approximately {expected}'
