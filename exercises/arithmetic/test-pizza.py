import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("n_people, slices_per_pizza", [
    (n_people, slices_per_pizza)
    for n_people in range(0, 50)
    for slices_per_pizza in range(1, 8)
])
def test_pizza(n_people, slices_per_pizza):
    actual = student.pizza(n_people=n_people, slices_per_pizza=slices_per_pizza)

    assert actual * slices_per_pizza >= n_people, f"pizza({n_people}, {slices_per_pizza}) returned {actual}, underestimating the number of pizzas needed"
    assert (actual - 1) * slices_per_pizza < n_people, f"pizza({n_people}, {slices_per_pizza}) returned {actual}, overestimating the number of pizzas needed"
