import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize('stock, ingredients, expected', [
    (
        {
            'sugar': 1000
        },
        {
            'sugar': 100
        },
        10
    ),
    (
        {
            'sugar': 1000
        },
        {
            'flour': 100
        },
        0
    ),
    (
        {
            'eggs': 100
        },
        {
            'eggs': 100
        },
        1
    ),
    (
        {
            'water': 1000
        },
        {
            'water': 1001
        },
        0
    ),
    (
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        1
    ),
    (
        {
            'sugar': 500,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        1
    ),
    (
        {
            'sugar': 500,
            'flour': 500,
            'eggs': 4,
            'butter': 250,
        },
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        1
    ),
    (
        {
            'sugar': 500,
            'flour': 500,
            'eggs': 8,
            'butter': 250,
        },
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        1
    ),
    (
        {
            'sugar': 500,
            'flour': 500,
            'eggs': 8,
            'butter': 500,
        },
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        2
    ),
    (
        {
            'sugar': 5000,
            'flour': 2500,
            'eggs': 50,
            'butter': 1500,
            'chocolate': 10000,
        },
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 250,
        },
        6
    ),
    (
        {
            'sugar': 5000,
            'flour': 2500,
            'eggs': 50,
            'butter': 1500,
            'chocolate': 10000,
        },
        {
            'sugar': 250,
            'flour': 250,
            'eggs': 4,
            'butter': 125,
        },
        10
    ),
    (
        {
            'sugar': 5000,
            'flour': 2500,
            'eggs': 50,
            'butter': 1500,
            'chocolate': 10000,
        },
        {
            'sugar': 250,
            'flour': 200,
            'eggs': 4,
            'butter': 125,
        },
        12
    ),
])
def test_cake(stock, ingredients, expected):
    actual = student.cake(stock, ingredients)
    assert expected == actual
