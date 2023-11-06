import pytest
import student


@pytest.mark.timeout(1)
@pytest.mark.parametrize("people_count", [0, 1, 10, 55, 94, 104, 4201])
@pytest.mark.parametrize("bus_capacity", [1, 5, 10, 20, 50, 100])
def test_buses_needed(people_count, bus_capacity):
    actual = student.buses_needed(people_count=people_count, bus_capacity=bus_capacity)

    assert bus_capacity * actual >= people_count, f'{actual} buses with capacity {bus_capacity} is insufficient to transport {people_count} people'
    assert bus_capacity * (actual - 1) < people_count, f'{actual} buses with capacity {bus_capacity} is too many to transport {people_count} people'
