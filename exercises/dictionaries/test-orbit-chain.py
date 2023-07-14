import pytest
import student


@pytest.fixture
def orbits():
    return {
        'Moon': 'Earth',
        'Mars': 'Sun',
        'Earth': 'Sun',
        'Jupiter': 'Sun',
        'Saturn': 'Sun',
        'Sun': 'Sagittarius A*',
        'Phobos': 'Mars',
        'Deimos': 'Mars',
        'Titan': 'Saturn',
        'Enceladus': 'Saturn',
        'Hyperion': 'Saturn',
        'Tethys': 'Saturn',
        'Ganymede': 'Jupiter',
        'Callisto': 'Jupiter',
        'Europa': 'Jupiter',
        'Proxima Centauri b': 'Proxima Centauri',
        'Proxima Centauri': 'Sagittarius A*',
    }


@pytest.mark.timeout(1)
@pytest.mark.parametrize("start, expected", [
    (
        'Moon',
        ['Moon', 'Earth', 'Sun', 'Sagittarius A*']
    ),
    (
        'Titan',
        ['Titan', 'Saturn', 'Sun', 'Sagittarius A*']
    ),
    (
        'Earth',
        ['Earth', 'Sun', 'Sagittarius A*']
    ),
    (
        'Sagittarius A*',
        ['Sagittarius A*']
    ),
    (
        'Ganymede',
        ['Ganymede', 'Jupiter', 'Sun', 'Sagittarius A*']
    ),
    (
        'Deimos',
        ['Deimos', 'Mars', 'Sun', 'Sagittarius A*']
    ),
    (
        'Proxima Centauri b',
        ['Proxima Centauri b', 'Proxima Centauri', 'Sagittarius A*']
    ),
    (
        'Hyperion',
        ['Hyperion', 'Saturn', 'Sun', 'Sagittarius A*']
    ),
])
def test_orbit_chain(orbits, start, expected):
    actual = student.orbit_chain(orbits, start)
    assert expected == actual
