import pytest
import student


@pytest.mark.parametrize("eggs", range(0, 100))
def test_cake(eggs):
    eggs_per_cake = 5
    actual = student.cake(eggs=eggs)

    assert actual * eggs_per_cake <= eggs
    assert (actual + 1) * eggs_per_cake > eggs
