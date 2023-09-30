import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("eggs", range(0, 100))
def test_cake(eggs):
    eggs_per_cake = 5
    actual = student.cake(eggs=eggs)

    assert actual * eggs_per_cake <= eggs, f"cake({eggs}) returned {actual}, overestimating the number of cakes"
    assert (actual + 1) * eggs_per_cake > eggs, f"cake({eggs}) returned {actual}, underestimating the number of cakes"
