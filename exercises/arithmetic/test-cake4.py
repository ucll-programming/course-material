import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("eggs", [0, 1, 5, 200])
@pytest.mark.parametrize("flour", [0, 250, 1900])
@pytest.mark.parametrize("butter", [0, 200, 2000 ])
@pytest.mark.parametrize("sugar", [0, 800, 1000])
@pytest.mark.parametrize('eggs_per_cake', [1, 3, 5])
@pytest.mark.parametrize('flour_per_cake', [100, 250])
@pytest.mark.parametrize('butter_per_cake', [100, 550])
@pytest.mark.parametrize('sugar_per_cake', [100, 200])
def test_cake4(eggs, flour, sugar, butter, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    actual = student.cake4(
        eggs=eggs,
        flour=flour,
        sugar=sugar,
        butter=butter,
        eggs_per_cake=eggs_per_cake,
        flour_per_cake=flour_per_cake,
        butter_per_cake=butter_per_cake,
        sugar_per_cake=sugar_per_cake,
    )

    assert actual * eggs_per_cake <= eggs, f"cake4 returned {actual}, which needs too many eggs"
    assert actual * flour_per_cake <= flour, f"cake4 returned {actual}, which needs too much flour"
    assert actual * butter_per_cake <= butter, f"cake4 returned {actual}, which needs too many butter"
    assert actual * sugar_per_cake <= sugar, f"cake4 returned {actual}, which needs too many sugar"
    assert (actual + 1) * eggs_per_cake > eggs or (actual + 1) * flour_per_cake > flour or (actual + 1) * butter_per_cake > butter or (actual + 1) * sugar_per_cake > sugar, f"cake4 underestimates the number of bakeable cakes"
