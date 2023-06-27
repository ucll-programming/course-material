import pytest
import student


@pytest.mark.parametrize("eggs", range(0, 100, 3))
@pytest.mark.parametrize("flour", range(0, 1000, 40))
def test_cake2(eggs, flour):
    eggs_per_cake = 5
    flour_per_cake = 250
    actual = student.cake2(eggs=eggs, flour=flour)

    assert actual * eggs_per_cake <= eggs
    assert actual * flour_per_cake <= flour
    assert (actual + 1) * eggs_per_cake > eggs or (actual + 1) * flour_per_cake > flour
