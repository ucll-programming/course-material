import pytest
import student


@pytest.fixture
def catalog():
    return {
        'Intel Core i7 13700K': 439,
        'Intel Core i5 13600K': 331,
        'Gigabyte Z790 AORUS ELITE AX': 261,
        'MSI MAG Z790 TOMAHAWK WIFI': 279,
        'Corsair DDR5 Vengeance 2x16GB 5600': 95,
        'Corsair DDR5 Vengeance 2x32GB 5600': 165,
        'MSI GeForce RTX 4070 VENTUS 3X 12G OC GPU': 659,
        'Gigabyte GeForce RTX 4090 GAMING OC 24G GPU': 1849,
    }


@pytest.mark.timeout(1)
@pytest.mark.parametrize('components, expected', [
    (
        [],
        0
    ),
    (
        ['Intel Core i7 13700K'],
        439,
    ),
    (
        ['Intel Core i5 13600K'],
        331,
    ),
    (
        ['Intel Core i7 13700K', 'Gigabyte Z790 AORUS ELITE AX'],
        439 + 261,
    ),
    (
        ['Intel Core i7 13700K', 'Gigabyte Z790 AORUS ELITE AX', 'Corsair DDR5 Vengeance 2x32GB 5600'],
        439 + 261 + 165,
    ),
    (
        ['Intel Core i7 13700K', 'Gigabyte Z790 AORUS ELITE AX', 'Corsair DDR5 Vengeance 2x32GB 5600', 'Gigabyte GeForce RTX 4090 GAMING OC 24G GPU'],
        439 + 261 + 165 + 1849,
    ),
])
def test_desktop(catalog, components, expected):
    actual = student.desktop(catalog, components)
    assert expected == actual
