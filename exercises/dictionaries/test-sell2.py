import pytest
import student


@pytest.fixture
def stock():
    return {
        'New Balance 530': {44: 2, 45: 3, 47: 1},
        'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
        'Air Jordan 1 Retro': {46: 1},
        'Nike Air Max Tuned 1': {44: 2, 45: 1},
        'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
        'Vans Classic Slip-on Checkered': {43: 1},
    }


@pytest.mark.timeout(1)
@pytest.mark.parametrize('model, size, expected_return_value, expected_stock', [
    (
        'New Balance 530',
        44,
        True,
        {
            'New Balance 530': {44: 1, 45: 3, 47: 1},
            'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
            'Air Jordan 1 Retro': {46: 1},
            'Nike Air Max Tuned 1': {44: 2, 45: 1},
            'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
            'Vans Classic Slip-on Checkered': {43: 1},
        }
    ),
    (
        'New Balance 530',
        47,
        True,
        {
            'New Balance 530': {44: 2, 45: 3},
            'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
            'Air Jordan 1 Retro': {46: 1},
            'Nike Air Max Tuned 1': {44: 2, 45: 1},
            'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
            'Vans Classic Slip-on Checkered': {43: 1},
        }
    ),
    (
        'Vans Classic Slip-on Checkered',
        43,
        True,
        {
            'New Balance 530': {44: 2, 45: 3, 47: 1},
            'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
            'Air Jordan 1 Retro': {46: 1},
            'Nike Air Max Tuned 1': {44: 2, 45: 1},
            'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
        }
    ),
    (
        'Vans Classic Slip-on Checkered',
        47,
        False,
        {
            'New Balance 530': {44: 2, 45: 3, 47: 1},
            'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
            'Air Jordan 1 Retro': {46: 1},
            'Nike Air Max Tuned 1': {44: 2, 45: 1},
            'Adidas Superstar': {41: 2, 43: 2, 45: 1, 47: 3},
            'Vans Classic Slip-on Checkered': {43: 1},
        }
    ),
    (
        'Adidas Superstar',
        41,
        True,
        {
            'New Balance 530': {44: 2, 45: 3, 47: 1},
            'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
            'Air Jordan 1 Retro': {46: 1},
            'Nike Air Max Tuned 1': {44: 2, 45: 1},
            'Adidas Superstar': {41: 1, 43: 2, 45: 1, 47: 3},
            'Vans Classic Slip-on Checkered': {43: 1},
        }
    ),
    (
        'Adidas Superstar',
        45,
        True,
        {
            'New Balance 530': {44: 2, 45: 3, 47: 1},
            'Converse Chuck Taylor All Star 70 Hi': {39: 2, 40: 1, 43: 4, 44: 2},
            'Air Jordan 1 Retro': {46: 1},
            'Nike Air Max Tuned 1': {44: 2, 45: 1},
            'Adidas Superstar': {41: 2, 43: 2, 47: 3},
            'Vans Classic Slip-on Checkered': {43: 1},
        }
    ),
])
def test_sell(stock, model, size, expected_return_value, expected_stock):
    actual_return_value = student.sell2(stock, model, size)

    assert expected_return_value == actual_return_value
    assert expected_stock == stock
