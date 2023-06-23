import pytest
import student


@pytest.mark.parametrize("duration_in_seconds, cost_per_block, expected", [
    triple
    for cost_per_block in [0.1, 0.5, 1.0]
    for triple in [
        (0, cost_per_block, 0),
        (1, cost_per_block, cost_per_block),
        (359, cost_per_block, cost_per_block),
        (360, cost_per_block, cost_per_block),
        (361, cost_per_block, 2 * cost_per_block),
        (360 * 15 + 16, cost_per_block, 16 * cost_per_block)
    ]
])
def test_internet_costs(duration_in_seconds, cost_per_block, expected):
    actual = student.internet_costs(
        duration_in_seconds=duration_in_seconds,
        cost_per_block=cost_per_block
    )

    assert pytest.approx(expected, abs=0.001) == actual
