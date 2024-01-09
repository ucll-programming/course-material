import pytest
import student


def create_stock():
    return {
        'New Balance 530': 5,
        'Converse Chuck Taylor All Star 70 Hi': 2,
        'Air Jordan 1 Retro': 8,
        'Nike Air Max Tuned 1': 1,
        'Adidas Superstar': 4,
        'Vans Classic Slip-on Checkered': 15,
        'Asics GEL-KAYANO 30': 1,
        'Puma Speedcat': 2,
    }


@pytest.fixture
def stock():
    return create_stock()


@pytest.mark.timeout(1)
@pytest.mark.parametrize('item', create_stock().keys())
def test_sell(stock, item):
    amount_before = stock[item]
    student.sell(stock, item)

    if amount_before == 1:
        assert item not in stock
    else:
        assert stock[item] == amount_before - 1
