import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("card1, card2, expected", [
    *(
        (1, card, True)
        for card in range(2, 14)
    ),
    *(
        (card, 1, False)
        for card in range(2, 14)
    ),
    *(
        (card1, card2, card1 > card2)
        for card1 in range(2, 14)
        for card2 in range(2, 14)
    ),
    *(
        (card, card, False)
        for card in range(1, 14)
    )
])
def test_higher_card(card1, card2, expected):
    actual = student.higher_card(card1, card2)
    assert expected == actual, f'higher_card({card1}, {card2}) should return {expected}'
