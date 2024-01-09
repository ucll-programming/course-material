import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("eggs", range(0, 100, 13))
@pytest.mark.parametrize("flour", range(0, 1000, 175))
@pytest.mark.parametrize("sugar", range(0, 1000, 225))
@pytest.mark.parametrize("butter", range(0, 1000, 325))
def test_cake3(eggs, flour, sugar, butter):
    eggs_per_cake = 5
    flour_per_cake = 250
    butter_per_cake = 200
    sugar_per_cake = 250
    actual = student.cake3(eggs=eggs, flour=flour, sugar=sugar, butter=butter)

    assert actual * eggs_per_cake <= eggs, f"cake3({eggs}, {flour}, {sugar}, {butter}) returned {actual}, overestimating the number of cakes"
    assert actual * flour_per_cake <= flour, f"cake3({eggs}, {flour}, {sugar}, {butter}) returned {actual}, overestimating the number of cakes"
    assert actual * butter_per_cake <= butter, f"cake3({eggs}, {flour}, {sugar}, {butter}) returned {actual}, overestimating the number of cakes"
    assert actual * sugar_per_cake <= sugar, f"cake3({eggs}, {flour}, {sugar}, {butter}) returned {actual}, overestimating the number of cakes"
    assert (actual + 1) * eggs_per_cake > eggs or (actual + 1) * flour_per_cake > flour or (actual + 1) * butter_per_cake > butter or (actual + 1) * sugar_per_cake > sugar, f"cake3({eggs}, {flour}, {sugar}, {butter}) returned {actual}, underestimating the number of cakes"
